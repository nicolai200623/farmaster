# ============================================
# 📡 SIGNAL GENERATOR
# Kết hợp LSTM + RSI + OB Imbalance + Advanced Entry
# ============================================

import pandas as pd
import numpy as np
from ml.features import FeatureEngine
from ml.lstm_model import LSTMTrainer
from ml.ensemble import EnsemblePredictor
from config import Config
from utils.logger import logger
from trading.advanced_entry import AdvancedEntrySystem

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
        if Config.USE_ADVANCED_ENTRY:
            self.advanced_entry = AdvancedEntrySystem(
                min_confluence_score=Config.MIN_CONFLUENCE_SCORE
            )
            logger.info(f"🎯 Advanced Entry System enabled (min score: {Config.MIN_CONFLUENCE_SCORE})")
        else:
            self.advanced_entry = None
            logger.info("📡 Using legacy signal system")
    
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
                # Log individual model predictions
                if logger.level <= 20:  # INFO level
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

            # Use Advanced Entry System if enabled
            if Config.USE_ADVANCED_ENTRY and self.advanced_entry:
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

                # Filter by higher timeframe trend if enabled
                if Config.USE_MULTI_TIMEFRAME and signal != 'HOLD':
                    if signal == 'LONG' and htf_trend == 'DOWN':
                        logger.info(f"   ⚠️ HTF trend is bearish, filtering LONG signal")
                        return 'HOLD', confluence_score, reasons
                    elif signal == 'SHORT' and htf_trend == 'UP':
                        logger.info(f"   ⚠️ HTF trend is bullish, filtering SHORT signal")
                        return 'HOLD', confluence_score, reasons

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
        if sl_pct > 0 and pnl_pct <= -sl_pct:
            return True, f"SL ({pnl_pct*100:.2f}%)"

        # Position Timeout (24+ hours without hitting TP)
        if position_age_hours is not None and position_age_hours >= Config.POSITION_TIMEOUT_HOURS:
            return True, f"TIMEOUT ({position_age_hours:.1f}h, PnL: {pnl_pct*100:.2f}%)"

        return False, ""

