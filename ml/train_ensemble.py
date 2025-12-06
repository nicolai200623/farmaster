#!/usr/bin/env python3
# ============================================
# 🎭 TRAIN ENSEMBLE MODELS
# Train XGBoost, LightGBM, CatBoost for ensemble
# Models configured in .env: ENSEMBLE_MODELS
# ============================================

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from sklearn.model_selection import train_test_split

from ml.xgboost_model import XGBoostTrainer
from ml.lightgbm_model import LightGBMTrainer
from ml.catboost_model import CatBoostTrainer
from ml.features import FeatureEngine
from utils.data_fetcher import DataFetcher
from config import Config
from utils.logger import logger

def train_ensemble_models(symbols=None, days=360):
    """
    Train ensemble models (XGBoost, LightGBM, CatBoost)

    Args:
        symbols: List of symbols to train on (default: read from Config.SYMBOLS)
        days: Historical data days
    """
    # Use symbols from Config if not provided
    if symbols is None:
        symbols = Config.SYMBOLS
    logger.info("="*60)
    logger.info("🎭 ENSEMBLE MODEL TRAINING")
    logger.info("="*60)

    logger.info(f"📊 Training configuration:")
    logger.info(f"   Models: {Config.ENSEMBLE_MODELS}")
    logger.info(f"   Weights: {Config.ENSEMBLE_WEIGHTS}")
    logger.info(f"   Symbols: {symbols}")
    logger.info(f"   Days: {days}")

    # 1. Fetch data
    logger.info("\n📥 Fetching historical data...")
    data_dict = DataFetcher.fetch_multiple_symbols(symbols, days=days)

    if not data_dict:
        logger.error("❌ No data fetched! Exiting...")
        return False

    # Combine all data
    import pandas as pd
    df_combined = DataFetcher.combine_dataframes(data_dict)
    logger.info(f"\n📊 Combined dataset: {len(df_combined)} candles")

    # 2. Calculate indicators
    logger.info("\n🔧 Calculating indicators...")
    feature_engine = FeatureEngine()
    df_combined = feature_engine.calculate_indicators(df_combined)

    # 3. Prepare features
    logger.info("\n🎯 Preparing features...")
    feature_df = feature_engine.prepare_features(df_combined)

    # 4. Create sequences for LSTM
    logger.info(f"\n📦 Creating sequences (length={Config.SEQUENCE_LENGTH})...")
    X, y = feature_engine.create_sequences(
        data=feature_df.values,
        seq_length=Config.SEQUENCE_LENGTH
    )

    logger.info(f"   Sequences: {X.shape}")
    logger.info(f"   Labels: {y.shape}")
    logger.info(f"   Label distribution: UP={np.sum(y)}, DOWN={len(y)-np.sum(y)}")

    # 5. Train/Val split
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, shuffle=False
    )

    logger.info(f"\n✂️ Data split:")
    logger.info(f"   Train: {X_train.shape[0]} samples")
    logger.info(f"   Val: {X_val.shape[0]} samples")

    # 6. Train models
    results = {}

    for model_name in Config.ENSEMBLE_MODELS:
        logger.info(f"\n{'='*60}")
        logger.info(f"Training {model_name.upper()} model...")
        logger.info(f"{'='*60}")

        try:
            if model_name == 'lstm':
                # Train LSTM
                lstm_trainer = LSTMTrainer(
                    input_size=X_train.shape[2],
                    hidden_size=Config.LSTM_HIDDEN_SIZE,
                    num_layers=Config.LSTM_NUM_LAYERS
                )

                # Fit scaler on training data (flatten for scaler)
                # Reshape from (samples, seq_len, features) to (samples*seq_len, features)
                X_train_flat = X_train.reshape(-1, X_train.shape[2])
                lstm_trainer.scaler.fit(X_train_flat)
                logger.info(f"   ✅ Scaler fitted on training data")

                lstm_trainer.train(
                    X_train, y_train,
                    epochs=Config.LSTM_EPOCHS,
                    batch_size=32,
                    lr=Config.LSTM_LEARNING_RATE
                )

                # Evaluate on validation set
                y_val_pred = lstm_trainer.predict(X_val)
                y_val_pred_binary = (y_val_pred > 0.5).astype(int)
                val_acc = (y_val_pred_binary == y_val).sum() / len(y_val)

                # Save LSTM
                lstm_trainer.save(Config.MODEL_PATH, Config.SCALER_PATH)

                results['lstm'] = {'val_acc': val_acc}

                logger.info(f"✅ LSTM training complete!")
                logger.info(f"   Val Acc: {val_acc:.4f}")

            elif model_name == 'xgboost':
                # Train XGBoost
                xgb_trainer = XGBoostTrainer(input_size=X_train.shape[2])

                history = xgb_trainer.train(
                    X_train, y_train,
                    X_val, y_val,
                    epochs=Config.XGBOOST_N_ESTIMATORS
                )

                # Save XGBoost
                xgb_model_path = Config.MODEL_PATH.replace('lstm_model.pt', 'xgboost_model.json')
                xgb_scaler_path = Config.SCALER_PATH.replace('scaler.pkl', 'xgboost_scaler.pkl')
                xgb_trainer.save(xgb_model_path, xgb_scaler_path)
                results['xgboost'] = history

                logger.info(f"✅ XGBoost training complete!")
                logger.info(f"   Val AUC: {history.get('val_auc', 0):.4f}")

                # Feature importance
                xgb_trainer.get_feature_importance(
                    feature_names=FeatureEngine.FEATURE_COLUMNS,
                    top_n=10
                )

            elif model_name == 'lightgbm':
                # Train LightGBM
                lgb_trainer = LightGBMTrainer(input_size=X_train.shape[2])

                lgb_trainer.train(
                    X_train, y_train,
                    X_val, y_val
                )

                # Save LightGBM
                lgb_model_path = Config.MODEL_PATH.replace('lstm_model.pt', 'lightgbm_model.txt')
                lgb_scaler_path = Config.SCALER_PATH.replace('scaler.pkl', 'lightgbm_scaler.pkl')
                lgb_trainer.save(lgb_model_path, lgb_scaler_path)

                # Calculate validation accuracy
                y_val_pred = lgb_trainer.predict(X_val)
                y_val_pred_binary = (y_val_pred > 0.5).astype(int)
                val_acc = (y_val_pred_binary == y_val).sum() / len(y_val)
                results['lightgbm'] = {'val_acc': val_acc}

                logger.info(f"✅ LightGBM training complete!")
                logger.info(f"   Val Acc: {val_acc:.4f}")

            elif model_name == 'catboost':
                # Train CatBoost
                cb_trainer = CatBoostTrainer(input_size=X_train.shape[2])

                cb_trainer.train(
                    X_train, y_train,
                    X_val, y_val
                )

                # Save CatBoost
                cb_model_path = Config.MODEL_PATH.replace('lstm_model.pt', 'catboost_model.cbm')
                cb_scaler_path = Config.SCALER_PATH.replace('scaler.pkl', 'catboost_scaler.pkl')
                cb_trainer.save(cb_model_path, cb_scaler_path)

                # Calculate validation accuracy
                y_val_pred = cb_trainer.predict(X_val)
                y_val_pred_binary = (y_val_pred > 0.5).astype(int)
                val_acc = (y_val_pred_binary == y_val).sum() / len(y_val)
                results['catboost'] = {'val_acc': val_acc}

                logger.info(f"✅ CatBoost training complete!")
                logger.info(f"   Val Acc: {val_acc:.4f}")

        except Exception as e:
            logger.error(f"❌ Failed to train {model_name}: {e}")
            import traceback
            traceback.print_exc()
            continue

    # 7. Summary
    logger.info(f"\n{'='*60}")
    logger.info("📊 TRAINING SUMMARY")
    logger.info(f"{'='*60}")

    for model_name, history in results.items():
        logger.info(f"\n{model_name.upper()}:")
        for metric, value in history.items():
            if isinstance(value, (int, float)):
                logger.info(f"   {metric}: {value:.4f}")

    logger.info(f"\n✅ Ensemble training complete!")
    logger.info(f"   Trained models: {list(results.keys())}")
    logger.info(f"   Ready for ensemble prediction!")

    return True

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Train ensemble models')
    parser.add_argument('--symbols', type=str, default=None,
                        help='Comma-separated list of symbols (default: from .env SYMBOLS)')
    parser.add_argument('--days', type=int, default=360,
                        help='Days of historical data')

    args = parser.parse_args()

    # Parse symbols if provided via command line
    symbols = args.symbols.split(',') if args.symbols else None

    success = train_ensemble_models(symbols=symbols, days=args.days)

    if success:
        logger.info("\n🎉 SUCCESS! You can now run the bot with ensemble:")
        logger.info("   python bot.py")
        sys.exit(0)
    else:
        logger.error("\n❌ FAILED! Check errors above")
        sys.exit(1)
