# 📝 CHEAT SHEET - LỆNH NHANH

## 🚀 Setup Nhanh (Lần Đầu)

```bash
# 1. Cài đặt
pip install -r requirements.txt

# 2. Cấu hình
cp .env.example .env
# Sửa API_KEY, API_SECRET, và XAI_API_KEY trong .env

# 3. Validate
python -c "from config import Config; Config.validate()"

# 4. Train models (3 models: XGBoost, LightGBM, CatBoost)
python ml/train_ensemble.py --days 180

# 5. Backtest Entry Pipeline
python backtest_pipeline.py --days 30

# 6. Chạy bot
python bot.py
```

---

## 🧠 Training Models (3 Models)

> **Lưu ý:** Hệ thống sử dụng 3 models: XGBoost (40%), LightGBM (35%), CatBoost (25%)
> LSTM đã được loại bỏ để tối ưu hiệu suất.

```bash
# Train 3 models ensemble (KHUYẾN NGHỊ)
# 180 ngày (~10-15 phút) - Tốt nhất cho accuracy
python ml/train_ensemble.py --days 180

# Train với ít data hơn (nhanh hơn)
python ml/train_ensemble.py --days 90

# Kiểm tra models đã train
python -c "
from ml.ensemble import EnsemblePredictor
from config import Config
from ml.features import FeatureEngine

p = EnsemblePredictor(
    models=Config.ENSEMBLE_MODELS,
    weights=Config.ENSEMBLE_WEIGHTS,
    input_size=len(FeatureEngine.FEATURE_COLUMNS)
)
if p.load_models():
    print('OK! Models loaded:', list(p.models.keys()))
else:
    print('FAILED! Models not found')
"

# Verify model files exist
# Windows
dir models\*.json models\*.txt models\*.cbm models\*.pkl

# Linux/Mac
ls -lh models/
```

### Expected Model Files:
```
models/
├── xgboost_model.json      (~574 KB)
├── xgboost_scaler.pkl      (~1 KB)
├── lightgbm_model.txt      (~197 KB)
├── lightgbm_scaler.pkl     (~1 KB)
├── catboost_model.cbm      (~16 KB)
└── catboost_scaler.pkl     (~1 KB)
```

---

## � Entry Pipeline (5-Stage Validation)

> **NEW!** Entry Pipeline thay thế SmartEntryV2 với 5 stages validation

### Pipeline Flow:
```
Signal → Stage 1 (ML) → Stage 2 (Smart Entry) → Stage 3 (Price Action)
      → Stage 4 (HTF) → Stage 5 (AI Check) → ENTRY
```

### 5 Stages:

| Stage | Name | Description | Config |
|-------|------|-------------|--------|
| 1 | **ML Ensemble** | 3 models vote (XGBoost 40%, LightGBM 35%, CatBoost 25%) | `ML_CONFIDENCE_THRESHOLD=0.62` |
| 2 | **Smart Entry** | Confluence scoring (EMA, RSI, volume, session) | `MIN_ENTRY_SCORE=5` |
| 3 | **Price Action** | S/R levels, candlestick patterns, volume | `MIN_PRICE_ACTION_SCORE=5` |
| 4 | **HTF Alignment** | Higher timeframe trend confirmation | `USE_HTF_ALIGNMENT=True` |
| 5 | **AI Quick Check** | Grok/Claude/OpenAI/Gemini analysis | `AI_PROVIDER=grok` |

### Test Entry Pipeline:
```bash
python -c "
from trading.signal_generator import SignalGenerator
from ml.ensemble import EnsemblePredictor
from config import Config
from ml.features import FeatureEngine

predictor = EnsemblePredictor(
    models=Config.ENSEMBLE_MODELS,
    weights=Config.ENSEMBLE_WEIGHTS,
    input_size=len(FeatureEngine.FEATURE_COLUMNS)
)
predictor.load_models()

sg = SignalGenerator(predictor)
if sg.entry_pipeline:
    print('Entry Pipeline: OK')
    print('  ML Stage models:', list(sg.entry_pipeline.ml_stage.models.keys()))
    print('  Confidence threshold:', sg.entry_pipeline.ml_stage.confidence_threshold)
else:
    print('Entry Pipeline: NOT INITIALIZED')
"
```

---

## 📊 Backtest

