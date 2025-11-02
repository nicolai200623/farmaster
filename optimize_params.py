#!/usr/bin/env python3
"""
Grid search để tìm parameters tối ưu cho strategy
"""

import os
import sys
import itertools
from config import Config
from utils.logger import logger
from backtest.backtester import Backtester
from ml.lstm_model import LSTMTrainer
from ml.features import FeatureEngine

def test_params(lstm_trainer, tp_pct, sl_pct, lstm_threshold, min_signal_score):
    """
    Test một bộ parameters
    
    Returns:
        dict: Results
    """
    # Temporarily override config
    original_tp = Config.TP_PCT
    original_sl = Config.SL_PCT
    original_threshold = Config.LSTM_THRESHOLD
    original_min_score = Config.MIN_SIGNAL_SCORE
    
    try:
        Config.TP_PCT = tp_pct
        Config.SL_PCT = sl_pct
        Config.LSTM_THRESHOLD = lstm_threshold
        Config.MIN_SIGNAL_SCORE = min_signal_score
        
        # Run backtest
        backtester = Backtester(
            lstm_trainer=lstm_trainer,
            initial_capital=Config.BACKTEST_INITIAL_CAPITAL
        )
        
        results = backtester.run_backtest(
            symbols=Config.SYMBOLS[:2],  # Only test on BTC and ETH for speed
            days=30
        )
        
        return results
        
    finally:
        # Restore original config
        Config.TP_PCT = original_tp
        Config.SL_PCT = original_sl
        Config.LSTM_THRESHOLD = original_threshold
        Config.MIN_SIGNAL_SCORE = original_min_score

def main():
    """Main optimization workflow"""
    logger.info("=" * 60)
    logger.info("🔍 PARAMETER OPTIMIZATION")
    logger.info("=" * 60)
    
    # Load model
    logger.info("🧠 Loading LSTM model...")
    lstm_trainer = LSTMTrainer(input_size=len(FeatureEngine.FEATURE_COLUMNS))
    
    if not lstm_trainer.load():
        logger.error("❌ Model chưa được train!")
        logger.info("💡 Chạy: python ml/train.py")
        return False
    
    # Define parameter grid
    param_grid = {
        'tp_pct': [0.02, 0.03, 0.04],
        'sl_pct': [0.01, 0.015, 0.02],
        'lstm_threshold': [0.5, 0.55, 0.6],
        'min_signal_score': [1, 2]
    }
    
    logger.info(f"\n📊 Parameter Grid:")
    for key, values in param_grid.items():
        logger.info(f"   {key}: {values}")
    
    # Calculate total combinations
    total_combinations = 1
    for values in param_grid.values():
        total_combinations *= len(values)
    
    logger.info(f"\n🔢 Total combinations: {total_combinations}")
    logger.info(f"⏱️  Estimated time: ~{total_combinations * 2} minutes")
    
    # Grid search
    logger.info("\n" + "=" * 60)
    logger.info("🔍 Starting grid search...")
    logger.info("=" * 60)
    
    best_result = None
    best_params = None
    best_score = -float('inf')
    
    results_list = []
    
    count = 0
    for tp, sl, threshold, min_score in itertools.product(
        param_grid['tp_pct'],
        param_grid['sl_pct'],
        param_grid['lstm_threshold'],
        param_grid['min_signal_score']
    ):
        count += 1
        
        logger.info(f"\n[{count}/{total_combinations}] Testing:")
        logger.info(f"   TP={tp*100}%, SL={sl*100}%, Threshold={threshold}, MinScore={min_score}")
        
        try:
            results = test_params(lstm_trainer, tp, sl, threshold, min_score)
            
            # Calculate score (weighted combination of metrics)
            # Score = PnL * 0.5 + WinRate * 0.3 + ProfitFactor * 0.2
            score = (
                results['total_pnl'] * 0.5 +
                results['win_rate'] * 0.3 +
                results['profit_factor'] * 20 * 0.2
            )
            
            logger.info(f"   Trades: {results['total_trades']}")
            logger.info(f"   Win Rate: {results['win_rate']:.2f}%")
            logger.info(f"   PnL: {results['total_pnl']:.2f}%")
            logger.info(f"   Profit Factor: {results['profit_factor']:.2f}")
            logger.info(f"   Score: {score:.2f}")
            
            # Save result
            results_list.append({
                'params': {
                    'tp_pct': tp,
                    'sl_pct': sl,
                    'lstm_threshold': threshold,
                    'min_signal_score': min_score
                },
                'results': results,
                'score': score
            })
            
            # Update best
            if score > best_score:
                best_score = score
                best_result = results
                best_params = {
                    'tp_pct': tp,
                    'sl_pct': sl,
                    'lstm_threshold': threshold,
                    'min_signal_score': min_score
                }
                logger.info(f"   🌟 NEW BEST!")
                
        except Exception as e:
            logger.error(f"   ❌ Error: {e}")
            continue
    
    # Print results
    logger.info("\n" + "=" * 60)
    logger.info("📊 OPTIMIZATION RESULTS")
    logger.info("=" * 60)
    
    if best_params:
        logger.info(f"\n🏆 BEST PARAMETERS:")
        logger.info(f"   TP: {best_params['tp_pct']*100}%")
        logger.info(f"   SL: {best_params['sl_pct']*100}%")
        logger.info(f"   LSTM Threshold: {best_params['lstm_threshold']}")
        logger.info(f"   Min Signal Score: {best_params['min_signal_score']}")
        
        logger.info(f"\n📈 BEST RESULTS:")
        logger.info(f"   Total Trades: {best_result['total_trades']}")
        logger.info(f"   Win Rate: {best_result['win_rate']:.2f}%")
        logger.info(f"   Total PnL: {best_result['total_pnl']:.2f}%")
        logger.info(f"   Profit Factor: {best_result['profit_factor']:.2f}")
        logger.info(f"   Score: {best_score:.2f}")
        
        logger.info(f"\n💡 To use these parameters, update .env:")
        logger.info(f"   TP_PCT={best_params['tp_pct']}")
        logger.info(f"   SL_PCT={best_params['sl_pct']}")
        logger.info(f"   LSTM_THRESHOLD={best_params['lstm_threshold']}")
        logger.info(f"   # And update MIN_SIGNAL_SCORE in config.py to {best_params['min_signal_score']}")
    else:
        logger.error("❌ No valid results found!")
    
    # Print top 5
    logger.info(f"\n📊 TOP 5 PARAMETER SETS:")
    sorted_results = sorted(results_list, key=lambda x: x['score'], reverse=True)[:5]
    
    for i, item in enumerate(sorted_results, 1):
        params = item['params']
        results = item['results']
        score = item['score']
        
        logger.info(f"\n#{i} (Score: {score:.2f})")
        logger.info(f"   TP={params['tp_pct']*100}%, SL={params['sl_pct']*100}%, "
                   f"Threshold={params['lstm_threshold']}, MinScore={params['min_signal_score']}")
        logger.info(f"   Trades: {results['total_trades']}, "
                   f"WinRate: {results['win_rate']:.1f}%, "
                   f"PnL: {results['total_pnl']:.1f}%")
    
    logger.info("\n" + "=" * 60)
    
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

