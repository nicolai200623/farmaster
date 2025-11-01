# ⚡ Optimization Guide

Hướng dẫn tối ưu hóa bot để đạt performance tốt nhất.

## 📊 Performance Tuning

### 1. Signal Thresholds

#### LSTM Threshold
```env
# Conservative (ít trade, chất lượng cao)
LSTM_THRESHOLD=0.7

# Moderate (default)
LSTM_THRESHOLD=0.6

# Aggressive (nhiều trade, rủi ro cao)
LSTM_THRESHOLD=0.5
```

**Recommendation:** Start với 0.6, tăng lên 0.7 nếu win rate thấp.

#### RSI Levels
```env
# Conservative
RSI_OVERSOLD=25
RSI_OVERBOUGHT=75

# Moderate (default)
RSI_OVERSOLD=30
RSI_OVERBOUGHT=70

# Aggressive
RSI_OVERSOLD=35
RSI_OVERBOUGHT=65
```

#### Order Book Imbalance
```env
# Conservative
OB_IMBALANCE_LONG=2.0
OB_IMBALANCE_SHORT=0.5

# Moderate (default)
OB_IMBALANCE_LONG=1.5
OB_IMBALANCE_SHORT=0.67

# Aggressive
OB_IMBALANCE_LONG=1.2
OB_IMBALANCE_SHORT=0.8
```

### 2. Risk Parameters

#### Position Size
```env
# Conservative (5%)
SIZE_PCT=0.05

# Moderate (10%, default)
SIZE_PCT=0.1

# Aggressive (20%)
SIZE_PCT=0.2
```

**Impact:**
- Smaller size = Lower risk, lower profit
- Larger size = Higher risk, higher profit

#### Leverage
```env
# Conservative
LEVERAGE=3

# Moderate (default)
LEVERAGE=5

# Aggressive
LEVERAGE=10
```

**Warning:** Leverage >10x rất rủi ro!

#### TP/SL Ratio
```env
# Conservative (3:1)
TP_PCT=0.03
SL_PCT=0.01

# Moderate (2:1, default)
TP_PCT=0.02
SL_PCT=0.01

# Aggressive (1.5:1)
TP_PCT=0.015
SL_PCT=0.01
```

**Recommendation:** Maintain TP:SL ≥ 2:1

### 3. Trading Frequency

#### Loop Sleep
```env
# Low frequency (1 phút)
LOOP_SLEEP=60

# Moderate (30s, default)
LOOP_SLEEP=30

# High frequency (10s)
LOOP_SLEEP=10
```

**Trade-offs:**
- Faster = More trades, more API calls, higher CPU
- Slower = Fewer trades, miss opportunities

### 4. Signal Scoring

Edit `config.py`:
```python
# Require all 3 signals (very conservative)
MIN_SIGNAL_SCORE=3

# Require 2/3 signals (default)
MIN_SIGNAL_SCORE=2

# Require 1/3 signals (aggressive)
MIN_SIGNAL_SCORE=1
```

## 🧠 Model Optimization

### 1. Architecture Tuning

Edit `.env`:
```env
# Smaller model (faster, less accurate)
LSTM_HIDDEN_SIZE=32
LSTM_NUM_LAYERS=1

# Default
LSTM_HIDDEN_SIZE=64
LSTM_NUM_LAYERS=2

# Larger model (slower, more accurate)
LSTM_HIDDEN_SIZE=128
LSTM_NUM_LAYERS=3
```

### 2. Training Parameters

```env
# Quick training
LSTM_EPOCHS=30

# Default
LSTM_EPOCHS=50

# Thorough training
LSTM_EPOCHS=100
```

### 3. Sequence Length

```env
# Short-term (30 min)
SEQUENCE_LENGTH=30

# Default (1 hour)
SEQUENCE_LENGTH=60

# Long-term (2 hours)
SEQUENCE_LENGTH=120
```

### 4. Feature Selection

Edit `ml/features.py` để thêm/bớt features:

```python
# Add EMA
df['ema_20'] = ta.ema(df['close'], length=20)
df['ema_50'] = ta.ema(df['close'], length=50)

# Add ATR
df['atr'] = ta.atr(df['high'], df['low'], df['close'], length=14)

# Add Volume indicators
df['volume_sma'] = ta.sma(df['volume'], length=20)

# Update FEATURE_COLUMNS
FEATURE_COLUMNS = [
    'open', 'high', 'low', 'close', 'volume',
    'rsi', 'macd', 'macd_signal', 'macd_hist',
    'bb_upper', 'bb_middle', 'bb_lower', 'bb_width',
    'ob_imbalance',
    'ema_20', 'ema_50',  # New
    'atr',               # New
    'volume_sma'         # New
]
```

**Note:** Sau khi thay đổi features, phải retrain model!

## 📈 Backtesting Optimization

### Grid Search Parameters

Create `scripts/optimize.py`:

```python
import itertools
from backtest.backtester import Backtester

# Parameter grid
param_grid = {
    'lstm_threshold': [0.5, 0.6, 0.7],
    'rsi_oversold': [25, 30, 35],
    'tp_pct': [0.015, 0.02, 0.025],
    'sl_pct': [0.005, 0.01, 0.015]
}

# Generate combinations
keys = param_grid.keys()
values = param_grid.values()
combinations = list(itertools.product(*values))

best_result = None
best_params = None

for combo in combinations:
    params = dict(zip(keys, combo))
    
    # Update config
    Config.LSTM_THRESHOLD = params['lstm_threshold']
    Config.RSI_OVERSOLD = params['rsi_oversold']
    Config.TP_PCT = params['tp_pct']
    Config.SL_PCT = params['sl_pct']
    
    # Run backtest
    results = backtester.run_backtest(days=30)
    
    # Evaluate (Sharpe ratio or profit factor)
    score = results['profit_factor']
    
    if best_result is None or score > best_result:
        best_result = score
        best_params = params
        print(f"New best: {params} -> {score:.2f}")

print(f"\nBest params: {best_params}")
print(f"Best score: {best_result:.2f}")
```

