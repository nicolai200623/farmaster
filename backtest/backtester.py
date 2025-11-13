# ============================================
# 📈 BACKTESTER
# Simulate trading strategy với historical data
# ============================================

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from utils.data_fetcher import DataFetcher
from ml.features import FeatureEngine
from ml.lstm_model import LSTMTrainer
from config import Config
from utils.logger import logger

class Backtester:
    """Backtest trading strategy"""

    def __init__(self, lstm_trainer=None, ensemble_predictor=None, initial_capital=1000):
        self.lstm_trainer = lstm_trainer
        self.ensemble_predictor = ensemble_predictor
        self.initial_capital = initial_capital
        self.feature_engine = FeatureEngine()
    
    def run_backtest(self, symbols=None, days=30):
        """
        Chạy backtest
        
        Args:
            symbols: List symbols
            days: Số ngày backtest
            
        Returns:
            dict: Backtest results
        """
        symbols = symbols or Config.SYMBOLS
        
        logger.info("=" * 60)
        logger.info(f"📈 BẮT ĐẦU BACKTEST - {days} NGÀY")
        logger.info("=" * 60)
        
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
        
        for symbol in symbols:
            if symbol not in data_dict:
                continue
            
            logger.info(f"\n🔍 Backtesting {symbol}...")
            
            df = data_dict[symbol].copy()
            trades, pnl, volume = self._backtest_symbol(df, symbol)
            
            all_trades.extend(trades)
            total_pnl += pnl
            total_volume += volume
            
            logger.info(f"   Trades: {len(trades)} | PnL: {pnl:.2f}% | Volume: ${volume/1000:.1f}k")
        
        # Calculate stats
        results = self._calculate_stats(all_trades, total_pnl, total_volume)
        
        # Print results
        self._print_results(results)
        
        return results
    
    def _backtest_symbol(self, df, symbol):
        """Backtest 1 symbol"""
        # Calculate indicators
        df = self.feature_engine.calculate_indicators(df)

        # Prepare features
        feature_df = self.feature_engine.prepare_features(df)

        # Get prediction based on model type
        if self.ensemble_predictor:
            # Use ensemble prediction
            normalized = feature_df.values
        else:
            # Use LSTM prediction
            normalized = self.lstm_trainer.scaler.transform(feature_df.values)

        # Simulate trading
        trades = []
        position = None
        capital = self.initial_capital
        total_volume = 0

        for i in range(Config.SEQUENCE_LENGTH, len(df)):
            # Get prediction
            if self.ensemble_predictor:
                # Ensemble prediction
                sequence = normalized[i-Config.SEQUENCE_LENGTH:i]
                lstm_prob = self.ensemble_predictor.predict(sequence)
            else:
                # LSTM prediction
                lstm_input = normalized[i-Config.SEQUENCE_LENGTH:i]
                lstm_prob = self.lstm_trainer.predict(lstm_input)[0]
            
            # Get indicators
            rsi = df['rsi'].iloc[i]
            current_price = df['close'].iloc[i]
            
            # Generate signal (simplified - no OB data in backtest)
            score_long = 0
            score_short = 0
            
            if lstm_prob > Config.LSTM_THRESHOLD:
                score_long += 1
            elif lstm_prob < (1 - Config.LSTM_THRESHOLD):
                score_short += 1
            
            if rsi < Config.RSI_OVERSOLD:
                score_long += 1
            elif rsi > Config.RSI_OVERBOUGHT:
                score_short += 1
            
            # Entry
            if position is None:
                if score_long >= 2:
                    # Open LONG
                    quantity = (capital * Config.SIZE_PCT * Config.LEVERAGE) / current_price
                    position = {
                        'side': 'LONG',
                        'entry_price': current_price,
                        'quantity': quantity,
                        'entry_index': i
                    }
                    total_volume += quantity * current_price * Config.LEVERAGE
                
                elif score_short >= 2:
                    # Open SHORT
                    quantity = (capital * Config.SIZE_PCT * Config.LEVERAGE) / current_price
                    position = {
                        'side': 'SHORT',
                        'entry_price': current_price,
                        'quantity': quantity,
                        'entry_index': i
                    }
                    total_volume += quantity * current_price * Config.LEVERAGE
            
            # Exit
            elif position is not None:
                entry_price = position['entry_price']
                
                # Calculate PnL
                if position['side'] == 'LONG':
                    pnl_pct = (current_price - entry_price) / entry_price
                else:
                    pnl_pct = (entry_price - current_price) / entry_price
                
                # Check TP/SL
                should_close = False
                reason = ""

                if pnl_pct >= Config.TP_PCT:
                    should_close = True
                    reason = "TP"
                elif Config.SL_PCT is not None and pnl_pct <= -Config.SL_PCT:
                    should_close = True
                    reason = "SL"
                
                if should_close:
                    # Close position
                    pnl_usdt = capital * Config.SIZE_PCT * pnl_pct * Config.LEVERAGE
                    capital += pnl_usdt
                    
                    trades.append({
                        'symbol': symbol,
                        'side': position['side'],
                        'entry_price': entry_price,
                        'exit_price': current_price,
                        'pnl_pct': pnl_pct,
                        'pnl_usdt': pnl_usdt,
                        'reason': reason,
                        'duration': i - position['entry_index']
                    })
                    
                    position = None
        
        # Calculate total PnL %
        total_pnl_pct = (capital - self.initial_capital) / self.initial_capital * 100
        
        return trades, total_pnl_pct, total_volume
    
    def _calculate_stats(self, trades, total_pnl, total_volume):
        """Tính toán statistics"""
        if not trades:
            return {
                'total_trades': 0,
                'winning_trades': 0,
                'losing_trades': 0,
                'win_rate': 0,
                'total_pnl_pct': 0,
                'total_volume': 0,
                'avg_win': 0,
                'avg_loss': 0,
                'max_win': 0,
                'max_loss': 0,
                'profit_factor': 0
            }
        
        df_trades = pd.DataFrame(trades)
        
        winning_trades = df_trades[df_trades['pnl_pct'] > 0]
        losing_trades = df_trades[df_trades['pnl_pct'] <= 0]
        
        total_wins = len(winning_trades)
        total_losses = len(losing_trades)
        win_rate = total_wins / len(trades) * 100 if len(trades) > 0 else 0
        
        avg_win = winning_trades['pnl_pct'].mean() * 100 if total_wins > 0 else 0
        avg_loss = losing_trades['pnl_pct'].mean() * 100 if total_losses > 0 else 0
        max_win = winning_trades['pnl_pct'].max() * 100 if total_wins > 0 else 0
        max_loss = losing_trades['pnl_pct'].min() * 100 if total_losses > 0 else 0
        
        gross_profit = winning_trades['pnl_usdt'].sum() if total_wins > 0 else 0
        gross_loss = abs(losing_trades['pnl_usdt'].sum()) if total_losses > 0 else 0
        profit_factor = gross_profit / gross_loss if gross_loss > 0 else 0
        
        return {
            'total_trades': len(trades),
            'winning_trades': total_wins,
            'losing_trades': total_losses,
            'win_rate': win_rate,
            'total_pnl_pct': total_pnl,
            'total_volume': total_volume,
            'avg_win': avg_win,
            'avg_loss': avg_loss,
            'max_win': max_win,
            'max_loss': max_loss,
            'profit_factor': profit_factor,
            'trades': trades
        }
    
    def _print_results(self, results):
        """In kết quả backtest"""
        logger.info("\n" + "=" * 60)
        logger.info("📊 BACKTEST RESULTS")
        logger.info("=" * 60)
        logger.info(f"Total Trades: {results['total_trades']}")
        logger.info(f"Winning Trades: {results['winning_trades']}")
        logger.info(f"Losing Trades: {results['losing_trades']}")
        logger.info(f"Win Rate: {results['win_rate']:.2f}%")
        logger.info(f"")
        logger.info(f"Total PnL: {results['total_pnl_pct']:.2f}%")
        logger.info(f"Total Volume: ${results['total_volume']/1e6:.2f}M")
        logger.info(f"")
        logger.info(f"Avg Win: {results['avg_win']:.2f}%")
        logger.info(f"Avg Loss: {results['avg_loss']:.2f}%")
        logger.info(f"Max Win: {results['max_win']:.2f}%")
        logger.info(f"Max Loss: {results['max_loss']:.2f}%")
        logger.info(f"Profit Factor: {results['profit_factor']:.2f}")
        logger.info("=" * 60)

