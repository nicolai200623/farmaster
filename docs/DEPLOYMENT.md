# 🚀 Deployment Guide

Hướng dẫn deploy bot lên VPS/Cloud để chạy 24/7.

## 📋 Prerequisites

- VPS/Cloud server (Ubuntu 20.04+ recommended)
- SSH access
- Domain (optional, for monitoring)

## 🖥️ VPS Recommendations

### Budget Options
- **DigitalOcean Droplet:** $6/month (1GB RAM)
- **Vultr:** $5/month (1GB RAM)
- **Linode:** $5/month (1GB RAM)
- **AWS EC2 t2.micro:** Free tier (1 year)

### Recommended Specs
- **CPU:** 1 core (sufficient)
- **RAM:** 1-2GB
- **Storage:** 25GB SSD
- **Bandwidth:** 1TB/month
- **OS:** Ubuntu 20.04 LTS

## 🔧 Setup VPS

### 1. Connect to VPS

```bash
ssh root@your_vps_ip
```

### 2. Update System

```bash
apt update && apt upgrade -y
```

### 3. Install Python 3.8+

```bash
apt install python3 python3-pip python3-venv -y
python3 --version  # Should be 3.8+
```

### 4. Install Dependencies

```bash
# Build tools for ta-lib
apt install build-essential wget -y

# Install ta-lib
cd /tmp
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
make install
ldconfig
```

### 5. Create User (Security)

```bash
adduser botuser
usermod -aG sudo botuser
su - botuser
```

## 📦 Deploy Bot

### 1. Clone Repository

```bash
cd ~
git clone <your-repo-url> asterdex-bot
cd asterdex-bot
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install --upgrade pip

# Install core dependencies (pandas-ta is now optional)
pip install -r requirements-vps.txt

# Optional: Try to install pandas-ta (recommended but not required)
# If this fails, bot will use manual indicator calculation
pip install git+https://github.com/twopirllc/pandas-ta.git || echo "pandas-ta install failed, using manual calculation"
```

**Note:** If `pandas-ta` installation fails due to git authentication issues, the bot will automatically use manual indicator calculation. Performance is slightly slower but fully functional.

### 4. Configure Environment

```bash
cp .env.example .env
nano .env
```

Fill in:
```env
API_KEY=your_asterdex_api_key
API_SECRET=your_asterdex_secret
TELEGRAM_TOKEN=your_telegram_token
TELEGRAM_CHAT_ID=your_chat_id
TESTNET_MODE=False  # For production
```

Save: `Ctrl+O`, Exit: `Ctrl+X`

### 5. Train Model

```bash
# Use the correct script path
python scripts/train_lstm.py
```

Wait for completion (~10 minutes).

### 6. Test Bot

```bash
# Check balance
python scripts/check_balance.py

# Test signals
python scripts/test_signal.py

# Run backtest
python run_backtest.py
```

## 🔄 Run Bot 24/7

### Option 1: Screen (Simple)

```bash
# Install screen
sudo apt install screen -y

# Create screen session
screen -S asterdex-bot

# Run bot
python bot.py

# Detach: Ctrl+A, then D
# Reattach: screen -r asterdex-bot
```

### Option 2: Systemd (Recommended)

Create service file:

```bash
sudo nano /etc/systemd/system/asterdex-bot.service
```

Content:
```ini
[Unit]
Description=AsterDEX Perp Farm Bot
After=network.target

[Service]
Type=simple
User=botuser
WorkingDirectory=/home/botuser/asterdex-bot
Environment="PATH=/home/botuser/asterdex-bot/venv/bin"
ExecStart=/home/botuser/asterdex-bot/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable asterdex-bot
sudo systemctl start asterdex-bot

# Check status
sudo systemctl status asterdex-bot

# View logs
sudo journalctl -u asterdex-bot -f
```

### Option 3: PM2 (Node.js required)

```bash
# Install Node.js and PM2
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install nodejs -y
sudo npm install -g pm2

# Start bot
pm2 start bot.py --name asterdex-bot --interpreter python3

# Save config
pm2 save
pm2 startup

# Monitor
pm2 monit
pm2 logs asterdex-bot
```

## 📊 Monitoring

### 1. Check Logs

```bash
# Systemd
sudo journalctl -u asterdex-bot -f

# Screen
screen -r asterdex-bot

# PM2
pm2 logs asterdex-bot

# File logs
tail -f logs/bot_*.log
```

