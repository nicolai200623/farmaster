# 🪟 Windows Installation Guide

Quick installation guide for Windows users.

## ⚡ Quick Install (5 minutes)

### Step 1: Install Python

1. Download Python 3.8+ from https://www.python.org/downloads/
2. **IMPORTANT:** Check "Add Python to PATH" during installation
3. Verify installation:
```cmd
python --version
```

### Step 2: Install Dependencies

**Option A: Minimal (Recommended for Windows)**
```cmd
pip install -r requirements-minimal.txt
```

**Option B: Full (with TA-Lib - Advanced)**
```cmd
pip install -r requirements.txt
```

**Note:** TA-Lib requires manual installation on Windows. See below if needed.

### Step 3: Configure

```cmd
copy .env.example .env
notepad .env
```

Edit `.env` with your:
- AsterDEX API keys
- Telegram bot token (optional)

### Step 4: Train Model

```cmd
python ml/train.py
```

Wait 5-10 minutes for training to complete.

### Step 5: Backtest

```cmd
python run_backtest.py
```

### Step 6: Run Bot

**Testnet (Recommended first):**
```cmd
python bot.py
```

**Production:**
Edit `.env` and set `TESTNET=false`, then:
```cmd
python bot.py
```

---

## 🔧 Troubleshooting

### "pip is not recognized"

**Solution:**
```cmd
python -m pip install -r requirements-minimal.txt
```

### "torch installation failed"

**Solution 1: Use CPU version**
```cmd
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

**Solution 2: Use latest version**
```cmd
pip install torch
```

### "pandas-ta installation failed"

**Solution:**
```cmd
pip install pandas-ta --no-cache-dir
```

### "Permission denied"

**Solution:** Run Command Prompt as Administrator
1. Search "cmd" in Start Menu
2. Right-click → "Run as administrator"
3. Run install commands again

### "TA-Lib not found"

**Solution 1: Skip TA-Lib (Recommended)**
```cmd
pip install -r requirements-minimal.txt
```

**Solution 2: Install TA-Lib manually**
1. Download wheel from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
2. Choose correct version (e.g., `TA_Lib‑0.4.28‑cp311‑cp311‑win_amd64.whl` for Python 3.11)
3. Install:
```cmd
pip install TA_Lib‑0.4.28‑cp311‑cp311‑win_amd64.whl
```

---

## 🚀 Running the Bot

### Foreground (See logs in terminal)
```cmd
python bot.py
```

### Background (Using pythonw)
```cmd
start /B pythonw bot.py
```

### Using Task Scheduler (Auto-start on boot)

1. Open Task Scheduler
2. Create Basic Task
3. Trigger: At startup
4. Action: Start a program
5. Program: `C:\Path\To\Python\python.exe`
6. Arguments: `C:\Path\To\FarmAster\bot.py`
7. Start in: `C:\Path\To\FarmAster`

---

## 📊 Monitoring

### View Logs
```cmd
type logs\bot_%date:~-4,4%%date:~-10,2%%date:~-7,2%.log
```

### Check Balance
```cmd
python scripts/check_balance.py
```

### Test Signals
```cmd
python scripts/test_signal.py
```

### Emergency Close All
```cmd
python scripts/close_all.py
```

---

## 🛑 Stopping the Bot

### If running in foreground
Press `Ctrl+C`

### If running in background
```cmd
taskkill /F /IM python.exe
```

**Or find specific process:**
```cmd
tasklist | findstr python
taskkill /F /PID <process_id>
```

---

## 🔄 Updating

```cmd
git pull
pip install -r requirements-minimal.txt --upgrade
python ml/train.py
python bot.py
```

---

## 💡 Tips for Windows Users

### Use PowerShell (Better than CMD)
```powershell
# Install
pip install -r requirements-minimal.txt

# Run
python bot.py
```

### Use Windows Terminal (Modern)
Download from Microsoft Store: "Windows Terminal"

### Use Virtual Environment (Recommended)
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements-minimal.txt
```

### Create Desktop Shortcut

1. Right-click Desktop → New → Shortcut
2. Location: `C:\Path\To\Python\python.exe C:\Path\To\FarmAster\bot.py`
3. Name: "AsterDEX Bot"
4. Change icon if desired

### Create Batch File for Easy Start

Create `start_bot.bat`:
```batch
@echo off
cd /d C:\Path\To\FarmAster
python bot.py
pause
```

Double-click to run!

---

## 🔐 Security Tips

1. **Don't share .env file** - Contains API keys
2. **Use testnet first** - Test before real money
3. **Start small** - Use small capital initially
4. **Monitor regularly** - Check logs daily
5. **Backup .env** - Keep secure backup

---

## 📞 Common Issues

### "ModuleNotFoundError: No module named 'torch'"
```cmd
pip install torch
```

### "ModuleNotFoundError: No module named 'binance'"
```cmd
pip install python-binance
```

### "API Error: Invalid API key"
Check `.env` file:
- API_KEY is correct
- API_SECRET is correct
- No extra spaces

### "Connection Error"
Check:
- Internet connection
- Firewall settings
- Antivirus not blocking Python

### Bot stops unexpectedly
Check logs:
```cmd
type logs\bot_*.log | findstr ERROR
```

---

## 🎯 Next Steps

After installation:

1. ✅ Read [CHECKLIST.md](CHECKLIST.md)
2. ✅ Test on testnet (24 hours minimum)
3. ✅ Monitor performance
4. ✅ Optimize parameters
5. ✅ Deploy to production

---

## 📚 More Help

- **Full Installation Guide:** [INSTALL.md](INSTALL.md)
- **Quick Start:** [QUICKSTART.md](QUICKSTART.md)
- **FAQ:** [docs/FAQ.md](docs/FAQ.md)
- **Commands:** [COMMANDS.md](COMMANDS.md)

---

**Good luck! 🚀**

**Windows users can trade too! 💪**

