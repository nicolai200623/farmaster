# ❓ Frequently Asked Questions

## General

### Q: Bot này có miễn phí không?
**A:** Có, hoàn toàn miễn phí và open source (MIT License). Bạn chỉ cần trả phí trading cho AsterDEX.

### Q: Tôi cần bao nhiêu vốn để bắt đầu?
**A:** 
- **Minimum:** $100 (testnet)
- **Recommended:** $500-1000 (mainnet)
- **Optimal:** $2000+ (để đa dạng hóa)

### Q: Bot có tự động kiếm tiền không?
**A:** Không có gì đảm bảo 100%. Bot dựa trên ML và technical analysis, có thể có lãi hoặc lỗ. Luôn test kỹ trên testnet trước.

### Q: Tôi có cần biết code không?
**A:** Không bắt buộc. Chỉ cần:
1. Cài Python
2. Copy .env
3. Chạy commands trong README

### Q: Bot có chạy 24/7 không?
**A:** Có, nhưng bạn cần:
- VPS hoặc máy tính luôn bật
- Internet ổn định
- Monitor thường xuyên

## Technical

### Q: LSTM là gì?
**A:** Long Short-Term Memory - một loại neural network tốt cho time series prediction. Bot dùng nó để dự đoán giá.

### Q: Tại sao cần train model?
**A:** Model cần học patterns từ historical data. Mỗi market khác nhau, nên cần train riêng.

### Q: Train mất bao lâu?
**A:** 
- CPU: 10-15 phút
- GPU: 2-5 phút

### Q: Có cần GPU không?
**A:** Không bắt buộc. CPU đủ cho model size này.

### Q: Tôi có thể thay đổi parameters không?
**A:** Có, edit file `.env`:
```env
LEVERAGE=10        # Tăng leverage
SIZE_PCT=0.2       # Tăng position size
TP_PCT=0.03        # Tăng take profit
```

### Q: Làm sao biết model tốt?
**A:** Chạy backtest:
```bash
python run_backtest.py
```
Xem:
- Win Rate > 55% ✅
- Profit Factor > 1.3 ✅
- Max Drawdown < 15% ✅

## Trading

### Q: Bot mở bao nhiêu lệnh/ngày?
**A:** Trung bình 20-40 lệnh, tùy volatility.

### Q: Tại sao bot không mở lệnh?
**A:** Có thể:
1. Không có signal (cần 2/3 indicators)
2. Đã có position
3. Hit daily loss limit
4. Balance không đủ

Check logs: `tail -f logs/bot_*.log`

### Q: Bot có tự động đóng lệnh lỗ không?
**A:** Có, khi hit Stop Loss (default 1%).

### Q: Tôi có thể trade manual cùng lúc không?
**A:** Không nên. Bot quản lý positions tự động, manual trading có thể conflict.

### Q: Leverage bao nhiêu là an toàn?
**A:** 
- **Conservative:** 3-5x
- **Moderate:** 5-10x
- **Aggressive:** 10-20x
- **Degen:** 20x+ (không khuyến khích)

### Q: Tại sao dùng Isolated Margin?
**A:** An toàn hơn Cross Margin. Nếu 1 position bị liquidated, không ảnh hưởng positions khác.

## Airdrop

### Q: Bot có tối ưu cho airdrop không?
**A:** Có:
- Focus BTC/ETH (2x points Stage 3)
- High frequency trading
- Volume tracking
- Auto team join (nếu có API)

### Q: Tôi có thể farm bao nhiêu points/ngày?
**A:** 
- **Conservative:** 500-1000 points
- **Moderate:** 1000-3000 points
- **Aggressive:** 3000-5000+ points

Depends on volume.

### Q: Volume tính như thế nào?
**A:** 
```
Volume = Quantity × Price × Leverage

Example:
0.01 BTC × $50,000 × 5x = $2,500
```

### Q: Có cần join team không?
**A:** Có, để nhận team bonus. Bot có thể auto join nếu AsterDEX có API.

## Troubleshooting

### Q: "Model not found" error?
**A:** 
```bash
python ml/train.py
```

### Q: "API Error" khi chạy bot?
**A:** Check:
1. API keys đúng trong `.env`
2. Internet connection
3. AsterDEX status
4. API permissions (futures trading enabled)

### Q: Bot bị crash?
**A:** 
1. Check logs: `logs/bot_*.log`
2. Check balance
3. Restart: `python bot.py`

