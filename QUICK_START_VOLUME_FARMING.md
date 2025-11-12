# 🚀 QUICK START - VOLUME FARMING

## 📋 Tóm Tắt Nhanh

**Chiến lược:** Farm volume với 1% TP, 10x leverage, $10/trade, không SL

**Kết quả kỳ vọng:**
- 20-30 trades/tháng
- $400k-600k volume/tháng  
- 120-180% ROI/tháng
- Win rate >60%

---

## ⚡ 3 BƯỚC NHANH

### Bước 1: Áp Dụng Cấu Hình (30 giây)

```bash
# Tự động (khuyến nghị)
python scripts/apply_volume_farming_config.py

# Hoặc thủ công
cp .env.volume_farming .env
```

### Bước 2: Test Backtest (2 phút)

```bash
python scripts/test_volume_farming.py
```

**Kiểm tra:**
- ✅ Trades > 15
- ✅ Win rate > 55%
- ✅ Profit factor > 1.3

### Bước 3: Chạy Bot (1 phút)

```bash
# Testnet trước
python bot.py

# Sau 24h ổn định -> Mainnet
# Sửa .env: TESTNET_MODE=false
python bot.py
```

---

## 📊 So Sánh Cấu Hình

| Tham số | Cũ | Mới | Lý do |
|---------|-----|-----|-------|
| **SYMBOLS** | 6 | 8 | Tăng cơ hội |
| **LOOP_SLEEP** | 60s | 30s | Kiểm tra thường xuyên |
| **LSTM_THRESHOLD** | 0.45 | 0.40 | Nhiều tín hiệu hơn |
| **MIN_CONFLUENCE** | 4 | 3 | Dễ entry hơn |
| **TREND_FILTER** | ON | OFF | Ít filter |
| **VOLUME_FILTER** | ON | OFF | Ít filter |
| **TRAILING_STOP** | ON | OFF | Chỉ dùng TP 1% |
| **MARKET_REGIME** | ON | OFF | Trade mọi lúc |

**Kết quả:** +50-80% trades, +50-80% volume

---

## 🎯 Các Thay Đổi Chính

### 1. Tăng Số Lượng Tín Hiệu
- ✅ LSTM_THRESHOLD: 0.45 → 0.40
- ✅ MIN_CONFLUENCE_SCORE: 4 → 3
- ✅ Tắt TREND_FILTER
- ✅ Tắt VOLUME_FILTER
- ✅ Giảm MIN_SIGNAL_QUALITY_SCORE: 50 → 30

### 2. Tăng Tần Suất Kiểm Tra
- ✅ LOOP_SLEEP: 60s → 30s
- ✅ Kiểm tra 2x thường xuyên hơn

### 3. Tăng Số Symbols
- ✅ 6 pairs → 8 pairs
- ✅ Thêm BNBUSDT, ADAUSDT

### 4. Đơn Giản Hóa Exit
- ✅ Tắt TRAILING_STOP
- ✅ Tắt BREAKEVEN_STOP
- ✅ Tắt MARKET_REGIME
- ✅ Chỉ dùng TP 1% cố định

### 5. Tăng Position Timeout
- ✅ 24h → 48h
- ✅ Cho lệnh phát triển lâu hơn

---

## ✅ Checklist Trước Khi Chạy

### Cấu Hình
- [ ] File .env đã cập nhật
- [ ] LEVERAGE=10
- [ ] POSITION_SIZE_USDT=10
- [ ] TP_PCT=1.0
- [ ] SL_PCT=0
- [ ] SYMBOLS có 8 pairs

### Kiểm Tra
- [ ] `python -c "from config import Config; Config.validate()"` → OK
- [ ] Backtest results tốt (>15 trades, >55% win rate)
- [ ] ML models đã train
- [ ] Balance đủ ($150-200)

### Monitoring
- [ ] Telegram bot hoạt động
- [ ] Biết cách xem logs
- [ ] Biết cách stop bot khẩn cấp

---

## 📊 Kết Quả Mong Đợi

### Tuần 1
- 5-7 trades
- $100k-140k volume
- $3-5 profit

### Tháng 1
- 20-30 trades
- $400k-600k volume
- $12-18 profit
- 120-180% ROI

---

## 🔧 Troubleshooting Nhanh

### Quá Ít Trades (<10/tháng)
```bash
# Giảm threshold
LSTM_THRESHOLD=0.35
MIN_CONFLUENCE_SCORE=2
```

### Win Rate Thấp (<50%)
```bash
# Tăng threshold
LSTM_THRESHOLD=0.45
USE_TREND_FILTER=True
```

### Margin Insufficient
```bash
# Giảm symbols hoặc tăng balance
SYMBOLS=BTCUSDT,ETHUSDT,SOLUSDT,BNBUSDT
```

### Lệnh Đóng Ngay
```bash
# Kiểm tra
SL_PCT=0  # Phải = 0
# Kiểm tra bug fix ở signal_generator.py line 288
```

---

## 📞 Commands Hữu Ích

```bash
# Kiểm tra config
python -c "from config import Config; Config.validate()"

# Chạy backtest
python scripts/test_volume_farming.py

# Xem logs
tail -f logs/bot_*.log

# Stop bot
pkill -f bot.py

# Restore config
cp .env.backup_* .env
```

---

## 🎯 Khi Nào Chạy Mainnet?

**Sau khi testnet:**
- ✅ Chạy ổn định 24h không lỗi
- ✅ Có ít nhất 1-2 trades thành công
- ✅ Lệnh KHÔNG đóng ngay lập tức
- ✅ Win rate hợp lý
- ✅ Telegram notifications hoạt động

**Chuyển sang mainnet:**
```bash
# Sửa .env
TESTNET_MODE=false

# Restart
python bot.py
```

---

## 💡 Tips

1. **Bắt đầu với testnet** - Test 24-48h trước
2. **Theo dõi logs** - Đặc biệt 1 giờ đầu
3. **Kiên nhẫn** - Cần 1-2 tuần để đánh giá
4. **Điều chỉnh dần** - Không thay đổi quá nhiều cùng lúc
5. **Backup config** - Trước mỗi thay đổi

---

## 🚀 Sẵn Sàng!

Nếu đã hoàn thành checklist, bạn sẵn sàng để bắt đầu farming volume!

**Chúc may mắn! 🎉**

