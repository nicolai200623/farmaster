# ============================================
# 💡 LIGHTGBM MODEL
# Fast gradient boosting with leaf-wise tree growth
# ============================================

import numpy as np
import pickle
import os
from sklearn.preprocessing import MinMaxScaler
from utils.logger import logger
from config import Config

try:
    import lightgbm as lgb
    LIGHTGBM_AVAILABLE = True
except ImportError:
    LIGHTGBM_AVAILABLE = False
    logger.warning("⚠️ LightGBM not installed. Install: pip install lightgbm")


class LightGBMTrainer:
    """
    LightGBM model for price direction prediction

    Advantages over XGBoost:
    - Faster training speed
    - Lower memory usage
    - Better accuracy on large datasets
    - Leaf-wise tree growth (vs level-wise)
    """

    def __init__(self, input_size):
        """
        Initialize LightGBM trainer

        Args:
            input_size: Number of input features
        """
        self.input_size = input_size
        self.model = None
        self.scaler = MinMaxScaler()

        if not LIGHTGBM_AVAILABLE:
            logger.error("❌ LightGBM not available!")
        else:
            logger.info(f"💡 LightGBM Trainer initialized with {input_size} features")

    def train(self, X_train, y_train, X_val=None, y_val=None):
        """
        Train LightGBM model

        Args:
            X_train: Training features (n_samples, seq_len, features) or (n_samples, features)
            y_train: Training labels
            X_val: Validation features (optional)
            y_val: Validation labels (optional)
        """
        if not LIGHTGBM_AVAILABLE:
            logger.error("❌ Cannot train - LightGBM not installed")
            return

        try:
            # Reshape if needed (flatten sequence dimension)
            if len(X_train.shape) == 3:
                # Take last timestep or flatten
                X_train = X_train[:, -1, :]  # Use last timestep
                if X_val is not None and len(X_val.shape) == 3:
                    X_val = X_val[:, -1, :]

            # Scale features
            X_train_scaled = self.scaler.fit_transform(X_train)
            if X_val is not None:
                X_val_scaled = self.scaler.transform(X_val)

            # LightGBM parameters (optimized for anti-overfitting)
            params = {
                'objective': 'binary',
                'metric': 'binary_logloss',
                'boosting_type': 'gbdt',
                'num_leaves': 31,  # Default, good for most cases
                'learning_rate': 0.05,
                'feature_fraction': 0.7,  # Column sampling
                'bagging_fraction': 0.7,  # Row sampling
                'bagging_freq': 5,
                'min_child_samples': 20,  # Min data in leaf
                'lambda_l1': 0.5,  # L1 regularization
                'lambda_l2': 1.0,  # L2 regularization
                'verbose': -1,
                'seed': 42,
            }

            # Create datasets
            train_data = lgb.Dataset(X_train_scaled, label=y_train)
            valid_sets = [train_data]
            valid_names = ['train']

            if X_val is not None and y_val is not None:
                val_data = lgb.Dataset(X_val_scaled, label=y_val, reference=train_data)
                valid_sets.append(val_data)
                valid_names.append('valid')

            # Train
            logger.info("🏋️ Training LightGBM model...")
            self.model = lgb.train(
                params,
                train_data,
                num_boost_round=300,
                valid_sets=valid_sets,
                valid_names=valid_names,
                callbacks=[
                    lgb.early_stopping(stopping_rounds=30),
                    lgb.log_evaluation(period=50)
                ]
            )

            # Calculate accuracy
            y_pred = (self.model.predict(X_train_scaled) > 0.5).astype(int)
            train_acc = (y_pred == y_train).mean()

            logger.info(f"✅ LightGBM training completed!")
            logger.info(f"   Train accuracy: {train_acc:.2%}")

            if X_val is not None:
                y_val_pred = (self.model.predict(X_val_scaled) > 0.5).astype(int)
                val_acc = (y_val_pred == y_val).mean()
                logger.info(f"   Val accuracy: {val_acc:.2%}")

        except Exception as e:
            logger.error(f"LightGBM training error: {e}")
            raise

    def predict(self, X):
        """
        Predict probability

        Args:
            X: Features (seq_len, features) or (batch, seq_len, features)

        Returns:
            Probability of price going UP
        """
        if self.model is None:
            logger.warning("Model not loaded!")
            return 0.5

        try:
            # Handle different input shapes
            if len(X.shape) == 3:
                # Take last timestep
                X = X[:, -1, :]
            elif len(X.shape) == 2 and X.shape[0] != 1:
                # Single sample (seq_len, features)
                X = X[-1:, :]  # Take last timestep

            # Reshape to 2D if needed
            if len(X.shape) == 1:
                X = X.reshape(1, -1)

            # Scale
            X_scaled = self.scaler.transform(X)

            # Predict
            pred = self.model.predict(X_scaled)

            return pred[0] if len(pred) > 0 else 0.5

        except Exception as e:
            logger.error(f"LightGBM prediction error: {e}")
            return 0.5

    def save(self, model_path, scaler_path):
        """Save model and scaler"""
        if self.model is None:
            logger.warning("No model to save")
            return

        try:
            # Create directory
            os.makedirs(os.path.dirname(model_path), exist_ok=True)

            # Save model
            self.model.save_model(model_path)

            # Save scaler
            with open(scaler_path, 'wb') as f:
                pickle.dump(self.scaler, f)

            logger.info(f"💾 LightGBM saved to {model_path}")

        except Exception as e:
            logger.error(f"Failed to save LightGBM: {e}")

    def load(self, model_path, scaler_path):
        """Load model and scaler"""
        if not LIGHTGBM_AVAILABLE:
            logger.error("❌ LightGBM not installed")
            return False

        try:
            if not os.path.exists(model_path):
                logger.warning(f"Model file not found: {model_path}")
                return False

            # Load model
            self.model = lgb.Booster(model_file=model_path)

            # Load scaler
            if os.path.exists(scaler_path):
                with open(scaler_path, 'rb') as f:
                    self.scaler = pickle.load(f)

            logger.info(f"✅ LightGBM loaded from {model_path}")
            return True

        except Exception as e:
            logger.error(f"Failed to load LightGBM: {e}")
            return False

    def get_feature_importance(self):
        """Get feature importance"""
        if self.model is None:
            return None

        try:
            importance = self.model.feature_importance(importance_type='gain')
            return importance
        except Exception as e:
            logger.error(f"Failed to get feature importance: {e}")
            return None
