#!/usr/bin/env python3
# ============================================
# 🧪 TEST VOLUME FARMING CONFIGURATION
# Chạy backtest với cấu hình volume farming
# ============================================

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backtest.enhanced_backtester import EnhancedBacktester
from ml.ensemble import EnsemblePredictor
from ml.features import FeatureEngine
from config import Config
from utils.logger import logger

def print_header(title):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)

def print_config_summary():
    """Print current configuration summary"""
    print_header("📋 CẤU HÌNH HIỆN TẠI")
    
    config_items = [
        ("Symbols", f"{len(Config.SYMBOLS)} pairs: {', '.join(Config.SYMBOLS[:3])}..."),
        ("Leverage", f"{Config.LEVERAGE}x"),
        ("Position Size", f"${Config.POSITION_SIZE_USDT} USDT" if Config.POSITION_SIZE_USDT else f"{Config.SIZE_PCT*100}% balance"),
        ("Take Profit", f"{Config.TP_PCT}%"),
        ("Stop Loss", "Disabled" if not Config.SL_PCT or Config.SL_PCT == 0 else f"{Config.SL_PCT}%"),
        ("Loop Sleep", f"{Config.LOOP_SLEEP}s"),
        ("LSTM Threshold", f"{Config.LSTM_THRESHOLD}"),
        ("Min Confluence", f"{Config.MIN_CONFLUENCE_SCORE}"),
        ("Signal Filters", "Enabled" if Config.USE_SIGNAL_FILTERS else "Disabled"),
        ("Trend Filter", "Enabled" if Config.USE_TREND_FILTER else "Disabled"),
        ("Volume Filter", "Enabled" if Config.USE_VOLUME_FILTER else "Disabled"),
        ("Trailing Stop", "Enabled" if Config.USE_TRAILING_STOP else "Disabled"),
        ("Market Regime", "Enabled" if Config.USE_MARKET_REGIME else "Disabled"),
        ("Position Timeout", f"{Config.POSITION_TIMEOUT_HOURS}h"),
    ]
    
    for key, value in config_items:
        print(f"  {key:<20}: {value}")
    
    print("="*70)

def calculate_projections(results, days=30):
    """Calculate monthly projections"""
    if not results or results['total_trades'] == 0:
        return None
    
    # Calculate per-day metrics
    trades_per_day = results['total_trades'] / days
    volume_per_day = results['total_volume'] / days
    
    # Project to 30 days
    monthly_trades = trades_per_day * 30
    monthly_volume = volume_per_day * 30
    
    # Calculate profit (assuming $10 position, 10x leverage, 1% TP)
    # Each winning trade = $1 profit
    winning_trades = monthly_trades * (results['win_rate'] / 100)
    losing_trades = monthly_trades - winning_trades
    
    # Average loss per losing trade (in $)
    avg_loss_pct = abs(results['avg_loss']) if results['avg_loss'] < 0 else 0
    avg_loss_usd = (avg_loss_pct / 100) * 10  # $10 position
    
    monthly_profit = (winning_trades * 1.0) - (losing_trades * avg_loss_usd)
    
    return {
        'monthly_trades': monthly_trades,
        'monthly_volume': monthly_volume,
        'monthly_profit': monthly_profit,
        'winning_trades': winning_trades,
        'losing_trades': losing_trades,
    }

def print_results_summary(results, days=30):
    """Print backtest results summary"""
    print_header("📊 KẾT QUẢ BACKTEST")
    
    print(f"\n  Thời gian: {days} ngày")
    print(f"  Tổng trades: {results['total_trades']}")
    print(f"  Win rate: {results['win_rate']:.2f}%")
    print(f"  Total PnL: {results['total_pnl']:.2f}%")
    print(f"  Total Volume: ${results['total_volume']/1e6:.2f}M")
    print(f"  Profit Factor: {results['profit_factor']:.2f}")
    
    print(f"\n  Winning trades: {results['winning_trades']}")
    print(f"  Losing trades: {results['losing_trades']}")
    print(f"  Avg win: {results['avg_win']:.2f}%")
    print(f"  Avg loss: {results['avg_loss']:.2f}%")
    print(f"  Max win: {results['max_win']:.2f}%")
    print(f"  Max loss: {results['max_loss']:.2f}%")
    
    # Projections
    projections = calculate_projections(results, days)
    if projections:
        print_header("📈 DỰ ĐOÁN THÁNG (30 NGÀY)")
        
        print(f"\n  Trades/tháng: {projections['monthly_trades']:.1f}")
        print(f"    - Winning: {projections['winning_trades']:.1f}")
        print(f"    - Losing: {projections['losing_trades']:.1f}")
        
        print(f"\n  Volume/tháng: ${projections['monthly_volume']/1e6:.2f}M")
        print(f"  Profit/tháng: ${projections['monthly_profit']:.2f}")
        
        # ROI calculation (assuming $100 starting balance)
        roi = (projections['monthly_profit'] / 100) * 100
        print(f"  ROI/tháng: {roi:.1f}%")
        
        # Per-symbol breakdown
        if 'symbol_results' in results:
            print_header("📊 KẾT QUẢ THEO SYMBOL")
            
            symbol_data = []
            for symbol, data in results['symbol_results'].items():
                symbol_data.append({
                    'symbol': symbol,
                    'trades': data['trades'],
                    'win_rate': data['win_rate'] * 100,
                    'pnl': data['pnl_pct'],
                    'volume': data['volume']
                })
            
            # Sort by trades
            symbol_data.sort(key=lambda x: x['trades'], reverse=True)
            
            print(f"\n  {'Symbol':<12} {'Trades':<8} {'Win%':<8} {'PnL%':<10} {'Volume'}")
            print("  " + "-"*60)
            
            for data in symbol_data:
                print(f"  {data['symbol']:<12} {data['trades']:<8} {data['win_rate']:<8.1f} {data['pnl']:<10.2f} ${data['volume']/1000:.1f}k")

