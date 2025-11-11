# ============================================
# 📈 TRAILING STOP SYSTEM
# Bảo vệ profit bằng trailing stop
# ============================================

import pandas as pd
import numpy as np
from config import Config
from utils.logger import logger

class TrailingStopManager:
    """
    Quản lý trailing stop để bảo vệ profit
    """
    
    def __init__(self, activation_pct=0.5, trail_pct=0.3):
        """
        Initialize trailing stop manager
        
        Args:
            activation_pct: % profit để activate trailing stop (default 0.5%)
            trail_pct: % trailing distance (default 0.3%)
        """
        self.activation_pct = activation_pct
        self.trail_pct = trail_pct
        self.trailing_stops = {}  # {symbol: {'stop_price': float, 'highest_price': float}}
        
    def update_trailing_stop(self, symbol, side, entry_price, current_price):
        """
        Update trailing stop cho position
        
        Args:
            symbol: Trading pair
            side: 'LONG' hoặc 'SHORT'
            entry_price: Entry price
            current_price: Current price
            
        Returns:
            dict: {'should_close': bool, 'stop_price': float, 'reason': str}
        """
        # Calculate current profit %
        if side == 'LONG':
            profit_pct = ((current_price - entry_price) / entry_price) * 100
        else:  # SHORT
            profit_pct = ((entry_price - current_price) / entry_price) * 100
        
        # Initialize trailing stop if not exists
        if symbol not in self.trailing_stops:
            self.trailing_stops[symbol] = {
                'stop_price': None,
                'highest_profit_pct': profit_pct,
                'activated': False
            }
        
        ts = self.trailing_stops[symbol]
        
        # Update highest profit
        if profit_pct > ts['highest_profit_pct']:
            ts['highest_profit_pct'] = profit_pct
        
        # Check if should activate trailing stop
        if not ts['activated'] and profit_pct >= self.activation_pct:
            ts['activated'] = True
            logger.info(f"🎯 Trailing stop activated for {symbol} at {profit_pct:.2f}% profit")
        
        # Update trailing stop if activated
        if ts['activated']:
            if side == 'LONG':
                # LONG: Stop trails below current price
                new_stop = current_price * (1 - self.trail_pct / 100)
                
                # Only move stop up, never down
                if ts['stop_price'] is None or new_stop > ts['stop_price']:
                    ts['stop_price'] = new_stop
                    
                # Check if hit stop
                if current_price <= ts['stop_price']:
                    return {
                        'should_close': True,
                        'stop_price': ts['stop_price'],
                        'reason': f'Trailing stop hit (profit: {profit_pct:.2f}%)'
                    }
            else:  # SHORT
                # SHORT: Stop trails above current price
                new_stop = current_price * (1 + self.trail_pct / 100)
                
                # Only move stop down, never up
                if ts['stop_price'] is None or new_stop < ts['stop_price']:
                    ts['stop_price'] = new_stop
                    
                # Check if hit stop
                if current_price >= ts['stop_price']:
                    return {
                        'should_close': True,
                        'stop_price': ts['stop_price'],
                        'reason': f'Trailing stop hit (profit: {profit_pct:.2f}%)'
                    }
        
        return {
            'should_close': False,
            'stop_price': ts.get('stop_price'),
            'reason': None
        }
    
    def remove_trailing_stop(self, symbol):
        """Remove trailing stop cho symbol"""
        if symbol in self.trailing_stops:
            del self.trailing_stops[symbol]
    
    def get_trailing_stop_info(self, symbol):
        """Get trailing stop info"""
        return self.trailing_stops.get(symbol, {})


