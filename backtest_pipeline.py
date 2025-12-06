# ============================================
# 📊 ENTRY PIPELINE BACKTEST
# Backtest Entry Pipeline với historical data
# Usage: python backtest_pipeline.py --symbol BTCUSDT --days 30
# ============================================

import os
import sys
import argparse
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
from dataclasses import dataclass, field

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import Config
from trading.asterdex_client import AsterDEXClient
from ml.features import FeatureEngine
from trading.entry_pipeline import EntryPipeline, SignalDirection
from utils.logger import logger


@dataclass
class BacktestTrade:
    """Single trade record"""
    timestamp: datetime
    symbol: str
    direction: str  # LONG or SHORT
    entry_price: float
    exit_price: float = 0.0
    pnl_pct: float = 0.0
    pnl_usdt: float = 0.0
    exit_reason: str = ""
    confidence: float = 0.0
    stages_passed: List[str] = field(default_factory=list)
    duration_hours: float = 0.0
    # Trailing stop tracking
    max_pnl_pct: float = 0.0
    trailing_activated: bool = False
    trailing_stop_price: float = 0.0


@dataclass 
class BacktestResult:
    """Backtest summary"""
    symbol: str
    start_date: datetime
    end_date: datetime
    total_trades: int
    winning_trades: int
    losing_trades: int
    win_rate: float
    total_pnl_pct: float
    avg_pnl_pct: float
    max_drawdown: float
    sharpe_ratio: float
    profit_factor: float
    avg_duration_hours: float
    trades: List[BacktestTrade] = field(default_factory=list)
    
    # Stage statistics
    stage_pass_rates: Dict[str, float] = field(default_factory=dict)
    signals_generated: int = 0
    signals_passed_pipeline: int = 0


