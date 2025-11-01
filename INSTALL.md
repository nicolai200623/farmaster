# 📥 Installation Guide

Chi tiết hướng dẫn cài đặt cho mọi hệ điều hành.

## 📋 System Requirements

### Minimum
- **OS:** Windows 10, Ubuntu 18.04, macOS 10.14+
- **CPU:** 1 core
- **RAM:** 1GB
- **Storage:** 2GB free space
- **Python:** 3.8 or higher
- **Internet:** Stable connection

### Recommended
- **OS:** Ubuntu 20.04 LTS
- **CPU:** 2 cores
- **RAM:** 2GB
- **Storage:** 5GB free space
- **Python:** 3.9+
- **Internet:** 10+ Mbps

## 🐍 Python Installation

### Windows

#### Option 1: Official Installer
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Click "Install Now"

#### Option 2: Microsoft Store
```powershell
# Search "Python 3.11" in Microsoft Store
# Click Install
```

#### Verify
```powershell
python --version
pip --version
```

### Ubuntu/Debian

```bash
# Update package list
sudo apt update

# Install Python 3.9+
sudo apt install python3 python3-pip python3-venv -y

# Verify
python3 --version
pip3 --version
```

### macOS

#### Option 1: Homebrew (Recommended)
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.11

# Verify
python3 --version
pip3 --version
```

#### Option 2: Official Installer
1. Download from [python.org](https://www.python.org/downloads/macos/)
2. Run .pkg installer
3. Follow instructions

## 📦 Bot Installation

### Step 1: Clone Repository

#### Using Git
```bash
# Install git if needed
# Ubuntu: sudo apt install git
# Mac: brew install git
# Windows: Download from git-scm.com

# Clone
git clone https://github.com/YOUR_USERNAME/FarmAster.git
cd FarmAster
```

#### Using ZIP
1. Download ZIP from GitHub
2. Extract to folder
3. Open terminal in folder

### Step 2: Create Virtual Environment (Recommended)

#### Windows
```powershell
# Create venv
python -m venv venv

# Activate
venv\Scripts\activate

# You should see (venv) in prompt
```

#### Linux/Mac
```bash
# Create venv
python3 -m venv venv

# Activate
source venv/bin/activate

# You should see (venv) in prompt
```

### Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

**This will install:**
- python-binance (AsterDEX API)
- torch (LSTM model)
- pandas, numpy (Data processing)
- pandas-ta (Technical indicators)
- python-dotenv (Config)
- python-telegram-bot (Notifications)
- requests (HTTP)
- scikit-learn (ML utilities)

### Step 4: Install TA-Lib (Optional but Recommended)

#### Windows

**Option 1: Pre-built Wheel**
1. Download from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib](https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib)
2. Choose correct version:
   - Python 3.11 + 64-bit: `TA_Lib‑0.4.XX‑cp311‑cp311‑win_amd64.whl`
3. Install:
```powershell
pip install TA_Lib-0.4.XX-cp311-cp311-win_amd64.whl
```

**Option 2: Skip**
- Bot will work without TA-Lib
- Some indicators may be slower

#### Ubuntu/Debian
```bash
# Install dependencies
sudo apt-get install build-essential wget -y

# Download and install TA-Lib
cd /tmp
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
sudo make install
sudo ldconfig

# Install Python wrapper
pip install TA-Lib

# Verify
python -c "import talib; print('TA-Lib OK')"
```

#### macOS
```bash
# Install via Homebrew
brew install ta-lib

# Install Python wrapper
pip install TA-Lib

# Verify
python -c "import talib; print('TA-Lib OK')"
```

### Step 5: Configure Environment

```bash
# Copy example config
cp .env.example .env

# Edit config
# Windows: notepad .env
# Linux/Mac: nano .env
```

**Fill in:**
```env
API_KEY=your_asterdex_api_key_here
API_SECRET=your_asterdex_api_secret_here
TELEGRAM_TOKEN=your_telegram_bot_token  # Optional
TELEGRAM_CHAT_ID=your_chat_id           # Optional
TESTNET_MODE=True                        # Start with testnet
```

**Get API Keys:**
1. Login to [AsterDEX](https://asterdex.com)
2. Go to Account → API Management
3. Create new API key
4. Enable "Futures Trading"
5. ⚠️ DO NOT enable "Withdrawal"
6. Copy Key and Secret

### Step 6: Create Directories

```bash
# Create required directories
mkdir -p logs models