class ATRTrailingStop:
    """
    ATR-based trailing stop (more adaptive to volatility)
    """
    
    def __init__(self, activation_pct=0.5, atr_multiplier=2.0):
        """
        Initialize ATR trailing stop
        
        Args:
            activation_pct: % profit để activate (default 0.5%)
            atr_multiplier: ATR multiplier cho trailing distance (default 2.0)
        """
        self.activation_pct = activation_pct
        self.atr_multiplier = atr_multiplier
        self.trailing_stops = {}
        
    def update_trailing_stop(self, symbol, side, entry_price, current_price, atr):
        """
        Update ATR-based trailing stop
        
        Args:
            symbol: Trading pair
            side: 'LONG' hoặc 'SHORT'
            entry_price: Entry price
            current_price: Current price
            atr: Current ATR value
            
        Returns:
            dict: {'should_close': bool, 'stop_price': float, 'reason': str}
        """
        # Calculate current profit %
        if side == 'LONG':
            profit_pct = ((current_price - entry_price) / entry_price) * 100
        else:
            profit_pct = ((entry_price - current_price) / entry_price) * 100
        
        # Initialize if not exists
        if symbol not in self.trailing_stops:
            self.trailing_stops[symbol] = {
                'stop_price': None,
                'highest_profit_pct': profit_pct,
                'activated': False
            }
        
        ts = self.trailing_stops[symbol]
        
        # Update highest profit
        if profit_pct > ts['highest_profit_pct']:
            ts['highest_profit_pct'] = profit_pct
        
        # Activate if profit threshold reached
        if not ts['activated'] and profit_pct >= self.activation_pct:
            ts['activated'] = True
            logger.info(f"🎯 ATR trailing stop activated for {symbol} at {profit_pct:.2f}% profit")
        
        # Update trailing stop if activated
        if ts['activated']:
            trail_distance = atr * self.atr_multiplier
            
            if side == 'LONG':
                new_stop = current_price - trail_distance
                
                # Only move stop up
                if ts['stop_price'] is None or new_stop > ts['stop_price']:
                    ts['stop_price'] = new_stop
                    
                # Check if hit
                if current_price <= ts['stop_price']:
                    return {
                        'should_close': True,
                        'stop_price': ts['stop_price'],
                        'reason': f'ATR trailing stop hit (profit: {profit_pct:.2f}%)'
                    }
            else:  # SHORT
                new_stop = current_price + trail_distance
                
                # Only move stop down
                if ts['stop_price'] is None or new_stop < ts['stop_price']:
                    ts['stop_price'] = new_stop
                    
                # Check if hit
                if current_price >= ts['stop_price']:
                    return {
                        'should_close': True,
                        'stop_price': ts['stop_price'],
                        'reason': f'ATR trailing stop hit (profit: {profit_pct:.2f}%)'
                    }
        
        return {
            'should_close': False,
            'stop_price': ts.get('stop_price'),
            'reason': None
        }
    
    def remove_trailing_stop(self, symbol):
        """Remove trailing stop"""
        if symbol in self.trailing_stops:
            del self.trailing_stops[symbol]
    
    def get_trailing_stop_info(self, symbol):
        """Get info"""
        return self.trailing_stops.get(symbol, {})


class BreakevenStop:
    """
    Move stop to breakeven after certain profit
    """
    
    def __init__(self, activation_pct=0.5, breakeven_offset_pct=0.1):
        """
        Initialize breakeven stop
        
        Args:
            activation_pct: % profit để move to breakeven (default 0.5%)
            breakeven_offset_pct: Offset from entry (default 0.1%)
        """
        self.activation_pct = activation_pct
        self.breakeven_offset_pct = breakeven_offset_pct
        self.breakeven_stops = {}
        
    def update_breakeven_stop(self, symbol, side, entry_price, current_price):
        """
        Update breakeven stop
        
        Args:
            symbol: Trading pair
            side: 'LONG' hoặc 'SHORT'
            entry_price: Entry price
            current_price: Current price
            
        Returns:
            dict: {'should_close': bool, 'stop_price': float, 'reason': str}
        """
        # Calculate profit
        if side == 'LONG':
            profit_pct = ((current_price - entry_price) / entry_price) * 100
        else:
            profit_pct = ((entry_price - current_price) / entry_price) * 100
        
        # Initialize
        if symbol not in self.breakeven_stops:
            self.breakeven_stops[symbol] = {
                'stop_price': None,
                'moved_to_breakeven': False
            }
        
        bs = self.breakeven_stops[symbol]
        
        # Move to breakeven if profit threshold reached
        if not bs['moved_to_breakeven'] and profit_pct >= self.activation_pct:
            if side == 'LONG':
                bs['stop_price'] = entry_price * (1 + self.breakeven_offset_pct / 100)
            else:
                bs['stop_price'] = entry_price * (1 - self.breakeven_offset_pct / 100)
            
            bs['moved_to_breakeven'] = True
            logger.info(f"🎯 Stop moved to breakeven for {symbol} (profit: {profit_pct:.2f}%)")
        
        # Check if hit
        if bs['moved_to_breakeven']:
            if side == 'LONG' and current_price <= bs['stop_price']:
                return {
                    'should_close': True,
                    'stop_price': bs['stop_price'],
                    'reason': 'Breakeven stop hit'
                }
            elif side == 'SHORT' and current_price >= bs['stop_price']:
                return {
                    'should_close': True,
                    'stop_price': bs['stop_price'],
                    'reason': 'Breakeven stop hit'
                }
        
        return {
            'should_close': False,
            'stop_price': bs.get('stop_price'),
            'reason': None
        }
    
    def remove_breakeven_stop(self, symbol):
        """Remove breakeven stop"""
        if symbol in self.breakeven_stops:
            del self.breakeven_stops[symbol]

