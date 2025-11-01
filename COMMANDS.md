# 🎮 Command Reference

Tổng hợp tất cả commands hữu ích cho bot.

## 🚀 Quick Start

```bash
# 1. Setup
pip install -r requirements.txt
cp .env.example .env
# Edit .env với API keys

# 2. Train model
python ml/train.py

# 3. Backtest
python run_backtest.py

# 4. Run bot
python bot.py
```

## 📦 Installation

### Python Dependencies
```bash
# Install all
pip install -r requirements.txt

# Install individually
pip install python-binance torch pandas numpy pandas-ta python-dotenv python-telegram-bot requests scikit-learn
```

### TA-Lib (Optional but Recommended)
```bash
# Ubuntu/Debian
sudo apt-get install ta-lib

# Mac
brew install ta-lib

# Windows
# Download wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
pip install TA_Lib-0.4.XX-cpXX-cpXX-win_amd64.whl
```

## 🎓 Training

### Train LSTM Model
```bash
# Default (50 epochs, all symbols)
python ml/train.py

# Custom epochs (edit .env)
LSTM_EPOCHS=100 python ml/train.py
```

### Retrain Model
```bash
# Backup old model
cp models/lstm_model.pt models/lstm_model_backup.pt

# Train new
python ml/train.py

# Compare performance
python run_backtest.py
```

## 📈 Backtesting

### Run Backtest
```bash
# Default (30 days)
python run_backtest.py

# Custom days (edit config.py)
# BACKTEST_DAYS=60
python run_backtest.py
```

### Analyze Results
```bash
# View backtest output
cat logs/bot_*.log | grep "BACKTEST"

# Detailed analysis
python scripts/analyze_performance.py
```

## 🤖 Running Bot

### Start Bot
```bash
# Foreground
python bot.py

# Background (Linux/Mac)
nohup python bot.py > bot.out 2>&1 &

# Background (Windows)
start /B python bot.py
```

### With Screen (Linux/Mac)
```bash
# Create session
screen -S asterdex-bot

# Run bot
python bot.py

# Detach: Ctrl+A then D
# Reattach
screen -r asterdex-bot

# List sessions
screen -ls

# Kill session
screen -X -S asterdex-bot quit
```

### With Systemd (Linux)
```bash
# Start
sudo systemctl start asterdex-bot

# Stop
sudo systemctl stop asterdex-bot

# Restart
sudo systemctl restart asterdex-bot

# Status
sudo systemctl status asterdex-bot

# Enable auto-start
sudo systemctl enable asterdex-bot

# View logs
sudo journalctl -u asterdex-bot -f
```

### With PM2 (Node.js)
```bash
# Start
pm2 start bot.py --name asterdex-bot --interpreter python3

# Stop
pm2 stop asterdex-bot

# Restart
pm2 restart asterdex-bot

# Delete
pm2 delete asterdex-bot

# Logs
pm2 logs asterdex-bot

# Monitor
pm2 monit

# Save config
pm2 save

# Auto-start on boot
pm2 startup
```

## 🔍 Monitoring

### Check Balance
```bash
python scripts/check_balance.py
```

### Test Signals
```bash
python scripts/test_signal.py
```

### Analyze Performance
```bash
python scripts/analyze_performance.py
```

### View Logs
```bash
# Real-time
tail -f logs/bot_*.log

# Last 100 lines
tail -100 logs/bot_*.log

# Search for trades
grep "TRADE" logs/bot_*.log

# Search for errors
grep "ERROR" logs/bot_*.log

# Today's log
cat logs/bot_$(date +%Y%m%d).log
```

## 🛑 Emergency

### Close All Positions
```bash
python scripts/close_all.py
```

### Stop Bot
```bash
# If running in foreground
Ctrl+C

# If running in background
pkill -f bot.py

# If using screen
screen -X -S asterdex-bot quit

# If using systemd
sudo systemctl stop asterdex-bot

# If using PM2
pm2 stop asterdex-bot
```

## 🔧 Configuration

### Edit Config
```bash
# Main config
nano .env

# Advanced config
nano config.py
```

### View Current Config
```bash
python -c "from config import Config; Config.validate(); print(f'Symbols: {Config.SYMBOLS}'); print(f'Leverage: {Config.LEVERAGE}x')"
```

### Test Config
```bash
python -c "from config import Config; Config.validate()"
```

## 🧹 Maintenance

### Clean Cache
```bash
# Python cache
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# Or use Makefile
make clean
```

### Clean Logs
```bash
# Remove old logs (>7 days)
find logs/ -name "*.log" -mtime +7 -delete

# Archive logs
tar -czf logs_archive_$(date +%Y%m%d).tar.gz logs/
```

### Update Bot
```bash
# Pull latest
git pull

# Update dependencies
pip install -r requirements.txt --upgrade

# Restart
sudo systemctl restart asterdex-bot
# or
pm2 restart asterdex-bot
```

## 📊 Data Management

