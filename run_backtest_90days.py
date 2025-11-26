#!/usr/bin/env python3
"""
📈 BACKTEST WITH 90-DAY TRAINED MODELS
Backtest script optimized for models trained with 90 days of data
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from config import Config
from utils.logger import logger
from ml.ensemble import EnsemblePredictor
from ml.features import FeatureEngine
from backtest.enhanced_backtester import EnhancedBacktester

def print_header():
    """Print backtest header"""
    print("\n" + "=" * 70)
    print("📈 BACKTEST - MODELS TRAINED WITH 90 DAYS DATA")
    print("=" * 70)
    print(f"📊 Backtest Period: {Config.BACKTEST_DAYS} days")
    print(f"💰 Initial Capital: ${Config.BACKTEST_INITIAL_CAPITAL:,.2f}")
    print(f"🎯 Symbols: {', '.join(Config.SYMBOLS)}")
    print(f"📈 Leverage: {Config.LEVERAGE}x")
    print(f"💵 Position Size: ${Config.POSITION_SIZE_USDT}")
    sl_pct = Config.SL_PCT if Config.SL_PCT is not None else 0
    print(f"🎯 TP: {Config.TP_PCT*100:.1f}% | SL: {sl_pct*100:.1f}%")
    print("=" * 70 + "\n")

def print_results(results):
    """Print detailed backtest results"""
    print("\n" + "=" * 70)
    print("📊 BACKTEST RESULTS")
    print("=" * 70)

    # Overall metrics
    print(f"\n💰 PERFORMANCE:")
    print(f"   Total Trades: {results['total_trades']}")
    print(f"   Win Rate: {results['win_rate']:.2f}%")
    print(f"   Total PnL: {results.get('total_pnl', results.get('total_pnl_pct', 0)):.2f}%")
    print(f"   Total Volume: ${results['total_volume']:,.2f}")

    # Risk metrics
    print(f"\n📈 RISK METRICS:")
    print(f"   Profit Factor: {results.get('profit_factor', 0):.2f}")
    print(f"   Max Drawdown: {results.get('max_drawdown', 0):.2f}%")
    print(f"   Sharpe Ratio: {results.get('sharpe_ratio', 0):.2f}")
    
    # Per-symbol breakdown
    if 'symbol_results' in results:
        print(f"\n📊 PER-SYMBOL BREAKDOWN:")
        for symbol, data in results['symbol_results'].items():
            print(f"\n   {symbol}:")
            print(f"      Trades: {data['trades']}")
            print(f"      Win Rate: {data['win_rate']*100:.1f}%")
            print(f"      PnL: {data['pnl_pct']:.2f}%")
            print(f"      Volume: ${data['volume']:,.2f}")
    
    print("\n" + "=" * 70)

def print_recommendations(results):
    """Print trading recommendations"""
    print("\n" + "=" * 70)
    print("💡 RECOMMENDATIONS")
    print("=" * 70)
    
    win_rate = results['win_rate']
    profit_factor = results.get('profit_factor', 0)
    total_trades = results['total_trades']
    
    if win_rate >= 55 and profit_factor >= 1.3 and total_trades >= 20:
        print("\n✅ EXCELLENT - Ready for live trading!")
        print("   • Win rate is good (>55%)")
        print("   • Profit factor is healthy (>1.3)")
        print("   • Sufficient trade sample (>20)")
        print("\n🚀 Next Steps:")
        print("   1. Start with testnet: TESTNET_MODE=true")
        print("   2. Monitor for 24-48 hours")
        print("   3. If stable, switch to mainnet")
        
    elif win_rate >= 50 and profit_factor >= 1.2:
        print("\n⚠️ GOOD - But needs monitoring")
        print("   • Win rate is acceptable (>50%)")
        print("   • Profit factor is okay (>1.2)")
        print("\n🔧 Suggestions:")
        print("   1. Test on testnet first")
        print("   2. Consider tightening entry filters")
        print("   3. Monitor closely for first week")
        
    elif win_rate >= 45:
        print("\n⚠️ MARGINAL - Needs optimization")
        print("   • Win rate is low (<50%)")
        print("   • Strategy needs improvement")
        print("\n🔧 Suggestions:")
        print("   1. Retrain with more data (180 days)")
        print("   2. Adjust MIN_CONFLUENCE_SCORE")
        print("   3. Review symbol selection")
        
    else:
        print("\n❌ POOR - DO NOT USE LIVE!")
        print("   • Win rate is too low (<45%)")
        print("   • Strategy is not profitable")
        print("\n🔧 Required Actions:")
        print("   1. Retrain models with 180 days data")
        print("   2. Review and optimize parameters")
        print("   3. Consider different symbols")
        print("   4. Backtest again before going live")
    
    print("\n" + "=" * 70)

def main():
    """Main backtest runner"""
    # Create directories
    os.makedirs('logs', exist_ok=True)
    os.makedirs('models', exist_ok=True)
    
    # Print header
    print_header()
    
    # Validate config
    logger.info("🔧 Validating configuration...")
    Config.validate()
    
    # Load ensemble models
    logger.info("🎭 Loading Ensemble models...")
    ensemble = EnsemblePredictor(
        models=Config.ENSEMBLE_MODELS,
        weights=Config.ENSEMBLE_WEIGHTS,
        input_size=len(FeatureEngine.FEATURE_COLUMNS)
    )
    
    if not ensemble.load_models():
        logger.error("❌ Ensemble models not found!")
        logger.error("   Models should be trained with 90 days data")
        logger.error("   Run: python scripts/auto_retrain.py --days 90")
        sys.exit(1)
    
    logger.info("✅ Models loaded successfully")
    
    # Create backtester
    logger.info(f"📊 Initializing backtester...")
    backtester = EnhancedBacktester(
        ensemble_predictor=ensemble,
        initial_capital=Config.BACKTEST_INITIAL_CAPITAL
    )

    # Run backtest
    logger.info(f"🚀 Running backtest for {Config.BACKTEST_DAYS} days...")
    logger.info(f"   This may take 2-5 minutes depending on data size...")

    results = backtester.run_backtest(
        symbols=Config.SYMBOLS,
        days=Config.BACKTEST_DAYS
    )

    if not results:
        logger.error("❌ Backtest failed!")
        sys.exit(1)

    # Print results
    print_results(results)

    # Print recommendations
    print_recommendations(results)

    # Save results to file
    import json
    from datetime import datetime

    results_file = f"backtest_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(results_file, 'w') as f:
        # Convert numpy types to native Python types for JSON serialization
        json_results = {}
        for key, value in results.items():
            if isinstance(value, dict):
                json_results[key] = {k: float(v) if hasattr(v, 'item') else v for k, v in value.items()}
            else:
                json_results[key] = float(value) if hasattr(value, 'item') else value
        json.dump(json_results, f, indent=2)

    logger.info(f"\n💾 Results saved to: {results_file}")

    print("\n✅ Backtest completed successfully!\n")

if __name__ == '__main__':
    main()


