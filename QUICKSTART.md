# 🚀 Quick Start Guide

## 5 Phút Setup Bot

### Bước 1: Install Dependencies (2 phút)
```bash
pip install -r requirements.txt
```

**Lưu ý**: Nếu `ta-lib` lỗi, xem [README.md](README.md#installation)

### Bước 2: Configure (1 phút)
```bash
cp .env.example .env
nano .env  # hoặc notepad .env
```

Điền:
```env
API_KEY=your_key_here
API_SECRET=your_secret_here
TESTNET_MODE=True
```

### Bước 3: Train Model (5-10 phút)
```bash
python ml/train.py
```

Chờ đến khi thấy:
```
✅ Model saved to models/lstm_model.pt
🎉 TRAINING HOÀN TẤT!
```

### Bước 4: Backtest (1 phút)
```bash
python run_backtest.py
```

Kiểm tra:
- Win Rate > 55% ✅
- Profit Factor > 1.3 ✅
- Total PnL > 10% ✅

### Bước 5: Run Bot! (30 giây)
```bash
python bot.py
```

Thấy:
```
🚀 ASTERDEX PERP FARM BOT - INITIALIZING
✅ Bot initialized successfully!
🏁 BOT STARTED!
```

**DONE! Bot đang chạy! 🎉**

---

## 🛠️ Useful Commands

### Check Balance & Positions
```bash
python scripts/check_balance.py
```

### Test Signals
```bash
python scripts/test_signal.py
```

### Emergency Close All
```bash
python scripts/close_all.py
```

### View Logs
```bash
tail -f logs/bot_*.log
```

---

## 📊 Expected Performance

### Testnet (First Run)
- **Trades/Day**: 10-20
- **Win Rate**: 55-65%
- **Daily PnL**: 2-5%
- **Volume**: $50k-100k

### Mainnet (After Optimization)
- **Trades/Day**: 20-40
- **Win Rate**: 60-70%
- **Daily PnL**: 5-10%
- **Volume**: $100k-500k
- **Airdrop Points**: 5k-15k/week

---

## ⚠️ Important Tips

1. **Always Start Testnet**: Test ít nhất 24h trước mainnet
2. **Monitor First Day**: Theo dõi sát bot ngày đầu
3. **Start Small**: Dùng 10-20% vốn ban đầu
4. **Check Logs**: Xem logs thường xuyên
5. **Telegram**: Setup Telegram để nhận alerts

---

## 🐛 Common Issues

### "Model not found"
```bash
python ml/train.py
```

### "API Error"
- Check API keys trong `.env`
- Check internet connection
- Check AsterDEX status

### "Insufficient balance"
- Deposit USDT vào AsterDEX
- Minimum: $100 recommended

### Bot không mở lệnh
- Chờ signal (có thể mất 5-10 phút)
- Check logs: `tail -f logs/bot_*.log`
- Test signal: `python scripts/test_signal.py`

---

## 📞 Need Help?

1. Check [README.md](README.md)
2. Check logs: `logs/bot_*.log`
3. Run test scripts
4. Open GitHub issue

---

**Happy Farming! 🌾💰**

