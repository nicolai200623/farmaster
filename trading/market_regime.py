# ============================================
# 📊 MARKET REGIME DETECTION
# Phát hiện market regime để adjust strategy
# ============================================

import pandas as pd
import numpy as np
from utils.logger import logger

class MarketRegimeDetector:
    """
    Phát hiện market regime:
    - TRENDING_UP: Strong uptrend
    - TRENDING_DOWN: Strong downtrend
    - RANGING: Sideways/choppy
    - VOLATILE: High volatility
    """
    
    def __init__(self):
        self.regime_history = {}
        
    def detect_regime(self, df, lookback=50):
        """
        Detect current market regime
        
        Args:
            df: DataFrame với OHLCV + indicators
            lookback: Số candles để analyze
            
        Returns:
            dict: {
                'regime': str,
                'confidence': float (0-1),
                'metrics': dict
            }
        """
        if len(df) < lookback:
            return {
                'regime': 'UNKNOWN',
                'confidence': 0,
                'metrics': {}
            }
        
        recent_df = df.iloc[-lookback:]
        
        # Calculate metrics
        metrics = self._calculate_regime_metrics(recent_df)
        
        # Determine regime
        regime, confidence = self._classify_regime(metrics)
        
        return {
            'regime': regime,
            'confidence': confidence,
            'metrics': metrics
        }
    
    def _calculate_regime_metrics(self, df):
        """Calculate metrics for regime detection"""
        metrics = {}
        
        # 1. Trend strength (ADX-like)
        close = df['close'].values
        high = df['high'].values
        low = df['low'].values
        
        # Price change
        price_change_pct = ((close[-1] - close[0]) / close[0]) * 100
        metrics['price_change_pct'] = price_change_pct
        
        # 2. Volatility (ATR %)
        if 'atr' in df.columns:
            atr = df['atr'].iloc[-1]
            atr_pct = (atr / close[-1]) * 100
            metrics['atr_pct'] = atr_pct
        else:
            # Calculate simple volatility
            returns = np.diff(close) / close[:-1]
            volatility = np.std(returns) * 100
            metrics['atr_pct'] = volatility
        
        # 3. Trend consistency (% of candles in trend direction)
        if price_change_pct > 0:
            # Uptrend: count green candles
            trend_candles = np.sum(df['close'] > df['open'])
        else:
            # Downtrend: count red candles
            trend_candles = np.sum(df['close'] < df['open'])
        
        trend_consistency = trend_candles / len(df)
        metrics['trend_consistency'] = trend_consistency
        
        # 4. Range tightness (Bollinger Band width)
        if 'bb_width' in df.columns:
            bb_width = df['bb_width'].iloc[-1]
            metrics['bb_width'] = bb_width
        else:
            # Calculate simple range
            price_range = (high.max() - low.min()) / close[-1]
            metrics['bb_width'] = price_range
        
        # 5. Moving average alignment
        if len(df) >= 50:
            ema_20 = df['close'].ewm(span=20).mean().iloc[-1]
            ema_50 = df['close'].ewm(span=50).mean().iloc[-1]
            
            if ema_20 > ema_50:
                ma_alignment = 1  # Bullish
            elif ema_20 < ema_50:
                ma_alignment = -1  # Bearish
            else:
                ma_alignment = 0  # Neutral
            
            metrics['ma_alignment'] = ma_alignment
        else:
            metrics['ma_alignment'] = 0
        
        # 6. Higher highs / Lower lows
        recent_highs = df['high'].iloc[-10:].values
        recent_lows = df['low'].iloc[-10:].values
        
        higher_highs = np.sum(np.diff(recent_highs) > 0)
        lower_lows = np.sum(np.diff(recent_lows) < 0)
        
        metrics['higher_highs'] = higher_highs / 9  # Normalize
        metrics['lower_lows'] = lower_lows / 9
        
        return metrics
    
    def _classify_regime(self, metrics):
        """
        Classify regime based on metrics
        
        Returns:
            tuple: (regime, confidence)
        """
        price_change = metrics['price_change_pct']
        atr_pct = metrics['atr_pct']
        trend_consistency = metrics['trend_consistency']
        ma_alignment = metrics.get('ma_alignment', 0)
        
        # Thresholds
        STRONG_TREND_THRESHOLD = 3.0  # 3% price change
        WEAK_TREND_THRESHOLD = 1.0    # 1% price change
        HIGH_VOLATILITY_THRESHOLD = 3.0  # 3% ATR
        TREND_CONSISTENCY_THRESHOLD = 0.6  # 60% candles in trend
        
        # Detect VOLATILE regime
        if atr_pct > HIGH_VOLATILITY_THRESHOLD:
            confidence = min(atr_pct / HIGH_VOLATILITY_THRESHOLD, 1.0)
            return 'VOLATILE', confidence
        
        # Detect TRENDING regimes
        if abs(price_change) > STRONG_TREND_THRESHOLD and trend_consistency > TREND_CONSISTENCY_THRESHOLD:
            if price_change > 0 and ma_alignment >= 0:
                confidence = min(abs(price_change) / STRONG_TREND_THRESHOLD, 1.0)
                return 'TRENDING_UP', confidence
            elif price_change < 0 and ma_alignment <= 0:
                confidence = min(abs(price_change) / STRONG_TREND_THRESHOLD, 1.0)
                return 'TRENDING_DOWN', confidence
        
        # Detect weak trend
        if abs(price_change) > WEAK_TREND_THRESHOLD:
            if price_change > 0:
                confidence = abs(price_change) / STRONG_TREND_THRESHOLD
                return 'TRENDING_UP', confidence
            else:
                confidence = abs(price_change) / STRONG_TREND_THRESHOLD
                return 'TRENDING_DOWN', confidence
        
        # Default: RANGING
        confidence = 1.0 - (abs(price_change) / WEAK_TREND_THRESHOLD)
        return 'RANGING', max(confidence, 0.3)
    
    def get_regime_strategy_params(self, regime, confidence):
        """
        Get recommended strategy parameters based on regime
        
        Args:
            regime: Market regime
            confidence: Confidence level (0-1)
            
        Returns:
            dict: Recommended parameters
        """
        params = {
            'should_trade': True,
            'position_size_multiplier': 1.0,
            'tp_multiplier': 1.0,
            'sl_multiplier': 1.0,
            'min_confluence_score': 4,
            'use_trailing_stop': False
        }
        
        if regime == 'TRENDING_UP':
            # Favor LONG positions
            params['should_trade'] = True
            params['position_size_multiplier'] = 1.0 + (confidence * 0.5)  # Up to 1.5x
            params['tp_multiplier'] = 1.2  # Wider TP in trend
            params['use_trailing_stop'] = True
            params['min_confluence_score'] = 3  # Lower threshold in trend
            
        elif regime == 'TRENDING_DOWN':
            # Favor SHORT positions
            params['should_trade'] = True
            params['position_size_multiplier'] = 1.0 + (confidence * 0.5)
            params['tp_multiplier'] = 1.2
            params['use_trailing_stop'] = True
            params['min_confluence_score'] = 3
            
        elif regime == 'RANGING':
            # Mean reversion strategy
            params['should_trade'] = True
            params['position_size_multiplier'] = 0.8  # Smaller size
            params['tp_multiplier'] = 0.8  # Tighter TP
            params['sl_multiplier'] = 1.2  # Wider SL
            params['min_confluence_score'] = 5  # Higher threshold
            params['use_trailing_stop'] = False
            
        elif regime == 'VOLATILE':
            # Reduce trading in high volatility
            if confidence > 0.7:
                params['should_trade'] = False  # Too volatile
            else:
                params['should_trade'] = True
                params['position_size_multiplier'] = 0.5  # Much smaller size
                params['tp_multiplier'] = 1.5  # Wider TP
                params['sl_multiplier'] = 1.5  # Wider SL
                params['min_confluence_score'] = 6  # Much higher threshold
                params['use_trailing_stop'] = True
        
        return params
    
    def should_trade_in_regime(self, regime, signal, confidence):
        """
        Determine if should trade based on regime and signal
        
        Args:
            regime: Market regime
            signal: 'LONG' or 'SHORT'
            confidence: Regime confidence
            
        Returns:
            bool: True if should trade
        """
        # Don't trade in highly volatile markets
        if regime == 'VOLATILE' and confidence > 0.7:
            logger.info(f"⚠️ Skipping trade - market too volatile (confidence: {confidence:.2f})")
            return False
        
        # In trending markets, only trade with the trend
        if regime == 'TRENDING_UP' and signal == 'SHORT':
            if confidence > 0.6:
                logger.info(f"⚠️ Skipping SHORT in strong uptrend (confidence: {confidence:.2f})")
                return False
        
        if regime == 'TRENDING_DOWN' and signal == 'LONG':
            if confidence > 0.6:
                logger.info(f"⚠️ Skipping LONG in strong downtrend (confidence: {confidence:.2f})")
                return False
        
        return True
    
    def log_regime_info(self, symbol, regime_info):
        """Log regime information"""
        regime = regime_info['regime']
        confidence = regime_info['confidence']
        metrics = regime_info['metrics']
        
        logger.info(f"📊 {symbol} Market Regime: {regime} (confidence: {confidence:.2f})")
        logger.info(f"   Price change: {metrics.get('price_change_pct', 0):.2f}%")
        logger.info(f"   ATR: {metrics.get('atr_pct', 0):.2f}%")
        logger.info(f"   Trend consistency: {metrics.get('trend_consistency', 0):.2f}")

