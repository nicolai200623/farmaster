# 💰 Position Size Configuration Guide

## 📋 Overview

Bot hỗ trợ 2 cách tính position size:

1. **Percentage-based** (% của balance) - Mặc định
2. **Fixed USDT amount** (Số tiền cố định) - Mới

---

## 🔧 Configuration

### **Option 1: Percentage-based (Default)**

Sử dụng % của balance cho mỗi vị thế.

**Ví dụ:**
```env
SIZE_PCT=0.2
POSITION_SIZE_USDT=
```

**Cách tính:**
```
Balance: $100
SIZE_PCT: 0.2 (20%)
Leverage: 5x

→ Capital per trade: $100 × 0.2 = $20
→ Buying power: $20 × 5 = $100
→ Quantity (BTC @ $70,000): $100 / $70,000 = 0.00142 BTC
```

**Ưu điểm:**
- ✅ Tự động scale theo balance
- ✅ Risk management tốt hơn (% cố định)
- ✅ Phù hợp với compound growth

**Nhược điểm:**
- ❌ Position size thay đổi theo balance
- ❌ Khó kiểm soát chính xác số tiền mỗi trade

---

### **Option 2: Fixed USDT Amount (New)**

Sử dụng số tiền cố định (USDT) cho mỗi vị thế.

**Ví dụ:**
```env
SIZE_PCT=0.2
POSITION_SIZE_USDT=10
```

**Cách tính:**
```
Balance: $100
POSITION_SIZE_USDT: $10
Leverage: 5x

→ Capital per trade: $10 (fixed)
→ Buying power: $10 × 5 = $50
→ Quantity (BTC @ $70,000): $50 / $70,000 = 0.000714 BTC
```

**Ưu điểm:**
- ✅ Position size cố định, dễ kiểm soát
- ✅ Dễ tính toán risk/reward
- ✅ Phù hợp với budget cố định

**Nhược điểm:**
- ❌ Không scale theo balance
- ❌ Cần adjust manually khi balance thay đổi nhiều

---

## 📊 Comparison

| Metric | Percentage-based | Fixed USDT |
|--------|------------------|------------|
| **Position size** | Thay đổi theo balance | Cố định |
| **Risk management** | % cố định | $ cố định |
| **Compound growth** | ✅ Tự động | ❌ Manual |
| **Budget control** | ❌ Khó | ✅ Dễ |
| **Recommended for** | Long-term growth | Fixed budget |

---

## 🚀 Usage Examples

### **Example 1: Small Account ($50)**

**Percentage-based:**
```env
SIZE_PCT=0.2  # 20%
POSITION_SIZE_USDT=
```
- Capital per trade: $10
- Buying power (5x): $50

**Fixed USDT:**
```env
POSITION_SIZE_USDT=5
```
- Capital per trade: $5
- Buying power (5x): $25

---

### **Example 2: Medium Account ($500)**

**Percentage-based:**
```env
SIZE_PCT=0.1  # 10%
POSITION_SIZE_USDT=
```
- Capital per trade: $50
- Buying power (5x): $250

**Fixed USDT:**
```env
POSITION_SIZE_USDT=20
```
- Capital per trade: $20
- Buying power (5x): $100

---

### **Example 3: Large Account ($5000)**

**Percentage-based:**
```env
SIZE_PCT=0.05  # 5%
POSITION_SIZE_USDT=
```
- Capital per trade: $250
- Buying power (5x): $1250

**Fixed USDT:**
```env
POSITION_SIZE_USDT=100
```
- Capital per trade: $100
- Buying power (5x): $500

---

## ⚙️ How to Change

### **Switch to Fixed USDT:**

1. Edit `.env`:
```bash
nano .env
```

2. Set `POSITION_SIZE_USDT`:
```env
POSITION_SIZE_USDT=10  # $10 per trade
```

3. Save and restart bot:
```bash
# Ctrl+O, Enter, Ctrl+X
python bot.py
```

### **Switch back to Percentage:**

1. Edit `.env`:
```bash
nano .env
```

2. Clear `POSITION_SIZE_USDT`:
```env
POSITION_SIZE_USDT=
```

3. Save and restart bot.

---

## 🧪 Testing

### **Check current config:**

```bash
python scripts/check_order_size.py
```

**Output (Percentage-based):**
```
📊 Account Info:
   Total Balance: $100.00 USDT
   Position Size: 20%
   Leverage: 5x
   Capital per trade: $20.00
   Buying power: $100.00
```

**Output (Fixed USDT):**
```
📊 Account Info:
   Total Balance: $100.00 USDT
   Position Size: $10.00 USDT (fixed)
   Leverage: 5x
   Capital per trade: $10.00
   Buying power: $50.00
```

---

## 💡 Recommendations

### **Use Percentage-based if:**
- ✅ You want compound growth
- ✅ Balance changes frequently
- ✅ Long-term trading
- ✅ Risk management is priority

### **Use Fixed USDT if:**
- ✅ You have fixed budget per trade
- ✅ You want predictable position sizes
- ✅ Testing/backtesting with fixed capital
- ✅ Short-term trading

---

## ⚠️ Important Notes

1. **Priority:** If `POSITION_SIZE_USDT` is set, it will **override** `SIZE_PCT`

2. **Minimum notional:** Make sure your position size meets exchange minimum:
   ```bash
   python scripts/check_order_size.py
   ```

3. **Balance check:** Fixed USDT doesn't check if you have enough balance:
   ```
   Balance: $50
   POSITION_SIZE_USDT: $100  ← Will fail!
   ```

4. **Leverage:** Both methods use the same leverage setting

---

## 🔍 Validation

Bot will validate config on startup:

**Percentage-based:**
```
✅ Using percentage position size: 20% of balance per trade
✅ Config validation passed!
```

**Fixed USDT:**
```
✅ Using fixed position size: $10.0 USDT per trade
✅ Config validation passed!
```

---

## 📝 Summary

**Default (.env.example):**
```env
SIZE_PCT=0.1
POSITION_SIZE_USDT=
```

**Your config (.env):**
```env
SIZE_PCT=0.2
POSITION_SIZE_USDT=10  # ← Set this for fixed $10 per trade
```

**To use percentage:** Leave `POSITION_SIZE_USDT` empty
**To use fixed USDT:** Set `POSITION_SIZE_USDT=10` (or any amount)

---

**Happy Trading! 🚀**

