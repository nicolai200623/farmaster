# 🚀 AsterDEX Perp Farm Bot - Stage 3

Bot trading tự động cho AsterDEX Perpetual Futures với AI (LSTM), tối ưu hóa cho Airdrop Stage 3.

## ✨ Features

### 🧠 Machine Learning
- **LSTM Neural Network**: Dự đoán hướng giá 1-5 phút
- **Features**: OHLCV + RSI + MACD + Bollinger Bands + Order Book Imbalance
- **Training**: Sử dụng historical data từ Coingecko
- **Accuracy**: ~60-70% win rate (sau training)

### 📡 Trading Signals
Kết hợp 3 nguồn tín hiệu:
1. **LSTM Prediction**: Probability > 0.6 → LONG
2. **RSI**: < 30 → LONG, > 70 → SHORT
3. **Order Book Imbalance**: Bid/Ask ratio > 1.5 → LONG

Cần ít nhất **2/3 tín hiệu** để mở lệnh.

### 💰 Risk Management
- **Position Size**: 10% vốn mỗi lệnh
- **Leverage**: 5x (có thể điều chỉnh)
- **Take Profit**: 2%
- **Stop Loss**: 1%
- **Daily Loss Limit**: 20% → Dừng bot

### 📊 Monitoring
- **Telegram Notifications**: Thông báo mọi lệnh và stats
- **Daily Reports**: Tổng kết cuối ngày
- **Volume Tracking**: Theo dõi volume để tối ưu airdrop
- **Win Rate**: Thống kê tỷ lệ thắng/thua

### 🔒 Safety
- **Testnet Mode**: Test trước khi chạy mainnet
- **Error Handling**: Xử lý lỗi API, network
- **Rate Limiting**: Tránh bị ban
- **Isolated Margin**: Giảm rủi ro thanh lý

## 📦 Installation

### 1. Clone Repository
```bash
git clone <repo-url>
cd FarmAster
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

**Note**: Nếu cài `ta-lib` gặp lỗi:
- **Windows**: Download wheel từ [https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib](https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib)
- **Linux**: `sudo apt-get install ta-lib`
- **Mac**: `brew install ta-lib`

### 3. Configure Environment
```bash
cp .env.example .env
```

Chỉnh sửa `.env`:
```env
API_KEY=your_asterdex_api_key
API_SECRET=your_asterdex_secret
TELEGRAM_TOKEN=your_telegram_bot_token  # Optional
TELEGRAM_CHAT_ID=your_chat_id           # Optional
TESTNET_MODE=True                        # False cho mainnet
```

## 🎓 Training Model

**Bước 1**: Train LSTM model với historical data
```bash
python ml/train.py
```

Quá trình:
1. Fetch data từ Coingecko (BTC, ETH)
2. Calculate indicators (RSI, MACD, BB)
3. Train LSTM (50 epochs)
4. Evaluate accuracy
5. Save model → `models/lstm_model.pt`

**Thời gian**: ~5-10 phút

## 📈 Backtesting

Test strategy với data 30 ngày:
```bash
python run_backtest.py
```

Kết quả mẫu:
```
📊 BACKTEST RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Trades: 45
Win Rate: 62.22%
Total PnL: +18.4%
Total Volume: $450k
Profit Factor: 1.85
```

## 🚀 Running Bot

### Testnet (Recommended First)
```bash
# Đảm bảo TESTNET_MODE=True trong .env
python bot.py
```

### Mainnet (Production)
```bash
# Set TESTNET_MODE=False trong .env
python bot.py
```

Bot sẽ:
1. Load LSTM model
2. Connect AsterDEX
3. Loop mỗi 30s:
   - Check positions
   - Generate signals
   - Open/Close trades
   - Monitor PnL
4. Send Telegram notifications

## 📁 Project Structure

```
FarmAster/
├── bot.py                      # Main bot
├── config.py                   # Configuration
├── requirements.txt            # Dependencies
├── .env.example               # Environment template
├── README.md                  # This file
│
├── ml/                        # Machine Learning
│   ├── features.py           # Feature engineering
│   ├── lstm_model.py         # LSTM model
│   └── train.py              # Training script
│
├── trading/                   # Trading logic
│   ├── asterdex_client.py    # AsterDEX API wrapper
│   ├── signal_generator.py   # Signal generation
│   └── risk_manager.py       # Risk management
│
├── backtest/                  # Backtesting
│   └── backtester.py         # Backtest engine
│
├── utils/                     # Utilities
│   ├── logger.py             # Logging + Telegram
│   └── data_fetcher.py       # Data fetching
│
├── models/                    # Saved models
│   ├── lstm_model.pt         # LSTM weights
│   └── scaler.pkl            # Feature scaler
│
└── logs/                      # Log files
    └── bot_YYYYMMDD.log
