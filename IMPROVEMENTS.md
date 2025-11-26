# 🚀 Bot Trading Improvements - Phase 1

## Tổng quan các cải tiến

Các cải tiến này nhằm giải quyết 3 vấn đề chính:
1. **LSTM Model Accuracy thấp (47.5%)** → Cải thiện features và ensemble
2. **Signal Frequency quá thấp** → Giảm MIN_CONFLUENCE_SCORE và tối ưu entry logic
3. **Entry Timing chưa tối ưu** → SmartEntrySystemV2 với multi-timeframe và session timing

---

## 1. ✨ Cải thiện ML Features (`ml/features.py`)

### Features mới được thêm:

#### a. ATR (Average True Range)
```python
- atr: Độ biến động tuyệt đối
- atr_pct: ATR as % of price
```
**Mục đích:** Đo lường volatility để set SL/TP động và filter low-volatility periods

#### b. Volume Analysis
```python
- volume_ma_ratio: Volume / MA(20)
```
**Mục đích:** Phát hiện volume spikes và dry-ups (accumulation/distribution)

#### c. Price Distance from EMAs
```python
- price_distance_ema20: (Price - EMA20) / EMA20 * 100
- price_distance_ema50: (Price - EMA50) / EMA50 * 100
```
**Mục đích:** Xác định vị trí giá trong trend, tìm entry tốt khi pullback

#### d. RSI Divergence Score
```python
- rsi_divergence_score: -1 (bearish) to 1 (bullish)
```
**Mục đích:** Phát hiện divergence sớm (leading indicator)

#### e. Momentum Score
```python
- momentum_score: Kết hợp ROC(10) và ROC(20)
```
**Mục đích:** Đo strength của trend

#### f. Volatility Ratio
```python
- volatility_ratio: Current volatility / Average volatility
```
**Mục đích:** Filter periods có volatility quá cao/thấp

### Impact lên Model:
- **Số features:** 14 → 22 (+57%)
- **Chất lượng:** Thêm features có ý nghĩa kinh tế rõ ràng
- **Kỳ vọng accuracy:** 47.5% → 55-60% sau retrain

---

## 2. 🎯 SmartEntrySystemV2 (`trading/advanced_entry.py`)

### Nguyên tắc thiết kế:
1. **Trend Alignment First** - Không trade ngược trend
2. **Wait for Pullback** - Entry tại giá tốt
3. **Volume Confirmation** - Volume phải xác nhận
4. **Session Timing** - Entry khi liquidity cao
5. **R:R Filter** - Chỉ entry khi R:R ≥ 2:1

### Scoring System (0-15 points):

| Component | Max Points | Criteria |
|-----------|------------|----------|
| **Trend Alignment** | 3 | All TFs align = 3, HTF align = 2 |
| **Pullback Quality** | 3 | Perfect pullback to EMA21 = 3 |
| **Key Levels** | 2 | At S/R levels |
| **Volume Confirmation** | 2 | Volume spike > 2x avg = 2 |
| **Momentum** | 2 | RSI in neutral zone (40-60) = 2 |
| **Session Timing** | 2 | London/NY session = 2 |
| **R:R Ratio** | 1 | R:R ≥ 2:1 = 1 |

### Session Timing:
- **London Open** (15:00-17:00 VN): +2 points
- **NY Open** (20:00-22:00 VN): +2 points
- **London-NY Overlap** (20:00-00:00 VN): +2 points
- **Asian Session** (08:00-12:00 VN): +1 point
- **Off-peak**: 0 points

### R:R Calculation:
- **SL:** 1.5 × ATR
- **TP:** 2 × Risk (2:1 R:R)
- **Min R:R:** 2.0 (configurable)

