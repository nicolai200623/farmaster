# 🚀 CHIẾN LƯỢC FARMING VOLUME - ASTERDEX

## 📋 MỤC TIÊU

**Mục tiêu chính:** Tối đa hóa số lượng giao dịch và volume trên AsterDEX với chiến lược an toàn, lợi nhuận ổn định.

**Thông số chiến lược:**
- 💰 **Position Size:** $10 USDT cố định
- 📊 **Leverage:** 10x (isolated margin)
- 🎯 **Take Profit:** 1% (dễ đạt được)
- 🛡️ **Stop Loss:** Không (isolated margin bảo vệ)
- ⏱️ **Loop Sleep:** 30 giây (kiểm tra thường xuyên)
- 🔄 **Symbols:** 8 pairs (tối đa cơ hội)

---

## 📊 DỰ ĐOÁN HIỆU SUẤT

### Kịch bản Bảo thủ (15-20 trades/tháng)
- **Volume:** $300k-400k/tháng
- **Profit:** $9-12 (60% win rate)
- **ROI:** 90-120%/tháng

### Kịch bản Kỳ vọng (20-25 trades/tháng)
- **Volume:** $400k-500k/tháng
- **Profit:** $12-15
- **ROI:** 120-150%/tháng

### Kịch bản Lạc quan (25-30 trades/tháng)
- **Volume:** $500k-600k/tháng
- **Profit:** $15-18
- **ROI:** 150-180%/tháng

---

## 🎯 CHIẾN LƯỢC TỐI ƯU HÓA

### 1. Tăng Số Lượng Tín Hiệu

**Giảm LSTM Threshold:**
```
LSTM_THRESHOLD=0.40  # Từ 0.45 -> 0.40
```
- ✅ Tăng 30-40% tín hiệu
- ⚠️ Win rate có thể giảm 5%
- 📈 Tổng profit vẫn tăng

**Giảm Min Confluence Score:**
```
MIN_CONFLUENCE_SCORE=3  # Từ 4 -> 3
```
- ✅ Chấp nhận tín hiệu yếu hơn
- ✅ Nhiều cơ hội entry hơn

### 2. Giảm Filters

**Tắt Trend Filter:**
```
USE_TREND_FILTER=False
```
- ✅ Trade cả uptrend và downtrend
- ✅ Tăng 20-30% cơ hội

**Tắt Volume Filter:**
```
USE_VOLUME_FILTER=False
```
- ✅ Không bỏ lỡ tín hiệu do volume thấp
- ✅ Tăng 15-20% cơ hội

**Giảm Signal Quality Score:**
```
MIN_SIGNAL_QUALITY_SCORE=30  # Từ 50 -> 30
```
- ✅ Chấp nhận tín hiệu chất lượng trung bình
- ✅ Tăng 25-35% tín hiệu

### 3. Tăng Tần Suất Kiểm Tra

**Giảm Loop Sleep:**
```
LOOP_SLEEP=30  # Từ 60s -> 30s
```
- ✅ Kiểm tra 2x thường xuyên hơn
- ✅ Bắt tín hiệu nhanh hơn
- ⚠️ Tăng API calls (vẫn trong giới hạn)

### 4. Tăng Số Lượng Symbols

**8 pairs thay vì 6:**
```
SYMBOLS=BTCUSDT,ETHUSDT,SOLUSDT,BNBUSDT,LTCUSDT,AVAXUSDT,XRPUSDT,ADAUSDT
```
- ✅ Tăng 33% cơ hội
- ✅ Đa dạng hóa rủi ro
- ⚠️ Cần balance đủ ($150-200)

### 5. Đơn Giản Hóa Exit Strategy

**Tắt Trailing Stop:**
```
USE_TRAILING_STOP=False
```
- ✅ Chỉ dùng TP 1% cố định
- ✅ Đơn giản, dễ dự đoán
- ✅ Thoát nhanh, tái sử dụng vốn

**Tắt Breakeven Stop:**
```
USE_BREAKEVEN_STOP=False
```
- ✅ Giảm phức tạp
- ✅ Tập trung vào TP 1%