class PipelineBacktester:
    """Backtest Entry Pipeline với historical data"""

    def __init__(
        self,
        symbol: str = "BTCUSDT",
        timeframe: str = "1h",
        days: int = 30,
        initial_balance: float = 1000.0,
        position_size_pct: float = 0.1,
        leverage: int = 10,
        tp_pct: float = 0.02,
        sl_pct: float = 0.01,
        custom_config: Dict = None,
        use_trailing_stop: bool = True,
        trailing_activation_pct: float = 2.5,
        trailing_distance_pct: float = 2.2,
        use_breakeven: bool = True,
        breakeven_activation_pct: float = 2.5,
        breakeven_offset_pct: float = 0.4
    ):
        self.symbol = symbol
        self.timeframe = timeframe
        self.days = days
        self.initial_balance = initial_balance
        self.position_size_pct = position_size_pct
        self.leverage = leverage
        self.tp_pct = tp_pct
        self.sl_pct = sl_pct

        # Trailing stop settings
        self.use_trailing_stop = use_trailing_stop
        self.trailing_activation_pct = trailing_activation_pct / 100  # Convert to decimal
        self.trailing_distance_pct = trailing_distance_pct / 100
        self.use_breakeven = use_breakeven
        self.breakeven_activation_pct = breakeven_activation_pct / 100
        self.breakeven_offset_pct = breakeven_offset_pct / 100

        # Initialize components
        self.client = AsterDEXClient()
        self.feature_engine = FeatureEngine()

        # Build pipeline config from Config class or custom
        self.pipeline_config = self._build_pipeline_config(custom_config)
        self.pipeline = EntryPipeline(self.pipeline_config)
        
        # Tracking
        self.balance = initial_balance
        self.trades: List[BacktestTrade] = []
        self.equity_curve: List[float] = [initial_balance]
        
        logger.info(f"📊 PipelineBacktester initialized")
        logger.info(f"   Symbol: {symbol}, TF: {timeframe}, Days: {days}")
        logger.info(f"   Balance: ${initial_balance}, Leverage: {leverage}x")
        if self.use_trailing_stop:
            logger.info(f"   Trailing: {trailing_activation_pct}% activation, {trailing_distance_pct}% distance")
    
    def _build_pipeline_config(self, custom_config: Dict = None) -> Dict:
        """Build pipeline config from Config class or custom config"""
        default_config = {
            # Stage 1: ML - Disabled for backtest (no models)
            'USE_ML_ENSEMBLE': False,
            'ML_CONFIDENCE_THRESHOLD': 0.55,
            'ML_NEUTRAL_ZONE': 0.08,

            # Stage 2: Smart Entry
            'USE_SMART_ENTRY': True,
            'MIN_ENTRY_SCORE': 5,
            'MIN_RR_RATIO': 1.5,

            # Stage 3: Price Action
            'USE_PRICE_ACTION': True,
            'MIN_PRICE_ACTION_SCORE': 4,
            'SR_LOOKBACK_CANDLES': 50,
            'SR_PROXIMITY_PCT': 0.8,
            'VOLUME_CONFIRMATION_RATIO': 1.3,

            # Stage 4: HTF
            'USE_HTF_ALIGNMENT': False,
            'HTF_TIMEFRAME': '4h',
            'REQUIRE_HTF_ALIGNMENT': False,
            'HTF_STRICT_MODE': False,

            # Stage 5: AI - Disabled
            'USE_AI_CHECK': False,
        }

        if custom_config:
            default_config.update(custom_config)

        return default_config
    
    def fetch_historical_data(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Fetch historical OHLCV data"""
        logger.info(f"📥 Fetching {self.days} days of historical data...")
        
        # Calculate candles needed
        candles_per_day = 24 if self.timeframe == '1h' else 6
        limit = min(self.days * candles_per_day, 1000)
        
        # Fetch 1H data
        klines_1h = self.client.get_klines(
            self.symbol, 
            interval='1h',
            limit=limit
        )
        df_1h = self._parse_klines(klines_1h)
        df_1h = self.feature_engine.calculate_indicators(df_1h)
        
        # Fetch 4H data
        klines_4h = self.client.get_klines(
            self.symbol,
            interval='4h', 
            limit=limit // 4
        )
        df_4h = self._parse_klines(klines_4h)
        df_4h = self.feature_engine.calculate_indicators(df_4h)
        
        logger.info(f"   ✅ Loaded {len(df_1h)} 1H candles, {len(df_4h)} 4H candles")

        return df_1h, df_4h

    def _parse_klines(self, klines: List) -> pd.DataFrame:
        """Parse klines to DataFrame"""
        df = pd.DataFrame(klines, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_volume', 'trades', 'taker_buy_base',
            'taker_buy_quote', 'ignore'
        ])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        for col in ['open', 'high', 'low', 'close', 'volume']:
            df[col] = df[col].astype(float)
        return df

    def run_backtest(self) -> BacktestResult:
        """Run the backtest"""
        logger.info(f"\n{'='*50}")
        logger.info(f"🚀 Starting Backtest: {self.symbol}")
        logger.info(f"{'='*50}\n")

        # Fetch data
        df_1h, df_4h = self.fetch_historical_data()

        # Skip warmup period (need at least 50 candles for indicators)
        warmup = 60
        signals_generated = 0
        signals_passed = 0
        stage_pass_counts = {'ml': 0, 'smart_entry': 0, 'price_action': 0, 'htf': 0}

        # Simulate trading
        in_position = False
        current_trade = None

        for i in range(warmup, len(df_1h)):
            current_time = df_1h['timestamp'].iloc[i]
            current_price = df_1h['close'].iloc[i]

            # Get data window
            df_window = df_1h.iloc[:i+1].copy()

            # Get corresponding 4H candle
            df_4h_window = df_4h[df_4h['timestamp'] <= current_time].copy()

            # Check if in position
            if in_position and current_trade:
                # Check TP/SL
                exit_price, exit_reason = self._check_exit(
                    current_trade, current_price
                )

                if exit_price:
                    # Close position
                    current_trade.exit_price = exit_price
                    current_trade.exit_reason = exit_reason

                    # Calculate PnL
                    if current_trade.direction == 'LONG':
                        pnl_pct = (exit_price - current_trade.entry_price) / current_trade.entry_price
                    else:
                        pnl_pct = (current_trade.entry_price - exit_price) / current_trade.entry_price

                    pnl_pct *= self.leverage
                    current_trade.pnl_pct = pnl_pct
                    current_trade.pnl_usdt = self.balance * self.position_size_pct * pnl_pct
                    current_trade.duration_hours = (current_time - current_trade.timestamp).total_seconds() / 3600

                    # Update balance
                    self.balance += current_trade.pnl_usdt
                    self.equity_curve.append(self.balance)
                    self.trades.append(current_trade)

                    logger.info(f"   📍 EXIT {current_trade.direction} @ ${exit_price:.2f}")
                    logger.info(f"      Reason: {exit_reason}, PnL: {pnl_pct*100:.2f}%")

                    in_position = False
                    current_trade = None
                    continue

            # Only look for new entry if not in position
            if not in_position:
                signals_generated += 1

                # Evaluate with pipeline
                decision = self.pipeline.evaluate(
                    symbol=self.symbol,
                    df=df_window,
                    df_4h=df_4h_window if len(df_4h_window) > 0 else None
                )

                # Debug: Log first few rejections
                if signals_generated <= 5:
                    logger.info(f"   📡 Signal #{signals_generated}: {decision.direction.value}")
                    logger.info(f"      Should Enter: {decision.should_enter}")
                    logger.info(f"      Reason: {decision.reason}")
                    logger.info(f"      Passed: {decision.stages_passed}")
                    logger.info(f"      Failed: {decision.stages_failed}")

                # Track stage passes
                for stage in decision.stages_passed:
                    stage_key = stage.lower().replace(' ', '_')
                    if stage_key in stage_pass_counts:
                        stage_pass_counts[stage_key] += 1

                if decision.should_enter:
                    signals_passed += 1

                    # Open position
                    current_trade = BacktestTrade(
                        timestamp=current_time,
                        symbol=self.symbol,
                        direction=decision.direction.value,
                        entry_price=current_price,
                        confidence=decision.confidence,
                        stages_passed=decision.stages_passed
                    )
                    in_position = True

                    logger.info(f"\n📈 {current_time.strftime('%Y-%m-%d %H:%M')}")
                    logger.info(f"   ENTER {decision.direction.value} @ ${current_price:.2f}")
                    logger.info(f"   Confidence: {decision.confidence:.2%}")

        # Calculate results
        return self._calculate_results(
            df_1h, signals_generated, signals_passed, stage_pass_counts
        )

    def _check_exit(self, trade: BacktestTrade, current_price: float) -> Tuple[float, str]:
        """Check if should exit position with trailing stop support"""
        # Calculate current PnL
        if trade.direction == 'LONG':
            pnl_pct = (current_price - trade.entry_price) / trade.entry_price * self.leverage
        else:
            pnl_pct = (trade.entry_price - current_price) / trade.entry_price * self.leverage

        # Update max PnL seen
        if pnl_pct > trade.max_pnl_pct:
            trade.max_pnl_pct = pnl_pct

        # === TRAILING STOP LOGIC ===
        if self.use_trailing_stop:
            # Check if trailing should be activated
            if not trade.trailing_activated and pnl_pct >= self.trailing_activation_pct:
                trade.trailing_activated = True
                # Set trailing stop price
                if trade.direction == 'LONG':
                    # Trail from current high
                    trade.trailing_stop_price = current_price * (1 - self.trailing_distance_pct / self.leverage)
                else:
                    trade.trailing_stop_price = current_price * (1 + self.trailing_distance_pct / self.leverage)

            # Update trailing stop if activated
            if trade.trailing_activated:
                if trade.direction == 'LONG':
                    # Move stop up if price moves up
                    new_stop = current_price * (1 - self.trailing_distance_pct / self.leverage)
                    if new_stop > trade.trailing_stop_price:
                        trade.trailing_stop_price = new_stop

                    # Check if hit trailing stop
                    if current_price <= trade.trailing_stop_price:
                        return current_price, "TRAIL"
                else:
                    # SHORT - move stop down if price moves down
                    new_stop = current_price * (1 + self.trailing_distance_pct / self.leverage)
                    if new_stop < trade.trailing_stop_price:
                        trade.trailing_stop_price = new_stop

                    # Check if hit trailing stop
                    if current_price >= trade.trailing_stop_price:
                        return current_price, "TRAIL"

        # === BREAKEVEN LOGIC ===
        if self.use_breakeven and not trade.trailing_activated:
            if pnl_pct >= self.breakeven_activation_pct:
                # Move SL to breakeven + offset
                breakeven_price = trade.entry_price * (1 + self.breakeven_offset_pct / self.leverage) if trade.direction == 'LONG' else trade.entry_price * (1 - self.breakeven_offset_pct / self.leverage)

                if trade.direction == 'LONG' and current_price <= breakeven_price:
                    return current_price, "BE"
                elif trade.direction == 'SHORT' and current_price >= breakeven_price:
                    return current_price, "BE"

        # === FIXED TP/SL (fallback if trailing not activated) ===
        if not trade.trailing_activated:
            # Take Profit (only if not using trailing or as max TP)
            if self.tp_pct > 0 and pnl_pct >= self.tp_pct:
                return current_price, "TP"

            # Stop Loss
            if self.sl_pct > 0 and pnl_pct <= -self.sl_pct:
                return current_price, "SL"

        return None, ""

    def _calculate_results(
        self,
        df: pd.DataFrame,
        signals_generated: int,
        signals_passed: int,
        stage_pass_counts: Dict[str, int]
    ) -> BacktestResult:
        """Calculate backtest results"""
        if not self.trades:
            return BacktestResult(
                symbol=self.symbol,
                start_date=df['timestamp'].iloc[0],
                end_date=df['timestamp'].iloc[-1],
                total_trades=0, winning_trades=0, losing_trades=0,
                win_rate=0, total_pnl_pct=0, avg_pnl_pct=0,
                max_drawdown=0, sharpe_ratio=0, profit_factor=0,
                avg_duration_hours=0, trades=[],
                stage_pass_rates={}, signals_generated=signals_generated,
                signals_passed_pipeline=signals_passed
            )

        # Calculate stats
        winning = [t for t in self.trades if t.pnl_pct > 0]
        losing = [t for t in self.trades if t.pnl_pct <= 0]

        total_pnl = sum(t.pnl_pct for t in self.trades)
        avg_pnl = total_pnl / len(self.trades) if self.trades else 0

        # Calculate max drawdown
        peak = self.equity_curve[0]
        max_dd = 0
        for eq in self.equity_curve:
            if eq > peak:
                peak = eq
            dd = (peak - eq) / peak
            max_dd = max(max_dd, dd)

        # Sharpe Ratio (simplified)
        returns = [t.pnl_pct for t in self.trades]
        sharpe = 0
        if len(returns) > 1 and np.std(returns) > 0:
            sharpe = np.mean(returns) / np.std(returns) * np.sqrt(252)

        # Profit Factor
        gross_profit = sum(t.pnl_pct for t in winning) if winning else 0
        gross_loss = abs(sum(t.pnl_pct for t in losing)) if losing else 0
        profit_factor = gross_profit / gross_loss if gross_loss > 0 else 0

        # Stage pass rates
        stage_pass_rates = {}
        for stage, count in stage_pass_counts.items():
            rate = count / signals_generated if signals_generated > 0 else 0
            stage_pass_rates[stage] = rate

        return BacktestResult(
            symbol=self.symbol,
            start_date=df['timestamp'].iloc[0],
            end_date=df['timestamp'].iloc[-1],
            total_trades=len(self.trades),
            winning_trades=len(winning),
            losing_trades=len(losing),
            win_rate=len(winning) / len(self.trades) if self.trades else 0,
            total_pnl_pct=total_pnl,
            avg_pnl_pct=avg_pnl,
            max_drawdown=max_dd,
            sharpe_ratio=sharpe,
            profit_factor=profit_factor,
            avg_duration_hours=np.mean([t.duration_hours for t in self.trades]),
            trades=self.trades,
            stage_pass_rates=stage_pass_rates,
            signals_generated=signals_generated,
            signals_passed_pipeline=signals_passed
        )

    def print_results(self, result: BacktestResult):
        """Print backtest results"""
        print(f"\n{'='*60}")
        print(f"📊 ENTRY PIPELINE BACKTEST RESULTS")
        print(f"{'='*60}")
        print(f"Symbol: {result.symbol}")
        print(f"Period: {result.start_date.strftime('%Y-%m-%d')} to {result.end_date.strftime('%Y-%m-%d')}")
        print(f"\n📈 PERFORMANCE METRICS:")
        print(f"   Total Trades: {result.total_trades}")
        print(f"   Winning: {result.winning_trades} | Losing: {result.losing_trades}")
        print(f"   Win Rate: {result.win_rate*100:.1f}%")
        print(f"   Total PnL: {result.total_pnl_pct*100:.2f}%")
        print(f"   Avg PnL/Trade: {result.avg_pnl_pct*100:.2f}%")
        print(f"   Max Drawdown: {result.max_drawdown*100:.2f}%")
        print(f"   Sharpe Ratio: {result.sharpe_ratio:.2f}")
        print(f"   Profit Factor: {result.profit_factor:.2f}")
        print(f"   Avg Duration: {result.avg_duration_hours:.1f}h")

        # Exit reason breakdown
        if result.trades:
            exit_reasons = {}
            for t in result.trades:
                exit_reasons[t.exit_reason] = exit_reasons.get(t.exit_reason, 0) + 1
            print(f"\n📊 EXIT REASONS:")
            for reason, count in sorted(exit_reasons.items(), key=lambda x: -x[1]):
                pct = count / len(result.trades) * 100
                print(f"   {reason}: {count} ({pct:.1f}%)")

        print(f"\n🎯 PIPELINE STATISTICS:")
        print(f"   Signals Generated: {result.signals_generated}")
        print(f"   Signals Passed: {result.signals_passed_pipeline}")
        pipeline_rate = result.signals_passed_pipeline / result.signals_generated if result.signals_generated > 0 else 0
        print(f"   Pipeline Pass Rate: {pipeline_rate*100:.1f}%")

        print(f"\n📋 STAGE PASS RATES:")
        for stage, rate in result.stage_pass_rates.items():
            print(f"   {stage}: {rate*100:.1f}%")

        # Balance summary
        final_balance = self.equity_curve[-1] if self.equity_curve else self.initial_balance
        roi = (final_balance - self.initial_balance) / self.initial_balance
        print(f"\n💰 BALANCE:")
        print(f"   Initial: ${self.initial_balance:.2f}")
        print(f"   Final: ${final_balance:.2f}")
        print(f"   ROI: {roi*100:.2f}%")
        print(f"{'='*60}\n")


def run_all_symbols(days: int, balance: float = 1000, leverage: int = 10):
    """Run backtest for all symbols in Config.SYMBOLS"""
    from ml.ensemble import EnsemblePredictor
    from ml.features import FeatureEngine

    print("\n" + "="*70)
    print("🚀 ENTRY PIPELINE BACKTEST - ALL SYMBOLS")
    print("="*70)
    print(f"Symbols: {len(Config.SYMBOLS)} symbols")
    print(f"Period: {days} days")
    print(f"Balance: ${balance} | Leverage: {leverage}x")
    print(f"ML Threshold: {Config.ML_CONFIDENCE_THRESHOLD}")
    print(f"Entry Score: {Config.MIN_ENTRY_SCORE} | PA Score: {Config.MIN_PRICE_ACTION_SCORE}")
    print(f"Trailing: {Config.TRAILING_ACTIVATION_PCT}% activation, {Config.TRAILING_DISTANCE_PCT}% distance")
    print("="*70 + "\n")

    # Load ML models once
    print("📥 Loading ML models...")
    predictor = EnsemblePredictor(
        models=Config.ENSEMBLE_MODELS,
        weights=Config.ENSEMBLE_WEIGHTS,
        input_size=len(FeatureEngine.FEATURE_COLUMNS)
    )
    if predictor.load_models():
        print(f"   ✅ {len(predictor.models)} models loaded: {list(predictor.models.keys())}")
        ml_models = {name: trainer for name, trainer in predictor.models.items() if trainer is not None}
    else:
        print("   ⚠️ ML models not loaded - running without ML stage")
        ml_models = {}

    # Build config from .env
    pipeline_config = {
        'USE_ML_ENSEMBLE': len(ml_models) > 0,
        'ML_CONFIDENCE_THRESHOLD': Config.ML_CONFIDENCE_THRESHOLD,
        'ML_NEUTRAL_ZONE': getattr(Config, 'ML_NEUTRAL_ZONE', 0.08),
        'USE_SMART_ENTRY': True,
        'MIN_ENTRY_SCORE': Config.MIN_ENTRY_SCORE,
        'MIN_RR_RATIO': getattr(Config, 'MIN_RR_RATIO', 0),
        'USE_PRICE_ACTION': getattr(Config, 'USE_PRICE_ACTION', True),
        'MIN_PRICE_ACTION_SCORE': Config.MIN_PRICE_ACTION_SCORE,
        'SR_LOOKBACK_CANDLES': getattr(Config, 'SR_LOOKBACK_CANDLES', 50),
        'SR_PROXIMITY_PCT': getattr(Config, 'SR_PROXIMITY_PCT', 0.8),
        'VOLUME_CONFIRMATION_RATIO': getattr(Config, 'VOLUME_CONFIRMATION_RATIO', 1.5),
        'USE_HTF_ALIGNMENT': getattr(Config, 'USE_HTF_ALIGNMENT', True),
        'HTF_TIMEFRAME': '4h',
        'REQUIRE_HTF_ALIGNMENT': False,
        'HTF_STRICT_MODE': getattr(Config, 'HTF_STRICT_MODE', False),
        'USE_AI_CHECK': False,  # Disable AI for backtest
    }

    all_results = []
    total_trades = 0
    total_winning = 0
    total_pnl_pct = 0

    # Trailing stop settings from config
    trailing_activation = getattr(Config, 'TRAILING_ACTIVATION_PCT', 2.5)
    trailing_distance = getattr(Config, 'TRAILING_DISTANCE_PCT', 2.2)
    use_trailing = getattr(Config, 'USE_TRAILING_STOP', True)
    use_breakeven = getattr(Config, 'USE_BREAKEVEN_STOP', True)
    breakeven_activation = getattr(Config, 'BREAKEVEN_ACTIVATION_PCT', 2.5)
    breakeven_offset = getattr(Config, 'BREAKEVEN_OFFSET_PCT', 0.4)

    for i, symbol in enumerate(Config.SYMBOLS):
        print(f"\n[{i+1}/{len(Config.SYMBOLS)}] 📊 Backtesting {symbol}...")

        try:
            backtester = PipelineBacktester(
                symbol=symbol,
                days=days,
                initial_balance=balance,
                leverage=leverage,
                tp_pct=0.10,  # 10% max TP (fallback if trailing not hit)
                sl_pct=0.05,  # 5% max SL (emergency stop)
                custom_config=pipeline_config,
                use_trailing_stop=use_trailing,
                trailing_activation_pct=trailing_activation,
                trailing_distance_pct=trailing_distance,
                use_breakeven=use_breakeven,
                breakeven_activation_pct=breakeven_activation,
                breakeven_offset_pct=breakeven_offset
            )

            # Inject ML models
            if ml_models:
                backtester.pipeline.ml_stage.models = ml_models
                backtester.pipeline.ml_stage.predictor = predictor

            result = backtester.run_backtest()
            all_results.append(result)

            total_trades += result.total_trades
            total_winning += result.winning_trades
            total_pnl_pct += result.total_pnl_pct

            # Quick summary
            wr = result.win_rate * 100 if result.total_trades > 0 else 0
            print(f"   ✅ {symbol}: {result.total_trades} trades, {wr:.1f}% WR, {result.total_pnl_pct*100:.2f}% PnL")

        except Exception as e:
            print(f"   ❌ {symbol} error: {e}")
            import traceback
            traceback.print_exc()

    # Print summary
    print("\n" + "="*70)
    print("📊 AGGREGATE RESULTS - ALL SYMBOLS")
    print("="*70)

    if all_results:
        agg_win_rate = total_winning / total_trades * 100 if total_trades > 0 else 0

        print(f"\n📈 OVERALL METRICS:")
        print(f"   Total Symbols Tested: {len(all_results)}")
        print(f"   Total Trades: {total_trades}")
        print(f"   Total Winning: {total_winning}")
        print(f"   Overall Win Rate: {agg_win_rate:.1f}%")
        print(f"   Total PnL: {total_pnl_pct*100:.2f}%")
        print(f"   Avg PnL/Symbol: {total_pnl_pct*100/len(all_results):.2f}%")

        # Per-symbol breakdown
        print(f"\n📋 PER-SYMBOL BREAKDOWN:")
        print(f"{'Symbol':<12} {'Trades':>8} {'Wins':>6} {'WR%':>8} {'PnL%':>10} {'PF':>8} {'MaxDD%':>8}")
        print("-"*70)

        for r in all_results:
            wr = r.win_rate * 100 if r.total_trades > 0 else 0
            print(f"{r.symbol:<12} {r.total_trades:>8} {r.winning_trades:>6} {wr:>7.1f}% {r.total_pnl_pct*100:>9.2f}% {r.profit_factor:>8.2f} {r.max_drawdown*100:>7.2f}%")

        # Stage analysis
        print(f"\n🎯 PIPELINE STAGE ANALYSIS:")
        total_signals = sum(r.signals_generated for r in all_results)
        total_passed = sum(r.signals_passed_pipeline for r in all_results)
        pass_rate = total_passed / total_signals * 100 if total_signals > 0 else 0

        print(f"   Total Signals Analyzed: {total_signals}")
        print(f"   Signals Passed Pipeline: {total_passed}")
        print(f"   Pipeline Pass Rate: {pass_rate:.2f}%")

        # Aggregate stage pass rates
        stage_totals = {}
        for r in all_results:
            for stage, rate in r.stage_pass_rates.items():
                if stage not in stage_totals:
                    stage_totals[stage] = []
                stage_totals[stage].append(rate)

        print(f"\n   Stage Pass Rates (avg across symbols):")
        for stage, rates in stage_totals.items():
            avg_rate = np.mean(rates) * 100
            print(f"      {stage}: {avg_rate:.1f}%")

        # Exit reason analysis
        print(f"\n📊 EXIT REASONS (aggregate):")
        exit_totals = {}
        for r in all_results:
            for t in r.trades:
                exit_totals[t.exit_reason] = exit_totals.get(t.exit_reason, 0) + 1

        for reason, count in sorted(exit_totals.items(), key=lambda x: -x[1]):
            pct = count / total_trades * 100 if total_trades > 0 else 0
            avg_pnl = np.mean([t.pnl_pct for r in all_results for t in r.trades if t.exit_reason == reason]) * 100
            print(f"   {reason:>6}: {count:>4} ({pct:>5.1f}%)  | Avg PnL: {avg_pnl:>+7.2f}%")

        # Trading readiness assessment
        print(f"\n" + "="*70)
        print("🎯 TRADING READINESS ASSESSMENT")
        print("="*70)

        target_wr = 60
        target_pf = 1.5

        wr_ok = agg_win_rate >= target_wr
        pf_ok = any(r.profit_factor >= target_pf for r in all_results if r.total_trades >= 5)
        trades_ok = total_trades >= 20

        print(f"\n   Target Win Rate ({target_wr}%): {'✅ PASS' if wr_ok else '❌ FAIL'} (Actual: {agg_win_rate:.1f}%)")
        print(f"   Target Profit Factor ({target_pf}): {'✅ PASS' if pf_ok else '❌ FAIL'}")
        print(f"   Sufficient Trades (20+): {'✅ PASS' if trades_ok else '❌ FAIL'} (Actual: {total_trades})")

        if wr_ok and pf_ok and trades_ok:
            print(f"\n   🟢 SYSTEM READY FOR LIVE TRADING")
        elif wr_ok or pf_ok:
            print(f"\n   🟡 SYSTEM PARTIALLY READY - Review settings")
        else:
            print(f"\n   🔴 SYSTEM NOT READY - Needs optimization")

        # Recommendations
        print(f"\n💡 RECOMMENDATIONS:")
        if agg_win_rate < 55:
            print(f"   - Increase ML_CONFIDENCE_THRESHOLD (current: {Config.ML_CONFIDENCE_THRESHOLD})")
            print(f"   - Increase MIN_ENTRY_SCORE (current: {Config.MIN_ENTRY_SCORE})")
        elif agg_win_rate > 70 and total_trades < 30:
            print(f"   - Consider lowering thresholds for more trades")

        if total_trades < 10:
            print(f"   - Very few trades - consider running longer period or relaxing filters")

    print("\n" + "="*70 + "\n")

    return all_results


def main():
    parser = argparse.ArgumentParser(description='Backtest Entry Pipeline')
    parser.add_argument('--symbol', type=str, default=None, help='Trading symbol (None = all symbols)')
    parser.add_argument('--days', type=int, default=30, help='Days of historical data')
    parser.add_argument('--balance', type=float, default=1000, help='Initial balance')
    parser.add_argument('--leverage', type=int, default=10, help='Leverage')
    parser.add_argument('--tp', type=float, default=0.02, help='Take profit %')
    parser.add_argument('--sl', type=float, default=0.01, help='Stop loss %')
    parser.add_argument('--optimize', action='store_true', help='Run threshold optimization')
    parser.add_argument('--all', action='store_true', help='Run for all symbols')

    args = parser.parse_args()

    if args.optimize:
        optimize_thresholds(args.symbol or 'BTCUSDT', args.days)
    elif args.all or args.symbol is None:
        # Run for all symbols
        run_all_symbols(args.days, args.balance, args.leverage)
    else:
        # Run backtest for single symbol
        backtester = PipelineBacktester(
            symbol=args.symbol,
            days=args.days,
            initial_balance=args.balance,
            leverage=args.leverage,
            tp_pct=args.tp,
            sl_pct=args.sl
        )

        result = backtester.run_backtest()
        backtester.print_results(result)

        return result


def optimize_thresholds(symbol: str, days: int):
    """Optimize pipeline thresholds for best performance"""
    print("\n" + "="*60)
    print("🔧 THRESHOLD OPTIMIZATION")
    print("="*60)

    # Test configurations
    configs = [
        # Config 1: Relaxed (more trades)
        {'name': 'Relaxed', 'MIN_ENTRY_SCORE': 4, 'MIN_PRICE_ACTION_SCORE': 3},
        # Config 2: Balanced
        {'name': 'Balanced', 'MIN_ENTRY_SCORE': 5, 'MIN_PRICE_ACTION_SCORE': 4},
        # Config 3: Strict (fewer, higher quality trades)
        {'name': 'Strict', 'MIN_ENTRY_SCORE': 6, 'MIN_PRICE_ACTION_SCORE': 5},
        # Config 4: Very Strict
        {'name': 'Very Strict', 'MIN_ENTRY_SCORE': 7, 'MIN_PRICE_ACTION_SCORE': 5},
        # Config 5: With HTF
        {'name': 'With HTF', 'MIN_ENTRY_SCORE': 5, 'MIN_PRICE_ACTION_SCORE': 4, 'USE_HTF_ALIGNMENT': True},
    ]

    results = []

    for config in configs:
        name = config.pop('name')
        print(f"\n📊 Testing: {name}")

        backtester = PipelineBacktester(
            symbol=symbol,
            days=days,
            custom_config=config
        )

        result = backtester.run_backtest()

        results.append({
            'name': name,
            'trades': result.total_trades,
            'win_rate': result.win_rate,
            'total_pnl': result.total_pnl_pct,
            'profit_factor': result.profit_factor,
            'sharpe': result.sharpe_ratio,
            'max_dd': result.max_drawdown,
            'roi': result.total_pnl_pct / 10  # Approximate ROI
        })

        print(f"   Trades: {result.total_trades}, WR: {result.win_rate:.1f}%, PF: {result.profit_factor:.2f}")

    # Print comparison table
    print("\n" + "="*80)
    print("📈 OPTIMIZATION RESULTS COMPARISON")
    print("="*80)
    print(f"{'Config':<15} {'Trades':>8} {'WinRate':>10} {'PnL':>10} {'PF':>8} {'Sharpe':>8} {'MaxDD':>8} {'ROI':>8}")
    print("-"*80)

    for r in results:
        print(f"{r['name']:<15} {r['trades']:>8} {r['win_rate']:>9.1f}% {r['total_pnl']:>9.1f}% {r['profit_factor']:>8.2f} {r['sharpe']:>8.2f} {r['max_dd']:>7.1f}% {r['roi']:>7.2f}%")

    # Find best config
    best = max(results, key=lambda x: x['profit_factor'] * x['win_rate'] / 100 if x['trades'] > 5 else 0)
    print(f"\n🏆 Best Config: {best['name']} (WR: {best['win_rate']:.1f}%, PF: {best['profit_factor']:.2f})")


if __name__ == '__main__':
    main()
