#!/usr/bin/env python3
# ============================================
# 🔄 AUTO RETRAIN SCRIPT
# Automatically retrain all models with latest data
# ============================================

import os
import sys
# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split

from config import Config
from utils.logger import logger
from trading.asterdex_client import AsterDEXClient
from ml.features import FeatureEngine
from ml.lstm_model import LSTMTrainer
from ml.xgboost_model import XGBoostTrainer
from ml.lightgbm_model import LightGBMTrainer
from ml.catboost_model import CatBoostTrainer
from ml.ensemble import EnsemblePredictor


class AutoRetrainer:
    """
    Automatically retrain models with latest market data

    Features:
    - Fetch latest data from exchange
    - Train all models in ensemble
    - Save trained models
    - Log training metrics
    """

    def __init__(self, days=90):
        """
        Initialize retrainer

        Args:
            days: Number of days of historical data to fetch
        """
        self.days = days
        self.client = AsterDEXClient()
        self.feature_engine = FeatureEngine()

        logger.info(f"🔄 Auto Retrainer initialized")
        logger.info(f"   Training data: Last {days} days")
        logger.info(f"   Symbols: {Config.SYMBOLS}")

    def fetch_training_data(self, symbol, days=90):
        """
        Fetch training data for a symbol using multiple batches

        This method fetches historical data in batches to overcome the 1500 candle API limit.
        It uses startTime and endTime parameters to fetch data from different time periods.

        Args:
            symbol: Trading symbol
            days: Days of history (can be 90, 180, or any number)

        Returns:
            DataFrame with OHLCV data
        """
        import time

        logger.info(f"📥 Fetching {days} days of data for {symbol}...")

        # AsterDEX API limit: max 1500 candles per request
        # 1 day = 96 candles (24h * 4 candles/hour for 15m interval)
        # For 90 days: 90 * 96 = 8640 candles → need 6 batches
        # For 180 days: 180 * 96 = 17280 candles → need 12 batches

        max_candles_per_batch = 1500
        candles_per_day = 96
        interval_minutes = 15

        # Calculate total candles needed
        total_candles_needed = days * candles_per_day

        # Calculate number of batches
        num_batches = (total_candles_needed + max_candles_per_batch - 1) // max_candles_per_batch

        logger.info(f"   Total candles needed: {total_candles_needed}")
        logger.info(f"   Fetching in {num_batches} batches...")

        # Calculate time range
        end_time = int(time.time() * 1000)  # Current time in milliseconds
        start_time = end_time - (days * 24 * 60 * 60 * 1000)  # days ago

        all_klines = []

        try:
            # Fetch data in batches from oldest to newest
            current_start = start_time

            for batch_num in range(num_batches):
                # Calculate end time for this batch
                # Each batch covers max_candles_per_batch * interval_minutes
                batch_duration_ms = max_candles_per_batch * interval_minutes * 60 * 1000
                current_end = min(current_start + batch_duration_ms, end_time)

                logger.info(f"   Batch {batch_num + 1}/{num_batches}: Fetching from {pd.to_datetime(current_start, unit='ms')} to {pd.to_datetime(current_end, unit='ms')}")

                # Fetch this batch using Binance client with startTime and endTime
                try:
                    batch_klines = self.client.client.futures_klines(
                        symbol=symbol,
                        interval='15m',
                        startTime=current_start,
                        endTime=current_end,
                        limit=max_candles_per_batch
                    )

                    if batch_klines:
                        all_klines.extend(batch_klines)
                        logger.info(f"      ✅ Fetched {len(batch_klines)} candles")
                    else:
                        logger.warning(f"      ⚠️ No data in this batch")

                except Exception as e:
                    logger.error(f"      ❌ Error fetching batch {batch_num + 1}: {e}")
                    # Continue with next batch instead of failing completely

                # Move to next batch
                current_start = current_end

                # Rate limiting: wait between batches to avoid API ban
                if batch_num < num_batches - 1:
                    wait_time = 0.5  # 500ms between requests
                    time.sleep(wait_time)

                # Stop if we've reached the end time
                if current_start >= end_time:
                    break

            if not all_klines:
                logger.error(f"❌ No data received for {symbol}")
                return None

            # Parse klines
            df = pd.DataFrame(all_klines, columns=[
                'timestamp', 'open', 'high', 'low', 'close', 'volume',
                'close_time', 'quote_volume', 'trades', 'taker_buy_base',
                'taker_buy_quote', 'ignore'
            ])

            # Convert to float
            for col in ['open', 'high', 'low', 'close', 'volume']:
                df[col] = df[col].astype(float)

            # Keep only OHLCV
            df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]

            # Remove duplicates (in case of overlapping batches)
            df = df.drop_duplicates(subset=['timestamp'], keep='first')

            # Sort by timestamp
            df = df.sort_values('timestamp').reset_index(drop=True)

            actual_days = len(df) / candles_per_day
            logger.info(f"✅ Fetched {len(df)} candles for {symbol} (~{actual_days:.1f} days)")

            return df

        except Exception as e:
            logger.error(f"❌ Error fetching data for {symbol}: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return None

    def prepare_training_data(self):
        """
        Prepare training data from all symbols

        Returns:
            X, y arrays for training
        """
        logger.info("🔧 Preparing training data...")

        all_sequences = []
        all_labels = []

        for symbol in Config.SYMBOLS:
            logger.info(f"\n📊 Processing {symbol}...")

            # Fetch data
            df = self.fetch_training_data(symbol, self.days)

            if df is None or len(df) < 100:
                logger.warning(f"⚠️ Skipping {symbol} - insufficient data")
                continue

            # Calculate indicators
            df = self.feature_engine.calculate_indicators(df)

            # Prepare features
            feature_df = self.feature_engine.prepare_features(df)

            # Create sequences
            X_symbol, y_symbol = self.feature_engine.create_sequences(
                feature_df.values,
                seq_length=Config.SEQUENCE_LENGTH
            )

            logger.info(f"   Created {len(X_symbol)} sequences")

            all_sequences.append(X_symbol)
            all_labels.append(y_symbol)

        if not all_sequences:
            logger.error("❌ No training data collected!")
            return None, None

        # Combine all data
        X = np.vstack(all_sequences)
        y = np.concatenate(all_labels)

        logger.info(f"\n✅ Total training data:")
        logger.info(f"   Sequences: {len(X)}")
        logger.info(f"   Features: {X.shape[2]}")
        logger.info(f"   UP samples: {(y==1).sum()} ({(y==1).mean()*100:.1f}%)")
        logger.info(f"   DOWN samples: {(y==0).sum()} ({(y==0).mean()*100:.1f}%)")

        return X, y

    def train_all_models(self, X_train, y_train, X_val, y_val):
        """
        Train all models in ensemble

        Args:
            X_train, y_train: Training data
            X_val, y_val: Validation data

        Returns:
            Dict of trained models
        """
        logger.info("\n🏋️ Training all models...\n")

        models = {}
        input_size = X_train.shape[2]

        # ============================================
        # 🔧 FIT SCALER TRƯỚC KHI TRAINING
        # ============================================
        from sklearn.preprocessing import MinMaxScaler
        import pickle

        logger.info("📊 Fitting scaler on training data...")

        # Reshape X_train từ (n_samples, seq_len, features) thành (n_samples * seq_len, features)
        n_samples, seq_len, n_features = X_train.shape
        X_train_2d = X_train.reshape(-1, n_features)

        # Fit scaler
        scaler = MinMaxScaler()
        scaler.fit(X_train_2d)

        # Save scaler
        scaler_path = Config.SCALER_PATH
        os.makedirs(os.path.dirname(scaler_path), exist_ok=True)
        with open(scaler_path, 'wb') as f:
            pickle.dump(scaler, f)

        logger.info(f"✅ Scaler fitted and saved to {scaler_path}")
        logger.info(f"   n_features: {scaler.n_features_in_}")

        # Normalize training data
        X_train_normalized = scaler.transform(X_train_2d).reshape(n_samples, seq_len, n_features)

        # Normalize validation data
        n_val_samples = X_val.shape[0]
        X_val_2d = X_val.reshape(-1, n_features)
        X_val_normalized = scaler.transform(X_val_2d).reshape(n_val_samples, seq_len, n_features)

        logger.info(f"✅ Data normalized: train={X_train_normalized.shape}, val={X_val_normalized.shape}\n")

        # 1. LSTM
        if 'lstm' in Config.ENSEMBLE_MODELS:
            logger.info("=" * 60)
            logger.info("🧠 Training LSTM...")
            logger.info("=" * 60)

            lstm_trainer = LSTMTrainer(input_size=input_size)
            # Assign the fitted scaler to the trainer
            lstm_trainer.scaler = scaler
            lstm_trainer.train(X_train_normalized, y_train, epochs=Config.LSTM_EPOCHS)
            lstm_trainer.save(Config.MODEL_PATH, Config.SCALER_PATH)
            models['lstm'] = lstm_trainer

            logger.info("✅ LSTM training completed\n")

        # 2. XGBoost
        if 'xgboost' in Config.ENSEMBLE_MODELS:
            logger.info("=" * 60)
            logger.info("🚀 Training XGBoost...")
            logger.info("=" * 60)

            xgb_trainer = XGBoostTrainer(input_size=input_size)
            xgb_trainer.train(X_train, y_train, X_val, y_val)

            xgb_model_path = Config.MODEL_PATH.replace('lstm_model.pt', 'xgboost_model.json')
            xgb_scaler_path = Config.SCALER_PATH.replace('scaler.pkl', 'xgboost_scaler.pkl')
            xgb_trainer.save(xgb_model_path, xgb_scaler_path)
            models['xgboost'] = xgb_trainer

            logger.info("✅ XGBoost training completed\n")

        # 3. LightGBM
        if 'lightgbm' in Config.ENSEMBLE_MODELS:
            logger.info("=" * 60)
            logger.info("💡 Training LightGBM...")
            logger.info("=" * 60)

            lgb_trainer = LightGBMTrainer(input_size=input_size)
            lgb_trainer.train(X_train, y_train, X_val, y_val)

            lgb_model_path = Config.MODEL_PATH.replace('lstm_model.pt', 'lightgbm_model.txt')
            lgb_scaler_path = Config.SCALER_PATH.replace('scaler.pkl', 'lightgbm_scaler.pkl')
            lgb_trainer.save(lgb_model_path, lgb_scaler_path)
            models['lightgbm'] = lgb_trainer

            logger.info("✅ LightGBM training completed\n")

        # 4. CatBoost
        if 'catboost' in Config.ENSEMBLE_MODELS:
            logger.info("=" * 60)
            logger.info("🐱 Training CatBoost...")
            logger.info("=" * 60)

            cb_trainer = CatBoostTrainer(input_size=input_size)
            cb_trainer.train(X_train, y_train, X_val, y_val)

            cb_model_path = Config.MODEL_PATH.replace('lstm_model.pt', 'catboost_model.cbm')
            cb_scaler_path = Config.SCALER_PATH.replace('scaler.pkl', 'catboost_scaler.pkl')
            cb_trainer.save(cb_model_path, cb_scaler_path)
            models['catboost'] = cb_trainer

            logger.info("✅ CatBoost training completed\n")

        return models

    def run(self):
        """
        Run full retraining pipeline
        """
        try:
            logger.info("=" * 60)
            logger.info("🔄 AUTO RETRAIN STARTED")
            logger.info("=" * 60)
            logger.info(f"   Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logger.info(f"   Models: {Config.ENSEMBLE_MODELS}")
            logger.info("=" * 60 + "\n")

            # 1. Fetch and prepare data
            X, y = self.prepare_training_data()

            if X is None:
                logger.error("❌ Failed to prepare training data")
                return False

            # 2. Split data
            logger.info("\n📊 Splitting data...")
            X_train, X_val, y_train, y_val = train_test_split(
                X, y,
                test_size=0.2,
                shuffle=False  # Time series - no shuffle!
            )

            logger.info(f"   Train: {len(X_train)} samples")
            logger.info(f"   Val: {len(X_val)} samples")

            # 3. Train models
            models = self.train_all_models(X_train, y_train, X_val, y_val)

            if not models:
                logger.error("❌ No models trained")
                return False

            # 4. Test ensemble
            logger.info("\n" + "=" * 60)
            logger.info("🎭 Testing Ensemble...")
            logger.info("=" * 60)

            ensemble = EnsemblePredictor(
                models=Config.ENSEMBLE_MODELS,
                weights=Config.ENSEMBLE_WEIGHTS,
                input_size=X.shape[2]
            )

            if ensemble.load_models():
                # Test on validation set
                correct = 0
                total = len(X_val)

                for i in range(min(100, total)):  # Test on first 100 samples
                    pred = ensemble.predict(X_val[i])
                    pred_class = 1 if pred > 0.5 else 0
                    if pred_class == y_val[i]:
                        correct += 1

                test_accuracy = correct / min(100, total)
                logger.info(f"\n✅ Ensemble test accuracy: {test_accuracy:.2%}")

            # 5. Summary
            logger.info("\n" + "=" * 60)
            logger.info("✅ RETRAINING COMPLETED SUCCESSFULLY!")
            logger.info("=" * 60)
            logger.info(f"   Models trained: {len(models)}")
            logger.info(f"   Training samples: {len(X_train)}")
            logger.info(f"   Validation samples: {len(X_val)}")
            logger.info(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logger.info("=" * 60)

            return True

        except Exception as e:
            logger.error(f"\n❌ RETRAINING FAILED: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return False


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Auto retrain trading models')
    parser.add_argument('--days', type=int, default=90, help='Days of training data (default: 90)')
    args = parser.parse_args()

    retrainer = AutoRetrainer(days=args.days)
    success = retrainer.run()

    if success:
        logger.info("\n🎉 You can now restart the bot to use the new models!")
        sys.exit(0)
    else:
        logger.error("\n❌ Retraining failed. Check logs for details.")
        sys.exit(1)


if __name__ == '__main__':
    main()