### Q: Telegram không nhận notification?
**A:** 
1. Check `TELEGRAM_TOKEN` và `TELEGRAM_CHAT_ID`
2. Start chat với bot trước
3. Test: `python scripts/test_signal.py`

### Q: Win rate thấp (<50%)?
**A:** 
1. Retrain model: `python ml/train.py`
2. Adjust parameters trong `.env`
3. Check market conditions (sideways market khó trade)
4. Increase signal threshold

### Q: Bot mở quá nhiều lệnh lỗ?
**A:** 
1. Giảm `SIZE_PCT` (e.g., 0.05 = 5%)
2. Tăng `MIN_SIGNAL_SCORE` (cần 3/3 signals)
3. Giảm `LEVERAGE`
4. Tăng `LSTM_THRESHOLD` (e.g., 0.7)

## Safety & Security

### Q: API keys có an toàn không?
**A:** 
- Lưu trong `.env` (không commit lên Git)
- Enable IP whitelist trên AsterDEX
- Chỉ enable Futures trading permission
- Disable Withdrawal permission

### Q: Bot có thể rút tiền không?
**A:** KHÔNG. Bot chỉ trade, không có quyền withdraw.

### Q: Tôi có thể mất hết tiền không?
**A:** 
- Có thể nếu:
  - Leverage quá cao
  - Không set stop loss
  - Market crash đột ngột
- Giảm thiểu:
  - Dùng Isolated Margin
  - Set Daily Loss Limit
  - Start với vốn nhỏ
  - Monitor thường xuyên

### Q: Có nên để bot chạy không giám sát?
**A:** KHÔNG. Luôn:
- Check logs hàng ngày
- Monitor Telegram
- Review performance weekly
- Adjust parameters khi cần

## Performance

### Q: Backtest 18% PnL, nhưng live chỉ 5%?
**A:** Bình thường. Backtest không tính:
- Slippage
- Fees
- Network latency
- Market impact

Live performance thường thấp hơn 30-50%.

### Q: Làm sao tăng profit?
**A:** 
1. **Optimize parameters:** Backtest nhiều configs
2. **Retrain model:** Weekly với fresh data
3. **Increase capital:** Bigger positions
4. **Better timing:** Reduce loop sleep (10s)
5. **Multiple symbols:** Diversify

### Q: Làm sao giảm risk?
**A:** 
1. **Lower leverage:** 3x thay vì 5x
2. **Smaller positions:** 5% thay vì 10%
3. **Tighter SL:** 0.5% thay vì 1%
4. **Daily limit:** 10% thay vì 20%

## Advanced

### Q: Tôi có thể thêm symbols khác không?
**A:** Có, edit `.env`:
```env
SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT
```

Và update `COIN_MAP` trong `utils/data_fetcher.py`.

### Q: Tôi có thể dùng timeframe khác không?
**A:** Có, edit `trading/signal_generator.py`:
```python
klines = client.get_klines(symbol, interval='5m', limit=100)
```

Nhưng cần retrain model với data tương ứng.

### Q: Tôi có thể thêm indicators khác không?
**A:** Có, edit `ml/features.py`:
```python
# Add new indicator
df['ema'] = ta.ema(df['close'], length=20)

# Update FEATURE_COLUMNS
FEATURE_COLUMNS = [..., 'ema']
```

Sau đó retrain model.

### Q: Tôi có thể dùng cho exchange khác không?
**A:** Có thể, nhưng cần:
1. Implement client mới (thay `AsterDEXClient`)
2. Adjust API calls
3. Test kỹ

### Q: Có thể chạy nhiều bots cùng lúc?
**A:** Có:
1. Clone folder
2. Tạo `.env` riêng
3. Dùng symbols khác
4. Hoặc accounts khác

## Support

### Q: Tôi cần help, liên hệ ai?
**A:** 
1. Check README.md
2. Check logs
3. Open GitHub issue
4. Join Telegram group (nếu có)

### Q: Tôi tìm bug, báo ở đâu?
**A:** Open GitHub issue với:
- Error message
- Logs
- Steps to reproduce

### Q: Tôi muốn contribute?
**A:** Welcome! 
1. Fork repo
2. Create feature branch
3. Submit PR

---

**Không tìm thấy câu trả lời? Open an issue! 🚀**

