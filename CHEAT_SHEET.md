# 📝 CHEAT SHEET - LỆNH NHANH

## 🚀 Setup Nhanh (Lần Đầu)

```bash
# 1. Cài đặt
pip install -r requirements.txt

# 2. Cấu hình
cp .env.volume_farming .env
# Sửa API_KEY và API_SECRET trong .env

# 3. Validate
python -c "from config import Config; Config.validate()"

# 4. Train models
python ml/train_ensemble.py

# 5. Backtest
python scripts/test_volume_farming.py

source venv/bin/activate
python scripts/auto_retrain.py --days 180

# 6. Chạy bot (testnet)
python bot.py
```

---

## 🧠 Training Models

```bash
# Train LSTM only
python ml/train.py

# Train XGBoost only
python ml/xgboost_model.py

# Train Ensemble (khuyến nghị)
python ml/train_ensemble.py

# Retrain tất cả
python retrain_and_test.py
```

---

## 📊 Backtest

```bash
# Backtest cơ bản
python run_backtest.py

# Backtest volume farming (chi tiết)
python scripts/test_volume_farming.py

# Backtest 30 ngày
python -c "from config import Config; Config.BACKTEST_DAYS=90" && python run_backtest.py

# Quick test
python quick_test.py
```

---

## 🤖 Chạy Bot

```bash
# Testnet
python bot.py

# Mainnet (sau khi sửa TESTNET_MODE=false)
python bot.py

# Background (Linux/Mac)
nohup python bot.py > bot.log 2>&1 &

# Screen (Linux/Mac)
screen -S asterdex-bot
python bot.py
# Ctrl+A, D để detach
# screen -r asterdex-bot để attach lại

# Systemd (VPS)
sudo systemctl start asterdex-bot
sudo systemctl stop asterdex-bot
sudo systemctl restart asterdex-bot
sudo systemctl status asterdex-bot
```

---

## 👀 Monitoring

```bash
# Xem logs real-time
tail -f logs/bot_*.log

# Xem logs systemd
sudo journalctl -u asterdex-bot -f

# Check balance
python scripts/check_balance.py

# Test signals
python scripts/test_signal.py

# Check positions
python -c "from trading.asterdex_client import AsterDEXClient; c=AsterDEXClient(); print(c.get_all_positions())"

# Analyze performance
python scripts/analyze_performance.py
```

---

## 🔧 Utilities

```bash
# Validate config
python -c "from config import Config; Config.validate()"

# Test connections
python test_connections.py

# Check symbols
python check_symbols.py

# Test position size
python test_position_size.py

# Close all positions
python scripts/close_all.py
```

---

## 🛑 Stop Bot

```bash
# Ctrl+C (nếu chạy foreground)

# Kill process
pkill -f bot.py

# Systemd
sudo systemctl stop asterdex-bot

# Screen
screen -r asterdex-bot
# Ctrl+C
```

---

## ⚙️ Cấu Hình Nhanh

### Áp dụng volume farming config
```bash
python scripts/apply_volume_farming_config.py
```

### Sửa .env thủ công
```bash
# Windows
notepad .env

# Linux/Mac
nano .env
# hoặc
vim .env
```

### Backup/Restore config
```bash
# Backup
cp .env .env.backup_$(date +%Y%m%d)

# Restore
cp .env.backup_YYYYMMDD .env
```

---

## 🔍 Kiểm Tra

### Kiểm tra models đã train
```bash
# Windows
dir models

# Linux/Mac
ls -lh models/

# Phải có:
# - lstm_model.pt
# - scaler.pkl
# - xgboost_model.json
# - xgboost_scaler.pkl
```

### Kiểm tra config
```bash
# Xem config hiện tại
python -c "from config import Config; print(f'Symbols: {Config.SYMBOLS}'); print(f'Leverage: {Config.LEVERAGE}'); print(f'TP: {Config.TP_PCT}%'); print(f'SL: {Config.SL_PCT}')"

# Kiểm tra API keys
python -c "from config import Config; print('API_KEY:', Config.API_KEY[:10]+'...'); print('API_SECRET:', Config.API_SECRET[:10]+'...')"
```

### Test API connection
```bash
python -c "from trading.asterdex_client import AsterDEXClient; c=AsterDEXClient(); print('Balance:', c.get_account_balance())"
```

---

## 📈 Tối Ưu Hóa

### Tăng số lượng trades
```env
# Sửa .env:
LSTM_THRESHOLD=0.35
MIN_CONFLUENCE_SCORE=2
LOOP_SLEEP=20
USE_TREND_FILTER=False
USE_VOLUME_FILTER=False
```

