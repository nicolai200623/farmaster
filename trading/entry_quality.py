# ============================================
# 🎯 ENTRY QUALITY CHECKER
# Kiểm tra chất lượng entry sau khi vừa đóng lệnh
# Đảm bảo bot không vào lệnh kém chất lượng
# ============================================

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Optional, Tuple
from utils.logger import logger
from config import Config


class EntryQualityChecker:
    """
    Kiểm tra chất lượng entry point sau khi vừa đóng lệnh
    Đặc biệt sau TP để tránh FOMO entry
    """
    
    def __init__(self):
        """Initialize entry quality checker"""
        self.last_closes = {}  # {symbol: {'price': float, 'time': datetime, 'reason': str, 'side': str}}
        
    def record_close(self, symbol: str, close_price: float, close_reason: str, side: str):
        """
        Ghi nhận khi đóng lệnh
        
        Args:
            symbol: Trading pair
            close_price: Giá đóng lệnh
            close_reason: Lý do đóng (TP, SL, TRAILING, etc.)
            side: LONG hoặc SHORT
        """
        self.last_closes[symbol] = {
            'price': close_price,
            'time': datetime.now(),
            'reason': close_reason,
            'side': side
        }
        
    def check_entry_quality(
        self,
        symbol: str,
        df: pd.DataFrame,
        proposed_signal: str,
        current_price: float
    ) -> Tuple[bool, str, list]:
        """
        Kiểm tra chất lượng entry sau khi vừa đóng lệnh
        
        Args:
            symbol: Trading pair
            df: DataFrame với OHLCV data và indicators
            proposed_signal: 'LONG' hoặc 'SHORT' được đề xuất
            current_price: Giá hiện tại
            
        Returns:
            Tuple: (is_quality_entry: bool, reason: str, quality_factors: list)
        """
        quality_factors = []
        quality_score = 0
        max_score = 5
        
        # Nếu không có lịch sử đóng lệnh gần đây, OK
        if symbol not in self.last_closes:
            return True, "No recent close", ["fresh_entry"]
        
        last_close = self.last_closes[symbol]
        close_price = last_close['price']
        close_reason = last_close['reason']
        close_side = last_close['side']
        
        # 1. CHECK PULLBACK - Giá đã điều chỉnh chưa?
        price_change_pct = ((current_price - close_price) / close_price) * 100
        
        if close_side == 'LONG':
            # Sau LONG, giá nên pullback xuống để có entry tốt hơn
            if price_change_pct < -0.2:  # Pullback > 0.2%
                quality_score += 1
                quality_factors.append(f"pullback: {price_change_pct:.2f}%")
        else:  # SHORT
            # Sau SHORT, giá nên bounce lên để có entry tốt hơn
            if price_change_pct > 0.2:  # Bounce > 0.2%
                quality_score += 1
                quality_factors.append(f"bounce: {price_change_pct:.2f}%")
        
        # 2. CHECK RSI RESET - RSI đã về vùng trung tính chưa?
        if 'rsi' in df.columns:
            current_rsi = df['rsi'].iloc[-1]
            if 40 <= current_rsi <= 60:
                quality_score += 1
                quality_factors.append(f"RSI neutral: {current_rsi:.1f}")
            elif (proposed_signal == 'LONG' and current_rsi < 35) or \
                 (proposed_signal == 'SHORT' and current_rsi > 65):
                quality_score += 1
                quality_factors.append(f"RSI favorable: {current_rsi:.1f}")
        
        # 3. CHECK VOLUME - Volume đang cao không?
        if 'volume' in df.columns:
            avg_volume = df['volume'].rolling(20).mean().iloc[-1]
            current_volume = df['volume'].iloc[-1]
            if current_volume > avg_volume * 1.2:
                quality_score += 1
                quality_factors.append(f"volume spike: {(current_volume/avg_volume):.1f}x")
        
        # 4. CHECK CANDLE PATTERN - Có pattern tốt không?
        if len(df) >= 3:
            last_candle = df.iloc[-1]
            prev_candle = df.iloc[-2]
            
            # Check for reversal candle
            body = abs(last_candle['close'] - last_candle['open'])
            wick_upper = last_candle['high'] - max(last_candle['close'], last_candle['open'])
            wick_lower = min(last_candle['close'], last_candle['open']) - last_candle['low']
            
            if proposed_signal == 'LONG':
                # Bullish reversal signs
                if wick_lower > body * 2:  # Hammer-like
                    quality_score += 1
                    quality_factors.append("bullish wick")
                elif last_candle['close'] > last_candle['open'] and prev_candle['close'] < prev_candle['open']:
                    quality_score += 1
                    quality_factors.append("bullish engulfing")
            else:  # SHORT
                # Bearish reversal signs
                if wick_upper > body * 2:  # Shooting star-like
                    quality_score += 1
                    quality_factors.append("bearish wick")
                elif last_candle['close'] < last_candle['open'] and prev_candle['close'] > prev_candle['open']:
                    quality_score += 1
                    quality_factors.append("bearish engulfing")
        
        # 5. CHECK DIRECTION CHANGE - Có đang đổi hướng không?
        if proposed_signal != close_side:
            # Đổi hướng sau khi đóng lệnh - cần thận trọng hơn
            if quality_score >= 2:
                quality_score += 1
                quality_factors.append("direction_reversal_confirmed")
        else:
            # Cùng hướng - chờ pullback tốt hơn
            if quality_score >= 1:
                quality_factors.append("same_direction_continuation")
        
        # DECISION
        min_quality = 2  # Cần ít nhất 2 quality factors
        is_quality = quality_score >= min_quality
        
        if is_quality:
            reason = f"Quality entry ({quality_score}/{max_score}): {', '.join(quality_factors[:3])}"
        else:
            reason = f"Low quality ({quality_score}/{max_score}): waiting for better setup"
        
        return is_quality, reason, quality_factors
    
    def clear_close_record(self, symbol: str):
        """Xóa record khi đã vào lệnh mới thành công"""
        if symbol in self.last_closes:
            del self.last_closes[symbol]

