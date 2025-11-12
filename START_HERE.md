# 🚀 BẮT ĐẦU TẠI ĐÂY

## 👋 Chào mừng đến với FarmAster!

Bot trading tự động cho AsterDEX Perpetual Futures với chiến lược volume farming.

---

## 📚 BẠN NÊN ĐỌC GÌ?

### 🆕 Người mới bắt đầu (chưa từng setup)

**Đọc theo thứ tự:**

1. **[COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)** ⭐⭐⭐
   - Hướng dẫn đầy đủ từ A-Z
   - Setup → Train → Backtest → Run Bot
   - Tất cả lệnh cần thiết
   - **ĐỌC FILE NÀY TRƯỚC!**

2. **[INSTALL.md](INSTALL.md)**
   - Chi tiết cài đặt dependencies
   - Hướng dẫn cho Windows/Linux/Mac

3. **[QUICK_START_VOLUME_FARMING.md](QUICK_START_VOLUME_FARMING.md)**
   - Quick start 3 bước
   - Sau khi đã setup xong

---

### 🔧 Đã setup, muốn chạy volume farming

**Đọc theo thứ tự:**

1. **[QUICK_START_VOLUME_FARMING.md](QUICK_START_VOLUME_FARMING.md)** ⭐⭐⭐
   - 3 bước nhanh
   - Áp dụng config → Test → Run

2. **[VOLUME_FARMING_STRATEGY.md](VOLUME_FARMING_STRATEGY.md)**
   - Giải thích chiến lược
   - Tối ưu hóa chi tiết
   - Monitoring & troubleshooting

3. **[CHEAT_SHEET.md](CHEAT_SHEET.md)**
   - Tra cứu lệnh nhanh
   - Troubleshooting

---

### 💻 Đang chạy bot, cần tra cứu lệnh

**Đọc:**

1. **[CHEAT_SHEET.md](CHEAT_SHEET.md)** ⭐⭐⭐
   - Tất cả lệnh quan trọng
   - Troubleshooting nhanh
   - Tips & tricks

2. **[COMMANDS.md](COMMANDS.md)**
   - Lệnh chi tiết hơn

---

### 🐛 Gặp lỗi, cần fix

**Đọc:**

1. **[CHEAT_SHEET.md](CHEAT_SHEET.md)** - Section "Troubleshooting"
2. **[COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)** - Section "Troubleshooting"
3. **[docs/FAQ.md](docs/FAQ.md)** - 50+ câu hỏi thường gặp

---

## ⚡ QUICK START (3 BƯỚC)

Nếu bạn đã setup và muốn chạy ngay:

```bash
# Bước 1: Áp dụng config volume farming
python scripts/apply_volume_farming_config.py

# Bước 2: Test backtest
python scripts/test_volume_farming.py

# Bước 3: Chạy bot (testnet trước)
python bot.py
```

**Chi tiết:** Xem [QUICK_START_VOLUME_FARMING.md](QUICK_START_VOLUME_FARMING.md)

---

## 📋 CHECKLIST NHANH

### Lần đầu setup
- [ ] Đọc [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)
- [ ] Cài đặt dependencies
- [ ] Tạo file .env
- [ ] Train models
- [ ] Chạy backtest
- [ ] Chạy bot testnet

### Chạy volume farming
- [ ] Đọc [QUICK_START_VOLUME_FARMING.md](QUICK_START_VOLUME_FARMING.md)
- [ ] Áp dụng config: `python scripts/apply_volume_farming_config.py`
- [ ] Test backtest: `python scripts/test_volume_farming.py`
- [ ] Chạy bot: `python bot.py`

### Hàng ngày
- [ ] Xem logs: `tail -f logs/bot_*.log`
- [ ] Check balance: `python scripts/check_balance.py`
- [ ] Kiểm tra Telegram notifications

---

## 📁 CẤU TRÚC TÀI LIỆU

