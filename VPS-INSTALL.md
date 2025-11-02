# 🚀 VPS Installation Guide

Quick guide để deploy bot lên VPS.

## ⚡ Quick Install (Recommended)

### 1. Upload code lên VPS

```bash
# Option A: Clone từ git (nếu có repo)
git clone https://github.com/your-repo/FarmAster.git
cd FarmAster

# Option B: Upload từ local
# Dùng scp hoặc FileZilla để upload folder
```

### 2. Run install script

```bash
# Make executable
chmod +x install-vps.sh

# Run
bash install-vps.sh
```

### 3. Configure

```bash
# Edit .env
nano .env
```

Paste config của bạn:
```env
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
TELEGRAM_TOKEN=your_telegram_token
TELEGRAM_CHAT_ID=your_chat_id
TESTNET_MODE=false
SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT,ADAUSDT,DOTUSDT,AVAXUSDT,XRPUSDT,LTCUSDT,ASTERUSDT
```

Save: `Ctrl+O`, Enter, `Ctrl+X`

### 4. Train model

```bash
source venv/bin/activate
python scripts/train_lstm.py
```

### 5. Test

```bash
# Check balance
python scripts/check_balance.py

# Test signal
python scripts/test_signal.py BTCUSDT
```

### 6. Run bot

```bash
# Test run
python bot.py

# Run in background (recommended)
screen -S asterdex
python bot.py
# Press Ctrl+A+D to detach

# Reattach later
screen -r asterdex
```

---

## 📋 Manual Installation

### 1. Prepare VPS

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python 3.10+
sudo apt install python3 python3-pip python3-venv git -y

# Check version
python3 --version  # Should be 3.10+
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

### 3. Install dependencies

```bash
# Install core packages
pip install -r requirements-vps.txt

# Try to install pandas-ta (optional)
pip install git+https://github.com/twopirllc/pandas-ta.git || echo "Using manual calculation"
```

**Note:** If `pandas-ta` fails to install, bot will automatically use manual indicator calculation. This is slower but fully functional.

### 4. Configure

```bash
cp .env.example .env
nano .env
```

### 5. Train & Run

```bash
# Train
python scripts/train_lstm.py

# Test
python scripts/check_balance.py

# Run
python bot.py
```

---

## 🔧 Troubleshooting

### pandas-ta installation fails

**Error:**
```
fatal: Authentication failed for 'https://github.com/twopirllc/pandas-ta.git/'
```

**Solution:**
Bot will automatically use manual indicator calculation. No action needed!

**Verify:**
```bash
python -c "from ml.features import FeatureEngine; print('✅ Features OK')"
```

### Git authentication issues

**Option 1: Disable credential helper**
```bash
git config --global --unset credential.helper
pip install git+https://github.com/twopirllc/pandas-ta.git
```

**Option 2: Download manually**
```bash
wget https://github.com/twopirllc/pandas-ta/archive/refs/heads/main.tar.gz -O pandas-ta.tar.gz
tar -xzf pandas-ta.tar.gz
cd pandas-ta-main
pip install .
cd ..
rm -rf pandas-ta-main pandas-ta.tar.gz
```

**Option 3: Skip pandas-ta (recommended if issues persist)**
```bash
# Just install core dependencies
pip install -r requirements-vps.txt

# Bot will use manual calculation automatically
```

---

## 🎯 Running in Background

### Option 1: screen (Simple)

```bash
# Start
screen -S asterdex
python bot.py

# Detach: Ctrl+A+D

# Reattach
screen -r asterdex

# List screens
screen -ls

# Kill screen
screen -X -S asterdex quit
```

### Option 2: systemd (Production)

Create service file:
```bash
sudo nano /etc/systemd/system/asterdex.service
```

Paste:
```ini
[Unit]
Description=AsterDEX Trading Bot
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/FarmAster
Environment="PATH=/path/to/FarmAster/venv/bin"
ExecStart=/path/to/FarmAster/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable & start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable asterdex
sudo systemctl start asterdex
sudo systemctl status asterdex
```

View logs:
```bash
sudo journalctl -u asterdex -f
```

---

## 📊 Monitoring

### Check bot status

```bash
# If using screen
screen -r asterdex

# If using systemd
sudo systemctl status asterdex
sudo journalctl -u asterdex -f
```

### Check logs

```bash
# View latest log
tail -f logs/bot_*.log

# View all logs
ls -lh logs/
```

### Check balance

```bash
source venv/bin/activate
python scripts/check_balance.py
```

---

## 🔒 Security

### Protect .env file

```bash
chmod 600 .env
```

### Firewall

```bash
# Only allow SSH
sudo ufw allow 22/tcp
sudo ufw enable
```

### Auto-restart on reboot

```bash
# If using systemd (already enabled above)
# Service will auto-start on reboot

# If using screen, add to crontab
crontab -e

# Add:
@reboot cd /path/to/FarmAster && /path/to/venv/bin/python bot.py >> /var/log/asterdex.log 2>&1
```

---

## ✅ Verification Checklist

- [ ] Python 3.10+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed (pandas-ta optional)
- [ ] .env configured with API keys
- [ ] LSTM model trained
- [ ] Balance check successful
- [ ] Bot running in background
- [ ] Telegram notifications working
- [ ] Logs being written

---

## 🆘 Support

If you encounter issues:

1. Check logs: `tail -f logs/bot_*.log`
2. Verify config: `python -c "from config import Config; Config.validate()"`
3. Test connection: `python scripts/check_balance.py`
4. Check dependencies: `pip list | grep -E "binance|torch|pandas|telegram"`

---

**Happy farming! 🚀**

