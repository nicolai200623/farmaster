# ============================================
# 🎓 TRAINING SCRIPT
# Train LSTM model với historical data
# ============================================

import sys
import os
# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from utils.data_fetcher import DataFetcher
from ml.features import FeatureEngine
from ml.lstm_model import LSTMTrainer
from config import Config
from utils.logger import logger

def train_model(symbols=None, days=365, test_size=0.2):
    """
    Train LSTM model
    
    Args:
        symbols: List symbols để train
        days: Số ngày historical data
        test_size: Tỷ lệ test set
    """
    symbols = symbols or Config.SYMBOLS
    
    logger.info("=" * 60)
    logger.info("🎓 BẮT ĐẦU TRAINING LSTM MODEL")
    logger.info("=" * 60)
    
    # 1. Fetch historical data
    logger.info(f"📊 Fetching data for {len(symbols)} symbols...")
    data_dict = DataFetcher.fetch_multiple_symbols(symbols, days=days)
    
    if not data_dict:
        logger.error("❌ Không lấy được data!")
        return None
    
    # 2. Combine và calculate features
    logger.info("🔬 Calculating features...")
    combined_df = DataFetcher.combine_dataframes(data_dict)
    
    # Calculate indicators cho từng symbol
    processed_dfs = []
    for symbol in symbols:
        if symbol in data_dict:
            df = data_dict[symbol].copy()
            df = FeatureEngine.calculate_indicators(df)
            processed_dfs.append(df)
    
    # Combine lại
    all_data = pd.concat(processed_dfs, ignore_index=True)
    logger.info(f"✅ Total data points: {len(all_data)}")
    
    # 3. Prepare features
    feature_df = FeatureEngine.prepare_features(all_data)
    
    # 4. Normalize
    trainer = LSTMTrainer(input_size=len(FeatureEngine.FEATURE_COLUMNS))
    normalized_data = trainer.scaler.fit_transform(feature_df.values)
    
    # 5. Create sequences
    logger.info(f"🔄 Creating sequences (length={Config.SEQUENCE_LENGTH})...")
    X, y = FeatureEngine.create_sequences(normalized_data, seq_length=Config.SEQUENCE_LENGTH)
    
    logger.info(f"   X shape: {X.shape}")
    logger.info(f"   y shape: {y.shape}")
    logger.info(f"   UP samples: {y.sum()} ({y.sum()/len(y)*100:.1f}%)")
    logger.info(f"   DOWN samples: {len(y)-y.sum()} ({(len(y)-y.sum())/len(y)*100:.1f}%)")
    
    # 6. Split train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, shuffle=True, random_state=42
    )
    
    logger.info(f"📚 Train set: {len(X_train)} samples")
    logger.info(f"📝 Test set: {len(X_test)} samples")
    
    # 7. Train
    trainer.train(X_train, y_train, epochs=Config.LSTM_EPOCHS)
    
    # 8. Evaluate
    logger.info("\n📊 EVALUATING MODEL...")
    y_pred_proba = trainer.predict(X_test)
    y_pred = (y_pred_proba > 0.5).astype(int)
    
    accuracy = (y_pred == y_test).sum() / len(y_test)
    
    # Confusion matrix
    tp = ((y_pred == 1) & (y_test == 1)).sum()
    tn = ((y_pred == 0) & (y_test == 0)).sum()
    fp = ((y_pred == 1) & (y_test == 0)).sum()
    fn = ((y_pred == 0) & (y_test == 1)).sum()
    
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    
    logger.info(f"✅ Test Accuracy: {accuracy*100:.2f}%")
    logger.info(f"   Precision: {precision*100:.2f}%")
    logger.info(f"   Recall: {recall*100:.2f}%")
    logger.info(f"   F1 Score: {f1*100:.2f}%")
    logger.info(f"   TP: {tp}, TN: {tn}, FP: {fp}, FN: {fn}")
    
    # 9. Save model
    trainer.save()
    
    logger.info("=" * 60)
    logger.info("🎉 TRAINING HOÀN TẤT!")
    logger.info("=" * 60)
    
    return trainer

if __name__ == '__main__':
    # Validate config
    Config.validate()
    
    # Train model
    trainer = train_model(
        symbols=Config.SYMBOLS,
        days=365,
        test_size=0.2
    )
    
    if trainer:
        logger.info("✅ Model đã sẵn sàng để trading!")

