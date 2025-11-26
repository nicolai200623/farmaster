# ============================================
# 🎯 ADVANCED ENTRY SYSTEM
# Confluence scoring với market structure analysis
# ============================================

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from config import Config
from utils.logger import logger

class AdvancedEntrySystem:
    """
    Advanced Entry System với:
    - Market structure analysis
    - Price action patterns
    - Smart Money Concepts (Order Blocks, FVG, Liquidity Sweeps)
    - Technical confluence
    - Volume analysis
    """

    def __init__(self, min_confluence_score=7):
        self.min_confluence_score = min_confluence_score
        self.entry_reasons = []

    def should_enter_trade(self, df: pd.DataFrame, symbol: str) -> Tuple[str, float, List[str]]:
        """
        Determine if should enter trade với confluence analysis

        Args:
            df: DataFrame with OHLCV and indicators
            symbol: Trading symbol

        Returns:
            signal: 'LONG', 'SHORT', or 'HOLD'
            confluence_score: Total score
            reasons: List of entry reasons
        """
        try:
            # 1. Market Structure Analysis
            market_structure = self._analyze_market_structure(df)

            # 2. Price Action Patterns
            price_patterns = self._detect_price_patterns(df)

            # 3. Smart Money Concepts
            smc_signals = self._analyze_smart_money(df)

            # 4. Technical Indicators Confluence
            technical_confluence = self._check_technical_confluence(df)

            # 5. Volume Analysis
            volume_signal = self._analyze_volume(df)

            # 6. Calculate Total Confluence
            long_score = 0
            short_score = 0
            long_reasons = []
            short_reasons = []

            # Market Structure Scoring (3 points)
            if market_structure['trend'] == 'STRONG_UP':
                if market_structure['pullback_complete']:
                    long_score += 3
                    long_reasons.append("✅ Pullback complete in uptrend")
            elif market_structure['trend'] == 'STRONG_DOWN':
                if market_structure['pullback_complete']:
                    short_score += 3
                    short_reasons.append("✅ Pullback complete in downtrend")

            # Price away from EMAs (1 point for better entry)
            if market_structure['trend'] == 'STRONG_UP' and market_structure['position_in_range'] < 0.5:
                long_score += 1
                long_reasons.append("📍 Good entry position (lower range)")
            elif market_structure['trend'] == 'STRONG_DOWN' and market_structure['position_in_range'] > 0.5:
                short_score += 1
                short_reasons.append("📍 Good entry position (upper range)")

            # Price Pattern Scoring (2 points each)
            if price_patterns['bullish_engulfing']:
                long_score += 2
                long_reasons.append("🕯️ Bullish Engulfing")
            if price_patterns['bearish_engulfing']:
                short_score += 2
                short_reasons.append("🕯️ Bearish Engulfing")
            if price_patterns['pin_bar'] == 'bullish':
                long_score += 2
                long_reasons.append("📌 Bullish Pin Bar")
            elif price_patterns['pin_bar'] == 'bearish':
                short_score += 2
                short_reasons.append("📌 Bearish Pin Bar")
            if price_patterns['morning_star']:
                long_score += 3
                long_reasons.append("⭐ Morning Star")
            if price_patterns['evening_star']:
                short_score += 3
                short_reasons.append("⭐ Evening Star")

            # Smart Money Concepts (2-3 points)
            if smc_signals['order_block'] == 'bullish':
                long_score += 3
                long_reasons.append("🔷 Bullish Order Block")
            elif smc_signals['order_block'] == 'bearish':
                short_score += 3
                short_reasons.append("🔷 Bearish Order Block")

            if smc_signals['fair_value_gap'] == 'bullish':
                long_score += 2
                long_reasons.append("📊 Bullish FVG")
            elif smc_signals['fair_value_gap'] == 'bearish':
                short_score += 2
                short_reasons.append("📊 Bearish FVG")

            if smc_signals['liquidity_sweep'] == 'bullish':
                long_score += 3
                long_reasons.append("💧 Bullish Liquidity Sweep")
            elif smc_signals['liquidity_sweep'] == 'bearish':
                short_score += 3
                short_reasons.append("💧 Bearish Liquidity Sweep")

            # Technical Indicators (1-3 points)
            if technical_confluence['rsi_oversold']:
                long_score += 1
                long_reasons.append("📉 RSI Oversold")
            elif technical_confluence['rsi_overbought']:
                short_score += 1
                short_reasons.append("📈 RSI Overbought")

            if technical_confluence['rsi_divergence'] == 'bullish':
                long_score += 3
                long_reasons.append("🔀 Bullish RSI Divergence")
            elif technical_confluence['rsi_divergence'] == 'bearish':
                short_score += 3
                short_reasons.append("🔀 Bearish RSI Divergence")

            if technical_confluence['macd_cross'] == 'golden':
                long_score += 2
                long_reasons.append("⚡ MACD Golden Cross")
            elif technical_confluence['macd_cross'] == 'death':
                short_score += 2
                short_reasons.append("⚡ MACD Death Cross")

            if technical_confluence['bb_squeeze']:
                # BB squeeze + breakout direction
                if df['close'].iloc[-1] > df['bb_middle'].iloc[-1]:
                    long_score += 2
                    long_reasons.append("🎯 BB Squeeze Breakout Up")
                else:
                    short_score += 2
                    short_reasons.append("🎯 BB Squeeze Breakout Down")

            # Volume Confirmation (2 points)
            if volume_signal['volume_spike']:
                if long_score > short_score:
                    long_score += 2
                    long_reasons.append("📈 Volume Spike")
                elif short_score > long_score:
                    short_score += 2
                    short_reasons.append("📈 Volume Spike")

            # DECISION
            if long_score >= self.min_confluence_score and long_score > short_score:
                return 'LONG', long_score, long_reasons
            elif short_score >= self.min_confluence_score and short_score > long_score:
                return 'SHORT', short_score, short_reasons
            else:
                # Return reasons even for HOLD (for debugging)
                all_reasons = []
                if long_score > 0:
                    all_reasons.extend([f"LONG({long_score}): {r}" for r in long_reasons[:2]])
                if short_score > 0:
                    all_reasons.extend([f"SHORT({short_score}): {r}" for r in short_reasons[:2]])
                return 'HOLD', max(long_score, short_score), all_reasons

        except Exception as e:
            logger.error(f"Advanced entry error for {symbol}: {e}")
            return 'HOLD', 0, []

    def _analyze_market_structure(self, df: pd.DataFrame) -> Dict:
        """Analyze market structure để xác định trend và pullback"""

        # Calculate EMAs if not present
        if 'ema_8' not in df.columns:
            df['ema_8'] = df['close'].ewm(span=8, adjust=False).mean()
        if 'ema_21' not in df.columns:
            df['ema_21'] = df['close'].ewm(span=21, adjust=False).mean()
        if 'ema_50' not in df.columns:
            df['ema_50'] = df['close'].ewm(span=50, adjust=False).mean()
        if 'ema_200' not in df.columns:
            df['ema_200'] = df['close'].ewm(span=200, adjust=False).mean()

        current_price = df['close'].iloc[-1]

        # Determine trend
        if df['ema_8'].iloc[-1] > df['ema_21'].iloc[-1] > df['ema_50'].iloc[-1]:
            trend = 'STRONG_UP'
        elif df['ema_8'].iloc[-1] < df['ema_21'].iloc[-1] < df['ema_50'].iloc[-1]:
            trend = 'STRONG_DOWN'
        else:
            trend = 'RANGING'

        # Check for pullback completion
        pullback_complete = False
        if trend == 'STRONG_UP' and len(df) >= 3:
            # Price pulled back to EMA21 and bouncing
            if df['low'].iloc[-2] <= df['ema_21'].iloc[-2] and \
               df['close'].iloc[-1] > df['ema_21'].iloc[-1]:
                pullback_complete = True
        elif trend == 'STRONG_DOWN' and len(df) >= 3:
            # Price pulled up to EMA21 and rejecting
            if df['high'].iloc[-2] >= df['ema_21'].iloc[-2] and \
               df['close'].iloc[-1] < df['ema_21'].iloc[-1]:
                pullback_complete = True

        # Find key levels
        swing_high = df['high'].rolling(20).max().iloc[-1]
        swing_low = df['low'].rolling(20).min().iloc[-1]

        # Position in range
        range_size = swing_high - swing_low
        if range_size > 0:
            position_in_range = (current_price - swing_low) / range_size
        else:
            position_in_range = 0.5

        return {
            'trend': trend,
            'pullback_complete': pullback_complete,
            'swing_high': swing_high,
            'swing_low': swing_low,
            'position_in_range': position_in_range
        }

    def _detect_price_patterns(self, df: pd.DataFrame) -> Dict:
        """Detect important candlestick patterns"""

        patterns = {
            'bullish_engulfing': False,
            'bearish_engulfing': False,
            'pin_bar': None,
            'doji': False,
            'morning_star': False,
            'evening_star': False
        }

        if len(df) < 3:
            return patterns

        # Get last 3 candles
        prev2 = df.iloc[-3]
        prev = df.iloc[-2]
        curr = df.iloc[-1]

        # Bullish Engulfing
        if prev['close'] < prev['open'] and \
           curr['close'] > curr['open'] and \
           curr['open'] <= prev['close'] and \
           curr['close'] >= prev['open']:
            patterns['bullish_engulfing'] = True

        # Bearish Engulfing
        if prev['close'] > prev['open'] and \
           curr['close'] < curr['open'] and \
           curr['open'] >= prev['close'] and \
           curr['close'] <= prev['open']:
            patterns['bearish_engulfing'] = True

        # Pin Bar
        body = abs(curr['close'] - curr['open'])
        upper_wick = curr['high'] - max(curr['close'], curr['open'])
        lower_wick = min(curr['close'], curr['open']) - curr['low']
        total_range = curr['high'] - curr['low']

        if total_range > 0 and body > 0:
            if lower_wick > body * 2 and upper_wick < body:
                patterns['pin_bar'] = 'bullish'
            elif upper_wick > body * 2 and lower_wick < body:
                patterns['pin_bar'] = 'bearish'

        # Doji
        if total_range > 0 and body / total_range < 0.1:
            patterns['doji'] = True

        # Morning Star (bullish reversal)
        # Candle 1: bearish, Candle 2: small body (star), Candle 3: bullish
        if prev2['close'] < prev2['open']:  # First candle bearish
            prev_body = abs(prev['close'] - prev['open'])
            if prev_body < abs(prev2['close'] - prev2['open']) * 0.3:  # Small star
                if curr['close'] > curr['open'] and \
                   curr['close'] > (prev2['open'] + prev2['close']) / 2:  # Strong bullish close
                    patterns['morning_star'] = True

        # Evening Star (bearish reversal)
        if prev2['close'] > prev2['open']:  # First candle bullish
            prev_body = abs(prev['close'] - prev['open'])
            if prev_body < abs(prev2['close'] - prev2['open']) * 0.3:  # Small star
                if curr['close'] < curr['open'] and \
                   curr['close'] < (prev2['open'] + prev2['close']) / 2:  # Strong bearish close
                    patterns['evening_star'] = True

        return patterns

    def _analyze_smart_money(self, df: pd.DataFrame) -> Dict:
        """Analyze Smart Money Concepts"""

        smc_signals = {
            'order_block': None,
            'fair_value_gap': None,
            'liquidity_sweep': None,
            'break_of_structure': None
        }

        if len(df) < 20:
            return smc_signals

        # Order Block Detection
        # Tìm vùng có strong move sau consolidation
        avg_volume = df['volume'].rolling(20).mean().iloc[-1]

        for i in range(-10, -2):
            try:
                if df['volume'].iloc[i] > avg_volume * 2:
                    # High volume candle
                    if df['close'].iloc[i] > df['open'].iloc[i]:
                        # Bullish OB
                        ob_high = df['high'].iloc[i]
                        ob_low = df['low'].iloc[i]
                        # Check if current price is testing this OB
                        if df['low'].iloc[-1] <= ob_high and df['low'].iloc[-1] >= ob_low:
                            smc_signals['order_block'] = 'bullish'
                            break
                    else:
                        # Bearish OB
                        ob_high = df['high'].iloc[i]
                        ob_low = df['low'].iloc[i]
                        if df['high'].iloc[-1] >= ob_low and df['high'].iloc[-1] <= ob_high:
                            smc_signals['order_block'] = 'bearish'
                            break
            except:
                continue

        # Fair Value Gap (FVG)
        if len(df) >= 3:
            # Gap between candle 1 high and candle 3 low (bullish FVG)
            if df['low'].iloc[-1] > df['high'].iloc[-3]:
                smc_signals['fair_value_gap'] = 'bullish'
            # Gap between candle 1 low and candle 3 high (bearish FVG)
            elif df['high'].iloc[-1] < df['low'].iloc[-3]:
                smc_signals['fair_value_gap'] = 'bearish'

        # Liquidity Sweep
        # Price takes out previous low/high then reverses strongly
        if len(df) >= 25:
            recent_low = df['low'].iloc[-25:-5].min()
            recent_high = df['high'].iloc[-25:-5].max()

            # Bullish sweep: take out low then reverse up
            if df['low'].iloc[-2] < recent_low and \
               df['close'].iloc[-1] > recent_low and \
               df['close'].iloc[-1] > df['open'].iloc[-1]:
                smc_signals['liquidity_sweep'] = 'bullish'

            # Bearish sweep: take out high then reverse down
            elif df['high'].iloc[-2] > recent_high and \
                 df['close'].iloc[-1] < recent_high and \
                 df['close'].iloc[-1] < df['open'].iloc[-1]:
                smc_signals['liquidity_sweep'] = 'bearish'

        return smc_signals

    def _check_technical_confluence(self, df: pd.DataFrame) -> Dict:
        """Check technical indicators confluence"""

        confluence = {
            'rsi_oversold': False,
            'rsi_overbought': False,
            'rsi_divergence': None,
            'macd_cross': None,
            'bb_squeeze': False,
            'stochastic_oversold': False
        }

        # RSI
        if 'rsi' in df.columns:
            current_rsi = df['rsi'].iloc[-1]
            if current_rsi < 30:
                confluence['rsi_oversold'] = True
            elif current_rsi > 70:
                confluence['rsi_overbought'] = True

            # RSI Divergence
            divergence = self._detect_divergence(df['close'], df['rsi'], periods=14)
            if divergence == 'bullish':
                confluence['rsi_divergence'] = 'bullish'
            elif divergence == 'bearish':
                confluence['rsi_divergence'] = 'bearish'

        # MACD Cross
        if 'macd' in df.columns and 'macd_signal' in df.columns and len(df) >= 2:
            if df['macd'].iloc[-1] > df['macd_signal'].iloc[-1] and \
               df['macd'].iloc[-2] <= df['macd_signal'].iloc[-2]:
                confluence['macd_cross'] = 'golden'
            elif df['macd'].iloc[-1] < df['macd_signal'].iloc[-1] and \
                 df['macd'].iloc[-2] >= df['macd_signal'].iloc[-2]:
                confluence['macd_cross'] = 'death'

        # Bollinger Band Squeeze
        if 'bb_upper' in df.columns and 'bb_lower' in df.columns and len(df) >= 20:
            bb_width = df['bb_upper'].iloc[-1] - df['bb_lower'].iloc[-1]
            bb_width_avg = (df['bb_upper'] - df['bb_lower']).rolling(20).mean().iloc[-1]
            if bb_width < bb_width_avg * 0.7:
                confluence['bb_squeeze'] = True

        return confluence

    def _analyze_volume(self, df: pd.DataFrame) -> Dict:
        """Analyze volume for confirmation"""

        volume_analysis = {
            'volume_spike': False,
            'volume_dry_up': False,
            'volume_trend': None
        }

        if 'volume' not in df.columns or len(df) < 20:
            return volume_analysis

        current_vol = df['volume'].iloc[-1]
        avg_vol = df['volume'].rolling(20).mean().iloc[-1]

        if avg_vol > 0:
            if current_vol > avg_vol * 1.5:
                volume_analysis['volume_spike'] = True
            elif current_vol < avg_vol * 0.5:
                volume_analysis['volume_dry_up'] = True

        # Volume trend
        vol_sma_5 = df['volume'].rolling(5).mean().iloc[-1]
        vol_sma_20 = df['volume'].rolling(20).mean().iloc[-1]

        if vol_sma_5 > vol_sma_20:
            volume_analysis['volume_trend'] = 'increasing'
        else:
            volume_analysis['volume_trend'] = 'decreasing'

        return volume_analysis

    def _detect_divergence(self, price: pd.Series, indicator: pd.Series, periods: int = 14) -> str:
        """
        Detect divergence between price and indicator

        Returns:
            'bullish', 'bearish', or None
        """

        if len(price) < periods or len(indicator) < periods:
            return None

        # Find recent peaks/troughs
        price_peaks = []
        indicator_peaks = []

        price_troughs = []
        indicator_troughs = []

        for i in range(-periods, -1):
            try:
                # Price and indicator peaks
                if i > -periods and i < -1:
                    if price.iloc[i] > price.iloc[i-1] and price.iloc[i] > price.iloc[i+1]:
                        price_peaks.append((i, price.iloc[i]))
                    if indicator.iloc[i] > indicator.iloc[i-1] and indicator.iloc[i] > indicator.iloc[i+1]:
                        indicator_peaks.append((i, indicator.iloc[i]))

                    # Troughs
                    if price.iloc[i] < price.iloc[i-1] and price.iloc[i] < price.iloc[i+1]:
                        price_troughs.append((i, price.iloc[i]))
                    if indicator.iloc[i] < indicator.iloc[i-1] and indicator.iloc[i] < indicator.iloc[i+1]:
                        indicator_troughs.append((i, indicator.iloc[i]))
            except:
                continue

        # Check for bullish divergence (price lower low, indicator higher low)
        if len(price_troughs) >= 2 and len(indicator_troughs) >= 2:
            if price_troughs[-1][1] < price_troughs[-2][1] and \
               indicator_troughs[-1][1] > indicator_troughs[-2][1]:
                return 'bullish'

        # Check for bearish divergence (price higher high, indicator lower high)
        if len(price_peaks) >= 2 and len(indicator_peaks) >= 2:
            if price_peaks[-1][1] > price_peaks[-2][1] and \
               indicator_peaks[-1][1] < indicator_peaks[-2][1]:
                return 'bearish'

        return None

    def get_entry_price(self, df: pd.DataFrame, signal: str) -> float:
        """
        Calculate optimal entry price

        Args:
            df: DataFrame with OHLCV
            signal: 'LONG' or 'SHORT'

        Returns:
            float: Optimal entry price
        """

        current_price = df['close'].iloc[-1]

        # Calculate ATR if available
        if 'atr' in df.columns:
            atr = df['atr'].iloc[-1]
        else:
            # Calculate simple ATR
            high_low = df['high'] - df['low']
            atr = high_low.rolling(14).mean().iloc[-1]

        if signal == 'LONG':
            # Enter slightly above current price
            entry_price = current_price * 1.001  # 0.1% above

            # Or wait for pullback to EMA21
            if 'ema_21' in df.columns:
                ema21 = df['ema_21'].iloc[-1]
                if current_price > ema21 * 1.02:  # If price is 2% above EMA21
                    entry_price = ema21 * 1.005  # Set limit order at EMA21

        elif signal == 'SHORT':
            entry_price = current_price * 0.999  # 0.1% below

            if 'ema_21' in df.columns:
                ema21 = df['ema_21'].iloc[-1]
                if current_price < ema21 * 0.98:  # If price is 2% below EMA21
                    entry_price = ema21 * 0.995

        else:
            entry_price = current_price

        return round(entry_price, 8)  # Round to 8 decimals for crypto