```bash
# Backtest Entry Pipeline (KHUYẾN NGHỊ)
python backtest_pipeline.py --days 30

# Backtest với optimization
python backtest_pipeline.py --days 60 --optimize

# Quick test signal
python -c "
from trading.signal_generator import SignalGenerator
from ml.ensemble import EnsemblePredictor
from config import Config
from ml.features import FeatureEngine

predictor = EnsemblePredictor(
    models=Config.ENSEMBLE_MODELS,
    weights=Config.ENSEMBLE_WEIGHTS,
    input_size=len(FeatureEngine.FEATURE_COLUMNS)
)
predictor.load_models()
sg = SignalGenerator(predictor)
print('Signal Generator ready!')
print('Entry Pipeline:', 'Enabled' if sg.entry_pipeline else 'Disabled')
"
```

---

## 🤖 Chạy Bot

```bash
# Chạy bot (kiểm tra TESTNET_MODE trong .env trước!)
python bot.py

# Background (Linux/Mac)
nohup python bot.py > bot.log 2>&1 &

# Screen (Linux/Mac) - KHUYẾN NGHỊ cho VPS
screen -S farmbot
python bot.py
# Ctrl+A, D để detach
# screen -r farmbot để attach lại

# Tmux alternative
tmux new -s farmbot
python bot.py
# Ctrl+B, D để detach
# tmux attach -t farmbot để attach lại

# Systemd (VPS production)
sudo systemctl start asterdex-bot
sudo systemctl stop asterdex-bot
sudo systemctl restart asterdex-bot
sudo systemctl status asterdex-bot
```

---

## 👀 Monitoring

```bash
# Xem logs real-time
tail -f logs/bot_*.log

# Xem logs systemd
sudo journalctl -u asterdex-bot -f

# Check balance
python scripts/check_balance.py

# Test signals
python scripts/test_signal.py

# Check positions
python -c "from trading.asterdex_client import AsterDEXClient; c=AsterDEXClient(); print(c.get_all_positions())"

# Analyze performance
python scripts/analyze_performance.py
```

---

## 🔧 Utilities

```bash
# Validate config
python -c "from config import Config; Config.validate()"

# Test connections
python test_connections.py

# Check symbols
python check_symbols.py

# Test position size
python test_position_size.py

# Close all positions
python scripts/close_all.py
```

---

## 🛑 Stop Bot

```bash
# Ctrl+C (nếu chạy foreground)

# Kill process
pkill -f bot.py

# Systemd
sudo systemctl stop asterdex-bot

# Screen
screen -r asterdex-bot
# Ctrl+C
```

---

## ⚙️ Cấu Hình Nhanh

### Áp dụng volume farming config
```bash
python scripts/apply_volume_farming_config.py
```

### Sửa .env thủ công
```bash
# Windows
notepad .env

# Linux/Mac
nano .env
# hoặc
vim .env
```

### Backup/Restore config
```bash
# Backup
cp .env .env.backup_$(date +%Y%m%d)

# Restore
cp .env.backup_YYYYMMDD .env
```

---

## 🔍 System Readiness Check

### Kiểm tra toàn bộ hệ thống (KHUYẾN NGHỊ)
```bash
# Check models + pipeline + API trong 1 command
python -c "
import os
from datetime import datetime

print('='*50)
print('SYSTEM READINESS CHECK')
print('='*50)

# 1. Model files
print('\n[1] MODEL FILES:')
models = ['xgboost_model.json', 'xgboost_scaler.pkl',
          'lightgbm_model.txt', 'lightgbm_scaler.pkl',
          'catboost_model.cbm', 'catboost_scaler.pkl']
all_ok = True
for m in models:
    path = os.path.join('models', m)
    if os.path.exists(path):
        size = os.path.getsize(path) / 1024
        print(f'  OK: {m} ({size:.1f} KB)')
    else:
        print(f'  MISSING: {m}')
        all_ok = False
print(f'  Status: {\"READY\" if all_ok else \"INCOMPLETE\"}')

# 2. Load test
print('\n[2] ML MODELS LOAD:')
from config import Config
from ml.ensemble import EnsemblePredictor
from ml.features import FeatureEngine
p = EnsemblePredictor(Config.ENSEMBLE_MODELS, Config.ENSEMBLE_WEIGHTS, len(FeatureEngine.FEATURE_COLUMNS))
if p.load_models():
    print(f'  OK: {len(p.models)} models loaded')
else:
    print('  FAILED!')

# 3. Entry Pipeline
print('\n[3] ENTRY PIPELINE:')
from trading.signal_generator import SignalGenerator
sg = SignalGenerator(p)
if sg.entry_pipeline:
    ml_models = list(sg.entry_pipeline.ml_stage.models.keys())
    print(f'  OK: Pipeline initialized with {len(ml_models)} ML models')
else:
    print('  FAILED!')

# 4. API Connection
print('\n[4] API CONNECTION:')
from trading.asterdex_client import AsterDEXClient
c = AsterDEXClient()
balance = c.get_account_balance()
print(f'  OK: Balance = \${balance:.2f} USDT')

print('\n' + '='*50)
print('ALL CHECKS PASSED!' if all_ok else 'SOME CHECKS FAILED!')
print('='*50)
"
```