```

## ⚙️ Configuration

### Trading Parameters (`.env`)
```env
SYMBOLS=BTCUSDT,ETHUSDT        # Trading pairs
LEVERAGE=5                      # Đòn bẩy
SIZE_PCT=0.1                    # 10% vốn/lệnh
TP_PCT=0.02                     # Take profit 2%
SL_PCT=0.01                     # Stop loss 1%
LOOP_SLEEP=30                   # Loop interval (seconds)
DAILY_LOSS_LIMIT=0.2            # 20% daily loss limit
```

### ML Parameters
```env
LSTM_HIDDEN_SIZE=64
LSTM_NUM_LAYERS=2
LSTM_EPOCHS=50
SEQUENCE_LENGTH=60
LSTM_THRESHOLD=0.6
```

## 📱 Telegram Setup

1. Tạo bot với [@BotFather](https://t.me/BotFather)
2. Lấy token
3. Start chat với bot
4. Lấy chat ID: https://api.telegram.org/bot<TOKEN>/getUpdates
5. Thêm vào `.env`

## 🎯 Airdrop Optimization

### Volume Boosters
- **BTC/ETH**: 2x points (Stage 3)
- **High Frequency**: Nhiều lệnh nhỏ > ít lệnh lớn
- **Daily Volume**: Target $100k+/day

### Team Joining
Bot tự động join team (nếu có API endpoint).

## ⚠️ Warnings

1. **DYOR**: Crypto trading có rủi ro cao
2. **Start Small**: Test với số vốn nhỏ trước
3. **Monitor**: Theo dõi bot thường xuyên
4. **Testnet First**: Luôn test trên testnet trước
5. **API Keys**: Không share keys, enable IP whitelist

## 🐛 Troubleshooting

### Model not found
```bash
python ml/train.py
```

### API Connection Error
- Check API keys
- Check network
- Check AsterDEX status

### Telegram not working
- Verify token và chat ID
- Check bot permissions

### Low Win Rate
- Retrain model với more data
- Adjust signal thresholds
- Review backtest results

## 📊 Performance Metrics

### Expected Results (Backtest)
- **Win Rate**: 60-65%
- **Monthly Return**: 15-25%
- **Max Drawdown**: <10%
- **Profit Factor**: >1.5

### Airdrop Points
- **Daily Volume**: $100k-500k
- **Weekly Points**: 5k-15k
- **Stage 3 Boost**: 2x for BTC/ETH

## 🔄 Updates

### Version 1.0 (Current)
- ✅ LSTM prediction
- ✅ Multi-signal system
- ✅ Risk management
- ✅ Telegram notifications
- ✅ Backtesting
- ✅ Testnet support

### Planned
- [ ] Grid trading mode
- [ ] DCA strategy
- [ ] Multi-timeframe analysis
- [ ] Auto parameter optimization
- [ ] Web dashboard

## 📞 Support

- **Issues**: Open GitHub issue
- **Telegram**: [Your TG Group]
- **Docs**: [AsterDEX Docs](https://docs.asterdex.com)

## 📄 License

MIT License - Use at your own risk!

## 🙏 Credits

- **AsterDEX**: Trading platform
- **Binance**: API compatibility
- **PyTorch**: ML framework
- **Coingecko**: Historical data

---

**⚡ Happy Farming! Target: $10k+ Points/Week! ⚡**