### Usage:
```python
from trading.advanced_entry import SmartEntrySystemV2

entry_system = SmartEntrySystemV2(min_score=5, min_rr_ratio=2.0)

signal, score, entry, sl, tp, reasons = entry_system.evaluate_entry(
    symbol='BTCUSDT',
    df_primary=df_15m,   # Primary timeframe
    df_higher=df_1h,     # Higher timeframe
    df_4h=df_4h          # Long-term trend
)

# signal: 'LONG', 'SHORT', or 'HOLD'
# score: 0-15
# entry, sl, tp: Prices (or None if HOLD)
# reasons: List of scoring reasons
```

---

## 3. 🎲 Advanced Risk Manager (`trading/advanced_risk_manager.py`)

### A. Kelly Criterion Position Sizing

**Formula:**
```
Kelly % = W - [(1-W) / R]

Where:
- W = Win rate
- R = Avg Win / Avg Loss
```

**Safety Features:**
- Uses **Half-Kelly** (Kelly% / 2) để giảm volatility
- Requires **minimum 20 trades** trước khi dùng Kelly
- **Caps at 25%** of balance
- **Fallback to base size** nếu không đủ data

**Example:**
```python
# Win rate = 55%, R = 2.0
Kelly% = 0.55 - [(1-0.55) / 2.0] = 0.55 - 0.225 = 0.325 (32.5%)
Half-Kelly = 16.25% of balance
```

### B. Correlation-Based Position Limiting

**Correlated Pairs:**
```python
BTCUSDT ↔ ETHUSDT, BNBUSDT
SOLUSDT ↔ AVAXUSDT, DOTUSDT
XRPUSDT ↔ ADAUSDT
```

**Limits:**
- Max **2 correlated positions** simultaneously
- Max **4 total positions**

**Prevents:**
- Over-exposure to Bitcoin correlation
- Portfolio blow-up during market crash

### C. Dynamic Risk Adjustment

**Losing Streak Detection:**
- After **3 consecutive losses** → Reduce size to **50%**

**Winning Streak Bonus:**
- After **3 consecutive wins** → Increase size to **120%**

### D. Performance Tracking

Tracks last 100 trades:
- Win rate
- Average win/loss
- R:R ratio
- Current multiplier

### Usage:
```python
from trading.advanced_risk_manager import AdvancedRiskManager

risk_mgr = AdvancedRiskManager(
    max_correlated_positions=2,
    max_total_positions=4
)

# Check if can open new position
allowed, reason = risk_mgr.check_correlation_risk(
    new_symbol='ETHUSDT',
    existing_positions=['BTCUSDT', 'SOLUSDT']
)

# Calculate optimal position size
position_size = risk_mgr.calculate_optimal_position_size(
    balance=1000,
    base_size_pct=0.1,
    use_kelly=True
)

# Record trade result
risk_mgr.record_trade(win=True, profit_pct=0.025)  # 2.5% profit
```

---

## 4. ⚙️ Configuration Updates

### `.env.example` changes:

```bash
# Increased symbols for diversification
SYMBOLS=BTCUSDT,ETHUSDT,SOLUSDT,BNBUSDT,XRPUSDT,AVAXUSDT,DOTUSDT,LTCUSDT

# Reduced MIN_CONFLUENCE_SCORE
MIN_CONFLUENCE_SCORE=5  # Was 7

# Tighter TP/SL
TP_PCT=0.015  # 1.5% (was 3%)
SL_PCT=0      # Use trailing stop instead

# Risk limits
DAILY_LOSS_LIMIT=0.15  # 15% (was 20%)
MAX_POSITIONS=4

# SmartEntryV2 settings
USE_SMART_ENTRY_V2=True
MIN_ENTRY_SCORE=5
MIN_RR_RATIO=2.0

# Trailing Stop (tighter)
TRAILING_ACTIVATION_PCT=0.8   # 0.8% (was 1%)
TRAILING_DISTANCE_PCT=0.25    # 0.25% (was 0.3%)

# Advanced Risk
USE_KELLY_SIZING=True
MAX_CORRELATED_POSITIONS=2
REDUCE_RISK_AFTER_LOSSES=True
```

### `config.py` additions:

