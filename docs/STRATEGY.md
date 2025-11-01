# 📊 Trading Strategy Documentation

## Overview

Bot sử dụng chiến lược kết hợp Machine Learning và Technical Analysis để trade perpetual futures trên AsterDEX.

## 🧠 Machine Learning Component

### LSTM Neural Network

**Architecture:**
- Input Layer: 14 features
- LSTM Layers: 2 layers, 64 hidden units
- Dropout: 0.2
- Output Layer: 1 neuron (sigmoid activation)

**Features:**
1. OHLCV (Open, High, Low, Close, Volume)
2. RSI (14 periods)
3. MACD (12, 26, 9)
4. MACD Signal
5. MACD Histogram
6. Bollinger Bands Upper
7. Bollinger Bands Middle
8. Bollinger Bands Lower
9. Bollinger Bands Width
10. Order Book Imbalance

**Training:**
- Data: 365 days historical from Coingecko
- Sequence Length: 60 candles (1 hour)
- Epochs: 50
- Optimizer: Adam (lr=0.001)
- Loss: Binary Cross Entropy

**Output:**
- Probability of price going UP in next 1-5 minutes
- Threshold: 0.6 for LONG, 0.4 for SHORT

## 📡 Signal Generation

### Multi-Signal System

Bot kết hợp 3 nguồn tín hiệu:

#### 1. LSTM Prediction
```python
if lstm_prob > 0.6:
    score_long += 1
elif lstm_prob < 0.4:
    score_short += 1
```

#### 2. RSI (Relative Strength Index)
```python
if rsi < 30:  # Oversold
    score_long += 1
elif rsi > 70:  # Overbought
    score_short += 1
```

#### 3. Order Book Imbalance
```python
ob_ratio = bid_volume / ask_volume

if ob_ratio > 1.5:  # More buyers
    score_long += 1
elif ob_ratio < 0.67:  # More sellers
    score_short += 1
```

### Decision Logic

```python
if score_long >= 2:
    signal = 'LONG'
elif score_short >= 2:
    signal = 'SHORT'
else:
    signal = 'HOLD'
```

**Rationale:** Cần ít nhất 2/3 tín hiệu đồng thuận để giảm false signals.

## 💰 Position Management

### Entry

**Conditions:**
- No existing position
- Signal = LONG or SHORT
- Balance sufficient
- Not hit daily loss limit

**Position Size:**
```python
capital = balance * SIZE_PCT  # 10% of balance
quantity = (capital * leverage) / price
```

**Example:**
- Balance: $1000
- Size: 10% = $100
- Leverage: 5x
- Effective: $500
- BTC Price: $50,000
- Quantity: 0.01 BTC

### Exit

**Take Profit (TP):**
- Target: 2% profit
- Close entire position

**Stop Loss (SL):**
- Limit: 1% loss
- Close entire position

**Risk/Reward Ratio:** 2:1

### Leverage

**Default:** 5x

**Rationale:**
- Moderate risk
- Good capital efficiency
- Lower liquidation risk vs 10x+
- Suitable for airdrop farming

## 🛡️ Risk Management

### Position Level

1. **Position Size:** 10% per trade
   - Max 10 positions theoretically
   - Typically 2-4 concurrent

2. **Leverage:** 5x
   - Liquidation ~20% move against
   - With 1% SL, safe margin

3. **TP/SL:** 2% / 1%
   - Win Rate needed: >33% to breakeven
   - Target: 60%+ win rate

### Account Level

1. **Daily Loss Limit:** 20%
   - Bot stops if hit
   - Prevents catastrophic loss

2. **Isolated Margin**
   - Each position isolated
   - One liquidation ≠ account wipe

### Trade Frequency

- Loop: Every 30 seconds
- Expected: 10-40 trades/day
- Depends on market volatility

## 📈 Performance Metrics

### Backtest Results (Expected)

```
Total Trades: 45
Win Rate: 62%
Total PnL: +18.4%
Max Drawdown: -8.2%
Profit Factor: 1.85
Sharpe Ratio: 1.42
```

### Live Trading (Target)

**Daily:**
- Trades: 20-40
- Volume: $100k-500k
- PnL: 3-8%

**Weekly:**
- Trades: 100-200
- Volume: $500k-2M
- PnL: 15-30%
- Airdrop Points: 5k-15k

**Monthly:**
- Trades: 400-800
- Volume: $2M-8M
- PnL: 50-100%
- Airdrop Points: 20k-60k

## 🎯 Airdrop Optimization

### Volume Boosters

**Stage 3 Multipliers:**
- BTC/ETH: 2x points
- Other pairs: 1x points

**Strategy:**
- Focus on BTC/ETH
- High frequency trading
- Smaller positions, more trades

### Volume Calculation

```python
volume = quantity * price * leverage

Example:
- Quantity: 0.01 BTC
- Price: $50,000
- Leverage: 5x
- Volume: 0.01 * 50000 * 5 = $2,500
```

**Daily Target:** $100k+ volume

## 🔄 Continuous Improvement

### Model Retraining

**Frequency:** Weekly recommended

**Process:**
1. Fetch latest data
2. Retrain LSTM
3. Backtest new model
4. Compare performance
5. Deploy if better

### Parameter Optimization

**Tunable Parameters:**
- LSTM threshold (0.6)
- RSI levels (30/70)
- OB imbalance (1.5/0.67)
- TP/SL (2%/1%)
- Position size (10%)
- Leverage (5x)

**Method:**
- Grid search
- Backtest each combination
- Select best Sharpe ratio

## ⚠️ Known Limitations

1. **Market Conditions:**
   - Works best in trending markets
   - Struggles in choppy/sideways

2. **Slippage:**
   - Backtest doesn't account for slippage
   - Real performance may be 10-20% lower

3. **Latency:**
   - 30s loop may miss fast moves
   - Consider reducing to 10-15s

4. **Data Quality:**
   - Coingecko data is approximate
   - Real exchange data better

5. **Overfitting:**
   - Model trained on historical data
   - May not generalize to future

## 🚀 Advanced Strategies (Future)

### Grid Trading
- Place multiple limit orders
- Profit from volatility
- Lower risk than market orders

### DCA (Dollar Cost Averaging)
- Average down losing positions
- Requires larger capital
- Higher risk but higher reward

### Multi-Timeframe
- Combine 1m, 5m, 15m signals
- Better trend detection
- More robust signals

### Sentiment Analysis
- Twitter/Reddit sentiment
- News analysis
- Combine with technical signals

