# 🧠 Machine Learning Module

Module chứa LSTM model và feature engineering.

## Files

### `features.py`
Feature engineering - tính toán technical indicators.

**Features:**
- OHLCV (Open, High, Low, Close, Volume)
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)
- Bollinger Bands
- Order Book Imbalance

**Usage:**
```python
from ml.features import FeatureEngine

# Calculate indicators
df = FeatureEngine.calculate_indicators(df)

# Prepare features
features = FeatureEngine.prepare_features(df)

# Create sequences for LSTM
X, y = FeatureEngine.create_sequences(data, seq_length=60)
```

### `lstm_model.py`
LSTM Neural Network model.

**Architecture:**
- Input: (batch, 60, 14)
- LSTM: 2 layers, 64 hidden units
- Output: (batch, 1) - Probability of UP

**Usage:**
```python
from ml.lstm_model import LSTMTrainer

# Initialize
trainer = LSTMTrainer(input_size=14)

# Train
trainer.train(X_train, y_train, epochs=50)

# Predict
prob = trainer.predict(X_test)

# Save/Load
trainer.save()
trainer.load()
```

### `train.py`
Training script.

**Usage:**
```bash
python ml/train.py
```

**Process:**
1. Fetch historical data from Coingecko
2. Calculate indicators
3. Create sequences
4. Train LSTM
5. Evaluate on test set
6. Save model

## Model Files

After training, models are saved to `models/`:
- `lstm_model.pt` - PyTorch model weights
- `scaler.pkl` - Feature scaler

## Customization

### Add New Features

Edit `features.py`:
```python
# Add EMA
df['ema_20'] = ta.ema(df['close'], length=20)

# Update FEATURE_COLUMNS
FEATURE_COLUMNS = [..., 'ema_20']
```

### Change Model Architecture

Edit `lstm_model.py`:
```python
# Larger model
trainer = LSTMTrainer(
    input_size=14,
    hidden_size=128,  # Default: 64
    num_layers=3      # Default: 2
)
```

### Adjust Training

Edit `.env`:
```env
LSTM_EPOCHS=100        # Default: 50
SEQUENCE_LENGTH=120    # Default: 60
```

## Performance

**Expected Accuracy:** 60-70%

**Training Time:**
- CPU: 10-15 minutes
- GPU: 2-5 minutes

**Inference Time:** <10ms per prediction

