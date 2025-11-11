# ============================================
# 🌳 XGBOOST MODEL
# Gradient Boosting model for price prediction
# ============================================

import numpy as np
import pandas as pd
import pickle
import os
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
from utils.logger import logger

class XGBoostTrainer:
    """
    XGBoost model for price prediction
    - Fast training and inference
    - Good for tabular data
    - Handles missing values
    - Feature importance analysis
    """

    def __init__(self, input_size=None):
        """
        Initialize XGBoost trainer

        Args:
            input_size: Number of input features (for compatibility)
        """
        self.model = None
        self.scaler = StandardScaler()
        self.input_size = input_size
        self.feature_names = None

        # XGBoost parameters
        self.params = {
            'objective': 'binary:logistic',
            'eval_metric': 'auc',
            'max_depth': 6,
            'learning_rate': 0.05,
            'n_estimators': 200,
            'subsample': 0.8,
            'colsample_bytree': 0.8,
            'min_child_weight': 3,
            'gamma': 0.1,
            'reg_alpha': 0.1,
            'reg_lambda': 1.0,
            'random_state': 42,
            'n_jobs': -1,
            'tree_method': 'hist'  # Fast histogram-based algorithm
        }

    def train(self, X_train, y_train, X_val=None, y_val=None, epochs=200):
        """
        Train XGBoost model

        Args:
            X_train: Training features (n_samples, n_features) or (n_samples, seq_len, n_features)
            y_train: Training labels (n_samples,)
            X_val: Validation features
            y_val: Validation labels
            epochs: Number of boosting rounds (max iterations)

        Returns:
            dict: Training history
        """
        logger.info("🌳 Training XGBoost model...")

        # Flatten sequence data if needed (LSTM format)
        if len(X_train.shape) == 3:
            logger.info(f"   Reshaping from LSTM format: {X_train.shape}")
            # Take last timestep or aggregate
            X_train = X_train[:, -1, :]  # Use last timestep
            if X_val is not None and len(X_val.shape) == 3:
                X_val = X_val[:, -1, :]

        # Fit scaler on training data
        self.scaler.fit(X_train)
        X_train_scaled = self.scaler.transform(X_train)

        if X_val is not None:
            X_val_scaled = self.scaler.transform(X_val)

        # Create XGBoost model
        self.model = xgb.XGBClassifier(**self.params)

        # Training with early stopping if validation set provided
        if X_val is not None and y_val is not None:
            logger.info("   Training with early stopping...")
            eval_set = [(X_train_scaled, y_train), (X_val_scaled, y_val)]

            self.model.fit(
                X_train_scaled,
                y_train,
                eval_set=eval_set,
                early_stopping_rounds=20,
                verbose=False
            )

            # Get best iteration
            best_iteration = self.model.best_iteration
            logger.info(f"   Best iteration: {best_iteration}")

            # Evaluate
            train_pred = self.model.predict_proba(X_train_scaled)[:, 1]
            val_pred = self.model.predict_proba(X_val_scaled)[:, 1]

            from sklearn.metrics import roc_auc_score, accuracy_score
            train_auc = roc_auc_score(y_train, train_pred)
            val_auc = roc_auc_score(y_val, val_pred)
            train_acc = accuracy_score(y_train, train_pred > 0.5)
            val_acc = accuracy_score(y_val, val_pred > 0.5)

            logger.info(f"   Train AUC: {train_auc:.4f} | Val AUC: {val_auc:.4f}")
            logger.info(f"   Train Acc: {train_acc:.4f} | Val Acc: {val_acc:.4f}")

            history = {
                'train_auc': train_auc,
                'val_auc': val_auc,
                'train_acc': train_acc,
                'val_acc': val_acc,
                'best_iteration': best_iteration
            }
        else:
            logger.info("   Training without validation...")
            self.model.fit(X_train_scaled, y_train, verbose=False)

            train_pred = self.model.predict_proba(X_train_scaled)[:, 1]
            from sklearn.metrics import roc_auc_score, accuracy_score
            train_auc = roc_auc_score(y_train, train_pred)
            train_acc = accuracy_score(y_train, train_pred > 0.5)

            logger.info(f"   Train AUC: {train_auc:.4f}")
            logger.info(f"   Train Acc: {train_acc:.4f}")

            history = {
                'train_auc': train_auc,
                'train_acc': train_acc
            }

        logger.info("✅ XGBoost training complete!")
        return history

    def predict(self, X):
        """
        Predict probability

        Args:
            X: Input features (n_features,) or (seq_len, n_features)

        Returns:
            float: Probability of price going up (0-1)
        """
        if self.model is None:
            logger.error("Model not trained or loaded!")
            return 0.5

        # Handle different input shapes
        if len(X.shape) == 1:
            # Single sample: (n_features,)
            X = X.reshape(1, -1)
        elif len(X.shape) == 2:
            # Sequence: (seq_len, n_features) - take last timestep
            if X.shape[0] > 1:
                X = X[-1:, :]
        elif len(X.shape) == 3:
            # Batch of sequences: (batch, seq_len, n_features)
            X = X[:, -1, :]

        # Scale
        X_scaled = self.scaler.transform(X)

        # Predict
        prob = self.model.predict_proba(X_scaled)[:, 1]

        return prob

    def save(self, model_path='models/xgboost_model.json', scaler_path='models/xgboost_scaler.pkl'):
        """Save model and scaler"""
        if self.model is None:
            logger.error("No model to save!")
            return False

        try:
            # Create directory
            os.makedirs(os.path.dirname(model_path), exist_ok=True)

            # Save XGBoost model (JSON format)
            self.model.save_model(model_path)

            # Save scaler
            with open(scaler_path, 'wb') as f:
                pickle.dump(self.scaler, f)

            logger.info(f"✅ XGBoost model saved to {model_path}")
            return True

        except Exception as e:
            logger.error(f"Failed to save XGBoost model: {e}")
            return False

    def load(self, model_path='models/xgboost_model.json', scaler_path='models/xgboost_scaler.pkl'):
        """Load model and scaler"""
        try:
            if not os.path.exists(model_path):
                logger.warning(f"XGBoost model not found at {model_path}")
                return False

            # Load XGBoost model
            self.model = xgb.XGBClassifier()
            self.model.load_model(model_path)

            # Load scaler
            if os.path.exists(scaler_path):
                with open(scaler_path, 'rb') as f:
                    self.scaler = pickle.load(f)
            else:
                logger.warning(f"Scaler not found at {scaler_path}, using default")
                self.scaler = StandardScaler()

            logger.info(f"✅ XGBoost model loaded from {model_path}")
            return True

        except Exception as e:
            logger.error(f"Failed to load XGBoost model: {e}")
            return False

    def get_feature_importance(self, feature_names=None, top_n=10):
        """
        Get feature importance

        Args:
            feature_names: List of feature names
            top_n: Number of top features to return

        Returns:
            pd.DataFrame: Feature importance
        """
        if self.model is None:
            logger.error("Model not trained!")
            return None

        # Get importance
        importance = self.model.feature_importances_

        if feature_names is None:
            feature_names = [f'feature_{i}' for i in range(len(importance))]

        # Create DataFrame
        importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': importance
        }).sort_values('importance', ascending=False)

        if top_n:
            importance_df = importance_df.head(top_n)

        logger.info(f"\n📊 Top {top_n} Features:")
        for idx, row in importance_df.iterrows():
            logger.info(f"   {row['feature']}: {row['importance']:.4f}")

        return importance_df
