# ============================================
# ⏱️ POSITION TRACKER
# Track position opening times for timeout management
# ============================================

import json
import os
from datetime import datetime, timedelta
from utils.logger import logger

class PositionTracker:
    """
    Track position opening times to enable timeout-based closing.
    Persists data to disk to survive bot restarts.
    """
    
    def __init__(self, data_file='data/position_times.json'):
        """
        Initialize position tracker
        
        Args:
            data_file: Path to JSON file for persisting position times
        """
        self.data_file = data_file
        self.position_times = {}  # {symbol: timestamp_str}
        
        # Create data directory if needed
        os.makedirs(os.path.dirname(data_file), exist_ok=True)
        
        # Load existing data
        self._load()
    
    def _load(self):
        """Load position times from disk"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.position_times = json.load(f)
                logger.info(f"📂 Loaded {len(self.position_times)} position timestamps")
            except Exception as e:
                logger.error(f"Error loading position times: {e}")
                self.position_times = {}
        else:
            logger.info("📂 No existing position times file, starting fresh")
    
    def _save(self):
        """Save position times to disk"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.position_times, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving position times: {e}")
    
    def track_position_open(self, symbol):
        """
        Record when a position was opened
        
        Args:
            symbol: Trading pair (e.g., 'BTCUSDT')
        """
        timestamp = datetime.now().isoformat()
        self.position_times[symbol] = timestamp
        self._save()
        logger.info(f"⏱️ Tracking position open time for {symbol}: {timestamp}")
    
    def clear_position(self, symbol):
        """
        Clear position tracking when position is closed
        
        Args:
            symbol: Trading pair
        """
        if symbol in self.position_times:
            del self.position_times[symbol]
            self._save()
            logger.info(f"⏱️ Cleared position tracking for {symbol}")
    
    def get_position_age_hours(self, symbol):
        """
        Get how long a position has been open in hours
        
        Args:
            symbol: Trading pair
            
        Returns:
            float: Hours since position opened, or None if not tracked
        """
        if symbol not in self.position_times:
            return None
        
        try:
            open_time = datetime.fromisoformat(self.position_times[symbol])
            age = datetime.now() - open_time
            hours = age.total_seconds() / 3600
            return hours
        except Exception as e:
            logger.error(f"Error calculating position age for {symbol}: {e}")
            return None
    
    def is_position_timeout(self, symbol, timeout_hours):
        """
        Check if a position has exceeded the timeout threshold
        
        Args:
            symbol: Trading pair
            timeout_hours: Timeout threshold in hours
            
        Returns:
            bool: True if position has timed out
        """
        age_hours = self.get_position_age_hours(symbol)
        
        if age_hours is None:
            # Position not tracked - assume it's new
            return False
        
        return age_hours >= timeout_hours
    
    def cleanup_stale_positions(self, active_symbols):
        """
        Remove tracking for symbols that no longer have positions
        
        Args:
            active_symbols: List of symbols with active positions
        """
        stale_symbols = [s for s in self.position_times.keys() if s not in active_symbols]
        
        for symbol in stale_symbols:
            self.clear_position(symbol)
        
        if stale_symbols:
            logger.info(f"🧹 Cleaned up {len(stale_symbols)} stale position trackings")
    
    def get_all_tracked_positions(self):
        """
        Get all currently tracked positions with their ages
        
        Returns:
            dict: {symbol: age_hours}
        """
        result = {}
        for symbol in self.position_times.keys():
            age = self.get_position_age_hours(symbol)
            if age is not None:
                result[symbol] = age
        return result

