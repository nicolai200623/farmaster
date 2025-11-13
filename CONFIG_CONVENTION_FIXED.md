# ⚠️ SỬA LỖI CONVENTION - TP/SL/Trailing Stop

**Ngày:** 2025-11-13  
**Vấn đề:** Convention không thống nhất giữa TP/SL và Trailing Stop

---

## 🔍 VẤN ĐỀ PHÁT HIỆN

User báo nhầm lẫn giữa:
- `TP_PCT=1.0` (nghĩa là gì?)
- `TP_PCT=0.01` (nghĩa là gì?)

Sau khi kiểm tra code, phát hiện **2 convention KHÁC NHAU**:

### **1. TP/SL (Decimal Format):**
<augment_code_snippet path="trading/asterdex_client.py" mode="EXCERPT">
```python
# Calculate PnL %
if amt > 0:  # LONG
    pnl_pct = (mark_price - entry_price) / entry_price
    #         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #         Decimal: 0.01 = 1%, 0.02 = 2%
```
</augment_code_snippet>

<augment_code_snippet path="trading/signal_generator.py" mode="EXCERPT">
```python
# Take Profit
if pnl_pct >= tp_pct:
#  ^^^^^^    ^^^^^^
#  0.01      ???  → Phải là 0.01 để match!
```
</augment_code_snippet>

### **2. Trailing Stop (Percentage Format):**
<augment_code_snippet path="trading/trailing_stop.py" mode="EXCERPT">
```python
# Calculate current profit %
if side == 'LONG':
    profit_pct = ((current_price - entry_price) / entry_price) * 100
    #                                                            ^^^^
    #                                                            Percentage: 1.0 = 1%, 2.0 = 2%
```
</augment_code_snippet>

---

## ✅ GIẢI PHÁP

### **Convention đã sửa:**

| Config | Format | Ví dụ | Giải thích |
|--------|--------|-------|-----------|
| **TP_PCT** | Decimal | `0.01` | 1% take profit |
| **SL_PCT** | Decimal | `0.01` | 1% stop loss |
| **TRAILING_ACTIVATION_PCT** | Percentage | `1.0` | Activate tại 1% profit |
| **TRAILING_DISTANCE_PCT** | Percentage | `0.3` | Trailing 0.3% |

### **Lý do khác nhau:**
- **TP/SL:** So sánh trực tiếp với `pnl_pct` từ exchange (decimal format)
- **Trailing Stop:** Tính toán riêng `profit_pct * 100` (percentage format)

---

## 📝 CẤU HÌNH ĐÚNG

### **File `.env` - Cho chiến lược 1% TP:**

```env
# TP/SL (Decimal format: 0.01 = 1%)
TP_PCT=0.01                    # Take profit 1%
SL_PCT=0                       # No stop loss

# Trailing Stop (Percentage format: 1.0 = 1%)
USE_TRAILING_STOP=True
TRAILING_ACTIVATION_PCT=1.0    # Activate tại 1% profit
TRAILING_DISTANCE_PCT=0.3      # Trailing 0.3%

# Position Timeout
POSITION_TIMEOUT_HOURS=36
```

---

## 🔧 THAY ĐỔI CODE

### **1. config.py - Sửa comment và default:**

**CŨ (SAI):**
```python
# TP/SL in percentage (1.0 = 1%, not 0.01)  ← SAI!
TP_PCT = float(os.getenv('TP_PCT', '2.0'))  # Take profit 2%
```

**MỚI (ĐÚNG):**
```python
# TP/SL in decimal format (0.01 = 1%, NOT 1.0)
TP_PCT = float(os.getenv('TP_PCT', '0.02'))  # Take profit 2% (0.02)
SL_PCT = float(os.getenv('SL_PCT', '0.01')) if float(os.getenv('SL_PCT', '0')) > 0 else None  # Stop loss 1% (0.01)
```

**Trailing Stop (GIỮ NGUYÊN):**
```python
# Trailing Stop (percentage format: 1.0 = 1%, NOT 0.01)
# NOTE: Trailing stop uses percentage format (1.0 = 1%) because it calculates profit_pct * 100 internally
USE_TRAILING_STOP = os.getenv('USE_TRAILING_STOP', 'True').lower() == 'true'
TRAILING_ACTIVATION_PCT = float(os.getenv('TRAILING_ACTIVATION_PCT', '0.5'))  # 0.5%
TRAILING_DISTANCE_PCT = float(os.getenv('TRAILING_DISTANCE_PCT', '0.3'))  # 0.3%
```

### **2. bot.py - Sửa log display:**

**CŨ:**
```python
logger.info(f"   TP/SL: {Config.TP_PCT*100}% / {sl_display}")
#                        ^^^^^^^^^^^^
#                        1.0*100 = 100% ← SAI!
```

