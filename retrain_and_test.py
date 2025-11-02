#!/usr/bin/env python3
"""
Retrain LSTM model và chạy backtest để verify improvements
"""

import os
import sys
from config import Config
from utils.logger import logger

def main():
    """Main workflow"""
    logger.info("=" * 60)
    logger.info("🔄 RETRAIN & TEST WORKFLOW")
    logger.info("=" * 60)
    
    # Step 1: Validate config
    logger.info("\n📋 Step 1: Validating config...")
    Config.validate()
    
    logger.info(f"\n📊 Current Settings:")
    logger.info(f"   TP: {Config.TP_PCT*100}%")
    logger.info(f"   SL: {Config.SL_PCT*100}%")
    logger.info(f"   LSTM Threshold: {Config.LSTM_THRESHOLD}")
    logger.info(f"   LSTM Epochs: {Config.LSTM_EPOCHS}")
    logger.info(f"   Symbols: {', '.join(Config.SYMBOLS)}")
    
    # Step 2: Train model
    logger.info("\n" + "=" * 60)
    logger.info("🎓 Step 2: Training LSTM Model...")
    logger.info("=" * 60)
    
    from ml.train import train_model
    
    trainer = train_model(
        symbols=Config.SYMBOLS,
        days=365,  # 1 year of data
        test_size=0.2
    )
    
    if not trainer:
        logger.error("❌ Training failed!")
        return False
    
    # Step 3: Run backtest
    logger.info("\n" + "=" * 60)
    logger.info("📈 Step 3: Running Backtest...")
    logger.info("=" * 60)

    from backtest.backtester import Backtester
    from ml.features import FeatureEngine
    
    backtester = Backtester(
        lstm_trainer=trainer,
        initial_capital=Config.BACKTEST_INITIAL_CAPITAL
    )
    
    results = backtester.run_backtest(
        symbols=Config.SYMBOLS,
        days=Config.BACKTEST_DAYS
    )
    
    # Step 4: Analyze results
    logger.info("\n" + "=" * 60)
    logger.info("📊 Step 4: Analysis & Recommendations")
    logger.info("=" * 60)
    
    total_trades = results['total_trades']
    win_rate = results['win_rate']
    total_pnl = results['total_pnl']
    profit_factor = results['profit_factor']
    
    logger.info(f"\n📈 Results Summary:")
    logger.info(f"   Total Trades: {total_trades}")
    logger.info(f"   Win Rate: {win_rate:.2f}%")
    logger.info(f"   Total PnL: {total_pnl:.2f}%")
    logger.info(f"   Profit Factor: {profit_factor:.2f}")
    
    # Recommendations
    logger.info(f"\n💡 Recommendations:")
    
    if total_trades < 5:
        logger.warning("⚠️  Too few trades! Consider:")
        logger.warning("   - Lower LSTM_THRESHOLD (current: {})".format(Config.LSTM_THRESHOLD))
        logger.warning("   - Lower MIN_SIGNAL_SCORE")
        logger.warning("   - Add more symbols")
    
    if win_rate < 40:
        logger.warning("⚠️  Low win rate! Consider:")
        logger.warning("   - Widen SL (current: {}%)".format(Config.SL_PCT*100))
        logger.warning("   - Retrain model with more data")
        logger.warning("   - Check signal logic")
    
    if total_pnl < 0:
        logger.error("❌ Negative PnL! Strategy needs work:")
        logger.error("   - Review entry/exit logic")
        logger.error("   - Optimize TP/SL ratio")
        logger.error("   - Consider different strategy")
    
    # Final verdict
    logger.info("\n" + "=" * 60)
    
    if total_pnl > 10 and win_rate > 50 and profit_factor > 1.5:
        logger.info("✅ EXCELLENT! Strategy is ready for live trading!")
        logger.info("   Consider starting with small position size.")
    elif total_pnl > 0 and win_rate > 40 and profit_factor > 1.0:
        logger.info("✅ GOOD! Strategy shows promise.")
        logger.info("   Consider paper trading first.")
    elif total_pnl > -5 and win_rate > 30:
        logger.warning("⚠️  NEEDS IMPROVEMENT but has potential.")
        logger.warning("   Continue optimizing parameters.")
    else:
        logger.error("❌ POOR PERFORMANCE! Do NOT use live!")
        logger.error("   Major strategy overhaul needed.")
    
    logger.info("=" * 60)
    
    return True

if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        logger.info("\n⚠️  Interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

