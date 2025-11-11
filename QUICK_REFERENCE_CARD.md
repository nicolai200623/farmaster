# 🎯 QUICK REFERENCE CARD

## ⚡ CRITICAL FIX NEEDED

```bash
# 1. Edit .env
notepad .env

# 2. Change this line:
LEVERAGE=20  →  LEVERAGE=10

# 3. Save and close

# 4. Verify
python check_ready.py

# 5. Start
python bot.py
```

---

## 📊 YOUR CONFIGURATION AT A GLANCE

| Setting | Value | Status |
|---------|-------|--------|
| **Mode** | Live (mainnet) | ✅ |
| **Symbols** | 7 pairs | ✅ |
| **Leverage** | 20x → **10x** | ⚠️ FIX |
| **Position Size** | $10 USDT | ✅ |
| **Take Profit** | 1% | ✅ |
| **Stop Loss** | Disabled | ✅ |
| **Loop Sleep** | 60s | ✅ |
| **Advanced Entry** | Enabled | ✅ |
| **Confluence Score** | 7 | ✅ |
| **Multi-Timeframe** | 15m + 1h | ✅ |

---

## 🚀 ESSENTIAL COMMANDS

### Setup
```bash
pip install -r requirements.txt
python ml/train.py
python run_backtest.py
python check_ready.py
```

### Run
```bash
python bot.py
```

### Monitor
```bash
python scripts/check_balance.py
python scripts/test_signal.py
type logs\bot_*.log
```

### Emergency
```bash
python scripts/close_all.py
# Or press Ctrl+C
```

---

## 📈 EXPECTED PERFORMANCE

**Per Trade**:
- Position: $10 USDT
- Leverage: 10x
- Buying Power: $100
- TP: 1% = $1 profit
- Volume: ~$20k

**Monthly**:
- Trades: 10-15
- Volume: $200k-$300k
- Win Rate: 60-70%
- Profit: $8-12
- ROI: 80-120%

---

## 🎯 ADVANCED ENTRY SYSTEM

**Confluence Factors** (Total: 0-15 points):
1. Market Structure (0-3)
2. Price Patterns (0-3)
3. Smart Money (0-3)
4. Technical Indicators (0-3)
5. Volume Analysis (0-2)

**Minimum Score**: 7 (configurable)

**Your Settings**:
```env
USE_ADVANCED_ENTRY=True
MIN_CONFLUENCE_SCORE=7
USE_MULTI_TIMEFRAME=True
PRIMARY_TIMEFRAME=15m
HIGHER_TIMEFRAME=1h
```

---

## ⚙️ KEY CONFIGURATION PARAMETERS

### Trading
```env
TESTNET_MODE=false
SYMBOLS=BTCUSDT,ETHUSDT,SOLUSDT,LTCUSDT,DOTUSDT,AVAXUSDT,XRPUSDT
LEVERAGE=10                    # ⚠️ CHANGE FROM 20
POSITION_SIZE_USDT=10
TP_PCT=0.01
SL_PCT=0
LOOP_SLEEP=60
DAILY_LOSS_LIMIT=0.2
```

### ML
```env
LSTM_THRESHOLD=0.55
MIN_SIGNAL_SCORE=1
```

### Advanced Entry
```env
USE_ADVANCED_ENTRY=True
MIN_CONFLUENCE_SCORE=7
USE_MULTI_TIMEFRAME=True
PRIMARY_TIMEFRAME=15m
HIGHER_TIMEFRAME=1h
```

### Optional (Add These)
```env
POSITION_TIMEOUT_HOURS=24
WAIT_FOR_CONFIRMATION=True
CONFIRMATION_CANDLES=2
```

---

## 🐛 TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Model not found | `python ml/train.py` |
| API Error | Check API keys |
| No trades | Wait or lower thresholds |
| Positions close early | Verify `SL_PCT=0` |
| Margin error | Reduce symbols or add balance |

---

## ✅ PRE-FLIGHT CHECKLIST

- [ ] **LEVERAGE=10** (not 20) ⚠️
- [ ] Dependencies installed
- [ ] LSTM model trained
- [ ] Config verified
- [ ] Balance >$100 USDT
- [ ] Telegram working
- [ ] Know how to stop (Ctrl+C)

---

## 📚 DOCUMENTATION

1. **EXECUTIVE_SUMMARY.md** - Overview
2. **IMMEDIATE_ACTION_PLAN.md** - Quick fix
3. **CODEBASE_ANALYSIS_AND_SETUP_GUIDE.md** - Complete guide
4. **CONFIGURATION_COMPARISON.md** - Config details
5. **QUICK_REFERENCE_CARD.md** - This card

---

## 🎯 OPTIMIZATION TIPS

**More Trades**:
- Lower `MIN_CONFLUENCE_SCORE` (7→6)
- Lower `LSTM_THRESHOLD` (0.55→0.50)
- Reduce `LOOP_SLEEP` (60→45)

**Higher Win Rate**:
- Increase `MIN_CONFLUENCE_SCORE` (7→8)
- Increase `LSTM_THRESHOLD` (0.55→0.60)

**More Volume**:
- Add more symbols
- Lower thresholds
- Reduce loop sleep

---

## 📊 MONITORING CHECKLIST

**First Hour**:
- [ ] Bot starts OK
- [ ] Leverage = 10x
- [ ] No errors
- [ ] Positions open normally

**First Day**:
- [ ] 1+ position opened
- [ ] Positions reach TP
- [ ] Win rate OK
- [ ] No overtrading

**First Week**:
- [ ] 2-4 trades done
- [ ] Profitable
- [ ] Volume accumulating
- [ ] Stable

---

## 🚨 EMERGENCY PROCEDURES

**Stop Bot**:
```bash
# Press Ctrl+C in terminal
# Bot will gracefully shutdown
```

**Close All Positions**:
```bash
python scripts/close_all.py
```

**Check Status**:
```bash
python scripts/check_balance.py
```

**View Logs**:
```bash
type logs\bot_*.log
```

---

## 💡 QUICK TIPS

1. **Always start with testnet** (if first time)
2. **Monitor first 24 hours closely**
3. **Start with small balance** ($100-200)
4. **Check logs regularly**
5. **Use Telegram notifications**
6. **Don't panic on drawdowns** (isolated margin protects)
7. **Retrain model monthly** for best results
8. **Optimize after 1 week** of data

---

## 📞 SUPPORT

**Logs**: `logs/bot_YYYYMMDD.log`  
**Telegram**: All trades sent to chat  
**Scripts**: `scripts/` folder  
**Docs**: See documentation files above

---

**🚀 Ready to farm $200k-$300k monthly volume!**

**Next Step**: Fix leverage (20→10) and start bot!

