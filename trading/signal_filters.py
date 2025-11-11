# ============================================
# 🔍 SIGNAL FILTERS
# Filters để loại bỏ low-quality signals
# ============================================

import pandas as pd
import numpy as np
from config import Config
from utils.logger import logger

class SignalFilters:
    """
    Filters để cải thiện win rate bằng cách loại bỏ low-quality signals
    """
    
    @staticmethod
    def check_trend_alignment(df, signal):
        """
        Kiểm tra signal có align với trend không
        
        Args:
            df: DataFrame với indicators
            signal: 'LONG' hoặc 'SHORT'
            
        Returns:
            bool: True nếu aligned, False nếu không
        """
        if len(df) < 20:
            return False
            
        # Get EMAs
        ema_20 = df['close'].ewm(span=20).mean().iloc[-1]
        ema_50 = df['close'].ewm(span=50).mean().iloc[-1]
        current_price = df['close'].iloc[-1]
        
        if signal == 'LONG':
            # LONG: Price > EMA20 > EMA50 (uptrend)
            return current_price > ema_20 > ema_50
        elif signal == 'SHORT':
            # SHORT: Price < EMA20 < EMA50 (downtrend)
            return current_price < ema_20 < ema_50
            
        return False
    
    @staticmethod
    def check_volatility_filter(df, min_atr_pct=0.5, max_atr_pct=5.0):
        """
        Kiểm tra volatility có phù hợp không
        Loại bỏ market quá flat hoặc quá volatile
        
        Args:
            df: DataFrame với indicators
            min_atr_pct: Min ATR % (default 0.5%)
            max_atr_pct: Max ATR % (default 5%)
            
        Returns:
            bool: True nếu volatility OK
        """
        if 'atr' not in df.columns or len(df) < 14:
            return True  # Skip filter if no ATR
            
        current_atr = df['atr'].iloc[-1]
        current_price = df['close'].iloc[-1]
        atr_pct = (current_atr / current_price) * 100
        
        return min_atr_pct <= atr_pct <= max_atr_pct
    
    @staticmethod
    def check_volume_confirmation(df, signal, min_volume_ratio=1.2):
        """
        Kiểm tra volume có confirm signal không
        
        Args:
            df: DataFrame với volume
            signal: 'LONG' hoặc 'SHORT'
            min_volume_ratio: Min ratio so với avg volume
            
        Returns:
            bool: True nếu volume confirm
        """
        if len(df) < 20:
            return True  # Skip if not enough data
            
        current_volume = df['volume'].iloc[-1]
        avg_volume = df['volume'].iloc[-20:].mean()
        
        if avg_volume == 0:
            return True  # Skip if no volume data
            
        volume_ratio = current_volume / avg_volume
        
        # Require higher volume for entry
        return volume_ratio >= min_volume_ratio
    
    @staticmethod
    def check_rsi_divergence(df, signal):
        """
        Kiểm tra RSI divergence (bullish/bearish)
        
        Args:
            df: DataFrame với RSI
            signal: 'LONG' hoặc 'SHORT'
            
        Returns:
            bool: True nếu có divergence support signal
        """
        if 'rsi' not in df.columns or len(df) < 20:
            return True  # Skip if no RSI
            
        # Get last 20 candles
        recent_df = df.iloc[-20:]
        
        # Find price and RSI extremes
        price_low_idx = recent_df['low'].idxmin()
        price_high_idx = recent_df['high'].idxmax()
        
        if signal == 'LONG':
            # Bullish divergence: Price makes lower low, RSI makes higher low
            if price_low_idx < len(recent_df) - 5:  # Low was not too recent
                price_low = recent_df.loc[price_low_idx, 'low']
                rsi_at_low = recent_df.loc[price_low_idx, 'rsi']
                
                current_price = recent_df['low'].iloc[-1]
                current_rsi = recent_df['rsi'].iloc[-1]
                
                # Bullish divergence
                if current_price < price_low and current_rsi > rsi_at_low:
                    return True
                    
        elif signal == 'SHORT':
            # Bearish divergence: Price makes higher high, RSI makes lower high
            if price_high_idx < len(recent_df) - 5:
                price_high = recent_df.loc[price_high_idx, 'high']
                rsi_at_high = recent_df.loc[price_high_idx, 'rsi']
                
                current_price = recent_df['high'].iloc[-1]
                current_rsi = recent_df['rsi'].iloc[-1]
                
                # Bearish divergence
                if current_price > price_high and current_rsi < rsi_at_high:
                    return True
        
        # No divergence found, return True to not filter out
        return True
    
    @staticmethod
    def check_support_resistance(df, signal, lookback=50):
        """
        Kiểm tra price có gần support/resistance không
        
        Args:
            df: DataFrame
            signal: 'LONG' hoặc 'SHORT'
            lookback: Số candles để tìm S/R
            
        Returns:
            bool: True nếu gần S/R
        """
        if len(df) < lookback:
            return True  # Skip if not enough data
            
        recent_df = df.iloc[-lookback:]
        current_price = df['close'].iloc[-1]
        
        # Find support/resistance levels
        highs = recent_df['high'].values
        lows = recent_df['low'].values
        
        # Resistance: Recent highs
        resistance = np.percentile(highs, 95)
        # Support: Recent lows
        support = np.percentile(lows, 5)
        
        # Calculate distance to S/R
        dist_to_resistance = abs(current_price - resistance) / current_price
        dist_to_support = abs(current_price - support) / current_price
        
        threshold = 0.02  # 2% threshold
        
        if signal == 'LONG':
            # LONG: Should be near support
            return dist_to_support < threshold
        elif signal == 'SHORT':
            # SHORT: Should be near resistance
            return dist_to_resistance < threshold
            
        return True
    
    @staticmethod
    def apply_all_filters(df, signal, config=None):
        """
        Áp dụng tất cả filters
        
        Args:
            df: DataFrame với indicators
            signal: 'LONG', 'SHORT', hoặc 'HOLD'
            config: Dict với filter settings (optional)
            
        Returns:
            tuple: (passed, reasons)
                passed: bool - True nếu pass all filters
                reasons: list - Lý do fail (nếu có)
        """
        if signal == 'HOLD':
            return True, []
            
        config = config or {}
        failed_reasons = []
        
        # 1. Trend alignment filter
        if config.get('use_trend_filter', True):
            if not SignalFilters.check_trend_alignment(df, signal):
                failed_reasons.append("Trend not aligned")
        
        # 2. Volatility filter
        if config.get('use_volatility_filter', True):
            min_atr = config.get('min_atr_pct', 0.5)
            max_atr = config.get('max_atr_pct', 5.0)
            if not SignalFilters.check_volatility_filter(df, min_atr, max_atr):
                failed_reasons.append("Volatility out of range")
        
        # 3. Volume confirmation
        if config.get('use_volume_filter', True):
            min_vol_ratio = config.get('min_volume_ratio', 1.2)
            if not SignalFilters.check_volume_confirmation(df, signal, min_vol_ratio):
                failed_reasons.append("Insufficient volume")
        
        # 4. Support/Resistance filter
        if config.get('use_sr_filter', False):  # Disabled by default (too strict)
            if not SignalFilters.check_support_resistance(df, signal):
                failed_reasons.append("Not near S/R level")
        
        passed = len(failed_reasons) == 0
        return passed, failed_reasons
    
    @staticmethod
    def calculate_signal_quality_score(df, signal, ml_prob):
        """
        Tính quality score cho signal (0-100)
        
        Args:
            df: DataFrame
            signal: 'LONG' hoặc 'SHORT'
            ml_prob: ML prediction probability
            
        Returns:
            float: Quality score (0-100)
        """
        if signal == 'HOLD':
            return 0
            
        score = 0
        
        # 1. ML confidence (0-30 points)
        ml_confidence = abs(ml_prob - 0.5) * 2  # 0-1 range
        score += ml_confidence * 30
        
        # 2. Trend alignment (0-20 points)
        if SignalFilters.check_trend_alignment(df, signal):
            score += 20
        
        # 3. Volume (0-20 points)
        if SignalFilters.check_volume_confirmation(df, signal, min_volume_ratio=1.0):
            score += 10
        if SignalFilters.check_volume_confirmation(df, signal, min_volume_ratio=1.5):
            score += 10  # Bonus for high volume
        
        # 4. Volatility (0-15 points)
        if SignalFilters.check_volatility_filter(df):
            score += 15
        
        # 5. RSI position (0-15 points)
        if 'rsi' in df.columns:
            rsi = df['rsi'].iloc[-1]
            if signal == 'LONG' and rsi < 40:
                score += 15
            elif signal == 'SHORT' and rsi > 60:
                score += 15
        
        return min(score, 100)

