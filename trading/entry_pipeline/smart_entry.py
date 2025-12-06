# ============================================
# 🎯 STAGE 2: SMART ENTRY SCORING
# Integration with existing SmartEntryV2 or standalone scoring
# ============================================

import pandas as pd
import numpy as np
from typing import Dict, Optional, Tuple, List

from trading.entry_pipeline.models import SignalDirection, StageResult
from utils.logger import logger


class SmartEntryScoring:
    """
    Stage 2: Smart Entry Scoring System
    
    Scoring system with 15 points total:
    - Market Structure: 5 points
    - Price Action: 5 points
    - Technical Indicators: 5 points
    
    Can integrate with existing SmartEntrySystemV2 or work standalone.
    """
    
    def __init__(self, config: Dict, smart_entry_v2=None):
        """
        Initialize Smart Entry Scoring
        
        Args:
            config: Configuration dictionary
            smart_entry_v2: Optional SmartEntrySystemV2 instance
        """
        self.config = config
        self.smart_entry_v2 = smart_entry_v2
        
        # Thresholds
        self.min_score = config.get('MIN_ENTRY_SCORE', 7)
        self.min_rr_ratio = config.get('MIN_RR_RATIO', 2.0)
        
        logger.info(f"🎯 SmartEntryScoring initialized (min score: {self.min_score})")
    
    def calculate_score(
        self,
        df: pd.DataFrame,
        direction: SignalDirection,
        df_higher: Optional[pd.DataFrame] = None,
        df_4h: Optional[pd.DataFrame] = None,
        symbol: str = ""
    ) -> Tuple[int, List[str], StageResult]:
        """
        Calculate entry score
        
        Args:
            df: Primary timeframe DataFrame with indicators
            direction: Signal direction from Stage 1
            df_higher: Higher timeframe data (1H)
            df_4h: 4H timeframe data
            symbol: Trading symbol
        
        Returns:
            Tuple of (total_score, reasons, StageResult)
        """
        # If SmartEntryV2 is available, use it
        if self.smart_entry_v2 is not None:
            return self._use_smart_entry_v2(df, direction, df_higher, df_4h, symbol)
        
        # Otherwise, use standalone scoring
        return self._standalone_scoring(df, direction, df_higher)
    
    def _use_smart_entry_v2(
        self,
        df: pd.DataFrame,
        direction: SignalDirection,
        df_higher: Optional[pd.DataFrame],
        df_4h: Optional[pd.DataFrame],
        symbol: str
    ) -> Tuple[int, List[str], StageResult]:
        """Use existing SmartEntryV2 for scoring"""
        try:
            signal, score, entry_price, sl_price, tp_price, reasons = \
                self.smart_entry_v2.evaluate_entry(
                    symbol=symbol,
                    df_primary=df,
                    df_higher=df_higher,
                    df_4h=df_4h
                )
            
            # Check if signal matches direction
            signal_dir = SignalDirection.LONG if signal == 'LONG' else (
                SignalDirection.SHORT if signal == 'SHORT' else SignalDirection.HOLD
            )
            
            passed = score >= self.min_score and signal_dir == direction
            
            stage_result = StageResult(
                stage_name="smart_entry",
                passed=passed,
                score=score,
                max_score=15,
                reason=f"Score {score}/15, signal={signal}",
                details={
                    'entry_price': entry_price,
                    'sl_price': sl_price,
                    'tp_price': tp_price,
                    'reasons': reasons
                }
            )
            
            return score, reasons, stage_result
            
        except Exception as e:
            logger.error(f"SmartEntryV2 error: {e}")
            return 0, [], StageResult(
                stage_name="smart_entry",
                passed=False,
                score=0,
                max_score=15,
                reason=f"Error: {str(e)}"
            )
    
    def _standalone_scoring(
        self,
        df: pd.DataFrame,
        direction: SignalDirection,
        df_higher: Optional[pd.DataFrame]
    ) -> Tuple[int, List[str], StageResult]:
        """Standalone scoring without SmartEntryV2"""
        scores = {
            'market_structure': 0,  # 0-5
            'price_action': 0,      # 0-5
            'technical': 0          # 0-5
        }
        reasons = []
        
        # 1. MARKET STRUCTURE (5 points)
        ms_score, ms_reasons = self._score_market_structure(df, direction, df_higher)
        scores['market_structure'] = ms_score
        reasons.extend(ms_reasons)
        
        # 2. PRICE ACTION (5 points)
        pa_score, pa_reasons = self._score_price_action(df, direction)
        scores['price_action'] = pa_score
        reasons.extend(pa_reasons)
        
        # 3. TECHNICAL INDICATORS (5 points)
        tech_score, tech_reasons = self._score_technical(df, direction)
        scores['technical'] = tech_score
        reasons.extend(tech_reasons)
        
        total_score = sum(scores.values())
        passed = total_score >= self.min_score

        return total_score, reasons, StageResult(
            stage_name="smart_entry",
            passed=passed,
            score=total_score,
            max_score=15,
            reason=f"Score {total_score}/15 (MS:{scores['market_structure']}, PA:{scores['price_action']}, Tech:{scores['technical']})",
            details=scores
        )

    def _score_market_structure(
        self,
        df: pd.DataFrame,
        direction: SignalDirection,
        df_higher: Optional[pd.DataFrame]
    ) -> Tuple[int, List[str]]:
        """Score market structure (0-5 points)"""
        score = 0
        reasons = []

        if len(df) < 50:
            return score, reasons

        # Calculate EMAs
        ema_8 = df['close'].ewm(span=8, adjust=False).mean()
        ema_21 = df['close'].ewm(span=21, adjust=False).mean()
        ema_50 = df['close'].ewm(span=50, adjust=False).mean()

        current_price = df['close'].iloc[-1]

        # Trend alignment (0-3 points)
        if direction == SignalDirection.LONG:
            if ema_8.iloc[-1] > ema_21.iloc[-1] > ema_50.iloc[-1]:
                score += 3
                reasons.append("✅ Strong uptrend (EMA stacked)")
            elif ema_8.iloc[-1] > ema_21.iloc[-1]:
                score += 2
                reasons.append("⚠️ Moderate uptrend")
            elif current_price > ema_21.iloc[-1]:
                score += 1
                reasons.append("📍 Price above EMA21")
        else:  # SHORT
            if ema_8.iloc[-1] < ema_21.iloc[-1] < ema_50.iloc[-1]:
                score += 3
                reasons.append("✅ Strong downtrend (EMA stacked)")
            elif ema_8.iloc[-1] < ema_21.iloc[-1]:
                score += 2
                reasons.append("⚠️ Moderate downtrend")
            elif current_price < ema_21.iloc[-1]:
                score += 1
                reasons.append("📍 Price below EMA21")

        # Pullback quality (0-2 points)
        if direction == SignalDirection.LONG:
            recent_low = df['low'].iloc[-5:].min()
            if recent_low <= ema_21.iloc[-5:].max() * 1.01 and current_price > ema_21.iloc[-1]:
                score += 2
                reasons.append("✅ Pullback to EMA21 completed")
        else:
            recent_high = df['high'].iloc[-5:].max()
            if recent_high >= ema_21.iloc[-5:].min() * 0.99 and current_price < ema_21.iloc[-1]:
                score += 2
                reasons.append("✅ Pullback to EMA21 completed")

        return min(score, 5), reasons

    def _score_price_action(
        self,
        df: pd.DataFrame,
        direction: SignalDirection
    ) -> Tuple[int, List[str]]:
        """Score price action patterns (0-5 points)"""
        score = 0
        reasons = []

        if len(df) < 3:
            return score, reasons

        prev2, prev, curr = df.iloc[-3], df.iloc[-2], df.iloc[-1]

        # Check engulfing patterns (0-2 points)
        if direction == SignalDirection.LONG:
            if (prev['close'] < prev['open'] and
                curr['close'] > curr['open'] and
                curr['open'] <= prev['close'] and
                curr['close'] >= prev['open']):
                score += 2
                reasons.append("🕯️ Bullish Engulfing")
        else:
            if (prev['close'] > prev['open'] and
                curr['close'] < curr['open'] and
                curr['open'] >= prev['close'] and
                curr['close'] <= prev['open']):
                score += 2
                reasons.append("🕯️ Bearish Engulfing")

        # Check pin bars (0-2 points)
        body = abs(curr['close'] - curr['open'])
        upper_wick = curr['high'] - max(curr['close'], curr['open'])
        lower_wick = min(curr['close'], curr['open']) - curr['low']

        if body > 0:
            if direction == SignalDirection.LONG and lower_wick > body * 2:
                score += 2
                reasons.append("📌 Bullish Pin Bar (Hammer)")
            elif direction == SignalDirection.SHORT and upper_wick > body * 2:
                score += 2
                reasons.append("📌 Bearish Pin Bar (Shooting Star)")

        # Candle direction match (0-1 point)
        if direction == SignalDirection.LONG and curr['close'] > curr['open']:
            score += 1
            reasons.append("🟢 Bullish candle")
        elif direction == SignalDirection.SHORT and curr['close'] < curr['open']:
            score += 1
            reasons.append("🔴 Bearish candle")

        return min(score, 5), reasons

    def _score_technical(
        self,
        df: pd.DataFrame,
        direction: SignalDirection
    ) -> Tuple[int, List[str]]:
        """Score technical indicators (0-5 points)"""
        score = 0
        reasons = []

        # RSI (0-2 points)
        if 'rsi' in df.columns:
            rsi = df['rsi'].iloc[-1]
            if direction == SignalDirection.LONG:
                if rsi < 30:
                    score += 2
                    reasons.append(f"📉 RSI oversold ({rsi:.1f})")
                elif 30 <= rsi < 45:
                    score += 1
                    reasons.append(f"⚡ RSI favorable ({rsi:.1f})")
            else:
                if rsi > 70:
                    score += 2
                    reasons.append(f"📈 RSI overbought ({rsi:.1f})")
                elif 55 < rsi <= 70:
                    score += 1
                    reasons.append(f"⚡ RSI favorable ({rsi:.1f})")

        # MACD (0-2 points)
        if 'macd' in df.columns and 'macd_signal' in df.columns and len(df) >= 2:
            macd_cross_bullish = (df['macd'].iloc[-1] > df['macd_signal'].iloc[-1] and
                                  df['macd'].iloc[-2] <= df['macd_signal'].iloc[-2])
            macd_cross_bearish = (df['macd'].iloc[-1] < df['macd_signal'].iloc[-1] and
                                  df['macd'].iloc[-2] >= df['macd_signal'].iloc[-2])

            if direction == SignalDirection.LONG and macd_cross_bullish:
                score += 2
                reasons.append("⚡ MACD Golden Cross")
            elif direction == SignalDirection.SHORT and macd_cross_bearish:
                score += 2
                reasons.append("⚡ MACD Death Cross")
            elif direction == SignalDirection.LONG and df['macd'].iloc[-1] > df['macd_signal'].iloc[-1]:
                score += 1
                reasons.append("📊 MACD bullish")
            elif direction == SignalDirection.SHORT and df['macd'].iloc[-1] < df['macd_signal'].iloc[-1]:
                score += 1
                reasons.append("📊 MACD bearish")

        # BB Position (0-1 point)
        if all(col in df.columns for col in ['bb_lower', 'bb_upper']):
            price = df['close'].iloc[-1]
            bb_lower = df['bb_lower'].iloc[-1]
            bb_upper = df['bb_upper'].iloc[-1]

            if direction == SignalDirection.LONG and price <= bb_lower * 1.01:
                score += 1
                reasons.append("🎯 Near BB Lower")
            elif direction == SignalDirection.SHORT and price >= bb_upper * 0.99:
                score += 1
                reasons.append("🎯 Near BB Upper")

        return min(score, 5), reasons