```
📚 Tài Liệu Chính
├── START_HERE.md                    ← BẠN ĐANG Ở ĐÂY
├── COMPLETE_GUIDE.md                ⭐ Hướng dẫn đầy đủ A-Z
├── CHEAT_SHEET.md                   ⭐ Tra cứu lệnh nhanh
├── QUICK_START_VOLUME_FARMING.md    ⭐ Quick start 3 bước
└── INDEX.md                         📑 Index tất cả tài liệu

🎯 Volume Farming
├── VOLUME_FARMING_STRATEGY.md       Chiến lược chi tiết
├── VOLUME_FARMING_DEPLOYMENT.md     Deployment guide
├── .env.volume_farming              Cấu hình tối ưu
└── scripts/
    ├── apply_volume_farming_config.py
    └── test_volume_farming.py

📖 Tài Liệu Khác
├── README.md                        Tổng quan dự án
├── INSTALL.md                       Hướng dẫn cài đặt
├── COMMANDS.md                      Tất cả lệnh
└── docs/                            Tài liệu chi tiết
    ├── STRATEGY.md
    ├── API.md
    └── FAQ.md
```

---

## 🎯 MỤC TIÊU CỦA BẠN LÀ GÌ?

### 🆕 "Tôi muốn setup bot lần đầu"
→ Đọc **[COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)**

### 💰 "Tôi muốn farm volume trên AsterDEX"
→ Đọc **[QUICK_START_VOLUME_FARMING.md](QUICK_START_VOLUME_FARMING.md)**

### 📊 "Tôi muốn hiểu chiến lược volume farming"
→ Đọc **[VOLUME_FARMING_STRATEGY.md](VOLUME_FARMING_STRATEGY.md)**

### 🔧 "Tôi cần tra cứu lệnh nhanh"
→ Đọc **[CHEAT_SHEET.md](CHEAT_SHEET.md)**

### 🐛 "Bot bị lỗi, cần fix"
→ Đọc **[CHEAT_SHEET.md](CHEAT_SHEET.md)** section Troubleshooting

### 📚 "Tôi muốn xem tất cả tài liệu"
→ Đọc **[INDEX.md](INDEX.md)**

---

## 💡 TIPS

1. **Bắt đầu với testnet** - Luôn test trên testnet trước khi chạy mainnet
2. **Đọc COMPLETE_GUIDE.md** - Nếu bạn mới bắt đầu
3. **Bookmark CHEAT_SHEET.md** - Để tra cứu nhanh
4. **Theo dõi logs** - Đặc biệt trong 1 giờ đầu
5. **Kiên nhẫn** - Cần 1-2 tuần để đánh giá hiệu suất

---

## 🚀 SẴN SÀNG BẮT ĐẦU?

### Người mới:
```bash
# Đọc hướng dẫn đầy đủ
cat COMPLETE_GUIDE.md

# Hoặc mở trong browser
start COMPLETE_GUIDE.md  # Windows
open COMPLETE_GUIDE.md   # Mac
xdg-open COMPLETE_GUIDE.md  # Linux
```

### Đã setup:
```bash
# Quick start volume farming
cat QUICK_START_VOLUME_FARMING.md

# Hoặc chạy luôn
python scripts/apply_volume_farming_config.py
```

---

## 📞 HỖ TRỢ

### Tài liệu
- **[COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)** - Hướng dẫn đầy đủ
- **[CHEAT_SHEET.md](CHEAT_SHEET.md)** - Troubleshooting
- **[docs/FAQ.md](docs/FAQ.md)** - 50+ câu hỏi

### Logs
```bash
# Xem logs
tail -f logs/bot_*.log

# Tìm lỗi
grep -i error logs/bot_*.log
```

### Emergency
```bash
# Stop bot
pkill -f bot.py

# Đóng tất cả positions
python scripts/close_all.py
```

---

**Chúc bạn thành công! 🎉**

**Bắt đầu với:** [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) (nếu mới) hoặc [QUICK_START_VOLUME_FARMING.md](QUICK_START_VOLUME_FARMING.md) (nếu đã setup)