# Verify structure
ls -la
```

## ✅ Verify Installation

### Test Python Imports
```bash
python -c "import torch; print('PyTorch:', torch.__version__)"
python -c "import pandas; print('Pandas:', pandas.__version__)"
python -c "import binance; print('Binance: OK')"
python -c "import pandas_ta; print('Pandas-TA: OK')"
```

### Test Config
```bash
python -c "from config import Config; Config.validate(); print('Config: OK')"
```

### Test API Connection
```bash
python scripts/check_balance.py
```

**Expected output:**
```
💰 USDT Balance: $XXX.XX
📊 POSITIONS:
  No open positions
```

## 🎓 Train Model

```bash
# This will take 5-10 minutes
python ml/train.py
```

**Expected output:**
```
🧠 Training LSTM...
Epoch [10/50] Loss: 0.4523 Acc: 58.23%
Epoch [20/50] Loss: 0.4012 Acc: 62.45%
...
✅ Model saved to models/lstm_model.pt
🎉 TRAINING HOÀN TẤT!
```

## 📈 Run Backtest

```bash
python run_backtest.py
```

**Expected output:**
```
📈 BACKTEST RESULTS
Total Trades: 45
Win Rate: 62.22%
Total PnL: +18.4%
Profit Factor: 1.85
```

## 🚀 Run Bot

```bash
python bot.py
```

**Expected output:**
```
🚀 ASTERDEX PERP FARM BOT - INITIALIZING
✅ Bot initialized successfully!
   Symbols: ['BTCUSDT', 'ETHUSDT']
   Leverage: 5x
🏁 BOT STARTED!
💰 Starting balance: $XXX.XX
```

## 🐛 Troubleshooting

### "Python not found"
**Windows:**
```powershell
# Reinstall Python with "Add to PATH" checked
# Or add manually to PATH
```

**Linux/Mac:**
```bash
# Use python3 instead of python
python3 --version
```

### "pip not found"
```bash
# Windows
python -m pip --version

# Linux/Mac
python3 -m pip --version

# Install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### "No module named 'torch'"
```bash
# Reinstall requirements
pip install -r requirements.txt

# Or install individually
pip install torch
```

### "TA-Lib installation failed"
**Solution 1:** Skip TA-Lib
```bash
# Edit requirements.txt, remove ta-lib line
pip install -r requirements.txt
```

**Solution 2:** Use pandas-ta only
```python
# Bot will use pandas-ta as fallback
```

### "API Error: Invalid API Key"
1. Check .env file
2. Verify API key on AsterDEX
3. Check API permissions
4. Try regenerating keys

### "Model not found"
```bash
# Train model first
python ml/train.py
```

### "Permission denied"
**Linux/Mac:**
```bash
# Make scripts executable
chmod +x run.sh
chmod +x scripts/*.py

# Or use python explicitly
python bot.py
```

### "Port already in use"
```bash
# Kill existing process
# Linux/Mac
pkill -f bot.py

# Windows
taskkill /F /IM python.exe
```

## 🔄 Update Bot

```bash
# Pull latest changes
git pull

# Update dependencies
pip install -r requirements.txt --upgrade

# Retrain model (optional)
python ml/train.py

# Restart bot
python bot.py
```

## 🗑️ Uninstall

```bash
# Deactivate venv
deactivate

# Remove directory
cd ..
rm -rf FarmAster

# Or on Windows
rmdir /s FarmAster
```

## 📞 Get Help

- **Documentation:** [README.md](README.md)
- **FAQ:** [docs/FAQ.md](docs/FAQ.md)
- **Commands:** [COMMANDS.md](COMMANDS.md)
- **Issues:** GitHub Issues
- **Community:** Telegram group

---

**Installation complete! Ready to farm! 🌾💰**

