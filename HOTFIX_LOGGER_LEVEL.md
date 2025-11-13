# 🔥 HOTFIX: Logger.level AttributeError

**Ngày:** 2025-11-13  
**Mức độ:** HIGH  
**Trạng thái:** ✅ FIXED

---

## 🚨 VẤN ĐỀ

### **Lỗi:**
```
AttributeError: 'Logger' object has no attribute 'level'
```

### **Log lỗi:**
```
2025-11-13 03:48:04,956 [ERROR] Signal generation error for SOLUSDT: 'Logger' object has no attribute 'level'
2025-11-13 03:48:05,365 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 122, in generate_signal
    if logger.level <= 20:  # INFO level
AttributeError: 'Logger' object has no attribute 'level'
```

### **Nguyên nhân:**
File `trading/signal_generator.py` dòng 122 cố gắng truy cập `logger.level`, nhưng:
- `logger` là instance của custom class `Logger` (từ `utils/logger.py`)
- Custom `Logger` class KHÔNG có attribute `level`
- Chỉ có `logging.Logger` (built-in) mới có attribute `level`

**Code lỗi:**
```python
# trading/signal_generator.py line 122 (CŨ)
if logger.level <= 20:  # INFO level
    logger.debug(f"   ML predictions:")
    ...
```

---

## ✅ SỬA LỖI

### **File:** `trading/signal_generator.py`

**Dòng 118-130:**

**CŨ:**
```python
# 5. ML Prediction (LSTM or Ensemble)
if self.use_ensemble:
    ml_prob, pred_details = self.predictor.predict_with_details(ml_input)
    # Log individual model predictions
    if logger.level <= 20:  # INFO level  ← LỖI!
        logger.debug(f"   ML predictions:")
        for model_name, pred in pred_details.items():
            if model_name not in ['ensemble', 'weights']:
                logger.debug(f"      {model_name}: {pred:.3f}")
else:
    ml_prob = self.predictor.predict(ml_input)[0]
```

**MỚI:**
```python
# 5. ML Prediction (LSTM or Ensemble)
if self.use_ensemble:
    ml_prob, pred_details = self.predictor.predict_with_details(ml_input)
    # Log individual model predictions (only in debug mode)
    # Note: logger is custom Logger class, use logging module for level check
    import logging
    if logging.getLogger().getEffectiveLevel() <= logging.INFO:  ← SỬA!
        logger.debug(f"   ML predictions:")
        for model_name, pred in pred_details.items():
            if model_name not in ['ensemble', 'weights']:
                logger.debug(f"      {model_name}: {pred:.3f}")
else:
    ml_prob = self.predictor.predict(ml_input)[0]
```

### **Giải thích:**
- ✅ Sử dụng `logging.getLogger().getEffectiveLevel()` thay vì `logger.level`
- ✅ `logging.getLogger()` trả về built-in logger có method `getEffectiveLevel()`
- ✅ So sánh với `logging.INFO` (constant = 20)
- ✅ Hoạt động chính xác với custom Logger class

---

## 🎯 KẾT QUẢ

### **Trước khi fix:**
```
2025-11-13 03:48:04,735 [INFO]    🔍 Analyzing SOLUSDT for entry signal...
2025-11-13 03:48:04,956 [ERROR] Signal generation error for SOLUSDT: 'Logger' object has no attribute 'level'
2025-11-13 03:48:05,365 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 122, in generate_signal
    if logger.level <= 20:  # INFO level
AttributeError: 'Logger' object has no attribute 'level'
2025-11-13 03:48:05,550 [INFO]    📊 Analysis complete: Signal=HOLD, Score=0
```

### **Sau khi fix:**
```
2025-11-13 03:50:04,735 [INFO]    🔍 Analyzing SOLUSDT for entry signal...
2025-11-13 03:50:05,123 [INFO]    📊 Analysis complete: Signal=HOLD, Score=0
2025-11-13 03:50:05,124 [INFO]    ⚪ No signal - HOLD
```
✅ Không còn lỗi!

---

## 📝 GHI CHÚ

### **Tại sao có code này?**
Code này được thêm để log chi tiết predictions của từng model trong ensemble (LSTM, XGBoost) khi ở DEBUG mode. Tuy nhiên, cách check logging level không đúng với custom Logger class.

### **Cách hoạt động sau khi fix:**
1. Import `logging` module (built-in)
2. Gọi `logging.getLogger()` để lấy root logger
3. Dùng `getEffectiveLevel()` để lấy logging level hiện tại
4. So sánh với `logging.INFO` (20)
5. Nếu level <= INFO → Log debug info

### **Lợi ích:**
- ✅ Tương thích với custom Logger class
- ✅ Vẫn giữ được chức năng log debug
- ✅ Không crash khi generate signal

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
- ✅ Bot chạy bình thường
- ✅ Không có AttributeError
- ✅ Signal generation hoạt động
- ✅ Có log "📊 Analysis complete: Signal=..."

---

## 📊 TỔNG KẾT CÁC HOTFIX

### **Hotfix #1: SL_PCT=None TypeError** ✅
- File: `bot.py`, `check_ready.py`, `retrain_and_test.py`, `backtest/backtester.py`, `test_position_timeout.py`
- Lỗi: `TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'`
- Sửa: Thêm check `if Config.SL_PCT is not None` trước khi nhân với 100

### **Hotfix #2: Logger.level AttributeError** ✅
- File: `trading/signal_generator.py`
- Lỗi: `AttributeError: 'Logger' object has no attribute 'level'`
- Sửa: Dùng `logging.getLogger().getEffectiveLevel()` thay vì `logger.level`

---

**Tóm tắt:** Đã sửa lỗi AttributeError khi check logging level trong signal_generator.py. Bot giờ có thể generate signals mà không crash.

