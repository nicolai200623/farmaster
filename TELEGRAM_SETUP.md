# 📱 Hướng dẫn khắc phục lỗi Bot

## ⚠️ Nếu bot bị crash ngay khi start

Bot có thể crash vì **thiếu dependencies** (đặc biệt là `python-binance`).

### Kiểm tra và cài đặt dependencies:

```bash
cd /home/farmaster2/farmaster
source venv/bin/activate  # nếu dùng virtual environment
python3 check_dependencies.py
```

Script sẽ:
- ✅ Kiểm tra tất cả packages cần thiết
- ❌ Liệt kê packages bị thiếu
- 🔧 Tự động cài đặt nếu bạn chọn 'y'

**Hoặc cài đặt thủ công:**
```bash
pip install -r requirements-vps.txt
```

Sau khi cài đặt xong, restart bot:
```bash
sudo systemctl restart asterdex-bot2
```

---

## 📱 Cấu hình Telegram Notifications

### Vấn đề hiện tại
Bot đã chạy được nhưng không gửi thông báo qua Telegram vì chưa cấu hình `TELEGRAM_TOKEN` và `TELEGRAM_CHAT_ID`.

## Cách khắc phục (5 bước đơn giản)

### Bước 1: Tạo Telegram Bot
1. Mở Telegram, tìm kiếm: **@BotFather**
2. Gửi lệnh: `/newbot`
3. Đặt tên cho bot (ví dụ: `FarmAster Trading Bot`)
4. Đặt username (ví dụ: `farmaster_bot`)
5. BotFather sẽ trả về **Bot Token** (dạng: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)
6. **LUU LẠI** token này

### Bước 2: Lấy Chat ID
1. Tìm kiếm bot: **@userinfobot** trên Telegram
2. Gửi lệnh: `/start`
3. Bot sẽ trả về **Chat ID** của bạn (dạng: `123456789` hoặc `-123456789`)
4. **LUU LẠI** Chat ID này

### Bước 3: Start bot của bạn
1. Tìm bot bạn vừa tạo ở Bước 1
2. Click **START** hoặc gửi `/start`
3. Bot bây giờ có thể gửi tin nhắn cho bạn

### Bước 4: Cập nhật file .env trên VPS

Chạy lệnh sau trên VPS:

```bash
cd /home/farmaster2/farmaster
nano .env
```

Tìm và sửa 2 dòng sau (hoặc thêm vào nếu chưa có):

```bash
TELEGRAM_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz  # Thay bằng token thực
TELEGRAM_CHAT_ID=123456789  # Thay bằng chat ID thực
```

Lưu file:
- Nhấn `Ctrl + O` (Save)
- Nhấn `Enter` (Confirm)
- Nhấn `Ctrl + X` (Exit)

### Bước 5: Restart bot

```bash
sudo systemctl restart asterdex-bot2
```

## Kiểm tra cấu hình

Chạy script test (tùy chọn):

```bash
cd /home/farmaster2/farmaster
source venv/bin/activate  # Activate virtual environment nếu có
python test_telegram.py
```

Script sẽ:
- ✅ Kiểm tra file .env
- ✅ Kiểm tra TELEGRAM_TOKEN
- ✅ Kiểm tra TELEGRAM_CHAT_ID
- ✅ Gửi tin nhắn test

## Kết quả sau khi cấu hình

Bot sẽ gửi thông báo Telegram khi:
- ✅ **Bot khởi động**: `🏁 BOT STARTED!`
- ✅ **Mở vị thế**: `💰 OPEN LONG/SHORT {symbol}`
- ✅ **Đóng vị thế**: `💰 CLOSE {side} {symbol} | PnL: X%`
- ✅ **Cảnh báo**: Lỗi, daily loss limit, v.v.
- ✅ **Daily report**: Thống kê hàng ngày

## Lưu ý quan trọng

⚠️ **Bảo mật Bot Token:**
- KHÔNG share bot token với ai
- KHÔNG commit file .env lên Git
- Token có quyền gửi tin nhắn thay bạn

⚠️ **Nếu vẫn không nhận được thông báo:**
1. Kiểm tra bot đã START chưa
2. Kiểm tra Chat ID có đúng không (dùng @userinfobot)
3. Kiểm tra token có đúng không
4. Check logs: `sudo journalctl -u asterdex-bot2 -f`

## Ví dụ cấu hình hoàn chỉnh

```bash
# .env file
TELEGRAM_TOKEN=6234567890:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw
TELEGRAM_CHAT_ID=987654321

# ... các config khác ...
```

---

**Sau khi cấu hình xong, bạn sẽ nhận được tin nhắn test từ bot! 🎉**