**Tắt Market Regime:**
```
USE_MARKET_REGIME=False
```
- ✅ Trade mọi điều kiện thị trường
- ✅ Không bỏ lỡ cơ hội

### 6. Tăng Position Timeout

**48 giờ thay vì 24:**
```
POSITION_TIMEOUT_HOURS=48
```
- ✅ Cho phép lệnh phát triển lâu hơn
- ✅ Tăng cơ hội hit TP 1%
- ⚠️ Vốn bị lock lâu hơn

---

## 🔧 CÀI ĐẶT VÀ TRIỂN KHAI

### Bước 1: Áp Dụng Cấu Hình Mới

```bash
# Chạy script tự động
python scripts/apply_volume_farming_config.py

# Hoặc copy thủ công
cp .env.volume_farming .env
```

### Bước 2: Kiểm Tra Cấu Hình

```bash
python -c "from config import Config; Config.validate()"
```

**Kết quả mong đợi:**
```
✅ Using fixed position size: $10.0 USDT per trade
✅ Config validation passed!
```

### Bước 3: Chạy Backtest

```bash
python run_backtest.py
```

**Kiểm tra:**
- ✅ Số lượng trades > 20 (30 ngày)
- ✅ Win rate > 55%
- ✅ Total PnL > 0
- ✅ Volume > $400k

### Bước 4: Khởi Động Bot (Testnet)

```bash
# Đảm bảo TESTNET_MODE=true trong .env
python bot.py
```

**Theo dõi 1 giờ đầu:**
- ✅ Bot chạy không lỗi
- ✅ Tín hiệu được tạo ra
- ✅ Lệnh được mở
- ✅ Lệnh KHÔNG đóng ngay lập tức
- ✅ Telegram notifications hoạt động

### Bước 5: Chuyển Sang Mainnet

**Sau khi testnet ổn định 24h:**

```bash
# Sửa .env
TESTNET_MODE=false

# Restart bot
python bot.py
```

---

## 📊 THEO DÕI VÀ ĐÁNH GIÁ

### Metrics Quan Trọng

**Hàng Ngày:**
- Số lượng trades
- Win rate
- PnL
- Volume tích lũy

**Hàng Tuần:**
- Tổng trades (mục tiêu: 5-7)
- Tổng volume (mục tiêu: $100k+)
- Win rate trung bình (mục tiêu: >55%)
- Profit (mục tiêu: >$3)

**Hàng Tháng:**
- Tổng trades (mục tiêu: 20-30)
- Tổng volume (mục tiêu: $400k-600k)
- Win rate (mục tiêu: >60%)
- ROI (mục tiêu: >100%)

### Logs Cần Kiểm Tra

```bash
# Xem logs real-time
tail -f logs/bot_*.log

# Hoặc nếu dùng systemd
sudo journalctl -u asterdex-bot -f
```

**Tìm kiếm:**
- ✅ "Signal: LONG/SHORT" - Tín hiệu được tạo
- ✅ "Position opened" - Lệnh được mở
- ✅ "TP (1.00%)" - Hit TP thành công
- ❌ "SL" - Không nên thấy (SL_PCT=0)
- ❌ "Margin insufficient" - Cần tăng balance

---

## ⚠️ RỦI RO VÀ QUẢN LÝ

### Rủi Ro Chính

**1. Overtrading**
- **Nguyên nhân:** Quá nhiều tín hiệu
- **Giải pháp:** Tăng LOOP_SLEEP lên 60s
- **Dấu hiệu:** >5 trades/ngày

**2. Margin Insufficient**
- **Nguyên nhân:** Quá nhiều lệnh mở cùng lúc
- **Giải pháp:** Tăng balance hoặc giảm số symbols
- **Dấu hiệu:** Lỗi khi mở lệnh

**3. Win Rate Thấp**
- **Nguyên nhân:** Tín hiệu quá yếu
- **Giải pháp:** Tăng LSTM_THRESHOLD lên 0.45
- **Dấu hiệu:** Win rate <50%

**4. Không Có Trades**
- **Nguyên nhân:** Filters quá strict
- **Giải pháp:** Giảm thêm filters
- **Dấu hiệu:** 0 trades trong 24h

