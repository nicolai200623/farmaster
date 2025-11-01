# Changelog

All notable changes to AsterDEX Farm Bot will be documented in this file.

## [1.0.0] - 2024-01-XX

### Added
- 🧠 LSTM Neural Network for price prediction
- 📡 Multi-signal system (LSTM + RSI + OB Imbalance)
- 💰 Risk management with TP/SL
- 📊 Backtesting engine
- 📱 Telegram notifications
- 🔒 Testnet support
- 📈 Volume tracking for airdrop optimization
- 🛡️ Daily loss limit protection
- 📝 Comprehensive logging
- 🔧 Configuration via .env file

### Features
- Support for multiple symbols (BTC, ETH)
- Isolated margin mode
- Configurable leverage (1-125x)
- Automatic position management
- Real-time signal generation
- Historical data fetching from Coingecko
- Feature engineering (RSI, MACD, Bollinger Bands)
- Model training and evaluation
- Daily statistics and reports

### Scripts
- `bot.py` - Main trading bot
- `ml/train.py` - Model training
- `run_backtest.py` - Backtesting
- `scripts/check_balance.py` - Balance checker
- `scripts/close_all.py` - Emergency close
- `scripts/test_signal.py` - Signal testing

### Documentation
- README.md - Full documentation
- QUICKSTART.md - Quick start guide
- .env.example - Configuration template

## [Planned]

### Version 1.1
- [ ] Grid trading mode
- [ ] DCA (Dollar Cost Averaging) strategy
- [ ] Multi-timeframe analysis
- [ ] Auto parameter optimization
- [ ] Enhanced backtesting with slippage simulation

### Version 1.2
- [ ] Web dashboard
- [ ] Real-time performance charts
- [ ] Advanced risk metrics
- [ ] Portfolio management
- [ ] Multiple exchange support

### Version 2.0
- [ ] Reinforcement Learning agent
- [ ] Sentiment analysis integration
- [ ] Advanced order types (limit, stop-limit)
- [ ] Copy trading features
- [ ] Mobile app

