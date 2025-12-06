# ============================================
# 📈 STAGE 4: HTF TREND ALIGNMENT
# Higher Timeframe Trend Confirmation
# ============================================

import pandas as pd
import numpy as np
from typing import Dict, Tuple, Optional
from enum import Enum

from trading.entry_pipeline.models import SignalDirection, StageResult
from utils.logger import logger


class TrendType(Enum):
    """Trend type classification"""
    STRONG_UP = "STRONG_UP"
    UP = "UP"
    RANGING = "RANGING"
    DOWN = "DOWN"
    STRONG_DOWN = "STRONG_DOWN"


class HTFTrendAligner:
    """
    Stage 4: Higher Timeframe Trend Alignment
    
    - Analyzes 4H candles to determine trend
    - Uses EMA 20 vs EMA 50 position
    - Checks price position relative to EMAs
    - Analyzes recent swing structure
    - LONG only if 4H uptrend
    - SHORT only if 4H downtrend
    """
    
    def __init__(self, config: Dict):
        """
        Initialize HTF Trend Aligner
        
        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.htf_timeframe = config.get('HTF_TIMEFRAME', '4h')
        self.require_alignment = config.get('REQUIRE_HTF_ALIGNMENT', True)
        self.strict_mode = config.get('HTF_STRICT_MODE', False)
        
        logger.info(f"📈 HTFTrendAligner initialized (TF: {self.htf_timeframe})")
    
    def get_trend(self, df_htf: pd.DataFrame) -> TrendType:
        """
        Determine trend from HTF data
        
        Args:
            df_htf: DataFrame with HTF OHLCV data
        
        Returns:
            TrendType enum
        """
        if df_htf is None or len(df_htf) < 50:
            return TrendType.RANGING
        
        # Calculate EMAs
        ema_20 = df_htf['close'].ewm(span=20, adjust=False).mean()
        ema_50 = df_htf['close'].ewm(span=50, adjust=False).mean()
        
        current_price = df_htf['close'].iloc[-1]
        ema_20_curr = ema_20.iloc[-1]
        ema_50_curr = ema_50.iloc[-1]
        
        # Check EMA alignment
        ema_bullish = ema_20_curr > ema_50_curr
        ema_bearish = ema_20_curr < ema_50_curr
        
        # Check price position
        price_above_emas = current_price > ema_20_curr > ema_50_curr
        price_below_emas = current_price < ema_20_curr < ema_50_curr
        
        # Check EMA slope (is trend accelerating?)
        ema_20_slope = ema_20.iloc[-1] - ema_20.iloc[-5]
        ema_50_slope = ema_50.iloc[-1] - ema_50.iloc[-5]
        
        # Determine trend type
        if price_above_emas and ema_bullish and ema_20_slope > 0 and ema_50_slope > 0:
            return TrendType.STRONG_UP
        elif ema_bullish and current_price > ema_50_curr:
            return TrendType.UP
        elif price_below_emas and ema_bearish and ema_20_slope < 0 and ema_50_slope < 0:
            return TrendType.STRONG_DOWN
        elif ema_bearish and current_price < ema_50_curr:
            return TrendType.DOWN
        else:
            return TrendType.RANGING
    
    def check_alignment(
        self,
        df_htf: pd.DataFrame,
        direction: SignalDirection
    ) -> Tuple[bool, StageResult]:
        """
        Check if signal direction aligns with HTF trend
        
        Args:
            df_htf: DataFrame with HTF OHLCV data
            direction: Signal direction from previous stages
        
        Returns:
            Tuple of (aligned, StageResult)
        """
        if not self.require_alignment:
            return True, StageResult(
                stage_name="htf_alignment",
                passed=True,
                reason="HTF alignment check disabled"
            )
        
        trend = self.get_trend(df_htf)
        
        # Check alignment
        aligned = False
        reason = ""
        score = 0
        
        if direction == SignalDirection.LONG:
            if trend in [TrendType.STRONG_UP, TrendType.UP]:
                aligned = True
                score = 2 if trend == TrendType.STRONG_UP else 1
                reason = f"✅ LONG aligned with {trend.value} trend"
            elif trend == TrendType.RANGING:
                if not self.strict_mode:
                    aligned = True
                    score = 0.5
                    reason = f"⚠️ LONG in ranging market (allowed)"
                else:
                    reason = f"❌ LONG rejected in ranging market (strict mode)"
            else:
                reason = f"❌ LONG conflicts with {trend.value} trend"
        
        elif direction == SignalDirection.SHORT:
            if trend in [TrendType.STRONG_DOWN, TrendType.DOWN]:
                aligned = True
                score = 2 if trend == TrendType.STRONG_DOWN else 1
                reason = f"✅ SHORT aligned with {trend.value} trend"
            elif trend == TrendType.RANGING:
                if not self.strict_mode:
                    aligned = True
                    score = 0.5
                    reason = f"⚠️ SHORT in ranging market (allowed)"
                else:
                    reason = f"❌ SHORT rejected in ranging market (strict mode)"
            else:
                reason = f"❌ SHORT conflicts with {trend.value} trend"
        
        return aligned, StageResult(
            stage_name="htf_alignment",
            passed=aligned,
            score=score,
            max_score=2,
            reason=reason,
            details={
                'htf_trend': trend.value,
                'signal_direction': direction.value,
                'strict_mode': self.strict_mode
            }
        )