### Tăng win rate
```env
# Sửa .env:
LSTM_THRESHOLD=0.50
MIN_CONFLUENCE_SCORE=5
USE_TREND_FILTER=True
MIN_SIGNAL_QUALITY_SCORE=60
```

### Giảm risk
```env
# Sửa .env:
POSITION_SIZE_USDT=5
LEVERAGE=5
DAILY_LOSS_LIMIT=0.1
```

---

## 🐛 Troubleshooting

### Không có tín hiệu
```bash
# Test signal
python scripts/test_signal.py

# Giảm threshold
# Sửa .env: LSTM_THRESHOLD=0.35
```

### Margin insufficient
```bash
# Giảm symbols
# Sửa .env: SYMBOLS=BTCUSDT,ETHUSDT,SOLUSDT,BNBUSDT

# Hoặc tăng balance
```

### Lệnh đóng ngay
```bash
# Kiểm tra SL_PCT
cat .env | grep SL_PCT
# Phải = 0

# Kiểm tra bug fix
cat trading/signal_generator.py | grep -n "if sl_pct > 0"
# Phải có dòng: if sl_pct > 0 and pnl_pct <= -sl_pct:
```

### Model chưa train
```bash
# Train lại
python ml/train_ensemble.py
```

### API error
```bash
# Test connection
python test_connections.py

# Kiểm tra API keys
python -c "from config import Config; print(Config.API_KEY, Config.API_SECRET)"
```

---

## 📁 File Paths

```
FarmAster/
├── .env                          # Cấu hình chính
├── bot.py                        # Main bot
├── config.py                     # Config loader
│
├── ml/
│   ├── train.py                  # Train LSTM
│   ├── xgboost_model.py          # Train XGBoost
│   └── train_ensemble.py         # Train Ensemble
│
├── backtest/
│   └── enhanced_backtester.py    # Backtest engine
│
├── trading/
│   ├── asterdex_client.py        # API client
│   ├── signal_generator.py       # Signal logic
│   └── risk_manager.py           # Risk management
│
├── scripts/
│   ├── check_balance.py          # Check balance
│   ├── test_signal.py            # Test signals
│   ├── close_all.py              # Close all positions
│   └── test_volume_farming.py    # Test volume farming
│
├── logs/                         # Log files
└── models/                       # Trained models
```

---

## 🎯 Workflow Chuẩn

### Lần đầu setup
```bash
1. cp .env.volume_farming .env
2. # Sửa API keys
3. python -c "from config import Config; Config.validate()"
4. python ml/train_ensemble.py
5. python scripts/test_volume_farming.py
6. # Nếu OK -> python bot.py
```

### Hàng ngày
```bash
1. tail -f logs/bot_*.log
2. python scripts/check_balance.py
3. # Kiểm tra Telegram
```

### Hàng tuần
```bash
1. python scripts/analyze_performance.py
2. # Đánh giá win rate, volume
3. # Điều chỉnh config nếu cần
```

### Khi cần retrain
```bash
1. python ml/train_ensemble.py
2. python scripts/test_volume_farming.py
3. # Nếu tốt hơn -> restart bot
```

---

## 💡 Tips

```bash
# Xem log 100 dòng cuối
tail -n 100 logs/bot_*.log

# Tìm lỗi trong log
grep -i error logs/bot_*.log

# Đếm số trades
grep "Position opened" logs/bot_*.log | wc -l

# Xem tất cả TP
grep "TP (" logs/bot_*.log

# Xem tất cả SL (không nên có nếu SL_PCT=0)
grep "SL (" logs/bot_*.log

# Kiểm tra bot có đang chạy không
ps aux | grep bot.py

# Xem CPU/Memory usage
top -p $(pgrep -f bot.py)
```

---

## 🚨 Emergency Commands

```bash
# STOP BOT NGAY
pkill -9 -f bot.py

# ĐÓNG TẤT CẢ POSITIONS
python scripts/close_all.py

# RESTORE CONFIG
cp .env.backup .env

# RESTART BOT
pkill -f bot.py && sleep 2 && python bot.py &
```

---

## 📞 Support Commands

```bash
# Xem version Python
python --version

# Xem packages đã cài
pip list

# Kiểm tra disk space
df -h

# Kiểm tra memory
free -h

# Xem network
netstat -an | grep ESTABLISHED
```

---

**Lưu file này để tra cứu nhanh! 📌**