### Kiểm tra models đã train (3 models)
```bash
# Windows
dir models\*.json models\*.txt models\*.cbm models\*.pkl

# Linux/Mac
ls -lh models/

# Phải có 6 files:
# - xgboost_model.json + xgboost_scaler.pkl
# - lightgbm_model.txt + lightgbm_scaler.pkl
# - catboost_model.cbm + catboost_scaler.pkl
```

### Kiểm tra config
```bash
# Xem config hiện tại
python -c "from config import Config; print(f'Symbols: {Config.SYMBOLS}'); print(f'Leverage: {Config.LEVERAGE}'); print(f'TP: {Config.TP_PCT}%'); print(f'SL: {Config.SL_PCT}')"

# Kiểm tra API keys
python -c "from config import Config; print('API_KEY:', Config.API_KEY[:10]+'...'); print('API_SECRET:', Config.API_SECRET[:10]+'...')"
```

### Test API connection
```bash
python -c "from trading.asterdex_client import AsterDEXClient; c=AsterDEXClient(); print('Balance:', c.get_account_balance())"
```

---

## 📈 Tối Ưu Hóa

### Tăng số lượng trades (giảm filter)
```env
# Sửa .env:
ML_CONFIDENCE_THRESHOLD=0.55    # Giảm từ 0.62
MIN_ENTRY_SCORE=4               # Giảm từ 5
MIN_PRICE_ACTION_SCORE=4        # Giảm từ 5
LOOP_SLEEP=120                  # Tăng tần suất check
```

### Tăng win rate (strict filters)
```env
# Sửa .env:
ML_CONFIDENCE_THRESHOLD=0.65    # Tăng từ 0.62
MIN_ENTRY_SCORE=7               # Tăng từ 5
MIN_PRICE_ACTION_SCORE=6        # Tăng từ 5
USE_AI_CHECK=True               # Bật AI validation
```

### Giảm risk
```env
# Sửa .env:
POSITION_SIZE_USDT=5            # Giảm từ 10
LEVERAGE=5                      # Giảm từ 10
DAILY_LOSS_LIMIT=0.1            # 10% max daily loss
TRAILING_ACTIVATION_PCT=2.0     # Activate trailing sớm hơn
```

### Trailing Stop tối ưu
```env
# Conservative (bảo toàn profit)
TRAILING_ACTIVATION_PCT=2.0     # Activate sớm
TRAILING_DISTANCE_PCT=1.5       # Trail gần

# Aggressive (maximize profit)
TRAILING_ACTIVATION_PCT=3.5     # Activate muộn
TRAILING_DISTANCE_PCT=2.5       # Trail xa
```

---

## 🐛 Troubleshooting

### "All model predictions failed!"
```bash
# Nguyên nhân: Models chưa load hoặc không có
# Solution: Kiểm tra model files và reload
python ml/train_ensemble.py --days 180
```

### Không có tín hiệu (No signals)
```bash
# Giảm ML threshold
# Sửa .env: ML_CONFIDENCE_THRESHOLD=0.55

# Hoặc giảm entry score requirements
# Sửa .env: MIN_ENTRY_SCORE=4
```

### Entry Pipeline not working
```bash
# Kiểm tra pipeline đã khởi tạo
python -c "
from trading.signal_generator import SignalGenerator
from ml.ensemble import EnsemblePredictor
from config import Config
from ml.features import FeatureEngine

p = EnsemblePredictor(Config.ENSEMBLE_MODELS, Config.ENSEMBLE_WEIGHTS, len(FeatureEngine.FEATURE_COLUMNS))
p.load_models()
sg = SignalGenerator(p)
print('Pipeline:', sg.entry_pipeline)
print('ML Stage:', sg.entry_pipeline.ml_stage if sg.entry_pipeline else 'N/A')
"
```

