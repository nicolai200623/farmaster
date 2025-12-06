# ============================================
# 🎨 STAGE 3: PRICE ACTION VALIDATION
# Candlestick patterns, S/R levels, Volume, Divergence
# QUAN TRỌNG NHẤT - Core validation for entry quality
# ============================================

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field

from trading.entry_pipeline.models import SignalDirection, PriceActionResult, StageResult
from utils.logger import logger


@dataclass
class SupportResistanceLevels:
    """Support and Resistance levels"""
    supports: List[float] = field(default_factory=list)
    resistances: List[float] = field(default_factory=list)
    nearest_support: Optional[float] = None
    nearest_resistance: Optional[float] = None
    
    def get_nearest(self, price: float) -> Tuple[Optional[float], Optional[float]]:
        """Get nearest support and resistance to current price"""
        supports_below = [s for s in self.supports if s < price]
        resistances_above = [r for r in self.resistances if r > price]
        
        self.nearest_support = max(supports_below) if supports_below else None
        self.nearest_resistance = min(resistances_above) if resistances_above else None
        
        return self.nearest_support, self.nearest_resistance


class PriceActionValidator:
    """
    Stage 3: Price Action Validation
    
    Scoring system 8 points:
    1. Candlestick Pattern (0-2 points)
    2. Support/Resistance Proximity (0-2 points)
    3. Volume Confirmation (0-1 point)
    4. Candle Direction Match (0-1 point)
    5. No Divergence (0-1 point)
    6. Clean Price Structure (0-1 point)
    
    Minimum required: 5/8 points
    """
    
    # Pattern definitions
    BULLISH_PATTERNS = ['hammer', 'bullish_engulfing', 'morning_star', 'piercing_line', 'bullish_harami']
    BEARISH_PATTERNS = ['shooting_star', 'bearish_engulfing', 'evening_star', 'dark_cloud', 'bearish_harami']
    STRONG_PATTERNS = ['morning_star', 'evening_star', 'bullish_engulfing', 'bearish_engulfing']
    
    def __init__(self, config: Dict):
        """
        Initialize Price Action Validator
        
        Args:
            config: Configuration dictionary
        """
        self.config = config
        
        # Thresholds from config
        self.min_score = config.get('MIN_PRICE_ACTION_SCORE', 5)
        self.sr_lookback = config.get('SR_LOOKBACK_CANDLES', 50)
        self.sr_proximity_pct = config.get('SR_PROXIMITY_PCT', 0.5) / 100  # Convert to decimal
        self.volume_ratio = config.get('VOLUME_CONFIRMATION_RATIO', 1.5)
        
        # Cache for S/R levels (avoid recalculating every candle)
        self._sr_cache: Dict[str, SupportResistanceLevels] = {}
        self._sr_cache_candle: Dict[str, int] = {}  # Last candle count when cached
        
        logger.info(f"🎨 PriceActionValidator initialized (min score: {self.min_score}/8)")
    
    def validate(
        self,
        df: pd.DataFrame,
        direction: SignalDirection,
        symbol: str = ""
    ) -> Tuple[bool, int, PriceActionResult]:
        """
        Validate entry with Price Action analysis
        
        Args:
            df: DataFrame with OHLCV and indicators
            direction: Signal direction from previous stages
            symbol: Trading symbol (for caching)
        
        Returns:
            Tuple of (passed, score, PriceActionResult)
        """
        if len(df) < 20:
            return False, 0, PriceActionResult(passed=False, score=0)
        
        current_price = df['close'].iloc[-1]
        result = PriceActionResult(passed=False, score=0)
        
        # 1. Candlestick Pattern (0-2 points)
        patterns = self.detect_candlestick_patterns(df)
        pattern_score, detected = self._score_patterns(patterns, direction)
        result.candlestick_score = pattern_score
        result.patterns_detected = detected
        
        # 2. S/R Proximity (0-2 points)
        sr_levels = self._get_sr_levels(df, symbol)
        sr_score = self._score_sr_proximity(current_price, sr_levels, direction)
        result.sr_proximity_score = sr_score
        result.nearest_support = sr_levels.nearest_support
        result.nearest_resistance = sr_levels.nearest_resistance
        
        # 3. Volume Confirmation (0-1 point)
        volume_score = self._score_volume(df)
        result.volume_score = volume_score
        
        # 4. Candle Direction Match (0-1 point)
        direction_score = self._score_candle_direction(df, direction)
        result.candle_direction_score = direction_score
        
        # 5. No Divergence (0-1 point)
        divergence_score = self._score_divergence(df, direction)
        result.divergence_score = divergence_score
        
        # 6. Clean Price Structure (0-1 point)
        structure_score = self._score_structure(df)
        result.structure_score = structure_score
        
        # Calculate total score
        total = (pattern_score + sr_score + volume_score + 
                 direction_score + divergence_score + structure_score)
        result.score = total
        result.passed = total >= self.min_score
        
        # Build details
        result.details = {
            'patterns': detected,
            'sr_levels': {
                'support': sr_levels.nearest_support,
                'resistance': sr_levels.nearest_resistance
            },
            'volume_ratio': self._get_volume_ratio(df),
            'has_divergence': divergence_score == 0
        }

        return result.passed, result.score, result

    def detect_candlestick_patterns(self, df: pd.DataFrame) -> Dict[str, bool]:
        """
        Detect candlestick patterns in the data

        Args:
            df: DataFrame with OHLCV data

        Returns:
            Dictionary of pattern_name: detected (bool)
        """
        patterns = {p: False for p in self.BULLISH_PATTERNS + self.BEARISH_PATTERNS}

        if len(df) < 3:
            return patterns

        prev2, prev, curr = df.iloc[-3], df.iloc[-2], df.iloc[-1]

        # Helper calculations
        curr_body = abs(curr['close'] - curr['open'])
        curr_range = curr['high'] - curr['low']
        curr_upper_wick = curr['high'] - max(curr['close'], curr['open'])
        curr_lower_wick = min(curr['close'], curr['open']) - curr['low']
        curr_is_bullish = curr['close'] > curr['open']

        prev_body = abs(prev['close'] - prev['open'])
        prev_is_bullish = prev['close'] > prev['open']

        # Avoid division by zero
        if curr_range == 0:
            return patterns

        body_ratio = curr_body / curr_range

        # HAMMER (bullish) - Long lower wick, small body at top
        if curr_lower_wick > curr_body * 2 and curr_upper_wick < curr_body * 0.5:
            patterns['hammer'] = True

        # SHOOTING STAR (bearish) - Long upper wick, small body at bottom
        if curr_upper_wick > curr_body * 2 and curr_lower_wick < curr_body * 0.5:
            patterns['shooting_star'] = True

        # BULLISH ENGULFING
        if (not prev_is_bullish and curr_is_bullish and
            curr['open'] <= prev['close'] and curr['close'] >= prev['open'] and
            curr_body > prev_body * 1.1):
            patterns['bullish_engulfing'] = True

        # BEARISH ENGULFING
        if (prev_is_bullish and not curr_is_bullish and
            curr['open'] >= prev['close'] and curr['close'] <= prev['open'] and
            curr_body > prev_body * 1.1):
            patterns['bearish_engulfing'] = True

        # BULLISH HARAMI
        if (not prev_is_bullish and curr_is_bullish and
            curr['open'] > prev['close'] and curr['close'] < prev['open'] and
            curr_body < prev_body * 0.6):
            patterns['bullish_harami'] = True

        # BEARISH HARAMI
        if (prev_is_bullish and not curr_is_bullish and
            curr['open'] < prev['close'] and curr['close'] > prev['open'] and
            curr_body < prev_body * 0.6):
            patterns['bearish_harami'] = True

        # MORNING STAR (3-candle bullish reversal)
        prev2_is_bullish = prev2['close'] > prev2['open']
        prev2_body = abs(prev2['close'] - prev2['open'])
        prev_star = prev_body < prev2_body * 0.3  # Small middle candle

        if (not prev2_is_bullish and prev_star and curr_is_bullish and
            curr['close'] > (prev2['open'] + prev2['close']) / 2):
            patterns['morning_star'] = True

        # EVENING STAR (3-candle bearish reversal)
        if (prev2_is_bullish and prev_star and not curr_is_bullish and
            curr['close'] < (prev2['open'] + prev2['close']) / 2):
            patterns['evening_star'] = True

        # PIERCING LINE (bullish)
        if (not prev_is_bullish and curr_is_bullish and
            curr['open'] < prev['low'] and
            curr['close'] > (prev['open'] + prev['close']) / 2 and
            curr['close'] < prev['open']):
            patterns['piercing_line'] = True

        # DARK CLOUD COVER (bearish)
        if (prev_is_bullish and not curr_is_bullish and
            curr['open'] > prev['high'] and
            curr['close'] < (prev['open'] + prev['close']) / 2 and
            curr['close'] > prev['open']):
            patterns['dark_cloud'] = True

        return patterns

    def calculate_sr_levels(
        self,
        df: pd.DataFrame,
        lookback: int = 50
    ) -> SupportResistanceLevels:
        """
        Calculate Support/Resistance levels using swing points

        Args:
            df: DataFrame with OHLCV data
            lookback: Number of candles to analyze

        Returns:
            SupportResistanceLevels object
        """
        if len(df) < lookback:
            lookback = len(df)

        recent_df = df.tail(lookback)
        supports = []
        resistances = []

        # Find swing lows (support) and swing highs (resistance)
        for i in range(2, len(recent_df) - 2):
            # Swing low - lower than 2 candles on each side
            if (recent_df['low'].iloc[i] < recent_df['low'].iloc[i-1] and
                recent_df['low'].iloc[i] < recent_df['low'].iloc[i-2] and
                recent_df['low'].iloc[i] < recent_df['low'].iloc[i+1] and
                recent_df['low'].iloc[i] < recent_df['low'].iloc[i+2]):
                supports.append(recent_df['low'].iloc[i])

            # Swing high - higher than 2 candles on each side
            if (recent_df['high'].iloc[i] > recent_df['high'].iloc[i-1] and
                recent_df['high'].iloc[i] > recent_df['high'].iloc[i-2] and
                recent_df['high'].iloc[i] > recent_df['high'].iloc[i+1] and
                recent_df['high'].iloc[i] > recent_df['high'].iloc[i+2]):
                resistances.append(recent_df['high'].iloc[i])

        # Cluster nearby levels
        supports = self._cluster_levels(supports)
        resistances = self._cluster_levels(resistances)

        sr_levels = SupportResistanceLevels(
            supports=sorted(supports, reverse=True),
            resistances=sorted(resistances)
        )

        # Calculate nearest levels
        current_price = df['close'].iloc[-1]
        sr_levels.get_nearest(current_price)

        return sr_levels

    def _cluster_levels(self, levels: List[float], threshold: float = 0.005) -> List[float]:
        """Cluster nearby levels to avoid duplicates"""
        if not levels:
            return []

        levels = sorted(levels)
        clustered = [levels[0]]

        for level in levels[1:]:
            # If level is more than threshold away from last clustered level
            if abs(level - clustered[-1]) / clustered[-1] > threshold:
                clustered.append(level)
            else:
                # Average the nearby levels
                clustered[-1] = (clustered[-1] + level) / 2

        return clustered

    def _get_sr_levels(self, df: pd.DataFrame, symbol: str) -> SupportResistanceLevels:
        """Get S/R levels with caching"""
        candle_count = len(df)

        # Check cache validity (recalculate every 5 candles)
        if (symbol in self._sr_cache and
            symbol in self._sr_cache_candle and
            candle_count - self._sr_cache_candle[symbol] < 5):
            return self._sr_cache[symbol]

        # Calculate new levels
        sr_levels = self.calculate_sr_levels(df, self.sr_lookback)

        # Update cache
        self._sr_cache[symbol] = sr_levels
        self._sr_cache_candle[symbol] = candle_count

        return sr_levels

    def _score_patterns(
        self,
        patterns: Dict[str, bool],
        direction: SignalDirection
    ) -> Tuple[int, List[str]]:
        """Score candlestick patterns (0-2 points)"""
        detected = [p for p, v in patterns.items() if v]

        if not detected:
            return 0, []

        score = 0
        valid_patterns = []

        for pattern in detected:
            is_bullish = pattern in self.BULLISH_PATTERNS
            is_bearish = pattern in self.BEARISH_PATTERNS
            is_strong = pattern in self.STRONG_PATTERNS

            # Check if pattern matches direction
            if (direction == SignalDirection.LONG and is_bullish) or \
               (direction == SignalDirection.SHORT and is_bearish):
                valid_patterns.append(pattern)
                score += 2 if is_strong else 1

        return min(score, 2), valid_patterns

    def _score_sr_proximity(
        self,
        price: float,
        sr_levels: SupportResistanceLevels,
        direction: SignalDirection
    ) -> int:
        """Score S/R proximity (0-2 points)"""
        # LONG near support = good, SHORT near resistance = good
        if direction == SignalDirection.LONG and sr_levels.nearest_support:
            distance_pct = (price - sr_levels.nearest_support) / price
            if distance_pct <= self.sr_proximity_pct:
                return 2
            elif distance_pct <= self.sr_proximity_pct * 2:
                return 1

        elif direction == SignalDirection.SHORT and sr_levels.nearest_resistance:
            distance_pct = (sr_levels.nearest_resistance - price) / price
            if distance_pct <= self.sr_proximity_pct:
                return 2
            elif distance_pct <= self.sr_proximity_pct * 2:
                return 1

        return 0

    def _score_volume(self, df: pd.DataFrame) -> int:
        """Score volume confirmation (0-1 point)"""
        if 'volume' not in df.columns or len(df) < 20:
            return 0

        current_vol = df['volume'].iloc[-1]
        avg_vol = df['volume'].rolling(20).mean().iloc[-1]

        if avg_vol > 0 and current_vol > avg_vol * self.volume_ratio:
            return 1
        return 0

    def _get_volume_ratio(self, df: pd.DataFrame) -> float:
        """Get current volume ratio"""
        if 'volume' not in df.columns or len(df) < 20:
            return 0.0

        current_vol = df['volume'].iloc[-1]
        avg_vol = df['volume'].rolling(20).mean().iloc[-1]

        return current_vol / avg_vol if avg_vol > 0 else 0.0

    def _score_candle_direction(self, df: pd.DataFrame, direction: SignalDirection) -> int:
        """Score candle direction match (0-1 point)"""
        curr = df.iloc[-1]
        is_bullish = curr['close'] > curr['open']

        if (direction == SignalDirection.LONG and is_bullish) or \
           (direction == SignalDirection.SHORT and not is_bullish):
            return 1
        return 0

    def _score_divergence(self, df: pd.DataFrame, direction: SignalDirection) -> int:
        """Score no divergence (0-1 point) - 1 if NO conflicting divergence"""
        if 'rsi' not in df.columns or len(df) < 20:
            return 1  # No data to check, assume OK

        # Check for divergence in last 20 candles
        has_bearish_div = self._check_divergence(df, 'bearish')
        has_bullish_div = self._check_divergence(df, 'bullish')

        # LONG signal + bearish divergence = bad
        if direction == SignalDirection.LONG and has_bearish_div:
            return 0

        # SHORT signal + bullish divergence = bad
        if direction == SignalDirection.SHORT and has_bullish_div:
            return 0

        return 1

    def _check_divergence(self, df: pd.DataFrame, div_type: str) -> bool:
        """Check for RSI divergence"""
        lookback = 20
        if len(df) < lookback:
            return False

        recent = df.tail(lookback)
        price = recent['close']
        rsi = recent['rsi']

        # Find peaks/troughs
        half = lookback // 2

        if div_type == 'bearish':
            # Price higher high, RSI lower high
            price_first_half_max = price.iloc[:half].max()
            price_second_half_max = price.iloc[half:].max()
            rsi_first_half_max = rsi.iloc[:half].max()
            rsi_second_half_max = rsi.iloc[half:].max()

            return price_second_half_max > price_first_half_max and \
                   rsi_second_half_max < rsi_first_half_max
        else:
            # Price lower low, RSI higher low
            price_first_half_min = price.iloc[:half].min()
            price_second_half_min = price.iloc[half:].min()
            rsi_first_half_min = rsi.iloc[:half].min()
            rsi_second_half_min = rsi.iloc[half:].min()

            return price_second_half_min < price_first_half_min and \
                   rsi_second_half_min > rsi_first_half_min

    def _score_structure(self, df: pd.DataFrame) -> int:
        """Score clean price structure (0-1 point)"""
        if len(df) < 10:
            return 0

        # Check for inside bar (indecision) - not good
        curr = df.iloc[-1]
        prev = df.iloc[-2]

        is_inside_bar = (curr['high'] < prev['high'] and
                         curr['low'] > prev['low'])
        if is_inside_bar:
            return 0

        # Check ATR consistency (not erratic)
        if 'atr' in df.columns:
            atr_recent = df['atr'].iloc[-5:].std()
            atr_avg = df['atr'].iloc[-20:].mean()

            if atr_avg > 0 and atr_recent / atr_avg < 0.5:
                return 1  # ATR is stable

        return 1  # Default to OK

    def to_stage_result(self, pa_result: PriceActionResult) -> StageResult:
        """Convert PriceActionResult to StageResult"""
        return StageResult(
            stage_name="price_action",
            passed=pa_result.passed,
            score=pa_result.score,
            max_score=pa_result.max_score,
            reason=f"PA Score {pa_result.score}/8 - Patterns: {pa_result.patterns_detected}",
            details={
                'candlestick': pa_result.candlestick_score,
                'sr_proximity': pa_result.sr_proximity_score,
                'volume': pa_result.volume_score,
                'direction': pa_result.candle_direction_score,
                'divergence': pa_result.divergence_score,
                'structure': pa_result.structure_score,
                'patterns': pa_result.patterns_detected,
                'support': pa_result.nearest_support,
                'resistance': pa_result.nearest_resistance
            }
        )