**MỚI:**
```python
# TP_PCT and SL_PCT are in decimal: 0.01 = 1%
sl_display = f"{Config.SL_PCT*100:.2f}%" if Config.SL_PCT is not None else "Disabled"
logger.info(f"   TP/SL: {Config.TP_PCT*100:.2f}% / {sl_display}")
#                        ^^^^^^^^^^^^
#                        0.01*100 = 1.00% ← ĐÚNG!
```

---

## 📊 SO SÁNH

### **Trước khi sửa:**
```env
TP_PCT=1.0  # User nghĩ: 1%
```

**Log hiển thị:**
```
TP/SL: 100.0% / Disabled  ← SAI!
```

**Code so sánh:**
```python
if pnl_pct >= tp_pct:  # 0.01 >= 1.0 → FALSE
#  ^^^^^^    ^^^^^^
#  0.01      1.0  → KHÔNG BAO GIỜ MATCH! ❌
```

**Kết quả:** Position KHÔNG BAO GIỜ đóng tại TP! ❌

---

### **Sau khi sửa:**
```env
TP_PCT=0.01  # 1% (decimal)
```

**Log hiển thị:**
```
TP/SL: 1.00% / Disabled  ← ĐÚNG!
```

**Code so sánh:**
```python
if pnl_pct >= tp_pct:  # 0.01 >= 0.01 → TRUE
#  ^^^^^^    ^^^^^^
#  0.01      0.01  → MATCH! ✅
```

**Kết quả:** Position đóng đúng tại 1% TP! ✅

---

## 🎯 CẤU HÌNH KHUYẾN NGHỊ

### **Cho Volume Farming (1% TP, No SL, Trailing Stop):**

```env
# TP/SL (Decimal: 0.01 = 1%)
TP_PCT=0.01                    # TP 1%
SL_PCT=0                       # No SL

# Trailing Stop (Percentage: 1.0 = 1%)
USE_TRAILING_STOP=True
TRAILING_ACTIVATION_PCT=1.0    # Activate tại 1%
TRAILING_DISTANCE_PCT=0.3      # Trail 0.3%

# Timeout
POSITION_TIMEOUT_HOURS=36
```

**Cách hoạt động:**
```
Entry: $100
Giá lên $101 (+1% = 0.01 decimal)
→ TP hit: Đóng tại $101 ✅
→ Trailing activate: Stop = $100.70

Nếu giá tiếp tục lên $102:
→ Trailing update: Stop = $101.70
→ TP KHÔNG hit (vì trailing đã activate)

Giá xuống $101.70:
→ Trailing hit: Đóng tại $101.70 với +1.7% ✅
```

---

## 🚀 HÀNH ĐỘNG

### **Trên VPS:**

```bash
# Pull code mới
cd /home/farmaster/farmaster
git pull

# Sửa .env (QUAN TRỌNG!)
nano .env

# Sửa dòng:
TP_PCT=0.01                    # ← Decimal: 0.01 = 1%
TRAILING_ACTIVATION_PCT=1.0    # ← Percentage: 1.0 = 1%
TRAILING_DISTANCE_PCT=0.3      # ← Percentage: 0.3 = 0.3%

# Lưu và thoát (Ctrl+O, Enter, Ctrl+X)

# Restart bot
sudo systemctl restart asterdex-bot
# hoặc
pm2 restart asterdex-bot

# Kiểm tra log
tail -f logs/bot_*.log | head -20
```

**Kết quả mong đợi:**
```
✅ Bot initialized successfully!
   Symbols: ['BTCUSDT', 'ETHUSDT', ...]
   Leverage: 10x
   Position Size: 20.0%
   TP/SL: 1.00% / Disabled  ← ĐÚNG!
   Position Timeout: 36.0h
📈 Trailing Stop enabled: Activation=1.0%, Trail=0.3%
```

---

## ⚠️ QUAN TRỌNG

### **Nhớ convention:**

| Config | Format | Ví dụ 1% | Ví dụ 2% |
|--------|--------|----------|----------|
| **TP_PCT** | Decimal | `0.01` | `0.02` |
| **SL_PCT** | Decimal | `0.01` | `0.02` |
| **TRAILING_ACTIVATION_PCT** | Percentage | `1.0` | `2.0` |
| **TRAILING_DISTANCE_PCT** | Percentage | `0.3` | `0.5` |

### **Công thức nhớ:**
- **TP/SL:** Giống Python decimal → `0.01 = 1%`
- **Trailing:** Giống số thập phân thông thường → `1.0 = 1%`

---

## 📁 FILES ĐÃ SỬA

1. ✅ **config.py** - Sửa comment và default values
2. ✅ **bot.py** - Sửa log display (không thay đổi logic)
3. ✅ **CONFIG_CONVENTION_FIXED.md** - Documentation

---

**Tóm tắt:** TP/SL dùng decimal (0.01 = 1%), Trailing Stop dùng percentage (1.0 = 1%). Đã sửa comment và default values để tránh nhầm lẫn.

