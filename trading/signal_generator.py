# ============================================
# 📡 SIGNAL GENERATOR
# Kết hợp LSTM + RSI + OB Imbalance + Advanced Entry
# + NEW: Entry Pipeline 5-Stage Validation
# ============================================

import pandas as pd
import numpy as np
from ml.features import FeatureEngine
from ml.lstm_model import LSTMTrainer
from ml.ensemble import EnsemblePredictor
from config import Config
from utils.logger import logger
from trading.advanced_entry import AdvancedEntrySystem, SmartEntrySystemV2
from trading.signal_cooldown import SignalCooldownTracker
from trading.entry_quality import EntryQualityChecker

# NEW: Entry Pipeline imports
try:
    from trading.entry_pipeline import EntryPipeline, SignalDirection
    ENTRY_PIPELINE_AVAILABLE = True
except ImportError:
    ENTRY_PIPELINE_AVAILABLE = False
    logger.warning("⚠️ Entry Pipeline not available")

class SignalGenerator:
    """
    Tạo trading signals từ nhiều nguồn:
    1. ML prediction (LSTM or Ensemble)
    2. RSI oversold/overbought
    3. Order Book imbalance
    4. Advanced Entry System (Market Structure + Price Patterns + SMC + Volume)
    """

    def __init__(self, predictor):
        """
        Initialize signal generator

        Args:
            predictor: LSTM trainer or Ensemble predictor
        """
        self.predictor = predictor  # Can be LSTMTrainer or EnsemblePredictor
        self.feature_engine = FeatureEngine()

        # Check if using ensemble
        self.use_ensemble = isinstance(predictor, EnsemblePredictor)

        if self.use_ensemble:
            logger.info(f"🎭 Using Ensemble predictor: {Config.ENSEMBLE_MODELS}")
            logger.info(f"   Weights: {Config.ENSEMBLE_WEIGHTS}")
        else:
            logger.info("🧠 Using LSTM predictor")

        # Initialize Advanced Entry System if enabled
        if Config.USE_SMART_ENTRY_V2:
            self.smart_entry_v2 = SmartEntrySystemV2(
                min_score=Config.MIN_ENTRY_SCORE,
                min_rr_ratio=Config.MIN_RR_RATIO
            )
            logger.info(f"🎯 SmartEntrySystemV2 enabled (min score: {Config.MIN_ENTRY_SCORE}, min R:R: {Config.MIN_RR_RATIO}:1)")
            self.advanced_entry = None
        elif Config.USE_ADVANCED_ENTRY:
            self.advanced_entry = AdvancedEntrySystem(
                min_confluence_score=Config.MIN_CONFLUENCE_SCORE
            )
            self.smart_entry_v2 = None
            logger.info(f"🎯 Advanced Entry System enabled (min score: {Config.MIN_CONFLUENCE_SCORE})")
        else:
            self.advanced_entry = None
            self.smart_entry_v2 = None

        # Initialize Signal Cooldown Tracker
        if Config.USE_SIGNAL_COOLDOWN:
            post_trade_mins = Config.POST_TRADE_COOLDOWN_MINUTES if Config.USE_POST_TRADE_COOLDOWN else 0
            self.cooldown_tracker = SignalCooldownTracker(
                cooldown_minutes=Config.SIGNAL_COOLDOWN_MINUTES,
                post_trade_cooldown_minutes=post_trade_mins
            )
            logger.info(f"🚫 Signal Cooldown enabled: {Config.SIGNAL_COOLDOWN_MINUTES}m signal, {post_trade_mins}m post-trade")
        else:
            self.cooldown_tracker = None
            logger.info("📡 Using legacy signal system")

        # Initialize Entry Quality Checker
        self.entry_quality_checker = EntryQualityChecker()
        logger.info("🎯 Entry Quality Checker enabled")

        # NEW: Initialize Entry Pipeline if enabled
        self.entry_pipeline = None
        if getattr(Config, 'USE_ENTRY_PIPELINE', False) and ENTRY_PIPELINE_AVAILABLE:
            try:
                pipeline_config = self._build_pipeline_config()
                self.entry_pipeline = EntryPipeline(
                    config=pipeline_config,
                    models=self._get_ml_models() if self.use_ensemble else None,
                    smart_entry_v2=self.smart_entry_v2
                )
                logger.info("🚀 Entry Pipeline enabled (5-stage validation)")
            except Exception as e:
                logger.error(f"Failed to initialize Entry Pipeline: {e}")
                self.entry_pipeline = None

    def _build_pipeline_config(self) -> dict:
        """Build config dict for Entry Pipeline"""
        return {
            # Stage 1: ML Ensemble
            'USE_ML_ENSEMBLE': getattr(Config, 'USE_ML_ENSEMBLE', True),
            'ML_CONFIDENCE_THRESHOLD': getattr(Config, 'ML_CONFIDENCE_THRESHOLD', 0.62),
            'ML_NEUTRAL_ZONE': getattr(Config, 'ML_NEUTRAL_ZONE', 0.08),

            # Stage 2: Smart Entry
            'USE_SMART_ENTRY': getattr(Config, 'USE_SMART_ENTRY', True),
            'MIN_ENTRY_SCORE': getattr(Config, 'MIN_ENTRY_SCORE', 7),
            'MIN_RR_RATIO': getattr(Config, 'MIN_RR_RATIO', 2.0),

            # Stage 3: Price Action
            'USE_PRICE_ACTION': getattr(Config, 'USE_PRICE_ACTION', True),
            'MIN_PRICE_ACTION_SCORE': getattr(Config, 'MIN_PRICE_ACTION_SCORE', 5),
            'SR_LOOKBACK_CANDLES': getattr(Config, 'SR_LOOKBACK_CANDLES', 50),
            'SR_PROXIMITY_PCT': getattr(Config, 'SR_PROXIMITY_PCT', 0.5),
            'VOLUME_CONFIRMATION_RATIO': getattr(Config, 'VOLUME_CONFIRMATION_RATIO', 1.5),

            # Stage 4: HTF Alignment
            'USE_HTF_ALIGNMENT': getattr(Config, 'USE_HTF_ALIGNMENT', True),
            'HTF_TIMEFRAME': getattr(Config, 'HTF_TIMEFRAME', '4h'),
            'REQUIRE_HTF_ALIGNMENT': getattr(Config, 'REQUIRE_HTF_ALIGNMENT', True),
            'HTF_STRICT_MODE': getattr(Config, 'HTF_STRICT_MODE', False),

            # Stage 5: AI Check
            'USE_AI_CHECK': getattr(Config, 'USE_AI_CHECK', False),
            'AI_API_KEY': getattr(Config, 'AI_API_KEY', ''),
            'AI_MODEL': getattr(Config, 'AI_MODEL', 'claude-3-haiku-20240307'),
            'AI_TIMEOUT_SECONDS': getattr(Config, 'AI_TIMEOUT_SECONDS', 5),
            'USE_AI_FOR_BORDERLINE': getattr(Config, 'USE_AI_FOR_BORDERLINE', True),
        }

    def _get_ml_models(self) -> dict:
        """Get ML models from ensemble predictor

        Returns dict of trainer objects that have .predict() method
        (XGBoostTrainer, LightGBMTrainer, CatBoostTrainer)
        """
        if not self.use_ensemble or not hasattr(self.predictor, 'models'):
            return {}

        # self.predictor.models is a dict like:
        # {'xgboost': XGBoostTrainer, 'lightgbm': LightGBMTrainer, 'catboost': CatBoostTrainer}
        # Each trainer has a .predict() method
        models = {}
        for name, trainer in self.predictor.models.items():
            # Check if trainer is loaded and has a model
            if trainer is not None and hasattr(trainer, 'model') and trainer.model is not None:
                models[name] = trainer
                logger.debug(f"   ML model '{name}' added to Entry Pipeline")

        if models:
            logger.info(f"🎭 Entry Pipeline received {len(models)} ML models: {list(models.keys())}")
        else:
            logger.warning("⚠️ No ML models available for Entry Pipeline")

        return models
    
    def generate_signal(self, client, symbol):
        """
        Tạo signal cho 1 symbol

        Args:
            client: AsterDEXClient instance
            symbol: Trading pair

        Returns:
            tuple: (signal, confluence_score, reasons) if USE_ADVANCED_ENTRY
                   OR str: 'LONG', 'SHORT', 'HOLD' (legacy mode)
        """
        try:
            # Determine interval
            interval = Config.PRIMARY_TIMEFRAME if Config.USE_ADVANCED_ENTRY else '15m'

            # 1. Get klines data (more data for advanced analysis)
            limit = 200 if Config.USE_ADVANCED_ENTRY else 100
            klines = client.get_klines(symbol, interval=interval, limit=limit)
            
            if not klines or len(klines) < 60:
                logger.warning(f"Insufficient klines data for {symbol}")
                if Config.USE_ADVANCED_ENTRY:
                    return 'HOLD', 0, []
                else:
                    return 'HOLD'
            
            # Parse klines
            df = self._parse_klines(klines)
            
            # 2. Calculate indicators
            df = self.feature_engine.calculate_indicators(df)
            
            # 3. Get Order Book (with error handling)
            orderbook = client.get_orderbook(symbol, limit=10)

            # If orderbook is empty (symbol unavailable), use neutral imbalance
            if not orderbook.get('bids') or not orderbook.get('asks'):
                logger.warning(f"Empty orderbook for {symbol}, using neutral imbalance")
                ob_imbalance = 1.0  # Neutral
            else:
                ob_imbalance = self.feature_engine.calculate_ob_imbalance(
                    orderbook['bids'],
                    orderbook['asks']
                )
            
            # Update OB imbalance
            df['ob_imbalance'] = ob_imbalance
            
            # 4. Prepare features for ML model
            feature_df = self.feature_engine.prepare_features(df)

            # Normalize
            normalized = self.predictor.scaler.transform(feature_df.values)

            # Get last 60 candles
            if len(normalized) < Config.SEQUENCE_LENGTH:
                logger.warning(f"Not enough data for ML model: {len(normalized)}")
                if Config.USE_ADVANCED_ENTRY:
                    return 'HOLD', 0, []
                else:
                    return 'HOLD'

            ml_input = normalized[-Config.SEQUENCE_LENGTH:]

            # 5. ML Prediction (LSTM or Ensemble)
            if self.use_ensemble:
                ml_prob, pred_details = self.predictor.predict_with_details(ml_input)
                # Log individual model predictions (only in debug mode)
                # Note: logger is custom Logger class, use logging module for level check
                import logging
                if logging.getLogger().getEffectiveLevel() <= logging.INFO:
                    logger.debug(f"   ML predictions:")
                    for model_name, pred in pred_details.items():
                        if model_name not in ['ensemble', 'weights']:
                            logger.debug(f"      {model_name}: {pred:.3f}")
            else:
                ml_prob = self.predictor.predict(ml_input)[0]

            # For backward compatibility, keep variable name as lstm_prob
            lstm_prob = ml_prob
            
            # 6. Get current indicators
            current_rsi = df['rsi'].iloc[-1]
            
            # 7. Calculate signal scores
            score_long = 0
            score_short = 0
            
            # LSTM signal
            if lstm_prob > Config.LSTM_THRESHOLD:
                score_long += 1
            elif lstm_prob < (1 - Config.LSTM_THRESHOLD):
                score_short += 1
            
            # RSI signal
            if current_rsi < Config.RSI_OVERSOLD:
                score_long += 1
            elif current_rsi > Config.RSI_OVERBOUGHT:
                score_short += 1
            
            # OB Imbalance signal
            if ob_imbalance > Config.OB_IMBALANCE_LONG:
                score_long += 1
            elif ob_imbalance < Config.OB_IMBALANCE_SHORT:
                score_short += 1
            
            # 8. Decision
            signal = 'HOLD'
            confluence_score = 0
            reasons = []

            # ============================================
            # NEW: Use Entry Pipeline if enabled (PRIORITY)
            # ============================================
            if self.entry_pipeline is not None:
                return self._generate_signal_with_pipeline(
                    client=client,
                    symbol=symbol,
                    df=df,
                    ml_input=ml_input,
                    lstm_prob=lstm_prob,
                    current_rsi=current_rsi
                )

            # Use SmartEntrySystemV2 if enabled (priority over AdvancedEntry)
            if Config.USE_SMART_ENTRY_V2 and self.smart_entry_v2:
                # Get multi-timeframe data for SmartEntryV2
                df_1h = None
                df_4h = None

                if Config.USE_MULTI_TIMEFRAME:
                    try:
                        # Get 1H data
                        klines_1h = client.get_klines(symbol, interval='1h', limit=100)
                        df_1h = self._parse_klines(klines_1h)
                        df_1h = self.feature_engine.calculate_indicators(df_1h)

                        # Get 4H data
                        klines_4h = client.get_klines(symbol, interval='4h', limit=100)
                        df_4h = self._parse_klines(klines_4h)
                        df_4h = self.feature_engine.calculate_indicators(df_4h)
                    except Exception as e:
                        logger.warning(f"Could not get HTF data: {e}")

                # Evaluate with SmartEntryV2
                signal, score, entry_price, sl_price, tp_price, reasons = self.smart_entry_v2.evaluate_entry(
                    symbol=symbol,
                    df_primary=df,  # 15m
                    df_higher=df_1h,  # 1h
                    df_4h=df_4h  # 4h
                )

                confluence_score = score

                # Apply additional ML filter
                if signal != 'HOLD' and Config.USE_ML_CONVICTION_FILTER:
                    ml_distance = abs(lstm_prob - 0.5)
                    if ml_distance < Config.MIN_ML_CONVICTION:
                        logger.info(f"   🚫 ML Conviction too low: {lstm_prob:.3f}")
                        signal = 'HOLD'

                # Signal Cooldown
                if signal != 'HOLD' and self.cooldown_tracker is not None:
                    can_signal, cooldown_reason = self.cooldown_tracker.can_signal(symbol, signal)
                    if not can_signal:
                        logger.info(f"   🚫 {cooldown_reason}")
                        signal = 'HOLD'

                # Post-Trade Cooldown (NEW!) - Check if we just closed a position
                if signal != 'HOLD' and self.cooldown_tracker is not None and Config.USE_POST_TRADE_COOLDOWN:
                    current_price = df['close'].iloc[-1]
                    can_enter, post_trade_reason = self.cooldown_tracker.can_enter_after_close(
                        symbol=symbol,
                        current_price=current_price,
                        require_pullback=Config.POST_TRADE_REQUIRE_PULLBACK,
                        pullback_pct=Config.PULLBACK_PCT
                    )
                    if not can_enter:
                        logger.info(f"   ⏳ {post_trade_reason}")
                        signal = 'HOLD'

                # Entry Quality Check (NEW!) - Check if entry is high quality after recent close
                if signal != 'HOLD' and getattr(Config, 'USE_ENTRY_QUALITY_CHECK', True):
                    current_price = df['close'].iloc[-1]
                    is_quality, quality_reason, factors = self.entry_quality_checker.check_entry_quality(
                        symbol=symbol,
                        df=df,
                        proposed_signal=signal,
                        current_price=current_price
                    )
                    if not is_quality:
                        logger.info(f"   🎯 {quality_reason}")
                        signal = 'HOLD'
                    else:
                        logger.info(f"   ✅ {quality_reason}")

                # Log result
                if signal != 'HOLD':
                    logger.info(f"🎯 {symbol} SmartEntryV2 Signal: {signal}")
                    logger.info(f"   📊 Score: {score}/15")
                    logger.info(f"   💰 Entry: ${entry_price:.2f} | SL: ${sl_price:.2f} | TP: ${tp_price:.2f}")
                    logger.info(f"   📈 ML: {lstm_prob:.3f} | RSI: {current_rsi:.1f}")
                    logger.info(f"   📝 Reasons:")
                    for i, reason in enumerate(reasons[:5], 1):
                        logger.info(f"      {i}. {reason}")
                else:
                    logger.info(f"📡 {symbol} Signal: HOLD (score: {score}/15)")

                return signal, confluence_score, reasons

            # Use Advanced Entry System if enabled
            elif Config.USE_ADVANCED_ENTRY and self.advanced_entry:
                # Get higher timeframe data for confirmation if enabled
                if Config.USE_MULTI_TIMEFRAME:
                    try:
                        klines_htf = client.get_klines(symbol, interval=Config.HIGHER_TIMEFRAME, limit=100)
                        df_htf = self._parse_klines(klines_htf)
                        df_htf = self.feature_engine.calculate_indicators(df_htf)

                        # Check HTF trend
                        htf_trend = self._get_trend(df_htf)
                    except Exception as e:
                        logger.warning(f"Could not get HTF data: {e}")
                        htf_trend = 'NEUTRAL'
                else:
                    htf_trend = 'NEUTRAL'

                # Get advanced signal
                signal, confluence_score, reasons = self.advanced_entry.should_enter_trade(df, symbol)

                # ============================================
                # APPLY ANTI-WHIPSAW FILTERS
                # ============================================
                if signal != 'HOLD':
                    # Filter 1: ML Conviction Filter
                    if Config.USE_ML_CONVICTION_FILTER:
                        ml_distance = abs(lstm_prob - 0.5)
                        if ml_distance < Config.MIN_ML_CONVICTION:
                            logger.info(f"   🚫 ML Conviction too low: {lstm_prob:.3f} (distance from 0.5: {ml_distance:.3f} < {Config.MIN_ML_CONVICTION})")
                            signal = 'HOLD'

                    # Filter 2: HTF Trend Alignment (Strict mode)
                    if signal != 'HOLD' and Config.REQUIRE_HTF_TREND_ALIGNMENT and Config.USE_MULTI_TIMEFRAME:
                        if signal == 'LONG' and htf_trend != 'UP':
                            logger.info(f"   🚫 HTF trend not bullish ({htf_trend}), filtering LONG signal")
                            signal = 'HOLD'
                        elif signal == 'SHORT' and htf_trend != 'DOWN':
                            logger.info(f"   🚫 HTF trend not bearish ({htf_trend}), filtering SHORT signal")
                            signal = 'HOLD'
                    # Filter 2b: HTF Trend Filter (Relaxed mode - original)
                    elif signal != 'HOLD' and not Config.REQUIRE_HTF_TREND_ALIGNMENT and Config.USE_MULTI_TIMEFRAME:
                        if signal == 'LONG' and htf_trend == 'DOWN':
                            logger.info(f"   ⚠️ HTF trend is bearish, filtering LONG signal")
                            signal = 'HOLD'
                        elif signal == 'SHORT' and htf_trend == 'UP':
                            logger.info(f"   ⚠️ HTF trend is bullish, filtering SHORT signal")
                            signal = 'HOLD'

                    # Filter 3: Signal Cooldown
                    if signal != 'HOLD' and self.cooldown_tracker is not None:
                        can_signal, cooldown_reason = self.cooldown_tracker.can_signal(symbol, signal)
                        if not can_signal:
                            logger.info(f"   🚫 {cooldown_reason}")
                            signal = 'HOLD'

                    # Filter 4: Post-Trade Cooldown (NEW!)
                    if signal != 'HOLD' and self.cooldown_tracker is not None and Config.USE_POST_TRADE_COOLDOWN:
                        current_price = df['close'].iloc[-1]
                        can_enter, post_trade_reason = self.cooldown_tracker.can_enter_after_close(
                            symbol=symbol,
                            current_price=current_price,
                            require_pullback=Config.POST_TRADE_REQUIRE_PULLBACK,
                            pullback_pct=Config.PULLBACK_PCT
                        )
                        if not can_enter:
                            logger.info(f"   ⏳ {post_trade_reason}")
                            signal = 'HOLD'

                    # Filter 5: Entry Quality Check (NEW!)
                    if signal != 'HOLD' and getattr(Config, 'USE_ENTRY_QUALITY_CHECK', True):
                        current_price = df['close'].iloc[-1]
                        is_quality, quality_reason, factors = self.entry_quality_checker.check_entry_quality(
                            symbol=symbol,
                            df=df,
                            proposed_signal=signal,
                            current_price=current_price
                        )
                        if not is_quality:
                            logger.info(f"   🎯 {quality_reason}")
                            signal = 'HOLD'
                        else:
                            logger.info(f"   ✅ {quality_reason}")

                # Log advanced signal
                if signal != 'HOLD':
                    logger.info(f"🎯 {symbol} Advanced Signal: {signal}")
                    logger.info(f"   📊 Confluence Score: {confluence_score}/{Config.MIN_CONFLUENCE_SCORE}")
                    logger.info(f"   📝 Top Reasons:")
                    for i, reason in enumerate(reasons[:3], 1):
                        logger.info(f"      {i}. {reason}")
                    logger.info(f"   📈 Legacy Signals - LSTM: {lstm_prob:.3f} | RSI: {current_rsi:.1f} | OB: {ob_imbalance:.2f}")
                else:
                    logger.info(f"📡 {symbol} Signal: HOLD (score: {confluence_score}/{Config.MIN_CONFLUENCE_SCORE})")
                    if reasons:
                        logger.info(f"   Partial signals: {', '.join(reasons[:2])}")

                return signal, confluence_score, reasons

            else:
                # Legacy signal system
                if score_long >= Config.MIN_SIGNAL_SCORE:
                    signal = 'LONG'
                elif score_short >= Config.MIN_SIGNAL_SCORE:
                    signal = 'SHORT'

                # Log signal details
                logger.info(f"📡 {symbol} Signal: {signal}")
                logger.info(f"   LSTM: {lstm_prob:.3f} | RSI: {current_rsi:.1f} | OB: {ob_imbalance:.2f}")
                logger.info(f"   Score LONG: {score_long} | SHORT: {score_short}")

                return signal
            
        except Exception as e:
            logger.error(f"Signal generation error for {symbol}: {e}")
            import traceback
            logger.error(traceback.format_exc())
            if Config.USE_ADVANCED_ENTRY:
                return 'HOLD', 0, []
            else:
                return 'HOLD'

    def _get_trend(self, df):
        """Get trend from higher timeframe"""
        if len(df) < 50:
            return 'NEUTRAL'

        ema_20 = df['close'].ewm(span=20, adjust=False).mean().iloc[-1]
        ema_50 = df['close'].ewm(span=50, adjust=False).mean().iloc[-1]
        current_price = df['close'].iloc[-1]

        if current_price > ema_20 > ema_50:
            return 'UP'
        elif current_price < ema_20 < ema_50:
            return 'DOWN'
        else:
            return 'NEUTRAL'
    
    def _parse_klines(self, klines):
        """Parse klines thành DataFrame"""
        df = pd.DataFrame(klines, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_volume', 'trades', 'taker_buy_base',
            'taker_buy_quote', 'ignore'
        ])
        
        # Convert to numeric
        for col in ['open', 'high', 'low', 'close', 'volume']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        
        return df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
    
    def should_close_position(self, position, tp_pct=None, sl_pct=None, position_age_hours=None):
        """
        Kiểm tra có nên đóng position không

        Args:
            position: Dict từ get_position()
            tp_pct: Take profit %
            sl_pct: Stop loss %
            position_age_hours: How long position has been open (hours)

        Returns:
            tuple: (should_close: bool, reason: str)
        """
        if not position:
            return False, ""

        tp_pct = tp_pct or Config.TP_PCT
        sl_pct = sl_pct or Config.SL_PCT

        pnl_pct = position['pnl_pct']

        # Take Profit
        if pnl_pct >= tp_pct:
            return True, f"TP ({pnl_pct*100:.2f}%)"

        # Stop Loss (only if SL_PCT > 0)
        if sl_pct is not None and sl_pct > 0 and pnl_pct <= -sl_pct:
            return True, f"SL ({pnl_pct*100:.2f}%)"

        # Position Timeout (24+ hours without hitting TP)
        if position_age_hours is not None and position_age_hours >= Config.POSITION_TIMEOUT_HOURS:
            return True, f"TIMEOUT ({position_age_hours:.1f}h, PnL: {pnl_pct*100:.2f}%)"

        return False, ""

    def _generate_signal_with_pipeline(
        self,
        client,
        symbol: str,
        df: pd.DataFrame,
        ml_input: np.ndarray,
        lstm_prob: float,
        current_rsi: float
    ):
        """
        Generate signal using Entry Pipeline (5-stage validation)

        Args:
            client: AsterDEXClient instance
            symbol: Trading symbol
            df: Primary timeframe DataFrame
            ml_input: Normalized ML input features
            lstm_prob: ML probability (for logging)
            current_rsi: Current RSI value

        Returns:
            tuple: (signal, confluence_score, reasons)
        """
        try:
            # Get multi-timeframe data
            df_1h = None
            df_4h = None

            if Config.USE_MULTI_TIMEFRAME:
                try:
                    # Get 1H data
                    klines_1h = client.get_klines(symbol, interval='1h', limit=100)
                    df_1h = self._parse_klines(klines_1h)
                    df_1h = self.feature_engine.calculate_indicators(df_1h)

                    # Get 4H data
                    klines_4h = client.get_klines(symbol, interval='4h', limit=100)
                    df_4h = self._parse_klines(klines_4h)
                    df_4h = self.feature_engine.calculate_indicators(df_4h)
                except Exception as e:
                    logger.warning(f"Could not get HTF data: {e}")

            # Run Entry Pipeline
            decision = self.entry_pipeline.evaluate(
                symbol=symbol,
                df=df,
                X_features=ml_input,
                df_higher=df_1h,
                df_4h=df_4h
            )

            # Convert decision to signal format
            if decision.should_enter:
                signal = decision.direction.value  # 'LONG' or 'SHORT'
                confluence_score = int(decision.confidence * 15)  # Scale to 15
                reasons = [f"Pipeline: {s}" for s in decision.stages_passed]

                # Apply cooldown checks
                if self.cooldown_tracker is not None:
                    can_signal, cooldown_reason = self.cooldown_tracker.can_signal(symbol, signal)
                    if not can_signal:
                        logger.info(f"   🚫 {cooldown_reason}")
                        return 'HOLD', 0, []

                # Log success
                logger.info(f"🚀 {symbol} Pipeline APPROVED: {signal}")
                logger.info(f"   📊 Confidence: {decision.confidence:.2%}")
                logger.info(f"   💰 Entry: ${decision.entry_price:.4f}" if decision.entry_price else "")
                logger.info(f"   📈 ML: {lstm_prob:.3f} | RSI: {current_rsi:.1f}")
                logger.info(f"   ✅ Stages: {', '.join(decision.stages_passed)}")

                return signal, confluence_score, reasons
            else:
                # Log rejection
                logger.debug(f"📡 {symbol} Pipeline REJECTED: {decision.reason}")
                if decision.stages_failed:
                    logger.debug(f"   ❌ Failed: {', '.join(decision.stages_failed)}")

                return 'HOLD', 0, []

        except Exception as e:
            logger.error(f"Entry Pipeline error for {symbol}: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            return 'HOLD', 0, []

