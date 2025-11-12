# 📚 HƯỚNG DẪN ĐẦY ĐỦ - TỪ A ĐẾN Z

## 🎯 Mục Lục

1. [Setup Ban Đầu](#1-setup-ban-đầu)
2. [Cấu Hình](#2-cấu-hình)
3. [Train Models](#3-train-models)
4. [Backtest](#4-backtest)
5. [Chạy Bot](#5-chạy-bot)
6. [Monitoring](#6-monitoring)
7. [Troubleshooting](#7-troubleshooting)

---

## 1. Setup Ban Đầu

### 1.1. Clone Repository (nếu chưa có)

```bash
git clone https://github.com/nicolai200623/farmaster.git
cd farmaster
```

### 1.2. Cài Đặt Dependencies

**Windows:**
```bash
# Tạo virtual environment
python -m venv venv
venv\Scripts\activate

# Cài đặt packages
pip install -r requirements.txt
```

**Linux/Mac:**
```bash
# Tạo virtual environment
python3 -m venv venv
source venv/bin/activate

# Cài đặt packages
pip install -r requirements.txt
```

### 1.3. Tạo Thư Mục Cần Thiết

```bash
# Windows
mkdir logs models data config

# Linux/Mac
mkdir -p logs models data config
```

### 1.4. Kiểm Tra Cài Đặt

```bash
python -c "import torch; import pandas; import numpy; print('✅ All packages installed!')"
```

---

## 2. Cấu Hình

### 2.1. Tạo File .env

**Cách 1: Copy từ template**
```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

**Cách 2: Sử dụng cấu hình volume farming**
```bash
# Windows
copy .env.volume_farming .env

# Linux/Mac
cp .env.volume_farming .env
```

### 2.2. Chỉnh Sửa .env

Mở file `.env` và điền thông tin:

```env
# API Credentials (BẮT BUỘC)
API_KEY=your_asterdex_api_key_here
API_SECRET=your_asterdex_api_secret_here

# Telegram (TÙY CHỌN - để nhận thông báo)
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id

# Trading Config
TESTNET_MODE=true  # Bắt đầu với testnet
SYMBOLS=BTCUSDT,ETHUSDT,SOLUSDT,BNBUSDT,LTCUSDT,AVAXUSDT,XRPUSDT,ADAUSDT
LEVERAGE=10
POSITION_SIZE_USDT=10
TP_PCT=1.0
SL_PCT=0
LOOP_SLEEP=30
```

### 2.3. Validate Config

```bash
python -c "from config import Config; Config.validate()"
```

**Kết quả mong đợi:**
```
✅ Using fixed position size: $10.0 USDT per trade
✅ Config validation passed!
```

---

## 3. Train Models

### 3.1. Kiểm Tra Kết Nối

```bash
# Test kết nối AsterDEX
python test_connections.py
```

**Kết quả mong đợi:**
```
✅ AsterDEX connection OK
✅ Balance: $XXX.XX
```

### 3.2. Train LSTM Model

```bash
python ml/train.py
```

**Thời gian:** 10-30 phút tùy máy

**Kết quả mong đợi:**
```
📊 Fetching data...
🧠 Training LSTM model...
Epoch 1/150: Loss: 0.XXX
...
✅ Model saved to models/lstm_model.pt
✅ Scaler saved to models/scaler.pkl
```

### 3.3. Train XGBoost Model

```bash
python ml/xgboost_model.py
```

**Thời gian:** 5-15 phút

**Kết quả mong đợi:**
```
📊 Fetching data...
🌲 Training XGBoost model...
✅ Model saved to models/xgboost_model.json
✅ Scaler saved to models/xgboost_scaler.pkl
```

### 3.4. Train Ensemble (Khuyến nghị)

```bash
python ml/train_ensemble.py
```

**Thời gian:** 15-45 phút

**Kết quả mong đợi:**
```
🎭 Training Ensemble Models...
📊 Fetching data...
🧠 Training LSTM...
🌲 Training XGBoost...
✅ All models trained successfully!
```

### 3.5. Kiểm Tra Models

```bash
# Kiểm tra files đã tạo
# Windows
dir models

# Linux/Mac
ls -lh models/
```

**Phải có các files:**
- `lstm_model.pt`
- `scaler.pkl`
- `xgboost_model.json`
- `xgboost_scaler.pkl`

---

## 4. Backtest

### 4.1. Backtest Cơ Bản

```bash
python run_backtest.py
```

**Kết quả mong đợi:**
```
📈 ENHANCED BACKTEST - 90 NGÀY
✅ Total Trades: 25-35
✅ Win Rate: 55-65%
✅ Total PnL: +XX%
✅ Total Volume: $XXXk
```

### 4.2. Backtest Volume Farming Config

```bash
python scripts/test_volume_farming.py
```

**Kết quả chi tiết hơn:**
```
📋 CẤU HÌNH HIỆN TẠI
  Symbols: 8 pairs
  Leverage: 10x
  Position Size: $10 USDT
  ...

📊 KẾT QUẢ BACKTEST
  Tổng trades: XX
  Win rate: XX%
  ...

📈 DỰ ĐOÁN THÁNG (30 NGÀY)
  Trades/tháng: XX
  Volume/tháng: $XXXk
  Profit/tháng: $XX
  ROI/tháng: XX%

💡 KHUYẾN NGHỊ
  ✅ Cấu hình tốt - sẵn sàng chạy!
```

### 4.3. Backtest Với Tham Số Khác

```bash
# Backtest 30 ngày
python -c "from config import Config; Config.BACKTEST_DAYS = 30; exec(open('run_backtest.py').read())"

# Backtest với symbols cụ thể
python -c "from config import Config; Config.SYMBOLS = ['BTCUSDT', 'ETHUSDT']; exec(open('run_backtest.py').read())"
```

### 4.4. Đánh Giá Kết Quả Backtest

**Kết quả TỐT (sẵn sàng chạy):**
- ✅ Total Trades ≥ 15 (30 ngày)
- ✅ Win Rate ≥ 55%
- ✅ Profit Factor ≥ 1.3
- ✅ Total PnL > 0

**Kết quả CẦN CẢI THIỆN:**
- ⚠️ Total Trades < 10
- ⚠️ Win Rate < 50%
- ⚠️ Profit Factor < 1.0

---

## 5. Chạy Bot

### 5.1. Chạy Testnet (BẮT BUỘC trước)

**Đảm bảo trong .env:**
```env
TESTNET_MODE=true
```

**Chạy bot:**
```bash
python bot.py
```

**Kết quả mong đợi:**
```
🚀 ASTERDEX PERP FARM BOT - INITIALIZING
✅ Bot initialized successfully!
🧠 Loading Ensemble models...
✅ Models loaded!
🏁 BOT STARTED!

🔄 LOOP #1 - 2024-XX-XX XX:XX:XX
📊 Processing BTCUSDT...
📡 Signal: LONG
💰 Opening position...
✅ Position opened!
```

### 5.2. Theo Dõi Testnet (24-48h)

**Kiểm tra:**
- ✅ Bot chạy không lỗi
- ✅ Có tín hiệu được tạo
- ✅ Lệnh được mở thành công
- ✅ Lệnh KHÔNG đóng ngay (trong vài phút)
- ✅ Lệnh đóng khi hit TP 1%
- ✅ Telegram notifications hoạt động (nếu có)

**Xem logs:**
```bash
# Windows
type logs\bot_*.log

# Linux/Mac
tail -f logs/bot_*.log
```

### 5.3. Chuyển Sang Mainnet

**Sau khi testnet ổn định 24-48h:**

1. **Stop bot:**
```bash
# Nhấn Ctrl+C
```

2. **Sửa .env:**
```env
TESTNET_MODE=false
```

3. **Khởi động lại:**
```bash
python bot.py
```

### 5.4. Chạy Bot Nền (Background)

**Windows (PowerShell):**
```powershell
Start-Process python -ArgumentList "bot.py" -WindowStyle Hidden
```

**Linux/Mac:**
```bash
# Sử dụng nohup
nohup python bot.py > bot.log 2>&1 &

# Hoặc screen
screen -S asterdex-bot
python bot.py
# Nhấn Ctrl+A, D để detach
```

### 5.5. Chạy Bot Như Service (VPS)

**Tạo systemd service (Linux):**

```bash
sudo nano /etc/systemd/system/asterdex-bot.service
```

**Nội dung:**
```ini
[Unit]
Description=AsterDEX Trading Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/farmaster
ExecStart=/path/to/farmaster/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Khởi động service:**
```bash
sudo systemctl daemon-reload
sudo systemctl enable asterdex-bot
sudo systemctl start asterdex-bot
```

---

## 6. Monitoring

### 6.1. Xem Logs Real-time

```bash
# Application logs
tail -f logs/bot_*.log

# System logs (nếu dùng systemd)
sudo journalctl -u asterdex-bot -f
```

### 6.2. Kiểm Tra Balance

```bash
python scripts/check_balance.py
```

**Kết quả:**
```
💰 Account Balance: $XXX.XX USDT
📊 Open Positions: X
  - BTCUSDT: LONG, Entry: $XX,XXX, PnL: +X.XX%
  - ETHUSDT: SHORT, Entry: $X,XXX, PnL: -X.XX%
```

### 6.3. Kiểm Tra Positions

```bash
python -c "from trading.asterdex_client import AsterDEXClient; c = AsterDEXClient(); print(c.get_all_positions())"
```

### 6.4. Test Signal

```bash
python scripts/test_signal.py
```

**Kết quả:**
```
📡 Testing signals for all symbols...
BTCUSDT: LONG (Confluence: 7/10)
ETHUSDT: HOLD (Confluence: 4/10)
SOLUSDT: SHORT (Confluence: 8/10)
...
```

### 6.5. Telegram Monitoring

Nếu đã cấu hình Telegram, bạn sẽ nhận:
- 📊 Thông báo mở lệnh
- ✅ Thông báo đóng lệnh (TP/SL)
- ⚠️ Thông báo lỗi
- 📈 Báo cáo hàng ngày

---

## 7. Troubleshooting

### 7.1. Lỗi Thường Gặp

#### "API_KEY và API_SECRET bắt buộc"
```bash
# Kiểm tra .env
cat .env | grep API_KEY

# Đảm bảo có giá trị
API_KEY=your_key_here
API_SECRET=your_secret_here
```

#### "Model chưa được train"
```bash
# Train lại models
python ml/train_ensemble.py
```

#### "Margin insufficient"
```bash
# Giảm số symbols hoặc tăng balance
# Sửa .env:
SYMBOLS=BTCUSDT,ETHUSDT,SOLUSDT,BNBUSDT
```

#### "Symbol temporarily unavailable"
```bash
# Bỏ qua - bot sẽ tự động skip symbol này
# Hoặc xóa symbol khỏi danh sách
```

### 7.2. Bot Không Tạo Tín Hiệu

**Kiểm tra:**
```bash
# Test signal thủ công
python scripts/test_signal.py

# Nếu không có signal, giảm threshold
# Sửa .env:
LSTM_THRESHOLD=0.35
MIN_CONFLUENCE_SCORE=2
```

### 7.3. Win Rate Quá Thấp

```bash
# Tăng chất lượng tín hiệu
# Sửa .env:
LSTM_THRESHOLD=0.50
MIN_CONFLUENCE_SCORE=5
USE_TREND_FILTER=True
```

### 7.4. Lệnh Đóng Ngay Lập Tức

**Kiểm tra:**
```bash
# 1. SL_PCT phải = 0
cat .env | grep SL_PCT
# Phải thấy: SL_PCT=0

# 2. Kiểm tra bug fix
cat trading/signal_generator.py | grep -A 2 "Stop Loss"
# Phải thấy: if sl_pct > 0 and pnl_pct <= -sl_pct:
```

### 7.5. Emergency Stop

```bash
# Stop bot ngay lập tức
pkill -f bot.py

# Hoặc nếu dùng systemd
sudo systemctl stop asterdex-bot
```

### 7.6. Đóng Tất Cả Positions

```bash
python scripts/close_all.py
```

**Xác nhận:**
```
⚠️  Bạn có chắc muốn đóng TẤT CẢ positions?
Nhập 'yes' để xác nhận: yes
```

---

## 📋 Checklist Tổng Hợp

### Setup Lần Đầu
- [ ] Clone repository
- [ ] Cài đặt dependencies
- [ ] Tạo file .env
- [ ] Điền API keys
- [ ] Validate config
- [ ] Train models (LSTM + XGBoost)
- [ ] Chạy backtest
- [ ] Kết quả backtest tốt

### Trước Khi Chạy Bot
- [ ] TESTNET_MODE=true (lần đầu)
- [ ] Balance đủ ($150-200 cho 8 symbols)
- [ ] Telegram bot setup (tùy chọn)
- [ ] Biết cách xem logs
- [ ] Biết cách stop bot

### Sau Khi Chạy Bot
- [ ] Theo dõi logs 1 giờ đầu
- [ ] Kiểm tra positions được mở
- [ ] Kiểm tra lệnh không đóng ngay
- [ ] Theo dõi Telegram (nếu có)
- [ ] Đánh giá sau 24-48h

### Chuyển Mainnet
- [ ] Testnet chạy ổn định 24-48h
- [ ] Có ít nhất 1-2 trades thành công
- [ ] Win rate hợp lý
- [ ] Không có lỗi nghiêm trọng
- [ ] Sửa TESTNET_MODE=false
- [ ] Restart bot

---

## 🚀 Quick Commands Reference

```bash
# Setup
pip install -r requirements.txt
cp .env.volume_farming .env
python -c "from config import Config; Config.validate()"

# Train
python ml/train_ensemble.py

# Backtest
python scripts/test_volume_farming.py

# Run
python bot.py

# Monitor
tail -f logs/bot_*.log
python scripts/check_balance.py
python scripts/test_signal.py

# Emergency
pkill -f bot.py
python scripts/close_all.py
```

---

**Chúc bạn farming thành công! 🎉**

