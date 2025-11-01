#!/usr/bin/env python3
# ============================================
# 📈 RUN BACKTEST
# Chạy backtest để đánh giá strategy
# ============================================

import os
import sys
# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from config import Config
from utils.logger import logger
from ml.lstm_model import LSTMTrainer
from ml.features import FeatureEngine
from backtest.backtester import Backtester

def main():
    """Main backtest runner"""
    # Create directories
    os.makedirs('logs', exist_ok=True)
    os.makedirs('models', exist_ok=True)
    
    logger.info("=" * 60)
    logger.info("📈 ASTERDEX BOT - BACKTEST MODE")
    logger.info("=" * 60)
    
    # Validate config
    Config.validate()
    
    # Load LSTM model
    logger.info("🧠 Loading LSTM model...")
    lstm_trainer = LSTMTrainer(input_size=len(FeatureEngine.FEATURE_COLUMNS))
    
    if not lstm_trainer.load():
        logger.error("❌ Model chưa được train!")
        logger.info("💡 Chạy: python ml/train.py")
        sys.exit(1)
    
    # Create backtester
    backtester = Backtester(
        lstm_trainer=lstm_trainer,
        initial_capital=Config.BACKTEST_INITIAL_CAPITAL
    )
    
    # Run backtest
    results = backtester.run_backtest(
        symbols=Config.SYMBOLS,
        days=Config.BACKTEST_DAYS
    )
    
    if results:
        logger.info("\n✅ Backtest completed successfully!")
        
        # Recommendations
        if results['win_rate'] >= 60 and results['profit_factor'] >= 1.5:
            logger.info("🎉 Strategy looks GOOD! Ready for live trading.")
        elif results['win_rate'] >= 50:
            logger.info("⚠️ Strategy is OK, but consider optimization.")
        else:
            logger.info("❌ Strategy needs improvement. Do NOT use live!")
    else:
        logger.error("❌ Backtest failed!")

if __name__ == '__main__':
    main()

