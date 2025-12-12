# 🚀 Binance Quick Start Guide

## Thêm Binance vào bot trong 5 phút!

### Bước 1: Lấy Binance API Keys

1. Truy cập https://www.binance.com/en/my/settings/api-management
2. Tạo API key mới với quyền:
   - ✅ **Enable Futures**
   - ✅ **Enable Reading**
   - ❌ Không enable Withdrawals
3. Copy API Key và Secret Key

### Bước 2: Cấu hình .env

Mở file `.env` và thêm:

```bash
# Bật cả AsterDEX và Binance
EXCHANGES=asterdex,binance

# Binance credentials
BINANCE_API_KEY=paste_your_api_key_here
BINANCE_API_SECRET=paste_your_secret_here
BINANCE_TESTNET_MODE=false

# Binance symbols (top 10 coins recommended)
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT,XRPUSDT,ADAUSDT,AVAXUSDT,DOTUSDT,LINKUSDT,MATICUSDT

# Binance leverage
BINANCE_LEVERAGE=10
```

### Bước 3: Chạy bot

```bash
python bot.py
```

Xong! Bot giờ sẽ trade trên **cả AsterDEX và Binance** 🎉

## ⚙️ Nếu chỉ muốn dùng Binance

```bash
# Chỉ Binance
EXCHANGES=binance

# Comment out hoặc xóa AsterDEX config
# API_KEY=...
# API_SECRET=...

# Chỉ cần Binance config
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT,XRPUSDT
BINANCE_LEVERAGE=10
```

## 📊 Top Binance Symbols (theo thanh khoản)

### Conservative (Top 5)
```
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT,XRPUSDT
```

### Balanced (Top 10)
```
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT,XRPUSDT,ADAUSDT,AVAXUSDT,DOTUSDT,LINKUSDT,MATICUSDT
```

### Aggressive (Top 20)
```
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT,XRPUSDT,ADAUSDT,DOGEUSDT,AVAXUSDT,DOTUSDT,LINKUSDT,UNIUSDT,NEARUSDT,MATICUSDT,LTCUSDT,ATOMUSDT,FILUSDT,ARBUSDT,OPUSDT,SHIBUSDT,APTUSDT
```

## ⚠️ Important Notes

1. **Transfer USDT**: Nhớ transfer USDT từ Spot wallet → **Futures wallet** trên Binance
2. **Position Size**: Khuyến nghị dùng `POSITION_SIZE_USDT` cố định khi trade multi-exchange:
   ```bash
   POSITION_SIZE_USDT=10  # Mỗi lệnh = $10
   ```
3. **Leverage**: Binance hỗ trợ đến 125x nhưng khuyến nghị 5-20x
4. **Testnet**: Để test trước, set `BINANCE_TESTNET_MODE=true`

## 🎯 Ưu điểm Binance vs AsterDEX

| Feature | AsterDEX | Binance |
|---------|----------|---------|
| **Số coins** | 12 | 200+ |
| **Thanh khoản** | Trung bình | Rất cao |
| **Spread** | Cao hơn | Thấp hơn |
| **Leverage** | 1-125x | 1-125x |
| **Phí** | Thấp | Rất thấp |
| **Execution** | Nhanh | Rất nhanh |

## 📖 Đọc thêm

- [MULTI_EXCHANGE_GUIDE.md](MULTI_EXCHANGE_GUIDE.md) - Hướng dẫn chi tiết
- [.env.binance.example](.env.binance.example) - Config template đầy đủ

## 🐛 Troubleshooting

**"BINANCE_API_KEY not found"**
→ Kiểm tra đã thêm credentials vào `.env` chưa

**"Invalid symbol"**
→ Symbol không hỗ trợ futures trên Binance, dùng list symbols recommended ở trên

**"Insufficient balance"**
→ Transfer USDT vào Futures wallet hoặc giảm `POSITION_SIZE_USDT`

---

Happy trading! 🚀