### Margin insufficient
```bash
# Giảm position size hoặc số symbols
# Sửa .env:
POSITION_SIZE_USDT=5
SYMBOLS=BTCUSDT,ETHUSDT,SOLUSDT,BNBUSDT
```

### API error
```bash
# Test connection
python -c "from trading.asterdex_client import AsterDEXClient; c=AsterDEXClient(); print('Balance:', c.get_account_balance())"

# Kiểm tra API keys
python -c "from config import Config; print('API_KEY:', Config.API_KEY[:10]+'...')"
```

---

## 📁 File Paths

```
FarmAster/
├── .env                          # Cấu hình chính (API keys, settings)
├── bot.py                        # Main bot entry point
├── config.py                     # Config loader
├── backtest_pipeline.py          # Backtest Entry Pipeline
├── paper_trade.py                # Paper trading script
│
├── ml/
│   ├── ensemble.py               # Ensemble predictor (main)
│   ├── train_ensemble.py         # Train 3 models
│   ├── xgboost_model.py          # XGBoost trainer
│   ├── lightgbm_model.py         # LightGBM trainer
│   ├── catboost_model.py         # CatBoost trainer
│   └── features.py               # Feature engineering
│
├── trading/
│   ├── asterdex_client.py        # API client (Binance)
│   ├── signal_generator.py       # Signal logic + Pipeline
│   ├── risk_manager.py           # Risk management
│   ├── trailing_stop.py          # Trailing stop manager
│   └── position_tracker.py       # Position tracking
│
├── trading/entry_pipeline/       # 🚀 Entry Pipeline (NEW!)
│   ├── __init__.py               # Pipeline exports
│   ├── pipeline.py               # Main 5-stage pipeline
│   ├── ml_ensemble.py            # Stage 1: ML Ensemble
│   ├── smart_entry.py            # Stage 2: Smart Entry
│   ├── price_action.py           # Stage 3: Price Action
│   ├── htf_alignment.py          # Stage 4: HTF Alignment
│   └── ai_check.py               # Stage 5: AI Check
│
├── models/                       # Trained ML models
│   ├── xgboost_model.json        # XGBoost model
│   ├── xgboost_scaler.pkl        # XGBoost scaler
│   ├── lightgbm_model.txt        # LightGBM model
│   ├── lightgbm_scaler.pkl       # LightGBM scaler
│   ├── catboost_model.cbm        # CatBoost model
│   └── catboost_scaler.pkl       # CatBoost scaler
│
├── utils/
│   ├── logger.py                 # Logging + Telegram
│   └── data_fetcher.py           # Historical data
│
└── logs/                         # Log files
```

---

## 🎯 Workflow Chuẩn

### Lần đầu setup
```bash
1. cp .env.example .env
2. # Sửa API_KEY, API_SECRET, XAI_API_KEY trong .env
3. python -c "from config import Config; Config.validate()"
4. python ml/train_ensemble.py --days 180
5. python backtest_pipeline.py --days 30
6. # Nếu OK -> python bot.py
```

### Hàng ngày
```bash
1. tail -f logs/bot_*.log
2. # Kiểm tra Telegram notifications
3. # Monitor open positions
```

### Hàng tuần
```bash
1. # Đánh giá win rate, PnL
2. # Điều chỉnh thresholds nếu cần
3. # Check model performance
```

### Khi cần retrain
```bash
1. python ml/train_ensemble.py --days 180
2. python backtest_pipeline.py --days 30
3. # So sánh với kết quả cũ
4. # Nếu tốt hơn -> restart bot
```

---

## 💡 Tips

```bash
# Xem log 100 dòng cuối
tail -n 100 logs/bot_*.log

# Tìm lỗi trong log
grep -i error logs/bot_*.log

# Đếm số trades
grep "Position opened" logs/bot_*.log | wc -l

# Xem tất cả TP
grep "TP (" logs/bot_*.log

# Xem tất cả SL (không nên có nếu SL_PCT=0)
grep "SL (" logs/bot_*.log

# Kiểm tra bot có đang chạy không
ps aux | grep bot.py

# Xem CPU/Memory usage
top -p $(pgrep -f bot.py)
```

---

## 🚨 Emergency Commands

