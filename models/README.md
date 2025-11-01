# 🧠 Models Directory

This directory contains trained machine learning models.

## 📁 Files

After training, you will find:

### `lstm_model.pt`
- **Type:** PyTorch model weights
- **Size:** ~500KB
- **Contains:** LSTM neural network parameters
- **Created by:** `python ml/train.py`

### `scaler.pkl`
- **Type:** Scikit-learn StandardScaler
- **Size:** ~10KB
- **Contains:** Feature scaling parameters
- **Created by:** `python ml/train.py`

## 🎓 Training

### Create Models
```bash
# Train new model
python ml/train.py
```

This will:
1. Fetch historical data from Coingecko
2. Calculate technical indicators
3. Create training sequences
4. Train LSTM model
5. Save model to `models/lstm_model.pt`
6. Save scaler to `models/scaler.pkl`

### Retrain
```bash
# Backup old model
cp models/lstm_model.pt models/lstm_model_backup.pt

# Train new
python ml/train.py

# Compare performance
python run_backtest.py
```

## 📊 Model Info

### Architecture
- **Input:** (batch, 60, 14)
  - 60 timesteps
  - 14 features
- **LSTM:** 2 layers, 64 hidden units
- **Output:** (batch, 1) - Probability of UP

### Features (14)
1. Open
2. High
3. Low
4. Close
5. Volume
6. RSI
7. MACD
8. MACD Signal
9. MACD Histogram
10. Bollinger Upper
11. Bollinger Middle
12. Bollinger Lower
13. Bollinger Width
14. Order Book Imbalance

### Performance
- **Training Accuracy:** 60-70%
- **Test Accuracy:** 55-65%
- **Training Time:** 5-10 minutes (CPU)

## 🔄 Model Lifecycle

### When to Retrain
- **Weekly:** Recommended
- **Monthly:** Minimum
- **After major market changes**
- **When performance degrades**

### Backup Strategy
```bash
# Daily backup
cp models/lstm_model.pt models/backup/lstm_$(date +%Y%m%d).pt

# Keep last 7 days
find models/backup/ -name "lstm_*.pt" -mtime +7 -delete
```

## 🛡️ Model Versioning

### Naming Convention
```
lstm_model.pt              # Current production model
lstm_model_backup.pt       # Previous version
lstm_model_20240101.pt     # Dated backup
lstm_model_v2.pt           # Version 2
```

### Git Ignore
Models are ignored by Git (see `.gitignore`):
```
models/*.pt
models/*.pkl
```

**Reason:** Models are large binary files, should be stored separately.

## 📥 Download Pre-trained

If you don't want to train:
1. Download from releases
2. Place in `models/` directory
3. Verify with `python -c "from ml.lstm_model import LSTMTrainer; t = LSTMTrainer(14); t.load()"`

## 🧪 Testing Model

```bash
# Test loading
python -c "from ml.lstm_model import LSTMTrainer; t = LSTMTrainer(14); t.load(); print('Model OK')"

# Test prediction
python scripts/test_signal.py
```

## 📊 Model Metrics

Track these metrics:
- **Accuracy:** >55%
- **Precision:** >60%
- **Recall:** >50%
- **F1 Score:** >55%

## 🔧 Customization

### Change Architecture
Edit `ml/lstm_model.py`:
```python
trainer = LSTMTrainer(
    input_size=14,
    hidden_size=128,  # Increase from 64
    num_layers=3      # Increase from 2
)
```

### Add Features
Edit `ml/features.py`:
```python
# Add new feature
df['new_feature'] = calculate_new_feature(df)

# Update FEATURE_COLUMNS
FEATURE_COLUMNS = [..., 'new_feature']
```

Then retrain!

## ⚠️ Important Notes

1. **Don't delete models while bot is running**
2. **Always backup before retraining**
3. **Test new models on testnet first**
4. **Keep at least one backup**
5. **Models are specific to feature set**

## 📞 Troubleshooting

### "Model not found"
```bash
# Train model
python ml/train.py
```

### "Model load error"
```bash
# Check file exists
ls -la models/

# Retrain
python ml/train.py
```

### "Scaler not found"
```bash
# Retrain (creates both model and scaler)
python ml/train.py
```

---

**Remember:** Good models = Good performance! 🚀

