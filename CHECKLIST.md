# ✅ Pre-Launch Checklist

Checklist đầy đủ trước khi chạy bot production.

## 📦 Installation

- [ ] Python 3.8+ installed
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] TA-Lib installed (optional but recommended)
- [ ] Virtual environment created and activated
- [ ] Git repository cloned/downloaded
- [ ] Directory structure verified (`logs/`, `models/`)

## 🔧 Configuration

- [ ] `.env` file created from `.env.example`
- [ ] API_KEY filled in
- [ ] API_SECRET filled in
- [ ] TESTNET_MODE set to `True` for testing
- [ ] SYMBOLS configured (default: BTCUSDT,ETHUSDT)
- [ ] LEVERAGE set appropriately (default: 5)
- [ ] SIZE_PCT configured (default: 0.1 = 10%)
- [ ] TP_PCT set (default: 0.02 = 2%)
- [ ] SL_PCT set (default: 0.01 = 1%)
- [ ] DAILY_LOSS_LIMIT configured (default: 0.2 = 20%)
- [ ] Config validated (`python -c "from config import Config; Config.validate()"`)

## 🔑 API Setup

- [ ] AsterDEX account created
- [ ] API key generated
- [ ] Futures trading enabled
- [ ] Withdrawal permission DISABLED
- [ ] IP whitelist configured (recommended)
- [ ] API key tested (`python scripts/check_balance.py`)
- [ ] Testnet balance available (if using testnet)

## 📱 Telegram (Optional)

- [ ] Telegram bot created via @BotFather
- [ ] Bot token obtained
- [ ] Chat started with bot
- [ ] Chat ID obtained
- [ ] TELEGRAM_TOKEN in `.env`
- [ ] TELEGRAM_CHAT_ID in `.env`
- [ ] Test message sent successfully

## 🧠 Model Training

- [ ] Training data fetched successfully
- [ ] Model trained (`python ml/train.py`)
- [ ] Training completed without errors
- [ ] Model saved to `models/lstm_model.pt`
- [ ] Scaler saved to `models/scaler.pkl`
- [ ] Training accuracy > 55%
- [ ] Model loaded successfully

## 📈 Backtesting

- [ ] Backtest executed (`python run_backtest.py`)
- [ ] Backtest completed without errors
- [ ] Win rate > 55%
- [ ] Profit factor > 1.3
- [ ] Max drawdown < 15%
- [ ] Results reviewed and acceptable
- [ ] Backtest logs saved

## 🧪 Testing

- [ ] Balance check works (`python scripts/check_balance.py`)
- [ ] Signal generation works (`python scripts/test_signal.py`)
- [ ] All imports successful
- [ ] No Python errors
- [ ] Config validation passes
- [ ] API connection stable

## 🔒 Security

- [ ] `.env` file permissions set to 600 (Linux/Mac)
- [ ] `.env` not committed to Git
- [ ] API keys kept secret
- [ ] Withdrawal permission disabled
- [ ] IP whitelist enabled (if possible)
- [ ] Strong API secret used
- [ ] Backup of `.env` stored securely

## 🎯 Testnet Testing (CRITICAL)

- [ ] TESTNET_MODE=True in `.env`
- [ ] Bot started successfully
- [ ] Bot runs for at least 1 hour without crashes
- [ ] Signals generated correctly
- [ ] Orders executed successfully
- [ ] Positions opened correctly
- [ ] TP/SL triggered correctly
- [ ] Positions closed correctly
- [ ] Logs reviewed for errors
- [ ] Performance acceptable
- [ ] No API errors
- [ ] No rate limiting issues
- [ ] Telegram notifications working (if enabled)

## 📊 Monitoring Setup

- [ ] Log directory created
- [ ] Logs writing correctly
- [ ] Log rotation configured (optional)
- [ ] Telegram notifications tested
- [ ] Performance tracking setup
- [ ] Alert system configured

## 🚀 Production Preparation

