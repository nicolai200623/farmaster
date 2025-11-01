# ============================================
# 🔬 FEATURE ENGINEERING
# Tính toán các chỉ báo kỹ thuật
# ============================================

import pandas as pd
import numpy as np
import pandas_ta as ta
from utils.logger import logger

class FeatureEngine:
    """Tính toán features cho ML model"""
    
    FEATURE_COLUMNS = [
        'open', 'high', 'low', 'close', 'volume',
        'rsi', 'macd', 'macd_signal', 'macd_hist',
        'bb_upper', 'bb_middle', 'bb_lower', 'bb_width',
        'ob_imbalance'
    ]
    
    @staticmethod
    def calculate_indicators(df):
        """
        Tính toán tất cả indicators
        
        Args:
            df: DataFrame với OHLCV
            
        Returns:
            DataFrame với indicators
        """
        df = df.copy()
        
        # RSI (14)
        df['rsi'] = ta.rsi(df['close'], length=14)
        
        # MACD (12, 26, 9)
        macd = ta.macd(df['close'], fast=12, slow=26, signal=9)
        if macd is not None:
            df['macd'] = macd['MACD_12_26_9']
            df['macd_signal'] = macd['MACDs_12_26_9']
            df['macd_hist'] = macd['MACDh_12_26_9']
        else:
            df['macd'] = 0
            df['macd_signal'] = 0
            df['macd_hist'] = 0
        
        # Bollinger Bands (20, 2)
        bbands = ta.bbands(df['close'], length=20, std=2)
        if bbands is not None and len(bbands.columns) >= 3:
            # pandas-ta may use different column names, find them dynamically
            bb_cols = bbands.columns.tolist()
            # Upper, Middle, Lower are usually in order
            df['bb_upper'] = bbands[bb_cols[0]]  # BBL (Lower)
            df['bb_middle'] = bbands[bb_cols[1]]  # BBM (Middle)
            df['bb_lower'] = bbands[bb_cols[2]]  # BBU (Upper)
            # Swap if needed (check which is actually upper/lower)
            if df['bb_upper'].iloc[-1] < df['bb_lower'].iloc[-1]:
                df['bb_upper'], df['bb_lower'] = df['bb_lower'].copy(), df['bb_upper'].copy()
            df['bb_width'] = (df['bb_upper'] - df['bb_lower']) / df['bb_middle']
        else:
            df['bb_upper'] = df['close']
            df['bb_middle'] = df['close']
            df['bb_lower'] = df['close']
            df['bb_width'] = 0
        
        # OB Imbalance (placeholder - sẽ update realtime)
        df['ob_imbalance'] = 1.0
        
        # Fill NaN (using bfill() instead of deprecated fillna(method='bfill'))
        df = df.bfill().fillna(0)
        
        return df
    
    @staticmethod
    def prepare_features(df, feature_cols=None):
        """
        Chuẩn bị features cho model
        
        Args:
            df: DataFrame với indicators
            feature_cols: List columns cần lấy
            
        Returns:
            DataFrame chỉ với feature columns
        """
        if feature_cols is None:
            feature_cols = FeatureEngine.FEATURE_COLUMNS
        
        # Đảm bảo tất cả columns tồn tại
        for col in feature_cols:
            if col not in df.columns:
                df[col] = 0
        
        return df[feature_cols].fillna(0)
    
    @staticmethod
    def create_sequences(data, seq_length=60):
        """
        Tạo sequences cho LSTM
        
        Args:
            data: numpy array (n_samples, n_features)
            seq_length: Độ dài sequence
            
        Returns:
            X: (n_sequences, seq_length, n_features)
            y: (n_sequences,) - 1 nếu giá tăng, 0 nếu giảm
        """
        X, y = [], []
        
        for i in range(len(data) - seq_length):
            X.append(data[i:i+seq_length])
            
            # Label: 1 nếu close tăng, 0 nếu giảm
            # Close ở index 3 (open, high, low, close, ...)
            future_close = data[i + seq_length, 3]
            current_close = data[i + seq_length - 1, 3]
            y.append(1 if future_close > current_close else 0)
        
        return np.array(X), np.array(y)
    
    @staticmethod
    def calculate_ob_imbalance(bids, asks):
        """
        Tính Order Book imbalance
        
        Args:
            bids: List of [price, quantity]
            asks: List of [price, quantity]
            
        Returns:
            float: bid_volume / ask_volume
        """
        try:
            bid_vol = sum(float(b[1]) for b in bids)
            ask_vol = sum(float(a[1]) for a in asks)
            
            if ask_vol == 0:
                return 1.0
            
            return bid_vol / ask_vol
        except Exception as e:
            logger.error(f"OB imbalance calculation error: {e}")
            return 1.0

