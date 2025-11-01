#!/usr/bin/env python3
# ============================================
# 📊 PERFORMANCE ANALYZER
# Phân tích performance từ logs
# ============================================

import sys
import os
import re
from datetime import datetime, timedelta
from collections import defaultdict

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logger import logger

class PerformanceAnalyzer:
    """Phân tích performance từ log files"""
    
    def __init__(self, log_dir='logs'):
        self.log_dir = log_dir
        self.trades = []
        self.daily_stats = defaultdict(lambda: {
            'trades': 0,
            'wins': 0,
            'losses': 0,
            'volume': 0,
            'pnl': 0
        })
    
    def parse_logs(self, days=7):
        """Parse log files từ N ngày gần nhất"""
        logger.info(f"📖 Parsing logs from last {days} days...")
        
        # Get log files
        log_files = []
        for i in range(days):
            date = datetime.now() - timedelta(days=i)
            log_file = os.path.join(self.log_dir, f"bot_{date.strftime('%Y%m%d')}.log")
            if os.path.exists(log_file):
                log_files.append(log_file)
        
        if not log_files:
            logger.warning("No log files found!")
            return
        
        # Parse each file
        for log_file in log_files:
            self._parse_file(log_file)
        
        logger.info(f"✅ Parsed {len(self.trades)} trades")
    
    def _parse_file(self, log_file):
        """Parse single log file"""
        with open(log_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Parse OPEN trades
                if 'OPEN LONG' in line or 'OPEN SHORT' in line:
                    self._parse_open_trade(line)
                
                # Parse CLOSE trades
                elif 'CLOSE' in line and 'PnL:' in line:
                    self._parse_close_trade(line)
    
    def _parse_open_trade(self, line):
        """Parse OPEN trade line"""
        # Example: "💰 OPEN LONG BTCUSDT | Qty: 0.01 | Price: $50000.00"
        match = re.search(r'OPEN (LONG|SHORT) (\w+) \| Qty: ([\d.]+) \| Price: \$([\d.]+)', line)
        
        if match:
            side = match.group(1)
            symbol = match.group(2)
            qty = float(match.group(3))
            price = float(match.group(4))
            
            # Extract timestamp
            timestamp_match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', line)
            timestamp = timestamp_match.group(1) if timestamp_match else None
            
            trade = {
                'type': 'OPEN',
                'side': side,
                'symbol': symbol,
                'qty': qty,
                'price': price,
                'timestamp': timestamp
            }
            
            self.trades.append(trade)
    
    def _parse_close_trade(self, line):
        """Parse CLOSE trade line"""
        # Example: "💰 CLOSE LONG BTCUSDT | TP (2.15%) | PnL: 2.15%"
        match = re.search(r'CLOSE (LONG|SHORT) (\w+) \| (\w+) \(([-\d.]+)%\) \| PnL: ([-\d.]+)%', line)
        
        if match:
            side = match.group(1)
            symbol = match.group(2)
            reason = match.group(3)
            pnl_pct = float(match.group(5))
            
            # Extract timestamp
            timestamp_match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', line)
            timestamp = timestamp_match.group(1) if timestamp_match else None
            
            trade = {
                'type': 'CLOSE',
                'side': side,
                'symbol': symbol,
                'reason': reason,
                'pnl_pct': pnl_pct,
                'timestamp': timestamp
            }
            
            self.trades.append(trade)
            
            # Update daily stats
            if timestamp:
                date = timestamp.split()[0]
                self.daily_stats[date]['trades'] += 1
                
                if pnl_pct > 0:
                    self.daily_stats[date]['wins'] += 1
                else:
                    self.daily_stats[date]['losses'] += 1
                
                self.daily_stats[date]['pnl'] += pnl_pct
    
    def calculate_metrics(self):
        """Tính toán performance metrics"""
        close_trades = [t for t in self.trades if t['type'] == 'CLOSE']
        
        if not close_trades:
            logger.warning("No closed trades found!")
            return None
        
        # Basic stats
        total_trades = len(close_trades)
        winning_trades = [t for t in close_trades if t['pnl_pct'] > 0]
        losing_trades = [t for t in close_trades if t['pnl_pct'] <= 0]
        
        wins = len(winning_trades)
        losses = len(losing_trades)
        win_rate = wins / total_trades * 100 if total_trades > 0 else 0
        
        # PnL stats
        total_pnl = sum(t['pnl_pct'] for t in close_trades)
        avg_win = sum(t['pnl_pct'] for t in winning_trades) / wins if wins > 0 else 0
        avg_loss = sum(t['pnl_pct'] for t in losing_trades) / losses if losses > 0 else 0
        
        max_win = max((t['pnl_pct'] for t in winning_trades), default=0)
        max_loss = min((t['pnl_pct'] for t in losing_trades), default=0)
        
        # Profit factor
        gross_profit = sum(t['pnl_pct'] for t in winning_trades)
        gross_loss = abs(sum(t['pnl_pct'] for t in losing_trades))
        profit_factor = gross_profit / gross_loss if gross_loss > 0 else 0
        
        # Symbol breakdown
        symbol_stats = defaultdict(lambda: {'trades': 0, 'wins': 0, 'pnl': 0})
        for t in close_trades:
            symbol = t['symbol']
            symbol_stats[symbol]['trades'] += 1
            if t['pnl_pct'] > 0:
                symbol_stats[symbol]['wins'] += 1
            symbol_stats[symbol]['pnl'] += t['pnl_pct']
        
        return {
            'total_trades': total_trades,
            'wins': wins,
            'losses': losses,
            'win_rate': win_rate,
            'total_pnl': total_pnl,
            'avg_win': avg_win,
            'avg_loss': avg_loss,
            'max_win': max_win,
            'max_loss': max_loss,
            'profit_factor': profit_factor,
            'symbol_stats': dict(symbol_stats)
        }
    
    def print_report(self):
        """In báo cáo performance"""
        metrics = self.calculate_metrics()
        
        if not metrics:
            return
        
        logger.info("\n" + "=" * 60)
        logger.info("📊 PERFORMANCE REPORT")
        logger.info("=" * 60)
        
        logger.info(f"\n📈 OVERALL STATS")
        logger.info(f"Total Trades: {metrics['total_trades']}")
        logger.info(f"Winning Trades: {metrics['wins']}")
        logger.info(f"Losing Trades: {metrics['losses']}")
        logger.info(f"Win Rate: {metrics['win_rate']:.2f}%")
        
        logger.info(f"\n💰 PNL STATS")
        logger.info(f"Total PnL: {metrics['total_pnl']:.2f}%")
        logger.info(f"Avg Win: {metrics['avg_win']:.2f}%")
        logger.info(f"Avg Loss: {metrics['avg_loss']:.2f}%")
        logger.info(f"Max Win: {metrics['max_win']:.2f}%")
        logger.info(f"Max Loss: {metrics['max_loss']:.2f}%")
        logger.info(f"Profit Factor: {metrics['profit_factor']:.2f}")
        
        logger.info(f"\n📊 BY SYMBOL")
        for symbol, stats in metrics['symbol_stats'].items():
            wr = stats['wins'] / stats['trades'] * 100 if stats['trades'] > 0 else 0
            logger.info(f"{symbol}:")
            logger.info(f"  Trades: {stats['trades']} | Win Rate: {wr:.1f}% | PnL: {stats['pnl']:.2f}%")
        
        logger.info(f"\n📅 DAILY BREAKDOWN")
        for date in sorted(self.daily_stats.keys()):
            stats = self.daily_stats[date]
            wr = stats['wins'] / stats['trades'] * 100 if stats['trades'] > 0 else 0
            logger.info(f"{date}:")
            logger.info(f"  Trades: {stats['trades']} | Win Rate: {wr:.1f}% | PnL: {stats['pnl']:.2f}%")
        
        logger.info("\n" + "=" * 60)
        
        # Recommendations
        logger.info("\n💡 RECOMMENDATIONS")
        
        if metrics['win_rate'] < 50:
            logger.info("⚠️  Win rate thấp! Consider:")
            logger.info("   - Tăng LSTM_THRESHOLD")
            logger.info("   - Tăng MIN_SIGNAL_SCORE")
            logger.info("   - Retrain model")
        
        if metrics['profit_factor'] < 1.3:
            logger.info("⚠️  Profit factor thấp! Consider:")
            logger.info("   - Tăng TP_PCT")
            logger.info("   - Giảm SL_PCT")
            logger.info("   - Optimize parameters")
        
        if abs(metrics['avg_loss']) > metrics['avg_win']:
            logger.info("⚠️  Avg loss > avg win! Consider:")
            logger.info("   - Tighten stop loss")
            logger.info("   - Let winners run longer")
        
        if metrics['win_rate'] >= 60 and metrics['profit_factor'] >= 1.5:
            logger.info("🎉 Performance tốt! Keep it up!")
        
        logger.info("=" * 60)

def main():
    """Main entry point"""
    analyzer = PerformanceAnalyzer()
    
    # Parse logs
    analyzer.parse_logs(days=7)
    
    # Print report
    analyzer.print_report()

if __name__ == '__main__':
    main()