```bash
# STOP BOT NGAY
pkill -9 -f bot.py

# ĐÓNG TẤT CẢ POSITIONS
python scripts/close_all.py

# RESTORE CONFIG
cp .env.backup .env

# RESTART BOT
pkill -f bot.py && sleep 2 && python bot.py &
```

---

## �️ VPS Deployment

### Files cần copy lên VPS:
```bash
# Minimum required files (~2-3 MB):
FarmAster/
├── .env                    # Config (UPDATE API KEYS!)
├── bot.py
├── config.py
├── requirements.txt
│
├── models/                 # Trained models (~0.8 MB)
│   ├── xgboost_model.json
│   ├── xgboost_scaler.pkl
│   ├── lightgbm_model.txt
│   ├── lightgbm_scaler.pkl
│   ├── catboost_model.cbm
│   └── catboost_scaler.pkl
│
├── ml/                     # All files
├── trading/                # All files (including entry_pipeline/)
└── utils/                  # All files
```

### Deploy từ Windows lên VPS:
```bash
# 1. Compress project (Windows)
# Zip toàn bộ folder FarmAster

# 2. Upload lên VPS
scp FarmAster.zip user@your-vps:/home/user/

# 3. SSH vào VPS
ssh user@your-vps

# 4. Unzip và setup
cd /home/user
unzip FarmAster.zip
cd FarmAster

# 5. Install Python 3.11+ và dependencies
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 6. Update .env với API keys
nano .env

# 7. Test system
python -c "from config import Config; Config.validate()"
python -c "from ml.ensemble import EnsemblePredictor; print('ML OK')"

# 8. Run bot với screen
screen -S farmbot
python bot.py
# Ctrl+A, D để detach
```

### Copy models đã train (không cần train lại):
```bash
# Từ Windows, copy folder models/ lên VPS:
scp -r models/ user@your-vps:/home/user/FarmAster/

# Verify trên VPS:
ls -lh models/
# Phải có 6 files: xgboost_*, lightgbm_*, catboost_*
```

### Systemd service (production):
```bash
# Tạo service file
sudo nano /etc/systemd/system/farmbot.service

# Nội dung:
[Unit]
Description=FarmAster Trading Bot
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/home/user/FarmAster
ExecStart=/home/user/FarmAster/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target

# Enable và start
sudo systemctl daemon-reload
sudo systemctl enable farmbot
sudo systemctl start farmbot
sudo systemctl status farmbot
```

---

## �📞 Support Commands

```bash
# Xem version Python
python --version

# Xem packages đã cài
pip list

# Kiểm tra disk space
df -h

# Kiểm tra memory
free -h

# Xem network
netstat -an | grep ESTABLISHED
```

---

## ⚙️ Config Reference (.env)

### Entry Pipeline Settings:
```env
# Master switch
USE_ENTRY_PIPELINE=True

# Stage 1: ML Ensemble
ENSEMBLE_MODELS=xgboost,lightgbm,catboost
ENSEMBLE_WEIGHTS=0.40,0.35,0.25
ML_CONFIDENCE_THRESHOLD=0.62

# Stage 2: Smart Entry
MIN_ENTRY_SCORE=5
MIN_RR_RATIO=0

# Stage 3: Price Action
USE_PRICE_ACTION=True
MIN_PRICE_ACTION_SCORE=5
SR_LOOKBACK_CANDLES=50
VOLUME_CONFIRMATION_RATIO=1.5

# Stage 4: HTF Alignment
USE_HTF_ALIGNMENT=True
HTF_STRICT_MODE=False

# Stage 5: AI Check
USE_AI_CHECK=True
AI_PROVIDER=grok
AI_CHECK_BORDERLINE_ONLY=True
```

### Trailing Stop Settings:
```env
USE_TRAILING_STOP=True
USE_PNL_BASED_TRAILING=True
TRAILING_ACTIVATION_PCT=2.5      # % PnL to activate
TRAILING_DISTANCE_PCT=2.2        # % PnL trail distance
USE_BREAKEVEN_STOP=True
BREAKEVEN_ACTIVATION_PCT=2.5
BREAKEVEN_OFFSET_PCT=0.4
```

### AI Provider API Keys:
```env
# Grok (recommended)
XAI_API_KEY=xai-xxx...

# Alternatives
ANTHROPIC_API_KEY=sk-ant-xxx...
OPENAI_API_KEY=sk-xxx...
GOOGLE_API_KEY=xxx...
```

---

**Lưu file này để tra cứu nhanh! 📌**

*Last updated: 2025-12-06*

