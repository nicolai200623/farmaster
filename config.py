# ============================================
# 🔧 CONFIGURATION MODULE
# Quản lý tất cả config từ .env
# ============================================

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Cấu hình toàn bộ bot"""
    
    # API Credentials
    API_KEY = os.getenv('API_KEY', '')
    API_SECRET = os.getenv('API_SECRET', '')
    
    # AsterDEX URLs
    FUTURES_BASE_URL = 'https://fapi.asterdex.com/fapi'
    TESTNET_URL = 'https://testnet.asterdex.com/fapi'
    
    # Telegram
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')
    
    # Trading Parameters
    TESTNET_MODE = os.getenv('TESTNET_MODE', 'True').lower() == 'true'
    SYMBOLS = os.getenv('SYMBOLS', 'BTCUSDT,ETHUSDT').split(',')
    LEVERAGE = int(os.getenv('LEVERAGE', '5'))

    # Position Size Config
    SIZE_PCT = float(os.getenv('SIZE_PCT', '0.1'))  # 10% vốn mỗi lệnh (nếu không dùng POSITION_SIZE_USDT)
    POSITION_SIZE_USDT = os.getenv('POSITION_SIZE_USDT', '')  # Số tiền cố định mỗi lệnh (ví dụ: 10 = $10)

    # Convert POSITION_SIZE_USDT to float if set
    if POSITION_SIZE_USDT:
        try:
            POSITION_SIZE_USDT = float(POSITION_SIZE_USDT)
        except ValueError:
            POSITION_SIZE_USDT = None
    else:
        POSITION_SIZE_USDT = None

    TP_PCT = float(os.getenv('TP_PCT', '0.02'))  # Take profit 2%
    SL_PCT = float(os.getenv('SL_PCT', '0.01'))  # Stop loss 1%
    LOOP_SLEEP = int(os.getenv('LOOP_SLEEP', '30'))  # 30 giây
    DAILY_LOSS_LIMIT = float(os.getenv('DAILY_LOSS_LIMIT', '0.2'))  # 20%
    POSITION_TIMEOUT_HOURS = float(os.getenv('POSITION_TIMEOUT_HOURS', '24'))  # Auto-close after 24 hours
    
    # ML Parameters
    LSTM_HIDDEN_SIZE = int(os.getenv('LSTM_HIDDEN_SIZE', '64'))
    LSTM_NUM_LAYERS = int(os.getenv('LSTM_NUM_LAYERS', '2'))
    LSTM_EPOCHS = int(os.getenv('LSTM_EPOCHS', '50'))
    SEQUENCE_LENGTH = int(os.getenv('SEQUENCE_LENGTH', '60'))
    LSTM_THRESHOLD = float(os.getenv('LSTM_THRESHOLD', '0.55'))
    
    # Signal Thresholds
    RSI_OVERSOLD = 30
    RSI_OVERBOUGHT = 70
    OB_IMBALANCE_LONG = 1.5
    OB_IMBALANCE_SHORT = 0.67
    MIN_SIGNAL_SCORE = 2  # Cần ít nhất 2/3 tín hiệu (balanced quality)
    
    # Model Path
    MODEL_PATH = 'models/lstm_model.pt'
    SCALER_PATH = 'models/scaler.pkl'
    
    # Backtest
    BACKTEST_DAYS = 30
    BACKTEST_INITIAL_CAPITAL = 1000
    
    @classmethod
    def validate(cls):
        """Kiểm tra config hợp lệ"""
        if not cls.API_KEY or not cls.API_SECRET:
            raise ValueError("❌ API_KEY và API_SECRET bắt buộc phải có trong .env!")

        # Validate position size config
        if cls.POSITION_SIZE_USDT is not None:
            if cls.POSITION_SIZE_USDT <= 0:
                raise ValueError("❌ POSITION_SIZE_USDT phải > 0")
            print(f"✅ Using fixed position size: ${cls.POSITION_SIZE_USDT} USDT per trade")
        else:
            if cls.SIZE_PCT <= 0 or cls.SIZE_PCT > 1:
                raise ValueError("❌ SIZE_PCT phải trong khoảng (0, 1]")
            print(f"✅ Using percentage position size: {cls.SIZE_PCT*100}% of balance per trade")

        if cls.LEVERAGE < 1 or cls.LEVERAGE > 125:
            raise ValueError("❌ LEVERAGE phải trong khoảng [1, 125]")

        print("✅ Config validation passed!")
        return True

