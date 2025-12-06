# ============================================
# 🚀 ENTRY PIPELINE - MAIN ORCHESTRATOR
# 5-Stage Entry Validation System
# ============================================

import time
import numpy as np
import pandas as pd
from typing import Dict, Optional, List, Tuple, Any
from dataclasses import asdict

from trading.entry_pipeline.models import (
    SignalDirection,
    EntryDecision,
    StageResult,
    MLPrediction,
    PriceActionResult
)
from trading.entry_pipeline.ml_ensemble import MLEnsembleSignal
from trading.entry_pipeline.smart_entry import SmartEntryScoring
from trading.entry_pipeline.price_action import PriceActionValidator
from trading.entry_pipeline.htf_alignment import HTFTrendAligner
from trading.entry_pipeline.ai_analyzer import AIEntryAnalyzer
from utils.logger import logger


class EntryPipeline:
    """
    🚀 Entry Pipeline - 5-Stage Entry Validation System
    
    Stages:
    1. ML Ensemble Signal - XGBoost, LightGBM, CatBoost voting
    2. Smart Entry Scoring - 15-point scoring system
    3. Price Action Validation - 8-point candlestick/S-R analysis
    4. HTF Trend Alignment - 4H trend confirmation
    5. AI Quick Check - Claude API for borderline cases (optional)
    
    Features:
    - Early exit on stage failure
    - Configurable thresholds per stage
    - Enable/disable stages via config
    - Detailed logging and metrics
    """
    
    def __init__(
        self,
        config: Dict,
        models: Optional[Dict] = None,
        smart_entry_v2=None
    ):
        """
        Initialize Entry Pipeline
        
        Args:
            config: Configuration dictionary
            models: Pre-loaded ML models {name: model}
            smart_entry_v2: Optional SmartEntrySystemV2 instance
        """
        self.config = config
        
        # Stage enable flags
        self.use_ml = config.get('USE_ML_ENSEMBLE', True)
        self.use_smart_entry = config.get('USE_SMART_ENTRY', True)
        self.use_price_action = config.get('USE_PRICE_ACTION', True)
        self.use_htf = config.get('USE_HTF_ALIGNMENT', True)
        self.use_ai = config.get('USE_AI_CHECK', False)
        
        # Initialize stages
        self.ml_stage = MLEnsembleSignal(config, models) if self.use_ml else None
        self.smart_entry_stage = SmartEntryScoring(config, smart_entry_v2) if self.use_smart_entry else None
        self.price_action_stage = PriceActionValidator(config) if self.use_price_action else None
        self.htf_stage = HTFTrendAligner(config) if self.use_htf else None
        self.ai_stage = AIEntryAnalyzer(config) if self.use_ai else None
        
        # Metrics
        self.total_evaluations = 0
        self.passed_evaluations = 0
        self.stage_pass_counts = {
            'ml_ensemble': 0,
            'smart_entry': 0,
            'price_action': 0,
            'htf_alignment': 0,
            'ai_check': 0
        }
        
        logger.info("🚀 EntryPipeline initialized")
        logger.info(f"   Stages enabled: ML={self.use_ml}, SmartEntry={self.use_smart_entry}, "
                   f"PA={self.use_price_action}, HTF={self.use_htf}, AI={self.use_ai}")
    
    def set_models(self, models: Dict):
        """Set ML models after initialization"""
        if self.ml_stage:
            self.ml_stage.set_models(models)
    
    def evaluate(
        self,
        symbol: str,
        df: pd.DataFrame,
        X_features: Optional[np.ndarray] = None,
        df_higher: Optional[pd.DataFrame] = None,
        df_4h: Optional[pd.DataFrame] = None
    ) -> EntryDecision:
        """
        Evaluate entry through all pipeline stages
        
        Args:
            symbol: Trading symbol
            df: Primary timeframe DataFrame with OHLCV and indicators
            X_features: Pre-computed features for ML (optional)
            df_higher: Higher timeframe data (1H)
            df_4h: 4H timeframe data for HTF alignment
        
        Returns:
            EntryDecision with all stage results
        """
        start_time = time.time()
        self.total_evaluations += 1

        stages_results: List[StageResult] = []
        direction = SignalDirection.NEUTRAL
        ml_prediction = None
        entry_score = 0
        pa_score = 0

        # ========== DETECT DIRECTION FROM PRICE ACTION ==========
        # If ML disabled, detect direction from recent price action
        if not self.use_ml or X_features is None:
            direction = self._detect_direction_from_price(df)
            if direction == SignalDirection.NEUTRAL:
                return self._create_decision(
                    symbol, df, direction, stages_results,
                    start_time, "No clear direction from price action"
                )

        # ========== STAGE 1: ML ENSEMBLE ==========
        if self.use_ml and self.ml_stage and X_features is not None:
            ml_prediction = self.ml_stage.predict(X_features)
            passed, reason = self.ml_stage.validate(ml_prediction)
            
            stages_results.append(StageResult(
                stage_name="ml_ensemble",
                passed=passed,
                score=ml_prediction.confidence,
                max_score=1.0,
                reason=reason,
                details=asdict(ml_prediction)
            ))
            
            if not passed:
                return self._create_decision(
                    symbol, df, direction, stages_results, 
                    start_time, "ML signal rejected"
                )
            
            direction = ml_prediction.direction
            self.stage_pass_counts['ml_ensemble'] += 1
        
        # ========== STAGE 2: SMART ENTRY SCORING ==========
        if self.use_smart_entry and self.smart_entry_stage:
            entry_score, reasons, stage_result = self.smart_entry_stage.calculate_score(
                df, direction, df_higher, df_4h, symbol
            )
            stages_results.append(stage_result)
            
            if not stage_result.passed:
                return self._create_decision(
                    symbol, df, direction, stages_results,
                    start_time, f"Smart Entry score too low: {entry_score}/15"
                )

            self.stage_pass_counts['smart_entry'] += 1

        # ========== STAGE 3: PRICE ACTION VALIDATION ==========
        if self.use_price_action and self.price_action_stage:
            passed, pa_score, pa_result = self.price_action_stage.validate(
                df, direction, symbol
            )
            stage_result = self.price_action_stage.to_stage_result(pa_result)
            stages_results.append(stage_result)

            if not passed:
                return self._create_decision(
                    symbol, df, direction, stages_results,
                    start_time, f"Price Action score too low: {pa_score}/8"
                )

            self.stage_pass_counts['price_action'] += 1

        # ========== STAGE 4: HTF TREND ALIGNMENT ==========
        if self.use_htf and self.htf_stage and df_4h is not None:
            aligned, stage_result = self.htf_stage.check_alignment(df_4h, direction)
            stages_results.append(stage_result)

            if not aligned:
                return self._create_decision(
                    symbol, df, direction, stages_results,
                    start_time, f"HTF trend not aligned"
                )

            self.stage_pass_counts['htf_alignment'] += 1

        # ========== STAGE 5: AI QUICK CHECK (OPTIONAL) ==========
        if self.use_ai and self.ai_stage and self.ai_stage.should_analyze(pa_score, entry_score):
            ai_result = self.ai_stage.analyze(
                symbol, ml_prediction, entry_score, pa_score, df
            )
            stage_result = self.ai_stage.to_stage_result(ai_result)
            stages_results.append(stage_result)

            if not stage_result.passed:
                return self._create_decision(
                    symbol, df, direction, stages_results,
                    start_time, f"AI rejected: {ai_result.reason}"
                )

            self.stage_pass_counts['ai_check'] += 1

        # ========== ALL STAGES PASSED ==========
        self.passed_evaluations += 1

        return self._create_decision(
            symbol, df, direction, stages_results,
            start_time, "All stages passed",
            should_enter=True
        )

    def _create_decision(
        self,
        symbol: str,
        df: pd.DataFrame,
        direction: SignalDirection,
        stages: List[StageResult],
        start_time: float,
        reason: str,
        should_enter: bool = False
    ) -> EntryDecision:
        """Create EntryDecision object"""
        current_price = df['close'].iloc[-1] if len(df) > 0 else 0

        # Calculate entry/SL/TP if entering
        entry_price = None
        stop_loss = None
        take_profit = None

        if should_enter and len(df) > 0:
            entry_price = current_price

            # Calculate volatility-based TP/SL
            stop_loss, take_profit = self._calculate_volatility_levels(
                df=df,
                entry_price=entry_price,
                direction=direction,
                confidence=self._calculate_overall_confidence(stages)
            )

        processing_time = time.time() - start_time

        decision = EntryDecision(
            should_enter=should_enter,
            direction=direction,
            confidence=self._calculate_overall_confidence(stages),
            entry_price=entry_price,
            stop_loss=stop_loss,
            take_profit=take_profit,
            stages_passed=[s.stage_name for s in stages if s.passed],
            stages_failed=[s.stage_name for s in stages if not s.passed],
            stage_results=stages,
            reason=reason,
            timestamp=time.time(),
            processing_time_ms=processing_time * 1000
        )

        # Log decision
        self._log_decision(symbol, decision)

        return decision

    def _calculate_overall_confidence(self, stages: List[StageResult]) -> float:
        """Calculate overall confidence from stage scores"""
        if not stages:
            return 0.0

        total_score = sum(s.score for s in stages if s.score is not None)
        max_score = sum(s.max_score for s in stages if s.max_score is not None)

        return total_score / max_score if max_score > 0 else 0.0

    def _log_decision(self, symbol: str, decision: EntryDecision):
        """Log the entry decision"""
        if decision.should_enter:
            logger.info(f"✅ {symbol} ENTRY APPROVED: {decision.direction.value}")
            logger.info(f"   Confidence: {decision.confidence:.2%}")
            if decision.entry_price:
                logger.info(f"   Entry: {decision.entry_price:.4f}")
            if decision.stop_loss and decision.take_profit:
                logger.info(f"   SL: {decision.stop_loss:.4f}, TP: {decision.take_profit:.4f}")
            logger.info(f"   Stages passed: {decision.stages_passed}")
        else:
            logger.debug(f"❌ {symbol} ENTRY REJECTED: {decision.reason}")
            logger.debug(f"   Failed stages: {decision.stages_failed}")

    def get_metrics(self) -> Dict[str, Any]:
        """Get pipeline metrics"""
        pass_rate = self.passed_evaluations / self.total_evaluations if self.total_evaluations > 0 else 0

        return {
            'total_evaluations': self.total_evaluations,
            'passed_evaluations': self.passed_evaluations,
            'pass_rate': pass_rate,
            'stage_pass_counts': self.stage_pass_counts,
            'stage_pass_rates': {
                k: v / self.total_evaluations if self.total_evaluations > 0 else 0
                for k, v in self.stage_pass_counts.items()
            }
        }

    def reset_metrics(self):
        """Reset pipeline metrics"""
        self.total_evaluations = 0
        self.passed_evaluations = 0
        self.stage_pass_counts = {k: 0 for k in self.stage_pass_counts}

    def _detect_direction_from_price(self, df: pd.DataFrame) -> SignalDirection:
        """
        Detect trading direction from price action when ML is disabled

        Uses:
        - Recent trend (last 10 candles)
        - RSI levels
        - Price position relative to moving averages
        """
        if len(df) < 20:
            return SignalDirection.NEUTRAL

        try:
            # Get recent data
            recent = df.tail(10)
            current_close = df['close'].iloc[-1]

            # 1. Trend direction (price change over last 10 candles)
            price_change = (current_close - df['close'].iloc[-10]) / df['close'].iloc[-10]

            # 2. RSI signal
            rsi_signal = 0
            if 'rsi' in df.columns:
                rsi = df['rsi'].iloc[-1]
                if rsi < 30:
                    rsi_signal = 1  # Oversold -> bullish
                elif rsi > 70:
                    rsi_signal = -1  # Overbought -> bearish

            # 3. MA crossover (if available)
            ma_signal = 0
            if 'sma_20' in df.columns and 'sma_50' in df.columns:
                sma20 = df['sma_20'].iloc[-1]
                sma50 = df['sma_50'].iloc[-1]
                if sma20 > sma50:
                    ma_signal = 1
                elif sma20 < sma50:
                    ma_signal = -1

            # 4. Recent candle pattern
            candle_signal = 0
            last_candle = df.iloc[-1]
            body = last_candle['close'] - last_candle['open']
            if body > 0:  # Bullish candle
                candle_signal = 1
            elif body < 0:  # Bearish candle
                candle_signal = -1

            # Combine signals
            total_signal = rsi_signal + ma_signal + candle_signal

            # Strong trend override
            if abs(price_change) > 0.02:  # 2% move
                if price_change > 0:
                    total_signal += 2
                else:
                    total_signal -= 2

            # Determine direction
            if total_signal >= 2:
                return SignalDirection.LONG
            elif total_signal <= -2:
                return SignalDirection.SHORT
            else:
                return SignalDirection.NEUTRAL

        except Exception as e:
            logger.error(f"Direction detection error: {e}")
            return SignalDirection.NEUTRAL

    def _calculate_volatility_levels(
        self,
        df: pd.DataFrame,
        entry_price: float,
        direction: SignalDirection,
        confidence: float
    ) -> tuple:
        """
        Calculate volatility-based TP/SL levels

        Adapts TP/SL based on:
        1. ATR (Average True Range) for base volatility
        2. Recent volatility regime (high/low vol)
        3. Confidence level (higher confidence = wider TP)
        4. Market structure (support/resistance proximity)

        Returns:
            tuple: (stop_loss, take_profit)
        """
        # 1. Get ATR
        if 'atr' in df.columns:
            atr = df['atr'].iloc[-1]
        else:
            # Calculate simple ATR if not available
            high_low = df['high'] - df['low']
            atr = high_low.rolling(14).mean().iloc[-1]

        # 2. Calculate volatility multiplier based on recent vol regime
        atr_pct = atr / entry_price  # ATR as % of price

        # Classify volatility regime
        if atr_pct > 0.025:  # High vol (>2.5% ATR)
            vol_regime = 'high'
            sl_mult = 2.0  # Wider SL in high vol
            tp_mult = 3.5  # Wider TP target
        elif atr_pct > 0.015:  # Normal vol (1.5-2.5%)
            vol_regime = 'normal'
            sl_mult = 1.5
            tp_mult = 3.0
        else:  # Low vol (<1.5%)
            vol_regime = 'low'
            sl_mult = 1.2  # Tighter in low vol
            tp_mult = 2.5

        # 3. Adjust based on confidence
        # Higher confidence = slightly wider TP (let winners run)
        if confidence > 0.7:
            tp_mult *= 1.2
        elif confidence < 0.5:
            tp_mult *= 0.9

        # 4. Calculate SL/TP prices
        sl_distance = atr * sl_mult
        tp_distance = atr * tp_mult

        if direction == SignalDirection.LONG:
            stop_loss = entry_price - sl_distance
            take_profit = entry_price + tp_distance
        elif direction == SignalDirection.SHORT:
            stop_loss = entry_price + sl_distance
            take_profit = entry_price - tp_distance
        else:
            stop_loss = None
            take_profit = None

        # 5. Ensure minimum R:R ratio of 1.5
        if stop_loss and take_profit:
            risk = abs(entry_price - stop_loss)
            reward = abs(take_profit - entry_price)
            rr_ratio = reward / risk if risk > 0 else 0

            if rr_ratio < 1.5:
                # Extend TP to achieve min R:R
                if direction == SignalDirection.LONG:
                    take_profit = entry_price + (risk * 1.5)
                else:
                    take_profit = entry_price - (risk * 1.5)

        return stop_loss, take_profit