- [ ] Testnet testing completed (minimum 24 hours)
- [ ] All tests passed
- [ ] Performance reviewed
- [ ] Parameters optimized
- [ ] Risk limits understood
- [ ] Emergency procedures known
- [ ] Backup plan ready
- [ ] Monitoring tools ready

## 💰 Capital Management

- [ ] Starting capital determined
- [ ] Risk per trade calculated (SIZE_PCT × LEVERAGE)
- [ ] Maximum loss per day understood (DAILY_LOSS_LIMIT)
- [ ] Total capital at risk acceptable
- [ ] Emergency fund available
- [ ] Withdrawal plan ready

## 📝 Documentation Review

- [ ] README.md read
- [ ] QUICKSTART.md reviewed
- [ ] FAQ.md checked
- [ ] STRATEGY.md understood
- [ ] COMMANDS.md bookmarked
- [ ] Emergency procedures known

## 🔄 Deployment (VPS/Cloud)

- [ ] VPS/Cloud server provisioned (if using)
- [ ] SSH access configured
- [ ] Firewall configured
- [ ] Bot deployed to server
- [ ] Systemd/PM2 service created
- [ ] Auto-start configured
- [ ] Remote monitoring setup
- [ ] Backup strategy implemented

## ⚠️ Risk Understanding

- [ ] Understand crypto trading risks
- [ ] Understand leverage risks
- [ ] Understand bot limitations
- [ ] Understand market volatility
- [ ] Understand potential losses
- [ ] Understand no guarantees
- [ ] Ready to monitor regularly
- [ ] Ready to intervene if needed

## 🎯 Launch Day

- [ ] All above items checked
- [ ] TESTNET_MODE=False in `.env`
- [ ] Starting balance confirmed
- [ ] Bot started
- [ ] First signals generated
- [ ] First trades executed
- [ ] Monitoring active
- [ ] Telegram alerts working
- [ ] Logs being written
- [ ] Performance tracking started

## 📅 Post-Launch (First Week)

- [ ] Daily balance checks
- [ ] Daily log reviews
- [ ] Performance analysis
- [ ] Win rate tracking
- [ ] PnL monitoring
- [ ] Error checking
- [ ] Parameter adjustments (if needed)
- [ ] Model retraining (if needed)

## 🔧 Maintenance Schedule

### Daily
- [ ] Check balance
- [ ] Review logs
- [ ] Monitor Telegram
- [ ] Check for errors

### Weekly
- [ ] Analyze performance
- [ ] Review trades
- [ ] Check win rate
- [ ] Optimize parameters (if needed)
- [ ] Retrain model (if needed)

### Monthly
- [ ] Full performance review
- [ ] Strategy evaluation
- [ ] Model retraining
- [ ] Dependency updates
- [ ] Backup verification

## 🆘 Emergency Contacts

- [ ] Support channels bookmarked
- [ ] GitHub issues page saved
- [ ] Telegram group joined (if available)
- [ ] Emergency close script tested
- [ ] Manual trading access ready

## 📞 Support Resources

- [ ] README.md location known
- [ ] FAQ.md bookmarked
- [ ] COMMANDS.md accessible
- [ ] API docs saved
- [ ] Community links saved

---

## ✅ Final Verification

Before going live, verify:

1. **Testnet Success:** Bot ran successfully on testnet for 24+ hours
2. **Positive Results:** Win rate > 55%, Profit Factor > 1.3
3. **No Errors:** No critical errors in logs
4. **Understanding:** You understand how the bot works
5. **Monitoring:** You can monitor and intervene if needed
6. **Risk Acceptance:** You accept the risks involved

## 🚦 Go/No-Go Decision

### ✅ GO if:
- All critical items checked
- Testnet results positive
- Comfortable with risks
- Ready to monitor

### 🛑 NO-GO if:
- Any critical items unchecked
- Testnet results poor
- Uncomfortable with risks
- Cannot monitor regularly

---

**Remember: Start small, monitor closely, scale gradually! 🚀**

**Last Updated:** Before each launch
**Next Review:** After 24 hours of live trading

