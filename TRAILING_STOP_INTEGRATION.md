# 📈 TRAILING STOP - Tích Hợp Vào Bot Chính

**Ngày:** 2025-11-13  
**Trạng thái:** ✅ HOÀN THÀNH

---

## 🎯 TỔNG QUAN

Trailing stop đã được tích hợp vào bot chính (`bot.py`) để **bảo vệ profit tự động** khi giá đảo chiều.

### **Cách hoạt động:**
1. **Khi profit đạt ngưỡng kích hoạt** (ví dụ: 1%) → Trailing stop được activate
2. **Stop loss tự động di chuyển theo giá** → Luôn cách giá hiện tại 1 khoảng cố định (ví dụ: 0.3%)
3. **Khi giá đảo chiều và chạm stop** → Đóng position, bảo vệ profit

### **Ví dụ:**
```
Entry: $100
Giá lên $101 (+1%) → Activate trailing stop
Giá lên $102 (+2%) → Stop = $101.70 (0.3% trailing)
Giá lên $103 (+3%) → Stop = $102.70
Giá xuống $102.70 → Đóng position với +2.7% profit ✅
```

---

## ⚙️ CẤU HÌNH

### **File `.env`:**
```env
# Trailing Stop
USE_TRAILING_STOP=True                # Bật/tắt trailing stop
TRAILING_ACTIVATION_PCT=1.0           # Kích hoạt khi profit đạt 1%
TRAILING_DISTANCE_PCT=0.3             # Khoảng cách trailing 0.3%
```

### **Giải thích:**

#### **1. USE_TRAILING_STOP**
- `True`: Bật trailing stop (KHUYẾN NGHỊ)
- `False`: Tắt trailing stop

#### **2. TRAILING_ACTIVATION_PCT**
- Ngưỡng profit để kích hoạt trailing stop
- Ví dụ: `1.0` = Kích hoạt khi profit đạt 1%
- **Khuyến nghị:** 0.5% - 1.5%

#### **3. TRAILING_DISTANCE_PCT**
- Khoảng cách giữa giá hiện tại và stop loss
- Ví dụ: `0.3` = Stop cách giá 0.3%
- **Khuyến nghị:** 0.2% - 0.5%

---

## 🔧 THAY ĐỔI CODE

### **1. Import TrailingStopManager**
<augment_code_snippet path="bot.py" mode="EXCERPT">
```python
from trading.trailing_stop import TrailingStopManager
```
</augment_code_snippet>

### **2. Khởi tạo trong __init__**
<augment_code_snippet path="bot.py" mode="EXCERPT">
```python
# Initialize trailing stop manager
if Config.USE_TRAILING_STOP:
    self.trailing_stop_mgr = TrailingStopManager(
        activation_pct=Config.TRAILING_ACTIVATION_PCT,
        trail_pct=Config.TRAILING_DISTANCE_PCT
    )
    logger.info(f"📈 Trailing Stop enabled: Activation={Config.TRAILING_ACTIVATION_PCT}%, Trail={Config.TRAILING_DISTANCE_PCT}%")
else:
    self.trailing_stop_mgr = None
    logger.info("📈 Trailing Stop disabled")
```
</augment_code_snippet>

### **3. Check trailing stop trong _process_symbol**
<augment_code_snippet path="bot.py" mode="EXCERPT">
```python
# Check trailing stop first (highest priority for profit protection)
should_close = False
reason = ""

if self.trailing_stop_mgr is not None:
    ts_result = self.trailing_stop_mgr.update_trailing_stop(
        symbol=symbol,
        side=position['side'],
        entry_price=position['entry_price'],
        current_price=position['mark_price']
    )
    
    if ts_result['should_close']:
        should_close = True
        reason = ts_result['reason']
        logger.info(f"   📈 {reason}")

# If not closed by trailing stop, check TP/SL/Timeout
if not should_close:
    should_close, reason = self.signal_generator.should_close_position(
        position,
        position_age_hours=position_age_hours
    )
```
</augment_code_snippet>

### **4. Clear trailing stop khi đóng position**
<augment_code_snippet path="bot.py" mode="EXCERPT">
```python
# Clear trailing stop
if self.trailing_stop_mgr is not None:
    self.trailing_stop_mgr.remove_trailing_stop(symbol)
```
</augment_code_snippet>

---

## 📊 THỨ TỰ ƯU TIÊN

Khi có position, bot kiểm tra theo thứ tự:

1. **Trailing Stop** (Cao nhất) - Bảo vệ profit
2. **Take Profit** - Đạt mục tiêu
3. **Stop Loss** - Cắt lỗ (nếu enabled)
4. **Position Timeout** - Quá thời gian

