#!/usr/bin/env python3
# ============================================
# 🧪 TEST SIGNAL GENERATOR
# Test signal generation cho symbols
# ============================================

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config
from trading.asterdex_client import AsterDEXClient
from trading.signal_generator import SignalGenerator
from ml.lstm_model import LSTMTrainer
from ml.features import FeatureEngine
from utils.logger import logger

def main():
    """Test signal generation"""
    Config.validate()
    
    logger.info("=" * 60)
    logger.info("🧪 TESTING SIGNAL GENERATOR")
    logger.info("=" * 60)
    
    # Load model
    logger.info("\n🧠 Loading LSTM model...")
    lstm_trainer = LSTMTrainer(input_size=len(FeatureEngine.FEATURE_COLUMNS))
    
    if not lstm_trainer.load():
        logger.error("❌ Model not found! Run: python ml/train.py")
        return
    
    # Initialize
    client = AsterDEXClient()
    signal_gen = SignalGenerator(lstm_trainer)
    
    # Test each symbol
    logger.info("\n📡 GENERATING SIGNALS...\n")
    
    for symbol in Config.SYMBOLS:
        logger.info(f"{'='*60}")
        signal = signal_gen.generate_signal(client, symbol)
        logger.info(f"{'='*60}\n")
    
    logger.info("✅ Test completed!")

if __name__ == '__main__':
    main()