Run:
```bash
python scripts/optimize.py
```

## 🎯 Symbol Selection

### High Volume Pairs (Better for Airdrop)
```env
SYMBOLS=BTCUSDT,ETHUSDT
```

### Diversification
```env
SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT
```

### Volatility Focus
```env
SYMBOLS=BTCUSDT,ETHUSDT,AVAXUSDT,MATICUSDT
```

**Tip:** Backtest mỗi symbol riêng để tìm best performers.

## 💰 Capital Allocation

### Equal Weight
```python
# 10% per symbol
SIZE_PCT=0.1
SYMBOLS=BTCUSDT,ETHUSDT
# Max 10 positions total
```

### Weighted by Performance
```python
# BTC: 15%, ETH: 10%, Others: 5%
# Implement trong bot.py
```

### Kelly Criterion
```python
# Optimal position size based on win rate
kelly_pct = (win_rate * avg_win - (1 - win_rate) * avg_loss) / avg_win
```

## 🔄 Retraining Strategy

### Frequency
- **Daily:** Nếu market thay đổi nhanh
- **Weekly:** Recommended
- **Monthly:** Minimum

### Rolling Window
```python
# Train với 90 ngày gần nhất
days = 90
```

### Walk-Forward Optimization
1. Train trên 60 ngày
2. Test trên 30 ngày tiếp theo
3. Retrain và repeat

## 📊 Performance Metrics

### Track These Metrics

```python
# Win Rate
win_rate = winning_trades / total_trades

# Profit Factor
profit_factor = gross_profit / gross_loss

# Sharpe Ratio
sharpe = (avg_return - risk_free_rate) / std_return

# Max Drawdown
max_dd = max(peak - trough) / peak

# Recovery Factor
recovery = net_profit / max_dd
```

### Target Metrics
- Win Rate: >55%
- Profit Factor: >1.5
- Sharpe Ratio: >1.0
- Max Drawdown: <15%

## 🚀 Advanced Strategies

### 1. Multi-Timeframe

```python
# Combine 1m, 5m, 15m signals
signal_1m = generate_signal(client, symbol, '1m')
signal_5m = generate_signal(client, symbol, '5m')
signal_15m = generate_signal(client, symbol, '15m')

# Trade only if all agree
if signal_1m == signal_5m == signal_15m:
    execute_trade()
```

### 2. Ensemble Models

```python
# Train multiple models
model_lstm = LSTMPredictor()
model_gru = GRUPredictor()
model_transformer = TransformerPredictor()

# Average predictions
pred = (model_lstm.predict(X) + 
        model_gru.predict(X) + 
        model_transformer.predict(X)) / 3
```

### 3. Adaptive Parameters

```python
# Adjust based on volatility
if volatility > threshold:
    SIZE_PCT *= 0.5  # Reduce size
    SL_PCT *= 1.5    # Wider stop loss
```

### 4. Market Regime Detection

```python
# Detect trending vs ranging
if adx > 25:
    # Trending market - use trend following
    strategy = 'trend'
else:
    # Ranging market - use mean reversion
    strategy = 'mean_reversion'
```

## 🔍 Monitoring & Analysis

### Daily Review
```bash
# Check performance
python scripts/check_balance.py

# Review trades
tail -100 logs/bot_*.log | grep "TRADE"

# Calculate metrics
python scripts/analyze_performance.py
```

### Weekly Optimization
1. Review win rate
2. Analyze losing trades
3. Adjust parameters
4. Backtest changes
5. Deploy if better

## ⚠️ Common Pitfalls

### 1. Overfitting
- **Problem:** Model quá fit với historical data
- **Solution:** Use validation set, cross-validation

### 2. Over-optimization
- **Problem:** Quá nhiều parameters, curve fitting
- **Solution:** Keep it simple, test out-of-sample

### 3. Ignoring Fees
- **Problem:** Backtest không tính fees
- **Solution:** Subtract 0.04% per trade

### 4. Survivorship Bias
- **Problem:** Chỉ test symbols còn tồn tại
- **Solution:** Include delisted pairs

### 5. Look-ahead Bias
- **Problem:** Dùng future data
- **Solution:** Strict time-based split

## 📈 Expected Improvements

### After Optimization
- Win Rate: 55% → 65%
- Profit Factor: 1.5 → 2.0
- Sharpe Ratio: 1.0 → 1.5
- Max Drawdown: 15% → 10%

### Realistic Goals
- **Month 1:** Break even, learn system
- **Month 2:** 10-20% profit
- **Month 3+:** 20-40% profit/month

## 🎓 Learning Resources

- **Books:**
  - "Advances in Financial Machine Learning" - Marcos López de Prado
  - "Algorithmic Trading" - Ernest Chan

- **Courses:**
  - Coursera: Machine Learning for Trading
  - Udemy: Algorithmic Trading with Python

- **Communities:**
  - QuantConnect Forum
  - /r/algotrading
  - TradingView Scripts

---

**Remember:** Optimization là quá trình liên tục. Test, measure, improve! 🚀

