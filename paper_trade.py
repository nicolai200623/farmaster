#!/usr/bin/env python3
"""
🧪 PAPER TRADING MODE - Test Entry Pipeline với Testnet

Chạy Entry Pipeline với testnet để validate trước khi chạy mainnet.

Usage:
    python paper_trade.py --symbol BTCUSDT --hours 4
    python paper_trade.py --all-symbols --hours 8
"""

import sys
import os
import argparse
import time
from datetime import datetime
from typing import Optional, List

import pandas as pd

from config import Config
from trading.entry_pipeline import EntryPipeline, SignalDirection
from utils.data_fetcher import DataFetcher
from ml.features import FeatureEngine
from utils.logger import logger


class PaperTrader:
    """Paper trading with Entry Pipeline validation"""

    def __init__(self, symbols: List[str] = None):
        self.symbols = symbols or Config.SYMBOLS[:3]  # Default top 3

        # Initialize feature engine for indicators
        self.feature_engine = FeatureEngine()

        # Initialize pipeline with config
        config = {
            'use_ml_ensemble': Config.USE_ML_ENSEMBLE,
            'ml_confidence_threshold': Config.ML_CONFIDENCE_THRESHOLD,
            'use_price_action': Config.USE_PRICE_ACTION,
            'min_price_action_score': Config.MIN_PRICE_ACTION_SCORE,
            'use_htf_alignment': Config.USE_HTF_ALIGNMENT,
            'use_ai_check': Config.USE_AI_CHECK,
            'min_entry_score': Config.MIN_ENTRY_SCORE,
            'min_rr_ratio': Config.MIN_RR_RATIO,
        }
        self.pipeline = EntryPipeline(config=config)
        
        # Stats
        self.signals_generated = 0
        self.signals_approved = 0
        self.trades_opened = 0
        self.trades_closed = 0
        self.total_pnl = 0.0
        
        # Active paper positions
        self.positions = {}  # symbol -> {entry, direction, time}
        
        logger.info(f"🧪 Paper Trader initialized (TESTNET)")
        logger.info(f"   Symbols: {self.symbols}")

    def fetch_data(self, symbol: str) -> tuple:
        """Fetch 1H and 4H data for symbol"""
        try:
            # Fetch 1H data
            df_1h = DataFetcher.fetch_historical_ohlcv(symbol, days=7)
            if df_1h.empty:
                return None, None

            # Calculate indicators
            df_1h = self.feature_engine.calculate_indicators(df_1h)

            # Create 4H data (use same data for simplicity)
            df_4h = df_1h.copy()

            return df_1h, df_4h
        except Exception as e:
            logger.error(f"Failed to fetch data for {symbol}: {e}")
            return None, None

    def check_signal(self, symbol: str):
        """Check for entry signal on symbol"""
        logger.info(f"\n📊 Checking {symbol}...")
        
        # Fetch data
        df_1h, df_4h = self.fetch_data(symbol)
        if df_1h is None:
            return
        
        self.signals_generated += 1
        
        # Run through Entry Pipeline
        decision = self.pipeline.evaluate(
            symbol=symbol,
            df=df_1h,
            df_higher=df_4h
        )
        
        if decision.should_enter:
            self.signals_approved += 1
            logger.info(f"✅ SIGNAL APPROVED: {decision.direction.value}")
            logger.info(f"   Confidence: {decision.confidence:.2%}")
            logger.info(f"   Entry: ${decision.entry_price:.2f}")
            logger.info(f"   SL: ${decision.stop_loss:.2f}")
            logger.info(f"   TP: ${decision.take_profit:.2f}")
            
            # Open paper position
            if symbol not in self.positions:
                self.positions[symbol] = {
                    'entry': decision.entry_price,
                    'direction': decision.direction,
                    'sl': decision.stop_loss,
                    'tp': decision.take_profit,
                    'time': datetime.now(),
                    'confidence': decision.confidence
                }
                self.trades_opened += 1
                logger.info(f"📝 Paper position OPENED: {symbol} {decision.direction.value}")
        else:
            logger.info(f"❌ Signal rejected: {decision.reason}")

    def check_exits(self, symbol: str):
        """Check if paper position should be closed"""
        if symbol not in self.positions:
            return
        
        pos = self.positions[symbol]
        
        # Get current price
        try:
            df = DataFetcher.fetch_historical_ohlcv(symbol, days=1)
            if df.empty:
                return
            current_price = df['close'].iloc[-1]
        except Exception:
            return
        
        # Calculate PnL
        if pos['direction'] == SignalDirection.LONG:
            pnl_pct = (current_price - pos['entry']) / pos['entry'] * 100 * Config.LEVERAGE
            hit_tp = current_price >= pos['tp']
            hit_sl = current_price <= pos['sl']
        else:
            pnl_pct = (pos['entry'] - current_price) / pos['entry'] * 100 * Config.LEVERAGE
            hit_tp = current_price <= pos['tp']
            hit_sl = current_price >= pos['sl']
        
        # Check TP/SL
        if hit_tp:
            self.total_pnl += pnl_pct
            self.trades_closed += 1
            logger.info(f"🎯 TP HIT: {symbol} PnL: +{pnl_pct:.2f}%")
            del self.positions[symbol]
        elif hit_sl:
            self.total_pnl += pnl_pct
            self.trades_closed += 1
            logger.info(f"🛑 SL HIT: {symbol} PnL: {pnl_pct:.2f}%")
            del self.positions[symbol]

    def run(self, hours: float = 4):
        """Run paper trading for specified hours"""
        logger.info(f"\n{'='*60}")
        logger.info(f"🚀 Starting Paper Trading for {hours} hours")
        logger.info(f"{'='*60}")
        
        end_time = time.time() + (hours * 3600)
        loop_count = 0
        
        try:
            while time.time() < end_time:
                loop_count += 1
                logger.info(f"\n📍 Loop #{loop_count} - {datetime.now()}")
                
                for symbol in self.symbols:
                    # Check exits first
                    self.check_exits(symbol)
                    
                    # Check new signals
                    if symbol not in self.positions:
                        self.check_signal(symbol)
                    
                    time.sleep(1)  # Rate limit
                
                # Print stats
                self.print_stats()
                
                # Wait before next loop
                logger.info(f"💤 Sleeping {Config.LOOP_SLEEP}s...")
                time.sleep(Config.LOOP_SLEEP)
                
        except KeyboardInterrupt:
            logger.info("\n⌨️ Stopped by user")
        
        self.print_final_stats()

    def print_stats(self):
        """Print current stats"""
        win_rate = self.signals_approved / max(self.signals_generated, 1) * 100
        logger.info(f"\n📊 Stats: Signals={self.signals_generated}, Approved={self.signals_approved} ({win_rate:.1f}%)")
        logger.info(f"   Trades: Opened={self.trades_opened}, Closed={self.trades_closed}")
        logger.info(f"   Active positions: {list(self.positions.keys())}")
        logger.info(f"   Total PnL: {self.total_pnl:+.2f}%")

    def print_final_stats(self):
        """Print final summary"""
        logger.info(f"\n{'='*60}")
        logger.info(f"📊 PAPER TRADING SUMMARY")
        logger.info(f"{'='*60}")
        logger.info(f"   Total Signals: {self.signals_generated}")
        logger.info(f"   Approved: {self.signals_approved}")
        logger.info(f"   Pass Rate: {self.signals_approved/max(self.signals_generated,1)*100:.1f}%")
        logger.info(f"   Trades Opened: {self.trades_opened}")
        logger.info(f"   Trades Closed: {self.trades_closed}")
        logger.info(f"   Total PnL: {self.total_pnl:+.2f}%")

        # Pipeline metrics
        metrics = self.pipeline.get_metrics()
        logger.info(f"\n📈 Pipeline Metrics:")
        for stage, rate in metrics.get('stage_pass_rates', {}).items():
            logger.info(f"   {stage}: {rate:.1f}%")


def main():
    parser = argparse.ArgumentParser(description='Paper Trading with Entry Pipeline')
    parser.add_argument('--symbol', type=str, help='Single symbol to trade')
    parser.add_argument('--all-symbols', action='store_true', help='Trade all config symbols')
    parser.add_argument('--hours', type=float, default=4, help='Hours to run (default: 4)')

    args = parser.parse_args()

    if args.symbol:
        symbols = [args.symbol]
    elif args.all_symbols:
        symbols = Config.SYMBOLS
    else:
        symbols = Config.SYMBOLS[:3]

    trader = PaperTrader(symbols=symbols)
    trader.run(hours=args.hours)


if __name__ == '__main__':
    main()