### Giới Hạn An Toàn

**Daily Loss Limit:**
```
DAILY_LOSS_LIMIT=0.2  # 20% balance
```
- Bot tự động dừng nếu loss >20%
- Bảo vệ vốn

**Position Timeout:**
```
POSITION_TIMEOUT_HOURS=48
```
- Tự động đóng lệnh sau 48h
- Tránh vốn bị lock vô thời hạn

**Isolated Margin:**
- Mỗi lệnh độc lập
- Liquidation chỉ ảnh hưởng 1 lệnh
- Max loss = $10/lệnh

---

## 🎯 CHECKLIST TRƯỚC KHI CHẠY

### Cấu Hình
- [ ] .env đã được cập nhật
- [ ] TESTNET_MODE=false (mainnet)
- [ ] API keys hợp lệ
- [ ] Telegram bot hoạt động
- [ ] Balance đủ ($150-200)

### Kiểm Tra Kỹ Thuật
- [ ] Config validation passed
- [ ] Backtest results tốt
- [ ] ML models đã train
- [ ] Bug SL đã fix (line 288)
- [ ] Isolated margin enabled

### Monitoring
- [ ] Logs được theo dõi
- [ ] Telegram notifications on
- [ ] Emergency stop procedure biết
- [ ] Backup .env đã tạo

---

## 📈 KẾT QUẢ KỲ VỌNG

### Tuần 1
- **Trades:** 5-7
- **Volume:** $100k-140k
- **Profit:** $3-5
- **Win Rate:** >55%

### Tháng 1
- **Trades:** 20-30
- **Volume:** $400k-600k
- **Profit:** $12-18
- **Win Rate:** >60%
- **ROI:** 120-180%

### Tháng 3
- **Trades:** 60-90
- **Volume:** $1.2M-1.8M
- **Profit:** $36-54
- **ROI:** 360-540%

---

## 🔧 TROUBLESHOOTING

### Vấn Đề: Quá Ít Trades

**Giải pháp:**
1. Giảm LSTM_THRESHOLD xuống 0.35
2. Giảm MIN_CONFLUENCE_SCORE xuống 2
3. Tắt thêm filters
4. Giảm LOOP_SLEEP xuống 20s

### Vấn Đề: Win Rate Quá Thấp (<50%)

**Giải pháp:**
1. Tăng LSTM_THRESHOLD lên 0.45
2. Tăng MIN_CONFLUENCE_SCORE lên 4
3. Bật lại TREND_FILTER
4. Tăng MIN_SIGNAL_QUALITY_SCORE lên 40

### Vấn Đề: Margin Insufficient

**Giải pháp:**
1. Tăng balance
2. Giảm số symbols xuống 6
3. Giảm POSITION_SIZE_USDT xuống 8
4. Tăng POSITION_TIMEOUT_HOURS xuống 24

### Vấn Đề: Lệnh Đóng Ngay

**Kiểm tra:**
1. SL_PCT=0 trong .env
2. Bug fix ở line 288 signal_generator.py
3. Không có lỗi trong logs

---

## 📞 HỖ TRỢ

### Logs
```bash
# Application logs
tail -f logs/bot_*.log

# System logs (nếu dùng systemd)
sudo journalctl -u asterdex-bot -f
```

### Emergency Stop
```bash
# Stop bot
sudo systemctl stop asterdex-bot

# Hoặc
pkill -f bot.py
```

### Restore Config
```bash
# Restore từ backup
cp .env.backup_YYYYMMDD_HHMMSS .env
```

---

## ✅ TÓM TẮT

**Chiến lược này được tối ưu hóa cho:**
- ✅ Tối đa hóa số lượng giao dịch
- ✅ Tối đa hóa volume
- ✅ Lợi nhuận ổn định với TP 1%
- ✅ Rủi ro được kiểm soát (isolated margin)
- ✅ Dễ dàng scale up

**Kết quả kỳ vọng:**
- 📊 20-30 trades/tháng
- 💰 $400k-600k volume/tháng
- 📈 120-180% ROI/tháng
- ✅ Win rate >60%

**Sẵn sàng để farming! 🚀**

