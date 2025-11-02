# 📈 Backtest Optimization Guide

## 🐛 Current Problem

```
Total Trades: 4
Win Rate: 0.00% ← ❌ NO WINS!
Total PnL: -19.96% ← ❌ LOSING 20%
```

**Root causes:**
1. LSTM model chưa train tốt
2. Signal logic quá strict
3. TP/SL chưa optimal
4. LSTM threshold quá cao

---

## ✅ Quick Fix (Phase 1)

### **Step 1: Update Parameters**

Đã update `.env` với settings tốt hơn:

```env
# OLD (Bad)
TP_PCT=0.02
SL_PCT=0.01
LSTM_THRESHOLD=0.6
LSTM_EPOCHS=50

# NEW (Better)
TP_PCT=0.03
SL_PCT=0.015
LSTM_THRESHOLD=0.55
LSTM_EPOCHS=100
```

**Changes:**
- ✅ TP tăng 2% → 3% (more room for profit)
- ✅ SL tăng 1% → 1.5% (less premature stops)
- ✅ LSTM threshold giảm 0.6 → 0.55 (more signals)
- ✅ Epochs tăng 50 → 100 (better training)

---

### **Step 2: Retrain Model**

```bash
# Option A: Simple retrain
python ml/train.py

# Option B: Retrain + Auto backtest
python retrain_and_test.py
```

**Expected output:**
```
✅ Test Accuracy: >55%
   Precision: >50%
   Recall: >50%
   F1 Score: >50%
```

**Nếu accuracy < 55%:**
- Model chưa đủ tốt
- Cần thử architecture khác hoặc more data

---

### **Step 3: Run Backtest**

```bash
python run_backtest.py
```

**Expected improvements:**
- Total Trades: >10 (was 4)
- Win Rate: >30% (was 0%)
- Total PnL: >-5% (was -20%)

---

## 🔍 Advanced Optimization (Phase 2)

### **Automatic Parameter Optimization**

```bash
python optimize_params.py
```

**What it does:**
- Tests different combinations of TP/SL/Threshold
- Finds best parameters automatically
- Shows top 5 parameter sets

**Parameter grid:**
```python
tp_pct: [0.02, 0.03, 0.04]
sl_pct: [0.01, 0.015, 0.02]
lstm_threshold: [0.5, 0.55, 0.6]
min_signal_score: [1, 2]
```

**Total combinations:** 54
**Estimated time:** ~2 hours

**Output:**
```
🏆 BEST PARAMETERS:
   TP: 3.0%
   SL: 1.5%
   LSTM Threshold: 0.55
   Min Signal Score: 2

📈 BEST RESULTS:
   Total Trades: 15
   Win Rate: 53.33%
   Total PnL: 12.45%
   Profit Factor: 1.85
```

---

## 📊 Success Metrics

### **Minimum Acceptable**
- ✅ Win Rate: >40%
- ✅ Total PnL: >0%
- ✅ Profit Factor: >1.0
- ✅ Total Trades: >10

### **Good**
- ✅ Win Rate: >50%
- ✅ Total PnL: >10%
- ✅ Profit Factor: >1.5
- ✅ Max Drawdown: <10%

### **Excellent**
- ✅ Win Rate: >60%
- ✅ Total PnL: >20%
- ✅ Profit Factor: >2.0
- ✅ Max Drawdown: <5%

---

## 🎯 Recommended Workflow

### **For Quick Testing:**

```bash
# 1. Update .env (already done)
# 2. Retrain + test
python retrain_and_test.py

# 3. If results good → deploy
# 4. If results bad → optimize
python optimize_params.py
```

---

### **For Thorough Optimization:**

```bash
# 1. Retrain model
python ml/train.py

# 2. Optimize parameters
python optimize_params.py

# 3. Update .env with best params
nano .env

# 4. Final backtest
python run_backtest.py

# 5. If good → deploy
python bot.py
```

---

## 💡 Alternative Strategies

Nếu LSTM vẫn không improve, thử strategies đơn giản hơn:

### **1. Mean Reversion**

```python
# Entry
if RSI < 30:
    BUY
elif RSI > 70:
    SELL

# Exit
if RSI == 50 or TP/SL hit:
    CLOSE
```

**Pros:**
- ✅ Simple
- ✅ Works in ranging markets
- ✅ No ML needed

**Cons:**
- ❌ Fails in trending markets
- ❌ Many false signals

---

### **2. Trend Following**

```python
# Entry
if EMA(20) > EMA(50):
    LONG
elif EMA(20) < EMA(50):
    SHORT

# Exit
if EMA crossover or TP/SL:
    CLOSE
```

**Pros:**
- ✅ Simple
- ✅ Works in trending markets
- ✅ Good risk/reward

**Cons:**
- ❌ Fails in ranging markets
- ❌ Late entries

---

### **3. Hybrid (Recommended)**

```python
# Combine LSTM + RSI + Trend
if (
    LSTM > 0.55 and
    RSI < 40 and
    EMA(20) > EMA(50)
):
    LONG
```

**Pros:**
- ✅ Multiple confirmations
- ✅ Better accuracy
- ✅ Filters noise

**Cons:**
- ❌ Fewer trades
- ❌ More complex

---

## 🔧 Troubleshooting

### **Problem: Too few trades**

**Solutions:**
1. Lower `LSTM_THRESHOLD` (0.6 → 0.5)
2. Lower `MIN_SIGNAL_SCORE` (2 → 1)
3. Add more symbols
4. Reduce `LOOP_SLEEP` (30s → 15s)

---

### **Problem: Low win rate**

**Solutions:**
1. Widen SL (1% → 2%)
2. Tighten entry criteria
3. Add trend filter
4. Retrain model with more data

---

### **Problem: Negative PnL**

**Solutions:**
1. Check TP/SL ratio (should be >2:1)
2. Review entry logic
3. Add stop loss trailing
4. Consider different strategy

---

### **Problem: Model accuracy < 55%**

**Solutions:**
1. Increase training data (365 → 730 days)
2. Increase epochs (100 → 200)
3. Try different architecture
4. Add more features
5. Use ensemble methods

---

## 📝 Checklist

Before going live:

- [ ] Model accuracy >55%
- [ ] Backtest win rate >40%
- [ ] Backtest PnL >0%
- [ ] Profit factor >1.0
- [ ] Max drawdown <15%
- [ ] Tested on multiple timeframes
- [ ] Tested on multiple symbols
- [ ] Risk management in place
- [ ] Emergency stop loss set
- [ ] Position size appropriate

---

## 🚀 Next Steps

1. **Run retrain + test:**
   ```bash
   python retrain_and_test.py
   ```

2. **Check results:**
   - If good (PnL >0%, WinRate >40%) → Deploy
   - If bad → Run optimization

3. **Optimize (if needed):**
   ```bash
   python optimize_params.py
   ```

4. **Update .env with best params**

5. **Final backtest:**
   ```bash
   python run_backtest.py
   ```

6. **Deploy:**
   ```bash
   python bot.py
   ```

---

**Good luck! 🚀**