```python
# SmartEntryV2
USE_SMART_ENTRY_V2 = True
MIN_ENTRY_SCORE = 5
MIN_RR_RATIO = 2.0

# Advanced Risk Management
USE_KELLY_SIZING = True
MAX_CORRELATED_POSITIONS = 2
MAX_POSITIONS = 4
REDUCE_RISK_AFTER_LOSSES = True
```

---

## 5. 📊 Expected Improvements

### A. Model Accuracy
- **Before:** 47.5% (near random)
- **Expected:** 55-60% (with new features + retrain)
- **Target:** 60%+ (với ensemble LSTM+XGBoost+LightGBM)

### B. Signal Frequency
- **Before:** Quá thấp (MIN_CONFLUENCE_SCORE = 7)
- **After:** Tăng ~40% (MIN_SCORE = 5)
- **Quality:** Vẫn cao nhờ multi-timeframe + R:R filter

### C. Win Rate
- **Before:** Unknown (model accuracy thấp)
- **Expected:** 50-55% (với entry timing tốt hơn)

### D. Risk/Reward
- **Before:** TP=3%, SL=1.5% (2:1 fixed)
- **After:** Dynamic R:R ≥ 2:1 dựa trên ATR
- **Benefit:** Adaptive theo volatility

### E. Position Sizing
- **Before:** Fixed % of balance
- **After:** Kelly Criterion + Dynamic adjustment
- **Benefit:** Maximize long-term growth, reduce drawdown

---

## 6. 🚦 Next Steps (Phase 2)

### Not implemented yet (đã đề xuất nhưng chưa làm):

1. **Ensemble với LightGBM & CatBoost**
   - Hiện tại: LSTM + XGBoost
   - Cần thêm: LightGBM, CatBoost
   - File: `ml/ensemble.py`

2. **Cross-validation với TimeSeriesSplit**
   - Hiện tại: Single train/test split
   - Cần: K-fold time series CV
   - File: `ml/train.py`

3. **Volume Profile Analysis**
   - Point of Control (POC)
   - Value Area High/Low
   - Volume clusters

4. **4H + 1H + 15M Multi-timeframe**
   - Hiện tại: Có cấu trúc nhưng chưa integrate vào bot.py
   - Cần: Update bot.py để fetch multiple timeframes

5. **A/B Testing Framework**
   - Test different parameters
   - Compare strategies
   - Track performance

---

## 7. 🔧 How to Use

### Retrain model với features mới:
```bash
cd /home/user/farmaster
python3 ml/train.py
```

### Test SmartEntryV2:
```bash
python3 tests/test_advanced_entry.py
```

### Run bot với new settings:
```bash
# 1. Copy .env.example to .env và fill API keys
cp .env.example .env
nano .env

# 2. Run bot
python3 bot.py
```

### Monitor performance:
```bash
# Check logs
tail -f logs/bot.log

# Analyze performance
python3 scripts/analyze_performance.py
```

---

## 8. ⚠️ Important Notes

1. **Retrain required:** Phải retrain LSTM model với features mới
2. **Test first:** Test trên testnet trước khi dùng real money
3. **Monitor closely:** Theo dõi trong 1-2 tuần đầu
4. **Adjust parameters:** Fine-tune MIN_ENTRY_SCORE, MIN_RR_RATIO nếu cần

---

## 9. 📈 Success Metrics

Track these metrics sau 2 tuần:

- [ ] Model accuracy > 55%
- [ ] Win rate > 50%
- [ ] Average R:R > 2.0
- [ ] Max drawdown < 15%
- [ ] Signal frequency: 5-10 signals/day
- [ ] Profitable after fees

---

## 10. 🙏 Credits

Based on analysis và đề xuất từ user, addressing:
- VẤN ĐỀ #1: Model Accuracy thấp
- VẤN ĐỀ #2: Signal Frequency thấp
- VẤN ĐỀ #3: Entry Timing chưa tối ưu
- VẤN ĐỀ #4: Risk Management cần cải thiện

Implemented by: Claude Code
Date: 2025-11-26