---

## 🎯 CHIẾN LƯỢC KHUYẾN NGHỊ

### **Cho Volume Farming (Hiện tại):**
```env
USE_TRAILING_STOP=True
TRAILING_ACTIVATION_PCT=1.0    # Activate tại TP target
TRAILING_DISTANCE_PCT=0.3      # Bảo vệ 0.7% profit tối thiểu
TP_PCT=0.01                    # TP 1%
SL_PCT=0                       # No fixed SL
POSITION_TIMEOUT_HOURS=36      # Timeout 36h
```

**Lợi ích:**
- ✅ Bảo vệ profit khi đạt TP
- ✅ Cho phép profit chạy xa hơn 1%
- ✅ Tự động đóng khi giá đảo chiều
- ✅ Không bị stop out sớm

### **Cho Trading Thông Thường:**
```env
USE_TRAILING_STOP=True
TRAILING_ACTIVATION_PCT=0.5    # Activate sớm hơn
TRAILING_DISTANCE_PCT=0.3      # Trailing 0.3%
TP_PCT=0.02                    # TP 2%
SL_PCT=0.01                    # SL 1%
POSITION_TIMEOUT_HOURS=24      # Timeout 24h
```

---

## 📝 LOG MẪU

### **Khi trailing stop activate:**
```
📊 Processing BTCUSDT...
   Current position: LONG 0.01
   Entry: $50000.00 | Mark: $50500.00
   PnL: 1.00% ($10.00)
🎯 Trailing stop activated for BTCUSDT at 1.00% profit
```

### **Khi trailing stop hit:**
```
📊 Processing BTCUSDT...
   Current position: LONG 0.01
   Entry: $50000.00 | Mark: $50850.00
   PnL: 1.70% ($17.00)
   📈 Trailing stop hit (profit: 1.70%)
   🔴 Closing position: Trailing stop hit (profit: 1.70%)
✅ CLOSE LONG BTCUSDT | Trailing stop hit (profit: 1.70%) | PnL: 1.70%
```

---

## ✅ KIỂM TRA

### **1. Kiểm tra config:**
```bash
cat .env | grep TRAILING
```

**Kết quả mong đợi:**
```
USE_TRAILING_STOP=True
TRAILING_ACTIVATION_PCT=1.0
TRAILING_DISTANCE_PCT=0.3
```

### **2. Kiểm tra bot log:**
```bash
tail -f logs/bot_*.log | grep "Trailing"
```

**Kết quả mong đợi:**
```
📈 Trailing Stop enabled: Activation=1.0%, Trail=0.3%
🎯 Trailing stop activated for BTCUSDT at 1.05% profit
📈 Trailing stop hit (profit: 1.42%)
```

---

## 🚀 HÀNH ĐỘNG

### **Trên VPS:**
```bash
# Pull code mới
cd /home/farmaster/farmaster
git pull

# Kiểm tra config
cat .env | grep TRAILING

# Restart bot
sudo systemctl restart asterdex-bot
# hoặc
pm2 restart asterdex-bot

# Monitor log
tail -f logs/bot_*.log
```

---

## 💡 TIP & TRICKS

### **Điều chỉnh trailing distance:**
- **Tight trailing (0.2%)**: Bảo vệ profit tốt hơn, nhưng dễ bị stop out sớm
- **Loose trailing (0.5%)**: Cho phép giá dao động nhiều hơn, nhưng có thể mất nhiều profit hơn

### **Điều chỉnh activation:**
- **Sớm (0.5%)**: Bảo vệ profit sớm, phù hợp với market volatile
- **Muộn (1.5%)**: Chỉ bảo vệ khi profit đủ lớn, phù hợp với trending market

### **Kết hợp với TP:**
```env
TP_PCT=0.02              # TP chính tại 2%
TRAILING_ACTIVATION_PCT=0.01  # Trailing activate tại 1%
TRAILING_DISTANCE_PCT=0.003   # Trailing 0.3%
```
→ Nếu giá chạy xa, trailing stop bảo vệ. Nếu không, TP tại 2%.

---

## 📊 TỔNG KẾT

| Tính năng | Trước | Sau |
|-----------|-------|-----|
| **Trailing Stop** | ❌ Không có | ✅ Có (trong bot chính) |
| **Bảo vệ profit** | ❌ Không | ✅ Tự động |
| **Priority** | - | 🥇 Cao nhất |
| **Config** | - | ✅ Linh hoạt |

---

**Tóm tắt:** Trailing stop đã được tích hợp vào bot chính, bảo vệ profit tự động khi giá đảo chiều. Sử dụng `USE_TRAILING_STOP=True` để bật.

