# ============================================
# 🚫 SIGNAL COOLDOWN TRACKER
# Prevent rapid signal flipping (whipsaw protection)
# ============================================

import json
import os
from datetime import datetime, timedelta
from typing import Optional
from utils.logger import logger

class SignalCooldownTracker:
    """
    Track last signal time for each symbol to prevent rapid flipping
    Also tracks post-trade cooldown (after closing positions)
    """

    def __init__(self, cooldown_minutes=60, post_trade_cooldown_minutes=5):
        """
        Initialize cooldown tracker

        Args:
            cooldown_minutes: Minimum minutes between signals for same symbol
            post_trade_cooldown_minutes: Minimum minutes after closing before new entry
        """
        self.cooldown_minutes = cooldown_minutes
        self.post_trade_cooldown_minutes = post_trade_cooldown_minutes
        self.data_file = 'data/signal_cooldown.json'
        self.last_signals = {}  # {symbol: {'time': datetime, 'signal': 'LONG/SHORT'}}
        self.post_trade_cooldowns = {}  # {symbol: {'time': datetime, 'close_price': float, 'close_reason': str}}
        self._load_data()
    
    def _load_data(self):
        """Load cooldown data from disk"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    # Load signal cooldowns
                    if 'signals' in data:
                        for symbol, info in data['signals'].items():
                            self.last_signals[symbol] = {
                                'time': datetime.fromisoformat(info['time']),
                                'signal': info['signal']
                            }
                    # Load post-trade cooldowns
                    if 'post_trade' in data:
                        for symbol, info in data['post_trade'].items():
                            self.post_trade_cooldowns[symbol] = {
                                'time': datetime.fromisoformat(info['time']),
                                'close_price': info.get('close_price', 0),
                                'close_reason': info.get('close_reason', '')
                            }
                    # Legacy format support
                    elif 'signals' not in data:
                        for symbol, info in data.items():
                            self.last_signals[symbol] = {
                                'time': datetime.fromisoformat(info['time']),
                                'signal': info['signal']
                            }
                logger.debug(f"Loaded cooldown data: {len(self.last_signals)} signals, {len(self.post_trade_cooldowns)} post-trade")
        except Exception as e:
            logger.warning(f"Could not load signal cooldown data: {e}")
            self.last_signals = {}
            self.post_trade_cooldowns = {}
    
    def _save_data(self):
        """Save cooldown data to disk"""
        try:
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            data = {'signals': {}, 'post_trade': {}}
            # Save signal cooldowns
            for symbol, info in self.last_signals.items():
                data['signals'][symbol] = {
                    'time': info['time'].isoformat(),
                    'signal': info['signal']
                }
            # Save post-trade cooldowns
            for symbol, info in self.post_trade_cooldowns.items():
                data['post_trade'][symbol] = {
                    'time': info['time'].isoformat(),
                    'close_price': info.get('close_price', 0),
                    'close_reason': info.get('close_reason', '')
                }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.error(f"Could not save signal cooldown data: {e}")
    
    def can_signal(self, symbol: str, new_signal: str) -> tuple[bool, Optional[str]]:
        """
        Check if we can generate a new signal for this symbol
        
        Args:
            symbol: Trading pair
            new_signal: 'LONG' or 'SHORT'
            
        Returns:
            tuple: (can_signal: bool, reason: str or None)
        """
        if symbol not in self.last_signals:
            return True, None
        
        last_info = self.last_signals[symbol]
        last_time = last_info['time']
        last_signal = last_info['signal']
        
        # Calculate time since last signal
        time_since = datetime.now() - last_time
        minutes_since = time_since.total_seconds() / 60
        
        # Check cooldown
        if minutes_since < self.cooldown_minutes:
            remaining = self.cooldown_minutes - minutes_since
            reason = f"Cooldown active: {remaining:.1f}m remaining (last: {last_signal} at {last_time.strftime('%H:%M')})"
            return False, reason
        
        return True, None
    
    def record_signal(self, symbol: str, signal: str):
        """
        Record a new signal for this symbol
        
        Args:
            symbol: Trading pair
            signal: 'LONG' or 'SHORT'
        """
        self.last_signals[symbol] = {
            'time': datetime.now(),
            'signal': signal
        }
        self._save_data()
        logger.debug(f"Recorded {signal} signal for {symbol}")
    
    def clear_signal(self, symbol: str):
        """
        Clear cooldown for a symbol (e.g., when position closed)
        
        Args:
            symbol: Trading pair
        """
        if symbol in self.last_signals:
            del self.last_signals[symbol]
            self._save_data()
            logger.debug(f"Cleared signal cooldown for {symbol}")
    
    def get_cooldown_info(self, symbol: str) -> Optional[dict]:
        """
        Get cooldown info for a symbol
        
        Args:
            symbol: Trading pair
            
        Returns:
            dict: {'last_signal': str, 'last_time': datetime, 'minutes_since': float, 'can_signal': bool}
                  or None if no record
        """
        if symbol not in self.last_signals:
            return None
        
        last_info = self.last_signals[symbol]
        time_since = datetime.now() - last_info['time']
        minutes_since = time_since.total_seconds() / 60
        
        return {
            'last_signal': last_info['signal'],
            'last_time': last_info['time'],
            'minutes_since': minutes_since,
            'can_signal': minutes_since >= self.cooldown_minutes
        }
    
    def cleanup_old_records(self, max_age_hours=48):
        """
        Remove old cooldown records

        Args:
            max_age_hours: Remove records older than this
        """
        cutoff = datetime.now() - timedelta(hours=max_age_hours)
        old_symbols = [
            symbol for symbol, info in self.last_signals.items()
            if info['time'] < cutoff
        ]

        for symbol in old_symbols:
            del self.last_signals[symbol]

        # Also cleanup post-trade cooldowns
        old_post_trade = [
            symbol for symbol, info in self.post_trade_cooldowns.items()
            if info['time'] < cutoff
        ]
        for symbol in old_post_trade:
            del self.post_trade_cooldowns[symbol]

        if old_symbols or old_post_trade:
            self._save_data()
            logger.info(f"Cleaned up {len(old_symbols)} signal + {len(old_post_trade)} post-trade cooldown records")

    # ============================================
    # POST-TRADE COOLDOWN METHODS
    # ============================================

    def record_trade_close(self, symbol: str, close_price: float, close_reason: str):
        """
        Record when a position is closed (for post-trade cooldown)

        Args:
            symbol: Trading pair
            close_price: Price at which position was closed
            close_reason: Reason for closing (TP, SL, TIMEOUT, etc.)
        """
        self.post_trade_cooldowns[symbol] = {
            'time': datetime.now(),
            'close_price': close_price,
            'close_reason': close_reason
        }
        self._save_data()
        logger.info(f"📝 Post-trade cooldown recorded for {symbol} (reason: {close_reason})")

    def can_enter_after_close(self, symbol: str, current_price: float = None, require_pullback: bool = False, pullback_pct: float = 0.3) -> tuple[bool, Optional[str]]:
        """
        Check if enough time has passed after closing a position

        Args:
            symbol: Trading pair
            current_price: Current market price (for pullback check)
            require_pullback: Whether to require price pullback before re-entry
            pullback_pct: Required pullback percentage from close price

        Returns:
            tuple: (can_enter: bool, reason: str or None)
        """
        if symbol not in self.post_trade_cooldowns:
            return True, None

        info = self.post_trade_cooldowns[symbol]
        time_since = datetime.now() - info['time']
        minutes_since = time_since.total_seconds() / 60

        # Check time cooldown
        if minutes_since < self.post_trade_cooldown_minutes:
            remaining = self.post_trade_cooldown_minutes - minutes_since
            reason = f"Post-trade cooldown: {remaining:.1f}m remaining (closed at {info['time'].strftime('%H:%M')} - {info['close_reason']})"
            return False, reason

        # Check pullback requirement (if enabled and price available)
        if require_pullback and current_price is not None and info.get('close_price', 0) > 0:
            close_price = info['close_price']
            price_change_pct = abs(current_price - close_price) / close_price * 100

            if price_change_pct < pullback_pct:
                reason = f"Waiting for pullback: {price_change_pct:.2f}% < {pullback_pct}% required (close: ${close_price:.2f}, now: ${current_price:.2f})"
                return False, reason

        return True, None

    def clear_post_trade_cooldown(self, symbol: str):
        """
        Clear post-trade cooldown for a symbol

        Args:
            symbol: Trading pair
        """
        if symbol in self.post_trade_cooldowns:
            del self.post_trade_cooldowns[symbol]
            self._save_data()
            logger.debug(f"Cleared post-trade cooldown for {symbol}")

    def get_post_trade_info(self, symbol: str) -> Optional[dict]:
        """
        Get post-trade cooldown info for a symbol

        Args:
            symbol: Trading pair

        Returns:
            dict with cooldown info or None
        """
        if symbol not in self.post_trade_cooldowns:
            return None

        info = self.post_trade_cooldowns[symbol]
        time_since = datetime.now() - info['time']
        minutes_since = time_since.total_seconds() / 60

        return {
            'close_time': info['time'],
            'close_price': info.get('close_price', 0),
            'close_reason': info.get('close_reason', ''),
            'minutes_since': minutes_since,
            'can_enter': minutes_since >= self.post_trade_cooldown_minutes
        }