### 2. Telegram Alerts

Bot tự động gửi alerts qua Telegram nếu configured.

### 3. Cron Jobs (Optional)

Daily report:

```bash
crontab -e
```

Add:
```bash
# Daily stats at 00:00
0 0 * * * cd /home/botuser/asterdex-bot && /home/botuser/asterdex-bot/venv/bin/python scripts/check_balance.py >> logs/daily_report.log 2>&1

# Weekly model retrain (Sunday 02:00)
0 2 * * 0 cd /home/botuser/asterdex-bot && /home/botuser/asterdex-bot/venv/bin/python ml/train.py >> logs/retrain.log 2>&1
```

## 🔒 Security

### 1. Firewall

```bash
sudo ufw allow 22/tcp  # SSH
sudo ufw enable
sudo ufw status
```

### 2. SSH Key Authentication

On local machine:
```bash
ssh-keygen -t rsa -b 4096
ssh-copy-id botuser@your_vps_ip
```

On VPS:
```bash
sudo nano /etc/ssh/sshd_config
```

Set:
```
PasswordAuthentication no
PermitRootLogin no
```

Restart SSH:
```bash
sudo systemctl restart sshd
```

### 3. API Key Security

- Enable IP whitelist on AsterDEX
- Disable withdrawal permission
- Use read-only keys for monitoring

### 4. Auto Updates (Optional)

```bash
# Install unattended-upgrades
sudo apt install unattended-upgrades -y
sudo dpkg-reconfigure -plow unattended-upgrades
```

## 🔄 Maintenance

### Update Bot

```bash
cd ~/asterdex-bot
git pull
source venv/bin/activate
pip install -r requirements.txt --upgrade

# Restart
sudo systemctl restart asterdex-bot
# or
pm2 restart asterdex-bot
```

### Retrain Model

```bash
cd ~/asterdex-bot
source venv/bin/activate
python ml/train.py

# Restart bot
sudo systemctl restart asterdex-bot
```

### Backup

```bash
# Backup .env and models
tar -czf backup_$(date +%Y%m%d).tar.gz .env models/ logs/

# Download to local
scp botuser@your_vps_ip:~/asterdex-bot/backup_*.tar.gz ./
```

### Restore

```bash
tar -xzf backup_20240101.tar.gz
```

## 📈 Scaling

### Multiple Bots

Run multiple instances for different symbols:

```bash
# Bot 1: BTC
cp -r asterdex-bot asterdex-bot-btc
cd asterdex-bot-btc
nano .env  # Set SYMBOLS=BTCUSDT

# Bot 2: ETH
cp -r asterdex-bot asterdex-bot-eth
cd asterdex-bot-eth
nano .env  # Set SYMBOLS=ETHUSDT

# Create separate systemd services
sudo nano /etc/systemd/system/asterdex-bot-btc.service
sudo nano /etc/systemd/system/asterdex-bot-eth.service
```

### Load Balancing

Use multiple VPS for redundancy:

```bash
# VPS 1: Primary
# VPS 2: Backup (different symbols or accounts)
```

## 🐛 Troubleshooting

### Bot Crashes

Check logs:
```bash
sudo journalctl -u asterdex-bot -n 100
```

Common issues:
- API rate limit → Increase `LOOP_SLEEP`
- Out of memory → Upgrade VPS
- Network timeout → Check internet

### High CPU Usage

```bash
top
htop
```

Solutions:
- Reduce `LSTM_HIDDEN_SIZE`
- Increase `LOOP_SLEEP`
- Use smaller model

### Disk Full

```bash
df -h
```

Clean logs:
```bash
cd ~/asterdex-bot/logs
rm bot_*.log.old
```

## 📞 Support

- Check logs first
- Review [FAQ.md](FAQ.md)
- Open GitHub issue
- Join Telegram group

---

## ✅ Deployment Checklist

- [ ] VPS setup complete
- [ ] Python 3.8+ installed
- [ ] Dependencies installed
- [ ] .env configured
- [ ] Model trained
- [ ] Backtest passed
- [ ] Bot running (screen/systemd/pm2)
- [ ] Telegram working
- [ ] Logs monitored
- [ ] Firewall enabled
- [ ] SSH key auth enabled
- [ ] Backup scheduled
- [ ] Cron jobs set (optional)

**Ready to farm! 🚀💰**

