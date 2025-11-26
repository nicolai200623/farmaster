# ============================================
# 🔬 FEATURE ENGINEERING
# Tính toán các chỉ báo kỹ thuật
# ============================================

import pandas as pd
import numpy as np
from utils.logger import logger

# Try pandas-ta first, fallback to manual calculation
try:
    import pandas_ta as ta
    USE_PANDAS_TA = True
except ImportError:
    # Silently use manual calculation - it works perfectly fine
    USE_PANDAS_TA = False

class FeatureEngine:
    """Tính toán features cho ML model"""

    FEATURE_COLUMNS = [
        'open', 'high', 'low', 'close', 'volume',
        'rsi', 'macd', 'macd_signal', 'macd_hist',
        'bb_upper', 'bb_middle', 'bb_lower', 'bb_width',
        'ob_imbalance',
        # New features for better accuracy
        'atr', 'atr_pct',
        'volume_ma_ratio',
        'price_distance_ema20',
        'price_distance_ema50',
        'rsi_divergence_score',
        'higher_tf_trend',
        'momentum_score',
        'volatility_ratio'
    ]

    @staticmethod
    def _calculate_rsi_manual(series, period=14):
        """Calculate RSI manually"""
        delta = series.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    @staticmethod
    def _calculate_macd_manual(series, fast=12, slow=26, signal=9):
        """Calculate MACD manually"""
        ema_fast = series.ewm(span=fast, adjust=False).mean()
        ema_slow = series.ewm(span=slow, adjust=False).mean()
        macd = ema_fast - ema_slow
        macd_signal = macd.ewm(span=signal, adjust=False).mean()
        macd_hist = macd - macd_signal
        return macd, macd_signal, macd_hist

    @staticmethod
    def _calculate_bbands_manual(series, length=20, std=2):
        """Calculate Bollinger Bands manually"""
        middle = series.rolling(window=length).mean()
        std_dev = series.rolling(window=length).std()
        upper = middle + (std_dev * std)
        lower = middle - (std_dev * std)
        return upper, middle, lower
    
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

        if USE_PANDAS_TA:
            # Use pandas-ta
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
        else:
            # Use manual calculation
            # RSI (14)
            df['rsi'] = FeatureEngine._calculate_rsi_manual(df['close'], period=14)

            # MACD (12, 26, 9)
            macd, macd_signal, macd_hist = FeatureEngine._calculate_macd_manual(
                df['close'], fast=12, slow=26, signal=9
            )
            df['macd'] = macd
            df['macd_signal'] = macd_signal
            df['macd_hist'] = macd_hist

            # Bollinger Bands (20, 2)
            bb_upper, bb_middle, bb_lower = FeatureEngine._calculate_bbands_manual(
                df['close'], length=20, std=2
            )
            df['bb_upper'] = bb_upper
            df['bb_middle'] = bb_middle
            df['bb_lower'] = bb_lower
            df['bb_width'] = (df['bb_upper'] - df['bb_lower']) / df['bb_middle']
        
        # OB Imbalance (placeholder - sẽ update realtime)
        df['ob_imbalance'] = 1.0

        # ============================================
        # NEW FEATURES FOR BETTER ACCURACY
        # ============================================

        # 1. ATR (Average True Range) - Volatility indicator
        high_low = df['high'] - df['low']
        high_close = abs(df['high'] - df['close'].shift(1))
        low_close = abs(df['low'] - df['close'].shift(1))
        true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        df['atr'] = true_range.rolling(14).mean()
        df['atr_pct'] = (df['atr'] / df['close']) * 100  # ATR as % of price

        # 2. Volume MA Ratio - Volume strength
        volume_ma_20 = df['volume'].rolling(20).mean()
        df['volume_ma_ratio'] = df['volume'] / volume_ma_20.replace(0, 1)

        # 3. Price Distance from EMAs
        ema_20 = df['close'].ewm(span=20, adjust=False).mean()
        ema_50 = df['close'].ewm(span=50, adjust=False).mean()
        df['price_distance_ema20'] = ((df['close'] - ema_20) / ema_20) * 100
        df['price_distance_ema50'] = ((df['close'] - ema_50) / ema_50) * 100

        # 4. RSI Divergence Score
        df['rsi_divergence_score'] = FeatureEngine._calculate_rsi_divergence_score(df)

        # 5. Higher Timeframe Trend (placeholder - will be updated with actual HTF data)
        # 1 = uptrend, 0 = ranging, -1 = downtrend
        df['higher_tf_trend'] = 0

        # 6. Momentum Score
        # Combine ROC and price momentum
        roc_10 = ((df['close'] - df['close'].shift(10)) / df['close'].shift(10)) * 100
        roc_20 = ((df['close'] - df['close'].shift(20)) / df['close'].shift(20)) * 100
        df['momentum_score'] = (roc_10 + roc_20) / 2

        # 7. Volatility Ratio
        # Compare current volatility to average
        current_volatility = df['high'].rolling(10).std()
        avg_volatility = df['high'].rolling(50).std()
        df['volatility_ratio'] = current_volatility / avg_volatility.replace(0, 1)

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
    def _calculate_rsi_divergence_score(df, lookback=14):
        """
        Calculate RSI divergence score

        Returns:
            Series: Divergence score (-1 to 1)
                -1 = bearish divergence
                0 = no divergence
                1 = bullish divergence
        """
        if 'rsi' not in df.columns or len(df) < lookback * 2:
            return pd.Series(0, index=df.index)

        scores = []

        for i in range(len(df)):
            if i < lookback * 2:
                scores.append(0)
                continue

            # Look at recent window
            price_window = df['close'].iloc[i-lookback:i]
            rsi_window = df['rsi'].iloc[i-lookback:i]

            # Find peaks and troughs
            price_max_idx = price_window.idxmax()
            price_min_idx = price_window.idxmin()
            rsi_max_idx = rsi_window.idxmax()
            rsi_min_idx = rsi_window.idxmin()

            # Check for bullish divergence (price lower low, RSI higher low)
            if i >= lookback * 2:
                prev_price_min = df['close'].iloc[i-lookback*2:i-lookback].min()
                curr_price_min = price_window.min()
                prev_rsi_min = df['rsi'].iloc[i-lookback*2:i-lookback].min()
                curr_rsi_min = rsi_window.min()

                if curr_price_min < prev_price_min and curr_rsi_min > prev_rsi_min:
                    scores.append(1)  # Bullish divergence
                    continue

                # Check for bearish divergence (price higher high, RSI lower high)
                prev_price_max = df['close'].iloc[i-lookback*2:i-lookback].max()
                curr_price_max = price_window.max()
                prev_rsi_max = df['rsi'].iloc[i-lookback*2:i-lookback].max()
                curr_rsi_max = rsi_window.max()

                if curr_price_max > prev_price_max and curr_rsi_max < prev_rsi_max:
                    scores.append(-1)  # Bearish divergence
                    continue

            scores.append(0)  # No divergence

        return pd.Series(scores, index=df.index)

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