def print_recommendations(results):
    """Print recommendations based on results"""
    print_header("💡 KHUYẾN NGHỊ")
    
    trades = results['total_trades']
    win_rate = results['win_rate']
    
    recommendations = []
    
    # Check trades
    if trades < 15:
        recommendations.append("⚠️  Số lượng trades thấp (<15). Đề xuất:")
        recommendations.append("   - Giảm LSTM_THRESHOLD xuống 0.35-0.38")
        recommendations.append("   - Giảm MIN_CONFLUENCE_SCORE xuống 2")
        recommendations.append("   - Tắt thêm filters")
    elif trades > 40:
        recommendations.append("⚠️  Số lượng trades cao (>40). Có thể overtrading:")
        recommendations.append("   - Tăng LSTM_THRESHOLD lên 0.45")
        recommendations.append("   - Tăng MIN_CONFLUENCE_SCORE lên 4")
        recommendations.append("   - Tăng LOOP_SLEEP lên 60s")
    else:
        recommendations.append("✅ Số lượng trades tốt (15-40)")
    
    # Check win rate
    if win_rate < 50:
        recommendations.append("\n⚠️  Win rate thấp (<50%). Đề xuất:")
        recommendations.append("   - Tăng LSTM_THRESHOLD lên 0.45-0.50")
        recommendations.append("   - Bật lại TREND_FILTER")
        recommendations.append("   - Tăng MIN_SIGNAL_QUALITY_SCORE lên 40-50")
    elif win_rate > 70:
        recommendations.append("\n✅ Win rate cao (>70%). Có thể:")
        recommendations.append("   - Giảm threshold để tăng trades")
        recommendations.append("   - Vẫn giữ nguyên nếu muốn an toàn")
    else:
        recommendations.append("\n✅ Win rate tốt (50-70%)")
    
    # Check profit factor
    if results['profit_factor'] < 1.0:
        recommendations.append("\n❌ Profit factor <1.0 (thua lỗ). KHÔNG nên chạy!")
        recommendations.append("   - Cần tối ưu lại cấu hình")
    elif results['profit_factor'] < 1.3:
        recommendations.append("\n⚠️  Profit factor thấp (<1.3). Cần cải thiện:")
        recommendations.append("   - Tăng chất lượng tín hiệu")
        recommendations.append("   - Giảm số lượng trades")
    else:
        recommendations.append(f"\n✅ Profit factor tốt ({results['profit_factor']:.2f})")
    
    # Overall recommendation
    if trades >= 15 and win_rate >= 55 and results['profit_factor'] >= 1.3:
        recommendations.append("\n" + "="*70)
        recommendations.append("🎯 KẾT LUẬN: CẤU HÌNH TỐT - SẴN SÀNG CHẠY!")
        recommendations.append("="*70)
    else:
        recommendations.append("\n" + "="*70)
        recommendations.append("⚠️  KẾT LUẬN: CẦN TỐI ƯU THÊM TRƯỚC KHI CHẠY")
        recommendations.append("="*70)
    
    for rec in recommendations:
        print(f"  {rec}")

def main():
    """Main function"""
    print_header("🚀 VOLUME FARMING BACKTEST")
    
    # Print config
    print_config_summary()
    
    # Load models
    logger.info("🧠 Loading ML models...")
    
    if Config.USE_ENSEMBLE:
        predictor = EnsemblePredictor(
            models=Config.ENSEMBLE_MODELS,
            weights=Config.ENSEMBLE_WEIGHTS,
            input_size=len(FeatureEngine.FEATURE_COLUMNS)
        )
        
        if not predictor.load_models():
            logger.error("❌ Ensemble models chưa được train!")
            logger.error("   Chạy: python ml/train_ensemble.py")
            return
        
        backtester = EnhancedBacktester(
            ensemble_predictor=predictor,
            initial_capital=Config.BACKTEST_INITIAL_CAPITAL
        )
    else:
        from ml.lstm_model import LSTMTrainer
        trainer = LSTMTrainer(input_size=len(FeatureEngine.FEATURE_COLUMNS))
        
        if not trainer.load():
            logger.error("❌ LSTM model chưa được train!")
            logger.error("   Chạy: python ml/train.py")
            return
        
        backtester = EnhancedBacktester(
            lstm_trainer=trainer,
            initial_capital=Config.BACKTEST_INITIAL_CAPITAL
        )
    
    # Run backtest
    logger.info(f"📊 Running backtest for {Config.BACKTEST_DAYS} days...")
    results = backtester.run_backtest(
        symbols=Config.SYMBOLS,
        days=Config.BACKTEST_DAYS
    )
    
    if not results:
        logger.error("❌ Backtest failed!")
        return
    
    # Print results
    print_results_summary(results, Config.BACKTEST_DAYS)
    
    # Print recommendations
    print_recommendations(results)
    
    print("\n")

if __name__ == '__main__':
    main()