### Backup
```bash
# Backup everything
tar -czf backup_$(date +%Y%m%d).tar.gz .env models/ logs/

# Backup models only
tar -czf models_backup_$(date +%Y%m%d).tar.gz models/

# Backup to remote
scp backup_*.tar.gz user@remote:/backups/
```

### Restore
```bash
# Extract backup
tar -xzf backup_20240101.tar.gz

# Restore specific files
tar -xzf backup_20240101.tar.gz .env
tar -xzf backup_20240101.tar.gz models/
```

## 🧪 Testing

### Test Components
```bash
# Test data fetcher
python -c "from utils.data_fetcher import DataFetcher; df = DataFetcher.fetch_historical_ohlcv('BTCUSDT', 7); print(df.tail())"

# Test features
python -c "from ml.features import FeatureEngine; print('Features OK')"

# Test client
python -c "from trading.asterdex_client import AsterDEXClient; c = AsterDEXClient(); print(f'Balance: {c.get_account_balance()}')"

# Test model
python -c "from ml.lstm_model import LSTMTrainer; t = LSTMTrainer(14); t.load(); print('Model OK')"
```

### Run All Tests
```bash
# If you have pytest
pytest tests/

# Manual testing
python scripts/test_signal.py
python scripts/check_balance.py
```

## 📱 Telegram

### Test Telegram
```bash
# Send test message
python -c "from utils.logger import logger; logger.info('Test message', send_tg=True)"
```

### Get Chat ID
```bash
# After starting chat with bot
curl https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
```

## 🔐 Security

### Check API Keys
```bash
# Verify .env exists
ls -la .env

# Check permissions (should be 600)
chmod 600 .env

# View (be careful!)
cat .env
```

### Generate New Keys
```bash
# Backup old .env
cp .env .env.backup

# Edit with new keys
nano .env
```

## 📈 Performance Optimization

### Profile Bot
```bash
# CPU profiling
python -m cProfile -o profile.stats bot.py

# View results
python -c "import pstats; p = pstats.Stats('profile.stats'); p.sort_stats('cumulative'); p.print_stats(20)"
```

### Memory Usage
```bash
# Monitor memory
watch -n 1 'ps aux | grep bot.py'

# Detailed memory
python -m memory_profiler bot.py
```

## 🐛 Debugging

### Debug Mode
```bash
# Enable debug logging (edit utils/logger.py)
# logging.basicConfig(level=logging.DEBUG)

# Run with verbose output
python -u bot.py 2>&1 | tee debug.log
```

### Check Errors
```bash
# Recent errors
grep -i error logs/bot_*.log | tail -20

# Count errors by type
grep -i error logs/bot_*.log | cut -d: -f4 | sort | uniq -c
```

## 🎯 Makefile Commands

```bash
# Show help
make help

# Install dependencies
make install

# Setup environment
make setup

# Train model
make train

# Run backtest
make backtest

# Run bot
make run

# Test signals
make test

# Check balance
make balance

# Close all positions
make close

# Clean cache
make clean

# Quick start (install + setup)
make quickstart
```

## 🌐 Network

### Test Connection
```bash
# Ping AsterDEX
ping fapi.asterdex.com

# Test API
curl https://fapi.asterdex.com/fapi/v1/ping

# Check DNS
nslookup fapi.asterdex.com
```

### Firewall
```bash
# Allow outbound HTTPS
sudo ufw allow out 443/tcp

# Check status
sudo ufw status
```

## 📊 Statistics

### Trading Stats
```bash
# Count trades
grep "TRADE" logs/bot_*.log | wc -l

# Win rate
grep "CLOSE.*TP" logs/bot_*.log | wc -l
grep "CLOSE.*SL" logs/bot_*.log | wc -l

# By symbol
grep "BTCUSDT" logs/bot_*.log | grep "TRADE" | wc -l
```

### System Stats
```bash
# Disk usage
df -h

# CPU usage
top -bn1 | grep "Cpu(s)"

# Memory usage
free -h

# Uptime
uptime
```

## 🔄 Automation

### Cron Jobs
```bash
# Edit crontab
crontab -e

# Daily report at 00:00
0 0 * * * cd /path/to/bot && python scripts/check_balance.py >> logs/daily.log 2>&1

# Weekly retrain (Sunday 02:00)
0 2 * * 0 cd /path/to/bot && python ml/train.py >> logs/retrain.log 2>&1

# Hourly backup
0 * * * * cd /path/to/bot && tar -czf backups/backup_$(date +\%Y\%m\%d_\%H).tar.gz models/

# List cron jobs
crontab -l
```

## 💡 Tips & Tricks

### Quick Balance Check
```bash
alias balance='python scripts/check_balance.py'
balance
```

### Quick Log View
```bash
alias botlog='tail -f logs/bot_$(date +%Y%m%d).log'
botlog
```

### Quick Restart
```bash
alias restart='sudo systemctl restart asterdex-bot && sudo journalctl -u asterdex-bot -f'
restart
```

---

**Need more help? Check [README.md](README.md) or [FAQ.md](docs/FAQ.md)! 🚀**

