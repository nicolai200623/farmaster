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
    """
    
    def __init__(self, cooldown_minutes=60):
        """
        Initialize cooldown tracker
        
        Args:
            cooldown_minutes: Minimum minutes between signals for same symbol
        """
        self.cooldown_minutes = cooldown_minutes
        self.data_file = 'data/signal_cooldown.json'
        self.last_signals = {}  # {symbol: {'time': datetime, 'signal': 'LONG/SHORT'}}
        self._load_data()
    
    def _load_data(self):
        """Load cooldown data from disk"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    # Convert ISO strings back to datetime
                    for symbol, info in data.items():
                        self.last_signals[symbol] = {
                            'time': datetime.fromisoformat(info['time']),
                            'signal': info['signal']
                        }
                logger.debug(f"Loaded signal cooldown data for {len(self.last_signals)} symbols")
        except Exception as e:
            logger.warning(f"Could not load signal cooldown data: {e}")
            self.last_signals = {}
    
    def _save_data(self):
        """Save cooldown data to disk"""
        try:
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            # Convert datetime to ISO strings for JSON
            data = {}
            for symbol, info in self.last_signals.items():
                data[symbol] = {
                    'time': info['time'].isoformat(),
                    'signal': info['signal']
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
        
        if old_symbols:
            self._save_data()
            logger.info(f"Cleaned up {len(old_symbols)} old signal cooldown records")

