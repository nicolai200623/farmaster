# ============================================
# 🐱 CATBOOST MODEL
# Gradient boosting with categorical features support
# ============================================

import numpy as np
import pickle
import os
from sklearn.preprocessing import MinMaxScaler
from utils.logger import logger
from config import Config

try:
    from catboost import CatBoostClassifier, Pool
    CATBOOST_AVAILABLE = True
except ImportError:
    CATBOOST_AVAILABLE = False
    logger.warning("⚠️ CatBoost not installed. Install: pip install catboost")


class CatBoostTrainer:
    """
    CatBoost model for price direction prediction

    Advantages:
    - Best handling of categorical features
    - Built-in overfitting detection
    - GPU support
    - Robust to hyperparameter choices
    """

    def __init__(self, input_size):
        """
        Initialize CatBoost trainer

        Args:
            input_size: Number of input features
        """
        self.input_size = input_size
        self.model = None
        self.scaler = MinMaxScaler()

        if not CATBOOST_AVAILABLE:
            logger.error("❌ CatBoost not available!")
        else:
            logger.info(f"🐱 CatBoost Trainer initialized with {input_size} features")

    def train(self, X_train, y_train, X_val=None, y_val=None):
        """
        Train CatBoost model

        Args:
            X_train: Training features
            y_train: Training labels
            X_val: Validation features (optional)
            y_val: Validation labels (optional)
        """
        if not CATBOOST_AVAILABLE:
            logger.error("❌ Cannot train - CatBoost not installed")
            return

        try:
            # Reshape if needed
            if len(X_train.shape) == 3:
                X_train = X_train[:, -1, :]  # Use last timestep
                if X_val is not None and len(X_val.shape) == 3:
                    X_val = X_val[:, -1, :]

            # Scale features
            X_train_scaled = self.scaler.fit_transform(X_train)
            if X_val is not None:
                X_val_scaled = self.scaler.transform(X_val)

            # CatBoost parameters (optimized for financial data)
            self.model = CatBoostClassifier(
                iterations=300,
                learning_rate=0.05,
                depth=4,  # Shallow trees to prevent overfitting
                l2_leaf_reg=3.0,  # L2 regularization
                bagging_temperature=1.0,  # Bayesian bootstrap
                random_strength=1.0,  # Randomness for splits
                border_count=128,  # Number of splits for numerical features
                early_stopping_rounds=30,
                verbose=50,
                random_seed=42,
                loss_function='Logloss',
                eval_metric='Accuracy',
            )

            # Create pools
            train_pool = Pool(X_train_scaled, y_train)
            eval_set = None
            if X_val is not None and y_val is not None:
                eval_set = Pool(X_val_scaled, y_val)

            # Train
            logger.info("🏋️ Training CatBoost model...")
            self.model.fit(
                train_pool,
                eval_set=eval_set,
                use_best_model=True if eval_set else False,
                plot=False
            )

            # Calculate accuracy
            y_pred = self.model.predict(X_train_scaled)
            train_acc = (y_pred.flatten() == y_train).mean()

            logger.info(f"✅ CatBoost training completed!")
            logger.info(f"   Train accuracy: {train_acc:.2%}")

            if X_val is not None:
                y_val_pred = self.model.predict(X_val_scaled)
                val_acc = (y_val_pred.flatten() == y_val).mean()
                logger.info(f"   Val accuracy: {val_acc:.2%}")

        except Exception as e:
            logger.error(f"CatBoost training error: {e}")
            raise

    def predict(self, X):
        """
        Predict probability

        Args:
            X: Features

        Returns:
            Probability of price going UP
        """
        if self.model is None:
            logger.warning("Model not loaded!")
            return 0.5

        try:
            # Handle different input shapes
            if len(X.shape) == 3:
                X = X[:, -1, :]
            elif len(X.shape) == 2 and X.shape[0] != 1:
                X = X[-1:, :]

            if len(X.shape) == 1:
                X = X.reshape(1, -1)

            # Scale
            X_scaled = self.scaler.transform(X)

            # Predict probabilities
            pred_proba = self.model.predict_proba(X_scaled)

            # Return probability of class 1 (UP)
            return pred_proba[0][1] if len(pred_proba) > 0 else 0.5

        except Exception as e:
            logger.error(f"CatBoost prediction error: {e}")
            return 0.5

    def save(self, model_path, scaler_path):
        """Save model and scaler"""
        if self.model is None:
            logger.warning("No model to save")
            return

        try:
            os.makedirs(os.path.dirname(model_path), exist_ok=True)

            # Save model
            self.model.save_model(model_path)

            # Save scaler
            with open(scaler_path, 'wb') as f:
                pickle.dump(self.scaler, f)

            logger.info(f"💾 CatBoost saved to {model_path}")

        except Exception as e:
            logger.error(f"Failed to save CatBoost: {e}")

    def load(self, model_path, scaler_path):
        """Load model and scaler"""
        if not CATBOOST_AVAILABLE:
            logger.error("❌ CatBoost not installed")
            return False

        try:
            if not os.path.exists(model_path):
                logger.warning(f"Model file not found: {model_path}")
                return False

            # Load model
            self.model = CatBoostClassifier()
            self.model.load_model(model_path)

            # Load scaler
            if os.path.exists(scaler_path):
                with open(scaler_path, 'rb') as f:
                    self.scaler = pickle.load(f)

            logger.info(f"✅ CatBoost loaded from {model_path}")
            return True

        except Exception as e:
            logger.error(f"Failed to load CatBoost: {e}")
            return False

    def get_feature_importance(self):
        """Get feature importance"""
        if self.model is None:
            return None

        try:
            importance = self.model.get_feature_importance()
            return importance
        except Exception as e:
            logger.error(f"Failed to get feature importance: {e}")
            return None
