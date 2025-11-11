# ============================================
# 🎭 ENSEMBLE MODEL SYSTEM
# Combines multiple models for better predictions
# ============================================

import numpy as np
from ml.lstm_model import LSTMTrainer
from ml.xgboost_model import XGBoostTrainer
from utils.logger import logger
from config import Config

class EnsemblePredictor:
    """
    Ensemble multiple ML models with weighted averaging

    Supported models:
    - LSTM: Good for sequential patterns
    - XGBoost: Good for feature-based patterns

    Benefits:
    - Reduced overfitting
    - Better generalization
    - More robust predictions
    """

    def __init__(self, models=['lstm', 'xgboost'], weights=[0.4, 0.6], input_size=14):
        """
        Initialize ensemble

        Args:
            models: List of model names to use
            weights: Weight for each model (must sum to 1.0)
            input_size: Number of input features
        """
        self.model_names = models
        self.weights = np.array(weights)
        self.input_size = input_size

        # Validate weights
        if abs(self.weights.sum() - 1.0) > 0.01:
            logger.warning(f"Weights don't sum to 1.0 ({self.weights.sum()}), normalizing...")
            self.weights = self.weights / self.weights.sum()

        # Initialize models
        self.models = {}

        for model_name in models:
            if model_name == 'lstm':
                self.models['lstm'] = LSTMTrainer(input_size=input_size)
            elif model_name == 'xgboost':
                self.models['xgboost'] = XGBoostTrainer(input_size=input_size)
            else:
                logger.warning(f"Unknown model: {model_name}")

        logger.info(f"🎭 Ensemble initialized with {len(self.models)} models")
        logger.info(f"   Models: {self.model_names}")
        logger.info(f"   Weights: {self.weights}")

    def load_models(self):
        """Load all models from disk"""
        success_count = 0

        for model_name, model in self.models.items():
            if model_name == 'lstm':
                if model.load(Config.MODEL_PATH, Config.SCALER_PATH):
                    success_count += 1
                    logger.info(f"✅ LSTM loaded")
                else:
                    logger.warning(f"⚠️ LSTM not loaded")

            elif model_name == 'xgboost':
                xgb_model_path = Config.MODEL_PATH.replace('lstm_model.pt', 'xgboost_model.json')
                xgb_scaler_path = Config.SCALER_PATH.replace('scaler.pkl', 'xgboost_scaler.pkl')

                if model.load(xgb_model_path, xgb_scaler_path):
                    success_count += 1
                    logger.info(f"✅ XGBoost loaded")
                else:
                    logger.warning(f"⚠️ XGBoost not loaded")

        if success_count == 0:
            logger.error("❌ No models loaded!")
            return False

        if success_count < len(self.models):
            logger.warning(f"⚠️ Only {success_count}/{len(self.models)} models loaded")
            # Adjust weights for available models
            self._adjust_weights()

        logger.info(f"✅ Ensemble loaded: {success_count}/{len(self.models)} models")
        return True

    def _adjust_weights(self):
        """Adjust weights when some models are missing"""
        available_models = []
        available_weights = []

        for i, model_name in enumerate(self.model_names):
            if model_name in self.models:
                # Check if model is actually loaded
                if model_name == 'lstm' and self.models[model_name].model is not None:
                    available_models.append(model_name)
                    available_weights.append(self.weights[i])
                elif model_name == 'xgboost' and self.models[model_name].model is not None:
                    available_models.append(model_name)
                    available_weights.append(self.weights[i])

        if available_weights:
            # Normalize weights
            self.weights = np.array(available_weights) / np.sum(available_weights)
            self.model_names = available_models
            logger.info(f"   Adjusted weights: {dict(zip(self.model_names, self.weights))}")

    def predict(self, X):
        """
        Ensemble prediction with weighted averaging

        Args:
            X: Input features (compatible with all models)
                - For LSTM: (seq_len, n_features)
                - For XGBoost: (seq_len, n_features) or (n_features,)

        Returns:
            float: Ensemble prediction (0-1)
        """
        predictions = []
        valid_weights = []

        for i, model_name in enumerate(self.model_names):
            try:
                if model_name not in self.models:
                    continue

                model = self.models[model_name]

                # Get prediction
                pred = model.predict(X)

                # Handle different return types
                if isinstance(pred, np.ndarray):
                    pred = pred[0] if len(pred) > 0 else 0.5

                predictions.append(pred)
                valid_weights.append(self.weights[i])

            except Exception as e:
                logger.warning(f"Prediction failed for {model_name}: {e}")
                continue

        if not predictions:
            logger.error("All model predictions failed!")
            return 0.5

        # Weighted average
        valid_weights = np.array(valid_weights)
        valid_weights = valid_weights / valid_weights.sum()  # Normalize

        ensemble_pred = np.average(predictions, weights=valid_weights)

        return ensemble_pred

    def predict_with_details(self, X):
        """
        Get ensemble prediction with individual model details

        Args:
            X: Input features

        Returns:
            tuple: (ensemble_pred, individual_preds_dict)
        """
        predictions = {}
        valid_weights = {}

        for i, model_name in enumerate(self.model_names):
            try:
                if model_name not in self.models:
                    continue

                model = self.models[model_name]
                pred = model.predict(X)

                if isinstance(pred, np.ndarray):
                    pred = pred[0] if len(pred) > 0 else 0.5

                predictions[model_name] = pred
                valid_weights[model_name] = self.weights[i]

            except Exception as e:
                logger.warning(f"Prediction failed for {model_name}: {e}")
                continue

        if not predictions:
            return 0.5, {}

        # Weighted average
        weights_array = np.array(list(valid_weights.values()))
        weights_array = weights_array / weights_array.sum()

        ensemble_pred = np.average(list(predictions.values()), weights=weights_array)

        # Add ensemble to predictions
        predictions['ensemble'] = ensemble_pred
        predictions['weights'] = valid_weights

        return ensemble_pred, predictions

    def get_model_agreement(self, X):
        """
        Check how much models agree on prediction

        Returns:
            float: Agreement score (0-1, higher = more agreement)
        """
        predictions = []

        for model_name in self.model_names:
            if model_name not in self.models:
                continue

            try:
                pred = self.models[model_name].predict(X)
                if isinstance(pred, np.ndarray):
                    pred = pred[0]
                predictions.append(pred)
            except:
                continue

        if len(predictions) < 2:
            return 1.0  # Perfect agreement if only 1 model

        # Calculate standard deviation (lower = more agreement)
        std = np.std(predictions)

        # Convert to agreement score (0-1)
        # std of 0.0 = perfect agreement (1.0)
        # std of 0.5 = maximum disagreement (0.0)
        agreement = 1.0 - min(std * 2, 1.0)

        return agreement

    @property
    def scaler(self):
        """Get scaler from first available model (for compatibility)"""
        for model_name in self.model_names:
            if model_name in self.models and self.models[model_name].scaler is not None:
                return self.models[model_name].scaler

        # Fallback to LSTM scaler if available
        if 'lstm' in self.models:
            return self.models['lstm'].scaler

        return None

    def save_models(self):
        """Save all models"""
        for model_name, model in self.models.items():
            try:
                if model_name == 'lstm':
                    model.save(Config.MODEL_PATH, Config.SCALER_PATH)
                elif model_name == 'xgboost':
                    xgb_model_path = Config.MODEL_PATH.replace('lstm_model.pt', 'xgboost_model.json')
                    xgb_scaler_path = Config.SCALER_PATH.replace('scaler.pkl', 'xgboost_scaler.pkl')
                    model.save(xgb_model_path, xgb_scaler_path)

                logger.info(f"✅ {model_name.upper()} saved")
            except Exception as e:
                logger.error(f"Failed to save {model_name}: {e}")
