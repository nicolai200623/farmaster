# ============================================
# 📡 SIGNAL GENERATOR
# Kết hợp LSTM + RSI + OB Imbalance
# ============================================

import pandas as pd
import numpy as np
from ml.features import FeatureEngine
from ml.lstm_model import LSTMTrainer
from config import Config
from utils.logger import logger

class SignalGenerator:
    """
    Tạo trading signals từ nhiều nguồn:
    1. LSTM prediction
    2. RSI oversold/overbought
    3. Order Book imbalance
    """
    
    def __init__(self, lstm_trainer):
        self.lstm_trainer = lstm_trainer
        self.feature_engine = FeatureEngine()
    
    def generate_signal(self, client, symbol):
        """
        Tạo signal cho 1 symbol
        
        Args:
            client: AsterDEXClient instance
            symbol: Trading pair
            
        Returns:
            str: 'LONG', 'SHORT', hoặc 'HOLD'
        """
        try:
            # 1. Get klines data
            klines = client.get_klines(symbol, interval='1m', limit=100)
            
            if not klines or len(klines) < 60:
                logger.warning(f"Insufficient klines data for {symbol}")
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
            
            # 4. Prepare features for LSTM
            feature_df = self.feature_engine.prepare_features(df)
            
            # Normalize
            normalized = self.lstm_trainer.scaler.transform(feature_df.values)
            
            # Get last 60 candles
            if len(normalized) < Config.SEQUENCE_LENGTH:
                logger.warning(f"Not enough data for LSTM: {len(normalized)}")
                return 'HOLD'
            
            lstm_input = normalized[-Config.SEQUENCE_LENGTH:]
            
            # 5. LSTM Prediction
            lstm_prob = self.lstm_trainer.predict(lstm_input)[0]
            
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
            return 'HOLD'
    
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
    
    def should_close_position(self, position, tp_pct=None, sl_pct=None):
        """
        Kiểm tra có nên đóng position không
        
        Args:
            position: Dict từ get_position()
            tp_pct: Take profit %
            sl_pct: Stop loss %
            
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
        
        # Stop Loss
        if pnl_pct <= -sl_pct:
            return True, f"SL ({pnl_pct*100:.2f}%)"
        
        return False, ""

