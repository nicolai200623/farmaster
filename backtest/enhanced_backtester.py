# ============================================
# 📈 ENHANCED BACKTESTER
# Backtest với filters, trailing stop, market regime
# ============================================

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from utils.data_fetcher import DataFetcher
from ml.features import FeatureEngine
from config import Config
from utils.logger import logger
from trading.signal_filters import SignalFilters
from trading.trailing_stop import TrailingStopManager, ATRTrailingStop, BreakevenStop
from trading.market_regime import MarketRegimeDetector
from trading.symbol_optimizer import SymbolOptimizer

class EnhancedBacktester:
    """Enhanced backtest với improvements"""

    # Trading costs configuration (realistic for crypto futures)
    DEFAULT_SLIPPAGE_PCT = 0.05      # 0.05% slippage per trade (entry + exit)
    DEFAULT_TAKER_FEE_PCT = 0.055    # 0.055% taker fee (AsterDEX typical)
    DEFAULT_MAKER_FEE_PCT = 0.02     # 0.02% maker fee

    def __init__(self, ensemble_predictor=None, lstm_trainer=None, initial_capital=1000,
                 slippage_pct=None, taker_fee_pct=None, maker_fee_pct=None, use_maker=False):
        self.ensemble_predictor = ensemble_predictor
        self.lstm_trainer = lstm_trainer
        self.initial_capital = initial_capital
        self.feature_engine = FeatureEngine()

        # Trading costs (can be customized)
        self.slippage_pct = slippage_pct if slippage_pct is not None else self.DEFAULT_SLIPPAGE_PCT
        self.taker_fee_pct = taker_fee_pct if taker_fee_pct is not None else self.DEFAULT_TAKER_FEE_PCT
        self.maker_fee_pct = maker_fee_pct if maker_fee_pct is not None else self.DEFAULT_MAKER_FEE_PCT
        self.use_maker = use_maker  # True = limit orders (maker), False = market orders (taker)

        # Calculate total cost per trade (entry + exit)
        fee_pct = self.maker_fee_pct if use_maker else self.taker_fee_pct
        self.total_cost_per_trade = (self.slippage_pct + fee_pct) * 2  # x2 for entry + exit
        
        # Initialize improvements
        self.signal_filters = SignalFilters()
        self.trailing_stop_mgr = TrailingStopManager(
            activation_pct=Config.TRAILING_ACTIVATION_PCT,
            trail_pct=Config.TRAILING_DISTANCE_PCT
        )
        self.breakeven_stop_mgr = BreakevenStop(
            activation_pct=Config.BREAKEVEN_ACTIVATION_PCT,
            breakeven_offset_pct=Config.BREAKEVEN_OFFSET_PCT
        )
        self.regime_detector = MarketRegimeDetector()
        self.symbol_optimizer = SymbolOptimizer(Config.SYMBOL_PARAMS_FILE) if Config.USE_SYMBOL_OPTIMIZER else None
        
    def run_backtest(self, symbols=None, days=30):
        """Run enhanced backtest"""
        symbols = symbols or Config.SYMBOLS
        
        # Filter enabled symbols
        if self.symbol_optimizer:
            symbols = self.symbol_optimizer.get_enabled_symbols(symbols)
        
        logger.info("=" * 60)
        logger.info(f"📈 ENHANCED BACKTEST - {days} NGÀY")
        logger.info("=" * 60)
        logger.info(f"✅ Filters: {Config.USE_SIGNAL_FILTERS}")
        logger.info(f"✅ Trailing Stop: {Config.USE_TRAILING_STOP}")
        logger.info(f"✅ Market Regime: {Config.USE_MARKET_REGIME}")
        logger.info(f"✅ Symbol Optimizer: {Config.USE_SYMBOL_OPTIMIZER}")
        logger.info(f"💰 Slippage: {self.slippage_pct}% | Fee: {self.taker_fee_pct if not self.use_maker else self.maker_fee_pct}% | Total cost/trade: {self.total_cost_per_trade:.3f}%")
        
        # Fetch data
        logger.info(f"📊 Fetching data for {len(symbols)} symbols...")
        data_dict = DataFetcher.fetch_multiple_symbols(symbols, days=days)
        
        if not data_dict:
            logger.error("❌ Không lấy được data!")
            return None
        
        # Run backtest cho từng symbol
        all_trades = []
        total_pnl = 0
        total_volume = 0
        symbol_results = {}
        
        for symbol in symbols:
            if symbol not in data_dict:
                continue
                
            logger.info(f"\n🔍 Backtesting {symbol}...")
            df = data_dict[symbol]
            
            trades, pnl, volume = self._backtest_symbol(df, symbol)
            
            all_trades.extend(trades)
            total_pnl += pnl
            total_volume += volume
            
            # Store symbol results
            symbol_results[symbol] = {
                'trades': len(trades),
                'pnl_pct': pnl,
                'volume': volume,
                'win_rate': len([t for t in trades if t['pnl'] > 0]) / len(trades) if trades else 0
            }
            
            logger.info(f"   Trades: {len(trades)} | PnL: {pnl:.2f}% | Volume: ${volume/1000:.1f}k")
        
        # Calculate stats
        results = self._calculate_stats(all_trades, total_pnl, total_volume)
        results['symbol_results'] = symbol_results
        
        # Print results
        self._print_results(results)
        
        return results
    
    def _backtest_symbol(self, df, symbol):
        """Backtest 1 symbol với improvements"""
        # Calculate indicators
        df = self.feature_engine.calculate_indicators(df)
        
        # Prepare features
        feature_df = self.feature_engine.prepare_features(df)
        
        # Get symbol-specific params
        symbol_params = self.symbol_optimizer.get_symbol_params(symbol) if self.symbol_optimizer else {}
        lstm_threshold = symbol_params.get('lstm_threshold', Config.LSTM_THRESHOLD)
        min_confluence = symbol_params.get('min_confluence_score', Config.MIN_CONFLUENCE_SCORE)
        use_trailing = symbol_params.get('use_trailing_stop', Config.USE_TRAILING_STOP)
        position_multiplier = symbol_params.get('position_size_multiplier', 1.0)
        
        # Normalize
        if self.ensemble_predictor:
            normalized = feature_df.values
        else:
            normalized = self.lstm_trainer.scaler.transform(feature_df.values)
        
        # Simulate trading
        trades = []
        position = None
        capital = self.initial_capital
        total_volume = 0
        
        for i in range(Config.SEQUENCE_LENGTH, len(df)):
            current_price = df['close'].iloc[i]
            current_atr = df['atr'].iloc[i] if 'atr' in df.columns else 0
            
            # Get prediction
            if self.ensemble_predictor:
                sequence = normalized[i-Config.SEQUENCE_LENGTH:i]
                ml_prob = self.ensemble_predictor.predict(sequence)
            else:
                lstm_input = normalized[i-Config.SEQUENCE_LENGTH:i]
                ml_prob = self.lstm_trainer.predict(lstm_input)[0]
            
            # Check trailing stop if in position
            if position is not None:
                # Trailing stop
                if use_trailing and Config.USE_TRAILING_STOP:
                    ts_result = self.trailing_stop_mgr.update_trailing_stop(
                        symbol, position['side'], position['entry_price'], current_price
                    )
                    if ts_result['should_close']:
                        # Close position
                        pnl_pct = self._calculate_pnl(position, current_price)
                        trades.append({
                            'entry_price': position['entry_price'],
                            'exit_price': current_price,
                            'side': position['side'],
                            'pnl': pnl_pct,
                            'reason': ts_result['reason']
                        })
                        total_volume += position['quantity'] * current_price
                        self.trailing_stop_mgr.remove_trailing_stop(symbol)
                        self.breakeven_stop_mgr.remove_breakeven_stop(symbol)
                        position = None
                        continue
                
                # Breakeven stop
                if Config.USE_BREAKEVEN_STOP:
                    be_result = self.breakeven_stop_mgr.update_breakeven_stop(
                        symbol, position['side'], position['entry_price'], current_price
                    )
                    if be_result['should_close']:
                        pnl_pct = self._calculate_pnl(position, current_price)
                        trades.append({
                            'entry_price': position['entry_price'],
                            'exit_price': current_price,
                            'side': position['side'],
                            'pnl': pnl_pct,
                            'reason': be_result['reason']
                        })
                        total_volume += position['quantity'] * current_price
                        self.trailing_stop_mgr.remove_trailing_stop(symbol)
                        self.breakeven_stop_mgr.remove_breakeven_stop(symbol)
                        position = None
                        continue
                
                # Normal TP/SL check
                hit, reason = self._check_tp_sl(position, current_price)

                if hit:
                    pnl_pct = self._calculate_pnl(position, current_price)
                    trades.append({
                        'entry_price': position['entry_price'],
                        'exit_price': current_price,
                        'side': position['side'],
                        'pnl': pnl_pct,
                        'reason': reason
                    })
                    total_volume += position['quantity'] * current_price
                    self.trailing_stop_mgr.remove_trailing_stop(symbol)
                    self.breakeven_stop_mgr.remove_breakeven_stop(symbol)
                    position = None
                    continue
            
            # Entry logic (no position)
            # Get current slice of df for filters
            current_df = df.iloc[:i+1]
            
            # Detect market regime
            regime_info = None
            if Config.USE_MARKET_REGIME:
                regime_info = self.regime_detector.detect_regime(current_df, Config.REGIME_LOOKBACK)
            
            # Generate signal
            signal = 'HOLD'
            rsi = df['rsi'].iloc[i]
            
            if ml_prob > lstm_threshold:
                signal = 'LONG'
            elif ml_prob < (1 - lstm_threshold):
                signal = 'SHORT'
            
            # Apply filters
            if signal != 'HOLD' and Config.USE_SIGNAL_FILTERS:
                filter_config = {
                    'use_trend_filter': Config.USE_TREND_FILTER,
                    'use_volatility_filter': Config.USE_VOLATILITY_FILTER,
                    'use_volume_filter': Config.USE_VOLUME_FILTER,
                    'min_volume_ratio': Config.MIN_VOLUME_RATIO,
                    'min_atr_pct': Config.MIN_ATR_PCT,
                    'max_atr_pct': Config.MAX_ATR_PCT
                }
                
                passed, reasons = self.signal_filters.apply_all_filters(current_df, signal, filter_config)
                
                if not passed:
                    signal = 'HOLD'
                    continue
                
                # Check signal quality
                quality_score = self.signal_filters.calculate_signal_quality_score(current_df, signal, ml_prob)
                if quality_score < Config.MIN_SIGNAL_QUALITY_SCORE:
                    signal = 'HOLD'
                    continue
            
            # Check market regime
            if signal != 'HOLD' and regime_info and Config.USE_MARKET_REGIME:
                if not self.regime_detector.should_trade_in_regime(
                    regime_info['regime'], signal, regime_info['confidence']
                ):
                    signal = 'HOLD'
                    continue
            
            # Entry
            if signal in ['LONG', 'SHORT']:
                quantity = (capital * Config.SIZE_PCT * Config.LEVERAGE * position_multiplier) / current_price
                position = {
                    'side': signal,
                    'entry_price': current_price,
                    'quantity': quantity
                }
                total_volume += quantity * current_price
        
        return trades, sum(t['pnl'] for t in trades), total_volume
    
    def _calculate_pnl(self, position, current_price, include_costs=True):
        """
        Calculate PnL % (with leverage and trading costs)

        Args:
            position: Position dict with entry_price, side
            current_price: Current market price
            include_costs: Whether to deduct slippage + fees (default True)

        Returns:
            PnL in percentage including leverage effect and costs
        """
        if position['side'] == 'LONG':
            price_change_pct = ((current_price - position['entry_price']) / position['entry_price']) * 100
        else:
            price_change_pct = ((position['entry_price'] - current_price) / position['entry_price']) * 100

        # Calculate raw PnL with leverage
        raw_pnl = price_change_pct * Config.LEVERAGE

        # Deduct trading costs (slippage + fees for both entry and exit)
        if include_costs:
            # Trading costs are calculated on leveraged position size
            # total_cost_per_trade already includes entry + exit
            cost_pct = self.total_cost_per_trade * Config.LEVERAGE
            return raw_pnl - cost_pct

        return raw_pnl

    def _check_tp_sl(self, position, current_price):
        """
        Check if TP/SL is hit
        TP_PCT and SL_PCT are in terms of price movement (not leveraged PnL)
        """
        if position['side'] == 'LONG':
            price_change_pct = ((current_price - position['entry_price']) / position['entry_price']) * 100
        else:
            price_change_pct = ((position['entry_price'] - current_price) / position['entry_price']) * 100

        # Check TP/SL based on price movement
        if price_change_pct >= Config.TP_PCT:
            return True, 'TP'
        elif Config.SL_PCT and price_change_pct <= -Config.SL_PCT:
            return True, 'SL'

        return False, None
    
    def _calculate_stats(self, trades, total_pnl, total_volume):
        """Calculate statistics including trading costs breakdown"""
        if not trades:
            return {
                'total_trades': 0,
                'winning_trades': 0,
                'losing_trades': 0,
                'win_rate': 0,
                'total_pnl': 0,
                'total_pnl_gross': 0,
                'total_costs': 0,
                'total_volume': 0,
                'avg_win': 0,
                'avg_loss': 0,
                'max_win': 0,
                'max_loss': 0,
                'profit_factor': 0,
                'cost_per_trade': 0
            }

        wins = [t for t in trades if t['pnl'] > 0]
        losses = [t for t in trades if t['pnl'] <= 0]

        # Calculate total costs (already deducted from PnL)
        cost_per_trade = self.total_cost_per_trade * Config.LEVERAGE
        total_costs = cost_per_trade * len(trades)
        total_pnl_gross = total_pnl + total_costs  # PnL before costs

        return {
            'total_trades': len(trades),
            'winning_trades': len(wins),
            'losing_trades': len(losses),
            'win_rate': len(wins) / len(trades) * 100,
            'total_pnl': total_pnl,
            'total_pnl_gross': total_pnl_gross,
            'total_costs': total_costs,
            'total_volume': total_volume,
            'avg_win': np.mean([t['pnl'] for t in wins]) if wins else 0,
            'avg_loss': np.mean([t['pnl'] for t in losses]) if losses else 0,
            'max_win': max([t['pnl'] for t in wins]) if wins else 0,
            'max_loss': min([t['pnl'] for t in losses]) if losses else 0,
            'profit_factor': abs(sum(t['pnl'] for t in wins) / sum(t['pnl'] for t in losses)) if losses and sum(t['pnl'] for t in losses) != 0 else 0,
            'cost_per_trade': cost_per_trade
        }
    
    def _print_results(self, results):
        """Print results with costs breakdown"""
        logger.info("\n" + "=" * 60)
        logger.info("📊 ENHANCED BACKTEST RESULTS (WITH COSTS)")
        logger.info("=" * 60)
        logger.info(f"Total Trades: {results['total_trades']}")
        logger.info(f"Winning Trades: {results['winning_trades']}")
        logger.info(f"Losing Trades: {results['losing_trades']}")
        logger.info(f"Win Rate: {results['win_rate']:.2f}%")
        logger.info("")
        logger.info(f"💰 PnL Breakdown:")
        logger.info(f"   Gross PnL (before costs): {results.get('total_pnl_gross', results['total_pnl']):.2f}%")
        logger.info(f"   Total Costs (slippage+fees): -{results.get('total_costs', 0):.2f}%")
        logger.info(f"   Net PnL (after costs): {results['total_pnl']:.2f}%")
        logger.info(f"   Cost per trade: {results.get('cost_per_trade', 0):.3f}%")
        logger.info("")
        logger.info(f"Total Volume: ${results['total_volume']/1e6:.2f}M")
        logger.info("")
        logger.info(f"Avg Win: {results['avg_win']:.2f}%")
        logger.info(f"Avg Loss: {results['avg_loss']:.2f}%")
        logger.info(f"Max Win: {results['max_win']:.2f}%")
        logger.info(f"Max Loss: {results['max_loss']:.2f}%")
        logger.info(f"Profit Factor: {results['profit_factor']:.2f}")
        logger.info("=" * 60)

