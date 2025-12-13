# ⚠️ VẤN ĐỀ ĐÃ TÌM RA!

## 🔍 Nguyên nhân

Bot đang dùng **API key CŨ** (`fRCloHf22a...`) chưa có đủ permissions.

API key MỚI từ ảnh của bạn: `dBJ6BqkVnColaGm2I9S3tQBETjrKzqzW2NawJIpdIKkGHCA8fHEF7zCiEeFrDWeh`

## ✅ GIẢI PHÁP - Cập nhật .env

### Trên máy local (Windows):

1. Mở file `.env`
2. Sửa lại:

```bash
EXCHANGES=binance

# API KEY MỚI
BINANCE_API_KEY=dBJ6BqkVnColaGm2I9S3tQBETjrKzqzW2NawJIpdIKkGHCA8fHEF7zCiEeFrDWeh
BINANCE_API_SECRET=<copy secret key từ Binance>
BINANCE_TESTNET_MODE=false

BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT,XRPUSDT,ADAUSDT,DOGEUSDT,AVAXUSDT,DOTUSDT,LINKUSDT,UNIUSDT,NEARUSDT,MATICUSDT,LTCUSDT,ATOMUSDT,FILUSDT,ARBUSDT,OPUSDT,SHIBUSDT,APTUSDT
BINANCE_LEVERAGE=10
```

3. Save file
4. Test lại:

```bash
python test_binance_connection.py
```

### Trên VPS:

```bash
# SSH vào VPS
ssh your_vps

# Vào thư mục bot
cd /root/FarmAster  # hoặc path của bạn

# Backup .env cũ
cp .env .env.backup

# Edit .env
nano .env

# Sửa:
EXCHANGES=binance
BINANCE_API_KEY=dBJ6BqkVnColaGm2I9S3tQBETjrKzqzW2NawJIpdIKkGHCA8fHEF7zCiEeFrDWeh
BINANCE_API_SECRET=<your_secret_key>
BINANCE_TESTNET_MODE=false

# Save: Ctrl+O, Enter, Ctrl+X

# Test
python3 test_binance_connection.py

# Nếu OK, restart bot
sudo systemctl restart asterdex-bot

# Check logs
sudo journalctl -u asterdex-bot -f
```

## 🎯 Kết quả mong đợi

Sau khi update API key mới, bạn sẽ thấy:

```
✅ USDT Balance: $110.31
✅ Available: $110.31
```

Thay vì:

```
❌ Balance: $0.00
```

---

## 📝 Lưu ý

1. **API Key mới đã có đủ permissions** (từ ảnh):
   - ✅ Cho phép đọc
   - ✅ Cho phép Giao dịch Futures

2. **IP đã được whitelist** (45.77.175.197)

3. **Balance đã có**: $110.31 USDT trong Futures wallet

Chỉ cần **update API key trong .env** là xong!
