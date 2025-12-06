# ============================================
# 🎭 STAGE 1: ML ENSEMBLE SIGNAL
# Improved ensemble with XGBoost, LightGBM, CatBoost
# Removed LSTM due to poor performance
# ============================================

import numpy as np
import pandas as pd
from typing import Dict, Optional, Tuple
from dataclasses import dataclass

from trading.entry_pipeline.models import MLPrediction, SignalDirection
from utils.logger import logger


class MLEnsembleSignal:
    """
    Stage 1: ML Ensemble Signal Generator
    
    - Uses XGBoost (40%), LightGBM (35%), CatBoost (25%)
    - LSTM removed due to poor performance (~47% accuracy)
    - Weighted voting mechanism
    - Output: direction (LONG/SHORT/NEUTRAL), confidence (0-1)
    """
    
    DEFAULT_WEIGHTS = {
        'xgboost': 0.40,
        'lightgbm': 0.35,
        'catboost': 0.25
    }
    
    def __init__(
        self,
        config: Dict,
        models: Optional[Dict] = None,
        weights: Optional[Dict[str, float]] = None
    ):
        """
        Initialize ML Ensemble Signal
        
        Args:
            config: Configuration dictionary
            models: Pre-loaded models dict {name: model}
            weights: Custom weights {model_name: weight}
        """
        self.config = config
        self.models = models or {}
        self.weights = weights or self.DEFAULT_WEIGHTS.copy()
        
        # Threshold for signal generation
        self.confidence_threshold = config.get('ML_CONFIDENCE_THRESHOLD', 0.62)
        self.neutral_zone = config.get('ML_NEUTRAL_ZONE', 0.08)  # 0.42-0.58 = neutral
        
        # Normalize weights
        self._normalize_weights()
        
        logger.info(f"🎭 MLEnsembleSignal initialized")
        logger.info(f"   Models: {list(self.weights.keys())}")
        logger.info(f"   Weights: {self.weights}")
        logger.info(f"   Confidence threshold: {self.confidence_threshold}")
    
    def _normalize_weights(self):
        """Normalize weights to sum to 1.0"""
        total = sum(self.weights.values())
        if total > 0:
            self.weights = {k: v / total for k, v in self.weights.items()}
    
    def set_models(self, models: Dict):
        """Set the model instances"""
        self.models = models
        # Adjust weights for available models only
        available = [m for m in self.weights.keys() if m in self.models]
        if len(available) < len(self.weights):
            logger.warning(f"Only {len(available)}/{len(self.weights)} models available")
            self.weights = {k: v for k, v in self.weights.items() if k in available}
            self._normalize_weights()
    
    def predict(self, X: np.ndarray) -> MLPrediction:
        """
        Generate ML prediction from ensemble
        
        Args:
            X: Input features (seq_len, n_features) or (n_samples, seq_len, n_features)
        
        Returns:
            MLPrediction with direction, confidence, and details
        """
        predictions = {}
        valid_weights = {}
        
        for model_name, weight in self.weights.items():
            if model_name not in self.models:
                continue
            
            model = self.models[model_name]
            if model is None or not hasattr(model, 'predict'):
                continue
            
            try:
                pred = model.predict(X)
                
                # Handle different return types
                if isinstance(pred, np.ndarray):
                    pred = float(pred.flatten()[0]) if pred.size > 0 else 0.5
                else:
                    pred = float(pred)
                
                # Clip to valid range
                pred = np.clip(pred, 0.0, 1.0)
                
                predictions[model_name] = pred
                valid_weights[model_name] = weight
                
            except Exception as e:
                logger.warning(f"Prediction failed for {model_name}: {e}")
                continue
        
        if not predictions:
            logger.error("All model predictions failed!")
            return MLPrediction(
                direction=SignalDirection.NEUTRAL,
                confidence=0.0,
                individual_predictions={},
                model_agreement=0.0
            )
        
        # Calculate weighted ensemble prediction
        weights_array = np.array(list(valid_weights.values()))
        weights_array = weights_array / weights_array.sum()
        
        preds_array = np.array(list(predictions.values()))
        ensemble_pred = np.average(preds_array, weights=weights_array)
        
        # Calculate model agreement (1 - normalized std)
        std = np.std(preds_array)
        agreement = 1.0 - min(std * 2, 1.0)
        
        # Determine direction and confidence
        direction, confidence = self._determine_direction(ensemble_pred)
        
        return MLPrediction(
            direction=direction,
            confidence=confidence,
            individual_predictions=predictions,
            model_agreement=agreement
        )

    def _determine_direction(self, prob: float) -> Tuple[SignalDirection, float]:
        """
        Determine signal direction from probability

        Args:
            prob: Probability from ensemble (0-1)
                  > 0.5 = bullish, < 0.5 = bearish

        Returns:
            Tuple of (SignalDirection, confidence)
        """
        # Distance from neutral (0.5)
        distance = abs(prob - 0.5)

        # Check neutral zone
        if distance < self.neutral_zone:
            return SignalDirection.NEUTRAL, 0.5

        # Calculate confidence as distance from 0.5 mapped to 0-1
        # prob=0.5 -> confidence=0.5
        # prob=1.0 -> confidence=1.0
        # prob=0.0 -> confidence=1.0 (for short)
        confidence = 0.5 + distance

        if prob > 0.5:
            return SignalDirection.LONG, confidence
        else:
            return SignalDirection.SHORT, confidence

    def get_prediction_details(self, X: np.ndarray) -> Dict:
        """
        Get detailed prediction info for logging/debugging

        Args:
            X: Input features

        Returns:
            Dictionary with detailed prediction info
        """
        prediction = self.predict(X)

        return {
            'direction': prediction.direction.value,
            'confidence': round(prediction.confidence, 4),
            'ensemble_prob': round(
                sum(p * self.weights.get(m, 0)
                    for m, p in prediction.individual_predictions.items()) /
                sum(self.weights.get(m, 0)
                    for m in prediction.individual_predictions.keys()),
                4
            ) if prediction.individual_predictions else 0.5,
            'model_agreement': round(prediction.model_agreement, 4),
            'individual': {
                m: round(p, 4)
                for m, p in prediction.individual_predictions.items()
            },
            'weights_used': {
                m: round(w, 3)
                for m, w in self.weights.items()
                if m in prediction.individual_predictions
            },
            'threshold': self.confidence_threshold,
            'passes_threshold': prediction.confidence >= self.confidence_threshold
        }

    def validate(self, prediction: MLPrediction) -> Tuple[bool, str]:
        """
        Validate if prediction passes threshold

        Args:
            prediction: MLPrediction object

        Returns:
            Tuple of (passed, reason)
        """
        if prediction.direction == SignalDirection.NEUTRAL:
            return False, f"Neutral signal (in neutral zone ±{self.neutral_zone})"

        if prediction.confidence < self.confidence_threshold:
            return False, f"Confidence {prediction.confidence:.2f} < threshold {self.confidence_threshold}"

        # Check model agreement for extra confidence
        if prediction.model_agreement < 0.5:
            logger.warning(f"Low model agreement: {prediction.model_agreement:.2f}")

        return True, f"ML signal valid: {prediction.direction.value} @ {prediction.confidence:.2f}"

