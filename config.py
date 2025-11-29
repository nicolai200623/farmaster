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

    # TP/SL in decimal format (0.01 = 1%, NOT 1.0)
    TP_PCT = float(os.getenv('TP_PCT', '0.02'))  # Take profit 2% (0.02)
    SL_PCT = float(os.getenv('SL_PCT', '0.01')) if float(os.getenv('SL_PCT', '0')) > 0 else None  # Stop loss 1% (0.01)
    LOOP_SLEEP = int(os.getenv('LOOP_SLEEP', '30'))  # 30 giây
    DAILY_LOSS_LIMIT = float(os.getenv('DAILY_LOSS_LIMIT', '0.2'))  # 20%
    POSITION_TIMEOUT_HOURS = float(os.getenv('POSITION_TIMEOUT_HOURS', '24'))  # Auto-close after 24 hours
    
    # ML Parameters
    LSTM_HIDDEN_SIZE = int(os.getenv('LSTM_HIDDEN_SIZE', '128'))
    LSTM_NUM_LAYERS = int(os.getenv('LSTM_NUM_LAYERS', '3'))
    LSTM_EPOCHS = int(os.getenv('LSTM_EPOCHS', '150'))
    LSTM_DROPOUT = float(os.getenv('LSTM_DROPOUT', '0.3'))
    LSTM_LEARNING_RATE = float(os.getenv('LSTM_LEARNING_RATE', '0.0005'))
    SEQUENCE_LENGTH = int(os.getenv('SEQUENCE_LENGTH', '60'))
    LSTM_THRESHOLD = float(os.getenv('LSTM_THRESHOLD', '0.55'))

    # ============================================
    # 🎭 ENSEMBLE MODEL SETTINGS
    # ============================================
    USE_ENSEMBLE = os.getenv('USE_ENSEMBLE', 'True').lower() == 'true'
    ENSEMBLE_MODELS = os.getenv('ENSEMBLE_MODELS', 'lstm,xgboost').split(',')

    # Parse ensemble weights
    ensemble_weights_str = os.getenv('ENSEMBLE_WEIGHTS', '0.3,0.7')
    ENSEMBLE_WEIGHTS = [float(w.strip()) for w in ensemble_weights_str.split(',')]

    # Validate ensemble weights
    if len(ENSEMBLE_WEIGHTS) != len(ENSEMBLE_MODELS):
        raise ValueError(f"ENSEMBLE_WEIGHTS length ({len(ENSEMBLE_WEIGHTS)}) must match ENSEMBLE_MODELS ({len(ENSEMBLE_MODELS)})")

    # XGBoost specific parameters (Anti-overfitting)
    XGBOOST_MAX_DEPTH = int(os.getenv('XGBOOST_MAX_DEPTH', '4'))
    XGBOOST_LEARNING_RATE = float(os.getenv('XGBOOST_LEARNING_RATE', '0.03'))
    XGBOOST_N_ESTIMATORS = int(os.getenv('XGBOOST_N_ESTIMATORS', '300'))
    XGBOOST_MIN_CHILD_WEIGHT = int(os.getenv('XGBOOST_MIN_CHILD_WEIGHT', '5'))
    XGBOOST_SUBSAMPLE = float(os.getenv('XGBOOST_SUBSAMPLE', '0.7'))
    XGBOOST_COLSAMPLE_BYTREE = float(os.getenv('XGBOOST_COLSAMPLE_BYTREE', '0.7'))
    XGBOOST_REG_ALPHA = float(os.getenv('XGBOOST_REG_ALPHA', '0.5'))
    XGBOOST_REG_LAMBDA = float(os.getenv('XGBOOST_REG_LAMBDA', '2.0'))
    
    # Signal Thresholds
    RSI_OVERSOLD = 20
    RSI_OVERBOUGHT = 80
    OB_IMBALANCE_LONG = 1.5
    OB_IMBALANCE_SHORT = 0.67
    MIN_SIGNAL_SCORE = 2  # Cần ít nhất 2/3 tín hiệu (balanced quality)

    # ============================================
    # 🎯 ADVANCED ENTRY SETTINGS
    # ============================================
    USE_ADVANCED_ENTRY = os.getenv('USE_ADVANCED_ENTRY', 'True').lower() == 'true'
    MIN_CONFLUENCE_SCORE = int(os.getenv('MIN_CONFLUENCE_SCORE', '5'))  # Giảm xuống 5 để tăng signal frequency

    # Smart Entry System V2
    USE_SMART_ENTRY_V2 = os.getenv('USE_SMART_ENTRY_V2', 'True').lower() == 'true'
    MIN_ENTRY_SCORE = int(os.getenv('MIN_ENTRY_SCORE', '5'))  # Minimum score for SmartEntryV2
    MIN_RR_RATIO = float(os.getenv('MIN_RR_RATIO', '2.0'))  # Minimum Risk:Reward ratio
    REQUIRE_SESSION_TIMING = os.getenv('REQUIRE_SESSION_TIMING', 'False').lower() == 'true'

    # Entry Confirmation
    WAIT_FOR_CONFIRMATION = os.getenv('WAIT_FOR_CONFIRMATION', 'True').lower() == 'true'
    CONFIRMATION_CANDLES = int(os.getenv('CONFIRMATION_CANDLES', '2'))

    # Multi-Timeframe Settings
    USE_MULTI_TIMEFRAME = os.getenv('USE_MULTI_TIMEFRAME', 'True').lower() == 'true'
    PRIMARY_TIMEFRAME = os.getenv('PRIMARY_TIMEFRAME', '15m')
    HIGHER_TIMEFRAME = os.getenv('HIGHER_TIMEFRAME', '1h')

    # Anti-Whipsaw Filters (Prevent rapid signal flipping)
    USE_SIGNAL_COOLDOWN = os.getenv('USE_SIGNAL_COOLDOWN', 'True').lower() == 'true'
    SIGNAL_COOLDOWN_MINUTES = int(os.getenv('SIGNAL_COOLDOWN_MINUTES', '60'))  # No new signal for 60 min after entry
    REQUIRE_HTF_TREND_ALIGNMENT = os.getenv('REQUIRE_HTF_TREND_ALIGNMENT', 'True').lower() == 'true'  # Only LONG when HTF UP, SHORT when HTF DOWN
    USE_ML_CONVICTION_FILTER = os.getenv('USE_ML_CONVICTION_FILTER', 'True').lower() == 'true'
    MIN_ML_CONVICTION = float(os.getenv('MIN_ML_CONVICTION', '0.1'))  # LSTM must be >0.6 or <0.4 (distance from 0.5)

    # Post-Trade Cooldown (after closing a position)
    USE_POST_TRADE_COOLDOWN = os.getenv('USE_POST_TRADE_COOLDOWN', 'True').lower() == 'true'
    POST_TRADE_COOLDOWN_MINUTES = int(os.getenv('POST_TRADE_COOLDOWN_MINUTES', '5'))  # Wait 5 min after closing before new entry
    POST_TRADE_REQUIRE_PULLBACK = os.getenv('POST_TRADE_REQUIRE_PULLBACK', 'True').lower() == 'true'  # Require price pullback after TP
    PULLBACK_PCT = float(os.getenv('PULLBACK_PCT', '0.3'))  # Require 0.3% pullback from close price

    # Entry Quality Check (smart entry after closing)
    USE_ENTRY_QUALITY_CHECK = os.getenv('USE_ENTRY_QUALITY_CHECK', 'True').lower() == 'true'
    MIN_ENTRY_QUALITY_SCORE = int(os.getenv('MIN_ENTRY_QUALITY_SCORE', '2'))  # Min quality score (out of 5)

    # Smart Money Concepts
    USE_SMC = os.getenv('USE_SMC', 'True').lower() == 'true'  # Use Smart Money Concepts
    DETECT_ORDER_BLOCKS = os.getenv('DETECT_ORDER_BLOCKS', 'True').lower() == 'true'
    DETECT_FVG = os.getenv('DETECT_FVG', 'True').lower() == 'true'  # Fair Value Gaps
    DETECT_LIQUIDITY_SWEEPS = os.getenv('DETECT_LIQUIDITY_SWEEPS', 'True').lower() == 'true'

    # Price Action Patterns
    USE_PRICE_PATTERNS = os.getenv('USE_PRICE_PATTERNS', 'True').lower() == 'true'
    DETECT_ENGULFING = os.getenv('DETECT_ENGULFING', 'True').lower() == 'true'
    DETECT_PIN_BARS = os.getenv('DETECT_PIN_BARS', 'True').lower() == 'true'
    DETECT_DOJI = os.getenv('DETECT_DOJI', 'True').lower() == 'true'

    # Volume Analysis
    VOLUME_CONFIRMATION = os.getenv('VOLUME_CONFIRMATION', 'True').lower() == 'true'
    MIN_VOLUME_SPIKE = float(os.getenv('MIN_VOLUME_SPIKE', '1.5'))  # 150% of average

    # Entry Optimization
    USE_LIMIT_ORDERS = os.getenv('USE_LIMIT_ORDERS', 'False').lower() == 'true'
    LIMIT_ORDER_OFFSET = float(os.getenv('LIMIT_ORDER_OFFSET', '0.001'))  # 0.1% offset

    # Risk Management Updates
    USE_ATR_STOPS = os.getenv('USE_ATR_STOPS', 'False').lower() == 'true'
    ATR_MULTIPLIER_SL = float(os.getenv('ATR_MULTIPLIER_SL', '1.5'))  # SL = 1.5x ATR
    ATR_MULTIPLIER_TP = float(os.getenv('ATR_MULTIPLIER_TP', '2.5'))  # TP = 2.5x ATR
    MIN_RR_RATIO = float(os.getenv('MIN_RR_RATIO', '1.5'))  # Minimum Risk:Reward ratio

    # Model Path
    MODEL_PATH = 'models/lstm_model.pt'
    SCALER_PATH = 'models/scaler.pkl'

    # Backtest
    BACKTEST_DAYS = int(os.getenv('BACKTEST_DAYS', '90'))
    BACKTEST_INITIAL_CAPITAL = int(os.getenv('BACKTEST_INITIAL_CAPITAL', '1000'))

    # Signal Filters
    USE_SIGNAL_FILTERS = os.getenv('USE_SIGNAL_FILTERS', 'True').lower() == 'true'
    USE_TREND_FILTER = os.getenv('USE_TREND_FILTER', 'True').lower() == 'true'
    USE_VOLATILITY_FILTER = os.getenv('USE_VOLATILITY_FILTER', 'True').lower() == 'true'
    USE_VOLUME_FILTER = os.getenv('USE_VOLUME_FILTER', 'True').lower() == 'true'
    MIN_VOLUME_RATIO = float(os.getenv('MIN_VOLUME_RATIO', '1.2'))
    MIN_ATR_PCT = float(os.getenv('MIN_ATR_PCT', '0.5'))
    MAX_ATR_PCT = float(os.getenv('MAX_ATR_PCT', '5.0'))
    MIN_SIGNAL_QUALITY_SCORE = float(os.getenv('MIN_SIGNAL_QUALITY_SCORE', '50'))

    # Trailing Stop (NOW PnL-BASED! 0.5 = 0.5% PnL profit)
    # NOTE: Trailing stop now uses PnL% (including leverage effect), NOT price movement%
    # With 10x leverage: 0.5% PnL = 0.05% price movement
    USE_TRAILING_STOP = os.getenv('USE_TRAILING_STOP', 'True').lower() == 'true'
    TRAILING_ACTIVATION_PCT = float(os.getenv('TRAILING_ACTIVATION_PCT', '0.5'))  # Activate at 0.5% PnL
    TRAILING_DISTANCE_PCT = float(os.getenv('TRAILING_DISTANCE_PCT', '0.3'))  # Trail by 0.3% PnL from peak
    USE_PNL_BASED_TRAILING = os.getenv('USE_PNL_BASED_TRAILING', 'True').lower() == 'true'  # Use PnL-based calculation
    USE_ATR_TRAILING = os.getenv('USE_ATR_TRAILING', 'False').lower() == 'true'
    ATR_TRAILING_MULTIPLIER = float(os.getenv('ATR_TRAILING_MULTIPLIER', '2.0'))
    USE_BREAKEVEN_STOP = os.getenv('USE_BREAKEVEN_STOP', 'True').lower() == 'true'
    BREAKEVEN_ACTIVATION_PCT = float(os.getenv('BREAKEVEN_ACTIVATION_PCT', '0.5'))
    BREAKEVEN_OFFSET_PCT = float(os.getenv('BREAKEVEN_OFFSET_PCT', '0.1'))

    # Market Regime Detection
    USE_MARKET_REGIME = os.getenv('USE_MARKET_REGIME', 'True').lower() == 'true'
    REGIME_LOOKBACK = int(os.getenv('REGIME_LOOKBACK', '50'))

    # Symbol Optimization
    USE_SYMBOL_OPTIMIZER = os.getenv('USE_SYMBOL_OPTIMIZER', 'True').lower() == 'true'
    SYMBOL_PARAMS_FILE = os.getenv('SYMBOL_PARAMS_FILE', 'config/symbol_params.json')

    # ============================================
    # 🎲 ADVANCED RISK MANAGEMENT
    # ============================================
    USE_KELLY_SIZING = os.getenv('USE_KELLY_SIZING', 'True').lower() == 'true'
    MAX_CORRELATED_POSITIONS = int(os.getenv('MAX_CORRELATED_POSITIONS', '2'))
    MAX_POSITIONS = int(os.getenv('MAX_POSITIONS', '4'))
    REDUCE_RISK_AFTER_LOSSES = os.getenv('REDUCE_RISK_AFTER_LOSSES', 'True').lower() == 'true'

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

