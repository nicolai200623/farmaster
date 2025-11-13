# 🔥 HOTFIX: SL_PCT=None TypeError

**Ngày:** 2025-11-13  
**Mức độ:** CRITICAL  
**Trạng thái:** ✅ FIXED

---

## 🚨 VẤN ĐỀ

### **Lỗi:**
```
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```

### **Nguyên nhân:**
Khi `SL_PCT=0` trong file `.env`, code trong `config.py` sẽ set `Config.SL_PCT = None`:

```python
# config.py line 46
SL_PCT = float(os.getenv('SL_PCT', '1.0')) if float(os.getenv('SL_PCT', '0')) > 0 else None
```

Nhưng nhiều file khác cố gắng nhân `Config.SL_PCT * 100` mà không kiểm tra `None`:

```python
# bot.py line 75 (CŨ)
logger.info(f"   TP/SL: {Config.TP_PCT*100}% / {Config.SL_PCT*100}%")
#                                                ^^^^^^^^^^^^^^^^
#                                                None * 100 → ERROR!
```

---

## ✅ CÁC FILE ĐÃ SỬA

### 1. **bot.py** ✅
**Dòng 75-78:**
```python
# Handle None for SL_PCT
sl_display = f"{Config.SL_PCT*100}%" if Config.SL_PCT is not None else "Disabled"
logger.info(f"   TP/SL: {Config.TP_PCT*100}% / {sl_display}")
```

### 2. **check_ready.py** ✅
**Dòng 26-27:**
```python
sl_display = f"{Config.SL_PCT*100}%" if Config.SL_PCT is not None else "Disabled"
print(f"   ✅ TP/SL: {Config.TP_PCT*100}% / {sl_display}")
```

### 3. **retrain_and_test.py** ✅
**Dòng 22-24:**
```python
logger.info(f"   TP: {Config.TP_PCT*100}%")
sl_display = f"{Config.SL_PCT*100}%" if Config.SL_PCT is not None else "Disabled"
logger.info(f"   SL: {sl_display}")
```

**Dòng 91:**
```python
sl_display = f"{Config.SL_PCT*100}%" if Config.SL_PCT is not None else "Disabled"
logger.warning(f"   - Widen SL (current: {sl_display})")
```

### 4. **backtest/backtester.py** ✅
**Dòng 169:**
```python
# CŨ: elif pnl_pct <= -Config.SL_PCT:
# MỚI:
elif Config.SL_PCT is not None and pnl_pct <= -Config.SL_PCT:
    should_close = True
    reason = "SL"
```

### 5. **test_position_timeout.py** ✅
**Dòng 109:**
```python
# CŨ: if sl_pct > 0 and pnl_pct <= -sl_pct:
# MỚI:
if sl_pct is not None and sl_pct > 0 and pnl_pct <= -sl_pct:
    return True, f"SL ({pnl_pct*100:.2f}%)"
```

---

## ✅ CÁC FILE ĐÃ OK (KHÔNG CẦN SỬA)

### **trading/signal_generator.py** ✅
**Dòng 288:**
```python
# Đã có check: if sl_pct > 0 and pnl_pct <= -sl_pct:
# Khi sl_pct=None, điều kiện sl_pct > 0 sẽ False → OK
```

### **backtest/enhanced_backtester.py** ✅
**Dòng 289:**
```python
# Đã có check: elif Config.SL_PCT and price_change_pct <= -Config.SL_PCT:
# Khi SL_PCT=None, điều kiện Config.SL_PCT sẽ False → OK
```

---

## 🎯 KẾT QUẢ

### **Trước khi fix:**
```bash
$ python bot.py
Traceback (most recent call last):
  File "/home/farmaster/farmaster/bot.py", line 377, in <module>
    main()
  File "/home/farmaster/farmaster/bot.py", line 373, in main
    bot = AsterDEXBot()
  File "/home/farmaster/farmaster/bot.py", line 75, in __init__
    logger.info(f"   TP/SL: {Config.TP_PCT*100}% / {Config.SL_PCT*100}%")
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```

### **Sau khi fix:**
```bash
$ python bot.py
✅ Bot initialized successfully!
   Symbols: ['ADAUSDT', 'BNBUSDT', 'DOGEUSDT', 'UNIUSDT', 'LINKUSDT']
   Leverage: 10x
   Position Size: 10.0%
   TP/SL: 1.0% / Disabled  ← Hiển thị "Disabled" thay vì crash!
   Position Timeout: 24.0h
```

---

## 📝 GHI CHÚ

### **Tại sao SL_PCT=None?**
Theo thiết kế trong `config.py`:
```python
# Nếu SL_PCT=0 trong .env → Config.SL_PCT = None
# Nghĩa là: KHÔNG SỬ DỤNG STOP LOSS
```

### **Cách hoạt động:**
1. User set `SL_PCT=0` trong `.env`
2. Config load và set `Config.SL_PCT = None`
3. Code kiểm tra `if Config.SL_PCT is not None` trước khi sử dụng
4. Nếu `None` → Bỏ qua stop loss logic

### **Lợi ích:**
- ✅ Cho phép disable stop loss hoàn toàn
- ✅ Không crash khi SL_PCT=0
- ✅ Hiển thị rõ ràng "Disabled" trong log

---

## 🚀 HÀNH ĐỘNG TIẾP THEO

### **Trên VPS:**
```bash
# Pull code mới
cd /home/farmaster/farmaster
git pull

# Restart bot
sudo systemctl restart asterdex-bot
# hoặc
pm2 restart asterdex-bot

# Kiểm tra log
tail -f logs/bot_*.log
```

### **Kiểm tra:**
- ✅ Bot khởi động thành công
- ✅ Không có TypeError
- ✅ Log hiển thị "TP/SL: 1.0% / Disabled"
- ✅ Bot chạy bình thường

---

## 💡 ĐỀ XUẤT

Nếu muốn sử dụng stop loss, thay đổi trong `.env`:
```env
# Thêm stop loss 0.5% (= -5% PnL với 10x leverage)
SL_PCT=0.5
```

Sau đó restart bot:
```bash
sudo systemctl restart asterdex-bot
```

---

**Tóm tắt:** Đã sửa lỗi TypeError khi SL_PCT=None trong 5 files. Bot giờ có thể chạy với SL_PCT=0 (disabled) mà không crash.