# ============================================
# 🎯 SMART ENTRY SYSTEM V2
# Improved entry timing with better scoring
# ============================================

class SmartEntrySystemV2:
    """
    Smart Entry System V2 - Focus on TIMING and QUALITY

    Principles:
    1. Trend Alignment First - Never trade against the trend
    2. Wait for Pullback - Don't entry at tops/bottoms
    3. Confirm with Volume - Volume must confirm the move
    4. Session Timing - Entry during high liquidity sessions
    5. Risk/Reward Filter - Only entry when R:R > min ratio
    """

    def __init__(self, min_score=6, min_rr_ratio=2.0):
        """
        Initialize Smart Entry System V2

        Args:
            min_score: Minimum total score to enter (0-15)
            min_rr_ratio: Minimum Risk:Reward ratio (default 2:1)
        """
        self.min_score = min_score
        self.min_rr_ratio = min_rr_ratio

    def evaluate_entry(self, symbol: str, df_primary: pd.DataFrame,
                      df_higher: pd.DataFrame = None,
                      df_4h: pd.DataFrame = None) -> Tuple[str, float, float, float, float, List[str]]:
        """
        Comprehensive entry evaluation

        Args:
            symbol: Trading symbol
            df_primary: Primary timeframe data (e.g., 15m)
            df_higher: Higher timeframe data (e.g., 1h)
            df_4h: 4H timeframe for long-term trend

        Returns:
            signal: 'LONG', 'SHORT', 'HOLD'
            score: Total score (0-15)
            entry_price: Suggested entry
            sl_price: Stop loss
            tp_price: Take profit
            reasons: List of reasons
        """
        try:
            scores = {
                'trend_alignment': 0,      # 0-3 (MOST IMPORTANT)
                'pullback_quality': 0,     # 0-3
                'key_level': 0,            # 0-2
                'volume_confirmation': 0,  # 0-2
                'momentum': 0,             # 0-2
                'session_timing': 0,       # 0-2
                'rr_ratio': 0,             # 0-1
            }
            reasons = []

            # 1. TREND ALIGNMENT (Most Important - 3 points)
            trend_primary = self._get_trend(df_primary)
            trend_higher = self._get_trend(df_higher) if df_higher is not None else trend_primary
            trend_4h = self._get_trend(df_4h) if df_4h is not None else trend_higher

            if trend_4h == trend_higher == trend_primary:
                scores['trend_alignment'] = 3
                direction = trend_4h
                reasons.append(f"✅ Perfect alignment: All TFs {direction}")
            elif trend_4h == trend_higher:
                scores['trend_alignment'] = 2
                direction = trend_4h
                reasons.append(f"⚠️ HTF aligned ({direction}), LTF diverging")
            elif trend_4h == trend_primary:
                scores['trend_alignment'] = 1
                direction = trend_4h
                reasons.append(f"⚠️ 4H & Primary aligned ({direction})")
            else:
                # No clear alignment - HOLD
                reasons.append("❌ No trend alignment - too risky")
                return 'HOLD', 0, None, None, None, reasons

            # 2. PULLBACK QUALITY (3 points)
            pullback_score, pullback_reason = self._evaluate_pullback(df_primary, direction)
            scores['pullback_quality'] = pullback_score
            reasons.append(pullback_reason)

            # 3. KEY LEVELS (2 points)
            level_score, level_reason = self._check_key_levels(df_primary, df_higher)
            scores['key_level'] = level_score
            if level_score > 0:
                reasons.append(level_reason)

            # 4. VOLUME CONFIRMATION (2 points)
            vol_score, vol_reason = self._check_volume_confirmation(df_primary)
            scores['volume_confirmation'] = vol_score
            if vol_score > 0:
                reasons.append(vol_reason)

            # 5. MOMENTUM (2 points)
            mom_score, mom_reason = self._check_momentum(df_primary, direction)
            scores['momentum'] = mom_score
            if mom_score > 0:
                reasons.append(mom_reason)

            # 6. SESSION TIMING (2 points)
            session_score, session_reason = self._get_session_score()
            scores['session_timing'] = session_score
            reasons.append(session_reason)

            # 7. CALCULATE R:R RATIO (1 point)
            entry_price = df_primary['close'].iloc[-1]
            sl_price = self._calculate_sl(df_primary, direction)
            tp_price = self._calculate_tp(entry_price, sl_price, direction)

            if sl_price and tp_price:
                risk = abs(entry_price - sl_price)
                reward = abs(tp_price - entry_price)
                rr_ratio = reward / risk if risk > 0 else 0

                if rr_ratio >= self.min_rr_ratio:
                    scores['rr_ratio'] = 1
                    reasons.append(f"✅ R:R = {rr_ratio:.1f}:1")
                else:
                    reasons.append(f"❌ R:R = {rr_ratio:.1f}:1 (need >{self.min_rr_ratio}:1)")
            else:
                reasons.append("❌ Cannot calculate R:R")

            # TOTAL SCORE
            total_score = sum(scores.values())

            # DECISION
            if total_score >= self.min_score and scores['trend_alignment'] >= 2:
                signal = 'LONG' if direction == 'UP' else 'SHORT'
                logger.info(f"🎯 {symbol} {signal} Signal | Score: {total_score}/15")
                for reason in reasons:
                    logger.info(f"   {reason}")
                return signal, total_score, entry_price, sl_price, tp_price, reasons
            else:
                return 'HOLD', total_score, None, None, None, reasons

        except Exception as e:
            logger.error(f"SmartEntryV2 error for {symbol}: {e}")
            return 'HOLD', 0, None, None, None, []

    def _get_trend(self, df: pd.DataFrame) -> str:
        """
        Determine trend direction

        Returns:
            'UP', 'DOWN', or 'RANGING'
        """
        if df is None or len(df) < 50:
            return 'RANGING'

        # Calculate EMAs if not present
        if 'ema_8' not in df.columns:
            df['ema_8'] = df['close'].ewm(span=8, adjust=False).mean()
        if 'ema_21' not in df.columns:
            df['ema_21'] = df['close'].ewm(span=21, adjust=False).mean()
        if 'ema_50' not in df.columns:
            df['ema_50'] = df['close'].ewm(span=50, adjust=False).mean()

        ema8 = df['ema_8'].iloc[-1]
        ema21 = df['ema_21'].iloc[-1]
        ema50 = df['ema_50'].iloc[-1]

        if ema8 > ema21 > ema50:
            return 'UP'
        elif ema8 < ema21 < ema50:
            return 'DOWN'
        else:
            return 'RANGING'

    def _evaluate_pullback(self, df: pd.DataFrame, direction: str) -> Tuple[int, str]:
        """
        Evaluate pullback quality

        Returns:
            score: 0-3
            reason: Description
        """
        if len(df) < 5:
            return 0, "Not enough data"

        current_price = df['close'].iloc[-1]
        ema21 = df['ema_21'].iloc[-1] if 'ema_21' in df.columns else df['close'].ewm(span=21).mean().iloc[-1]

        if direction == 'UP':
            # Check if price pulled back to EMA21 and bouncing
            recent_low = df['low'].iloc[-5:].min()
            if recent_low <= ema21 * 1.02 and current_price > ema21:
                return 3, "✅ Perfect pullback to EMA21"
            elif current_price > ema21 * 0.98:
                return 2, "⚠️ Near EMA21"
            else:
                return 1, "📍 Pullback in progress"

        elif direction == 'DOWN':
            # Check if price pulled up to EMA21 and rejecting
            recent_high = df['high'].iloc[-5:].max()
            if recent_high >= ema21 * 0.98 and current_price < ema21:
                return 3, "✅ Perfect pullback to EMA21"
            elif current_price < ema21 * 1.02:
                return 2, "⚠️ Near EMA21"
            else:
                return 1, "📍 Pullback in progress"

        return 0, "No clear pullback"

    def _check_key_levels(self, df_primary: pd.DataFrame, df_higher: pd.DataFrame) -> Tuple[int, str]:
        """
        Check if price is at key support/resistance levels

        Returns:
            score: 0-2
            reason: Description
        """
        if len(df_primary) < 20:
            return 0, ""

        current_price = df_primary['close'].iloc[-1]

        # Check swing highs/lows on primary timeframe
        swing_high = df_primary['high'].rolling(20).max().iloc[-1]
        swing_low = df_primary['low'].rolling(20).min().iloc[-1]

        # Check if at key level (within 1%)
        if abs(current_price - swing_low) / current_price < 0.01:
            return 2, "🔑 At swing low (support)"
        elif abs(current_price - swing_high) / current_price < 0.01:
            return 2, "🔑 At swing high (resistance)"

        # Check higher timeframe levels if available
        if df_higher is not None and len(df_higher) >= 20:
            htf_swing_high = df_higher['high'].rolling(20).max().iloc[-1]
            htf_swing_low = df_higher['low'].rolling(20).min().iloc[-1]

            if abs(current_price - htf_swing_low) / current_price < 0.015:
                return 1, "🔑 Near HTF support"
            elif abs(current_price - htf_swing_high) / current_price < 0.015:
                return 1, "🔑 Near HTF resistance"

        return 0, ""

    def _check_volume_confirmation(self, df: pd.DataFrame) -> Tuple[int, str]:
        """
        Check volume confirmation

        Returns:
            score: 0-2
            reason: Description
        """
        if 'volume' not in df.columns or len(df) < 20:
            return 0, ""

        current_vol = df['volume'].iloc[-1]
        avg_vol = df['volume'].rolling(20).mean().iloc[-1]

        if current_vol > avg_vol * 2:
            return 2, "📈 Strong volume spike (2x)"
        elif current_vol > avg_vol * 1.5:
            return 1, "📊 Above average volume"

        return 0, ""

    def _check_momentum(self, df: pd.DataFrame, direction: str) -> Tuple[int, str]:
        """
        Check momentum alignment

        Returns:
            score: 0-2
            reason: Description
        """
        if 'rsi' not in df.columns or len(df) < 14:
            return 0, ""

        rsi = df['rsi'].iloc[-1]

        if direction == 'UP':
            if 40 < rsi < 60:
                return 2, "⚡ RSI neutral (good for entry)"
            elif 30 < rsi < 70:
                return 1, "⚡ RSI acceptable range"
        elif direction == 'DOWN':
            if 40 < rsi < 60:
                return 2, "⚡ RSI neutral (good for entry)"
            elif 30 < rsi < 70:
                return 1, "⚡ RSI acceptable range"

        return 0, ""

    def _get_session_score(self) -> Tuple[int, str]:
        """
        Score based on trading session (UTC+7 Vietnam time)

        Returns:
            score: 0-2
            reason: Description
        """
        import datetime

        # Get current UTC hour
        utc_hour = datetime.datetime.utcnow().hour
        # Convert to Vietnam time (UTC+7)
        vn_hour = (utc_hour + 7) % 24

        # London Open: 15:00-17:00 VN (08:00-10:00 UTC)
        if 8 <= utc_hour <= 10:
            return 2, "🌍 London session (high liquidity)"

        # NY Open: 20:00-22:00 VN (13:00-15:00 UTC)
        elif 13 <= utc_hour <= 15:
            return 2, "🗽 NY session (high liquidity)"

        # Asian Session: 08:00-12:00 VN (01:00-05:00 UTC)
        elif 1 <= utc_hour <= 5:
            return 1, "🌏 Asian session"

        # Overlap: 20:00-00:00 VN (13:00-17:00 UTC)
        elif 13 <= utc_hour <= 17:
            return 2, "🔥 London-NY overlap (best liquidity)"

        # Off-peak
        else:
            return 0, "💤 Off-peak hours"

    def _calculate_sl(self, df: pd.DataFrame, direction: str) -> float:
        """
        Calculate stop loss based on ATR

        Args:
            df: DataFrame with price data
            direction: 'UP' or 'DOWN'

        Returns:
            Stop loss price
        """
        current_price = df['close'].iloc[-1]

        # Use ATR if available
        if 'atr' in df.columns:
            atr = df['atr'].iloc[-1]
        else:
            # Calculate simple ATR
            high_low = df['high'] - df['low']
            atr = high_low.rolling(14).mean().iloc[-1]

        # Set SL at 1.5x ATR
        atr_multiplier = 1.5

        if direction == 'UP':
            sl_price = current_price - (atr * atr_multiplier)
        else:  # DOWN
            sl_price = current_price + (atr * atr_multiplier)

        return round(sl_price, 8)

    def _calculate_tp(self, entry_price: float, sl_price: float, direction: str) -> float:
        """
        Calculate take profit based on R:R ratio

        Args:
            entry_price: Entry price
            sl_price: Stop loss price
            direction: 'UP' or 'DOWN'

        Returns:
            Take profit price
        """
        risk = abs(entry_price - sl_price)

        # Use 2:1 R:R ratio
        reward = risk * 2

        if direction == 'UP':
            tp_price = entry_price + reward
        else:  # DOWN
            tp_price = entry_price - reward

        return round(tp_price, 8)
