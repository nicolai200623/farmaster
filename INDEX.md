# 📚 Documentation Index

Quick navigation to all documentation files.

## 🚀 Getting Started

### New Users Start Here (Đọc theo thứ tự)
1. **[COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)** ⭐ - Hướng dẫn đầy đủ từ A-Z (Setup → Train → Backtest → Run)
2. **[QUICK_START_VOLUME_FARMING.md](QUICK_START_VOLUME_FARMING.md)** - Quick start 3 bước cho volume farming
3. **[CHEAT_SHEET.md](CHEAT_SHEET.md)** - Tra cứu lệnh nhanh
4. **[INSTALL.md](INSTALL.md)** - Hướng dẫn cài đặt chi tiết

### Experienced Users
- **[CHEAT_SHEET.md](CHEAT_SHEET.md)** - Tất cả lệnh quan trọng
- **[COMMANDS.md](COMMANDS.md)** - Lệnh chi tiết
- **[VOLUME_FARMING_STRATEGY.md](VOLUME_FARMING_STRATEGY.md)** - Chiến lược volume farming

### Before You Start
- **[CHECKLIST.md](CHECKLIST.md)** - Pre-launch checklist (MUST READ)
- **[docs/FAQ.md](docs/FAQ.md)** - Frequently asked questions (50+ Q&A)
- **[FIXES.md](FIXES.md)** - Recent fixes and updates

---

## 🎯 Volume Farming Strategy (MỚI)

### Tài Liệu Chính
- **[VOLUME_FARMING_STRATEGY.md](VOLUME_FARMING_STRATEGY.md)** ⭐ - Chiến lược chi tiết, tối ưu hóa
- **[QUICK_START_VOLUME_FARMING.md](QUICK_START_VOLUME_FARMING.md)** - Quick start 3 bước
- **[VOLUME_FARMING_DEPLOYMENT.md](VOLUME_FARMING_DEPLOYMENT.md)** - Deployment guide

### Scripts & Tools
- **[scripts/apply_volume_farming_config.py](scripts/apply_volume_farming_config.py)** - Áp dụng config tự động
- **[scripts/test_volume_farming.py](scripts/test_volume_farming.py)** - Test backtest với config mới
- **[.env.volume_farming](.env.volume_farming)** - Cấu hình tối ưu

---

## 📖 Core Documentation

### Understanding the Bot
- **[docs/STRATEGY.md](docs/STRATEGY.md)** - Trading strategy explained
- **[docs/API.md](docs/API.md)** - Complete API reference
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Project overview

### Using the Bot
- **[COMMANDS.md](COMMANDS.md)** - All commands reference
- **[CHEAT_SHEET.md](CHEAT_SHEET.md)** ⭐ - Quick reference cho tất cả lệnh
- **[docs/OPTIMIZATION.md](docs/OPTIMIZATION.md)** - Performance tuning guide
- **[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)** - VPS deployment guide

---

## 🛠️ Module Documentation

### Machine Learning
- **[ml/README.md](ml/README.md)** - ML module overview
- **[ml/features.py](ml/features.py)** - Feature engineering
- **[ml/lstm_model.py](ml/lstm_model.py)** - LSTM model
- **[ml/train.py](ml/train.py)** - Training script

### Trading
- **[trading/README.md](trading/README.md)** - Trading module overview
- **[trading/asterdex_client.py](trading/asterdex_client.py)** - API client
- **[trading/signal_generator.py](trading/signal_generator.py)** - Signal logic
- **[trading/risk_manager.py](trading/risk_manager.py)** - Risk management

### Scripts
- **[scripts/README.md](scripts/README.md)** - Scripts overview
- **[scripts/check_balance.py](scripts/check_balance.py)** - Balance checker
- **[scripts/test_signal.py](scripts/test_signal.py)** - Signal tester
- **[scripts/close_all.py](scripts/close_all.py)** - Emergency close
- **[scripts/analyze_performance.py](scripts/analyze_performance.py)** - Performance analyzer

---

## 🤝 Contributing

### For Contributors
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute
- **[CONTRIBUTORS.md](CONTRIBUTORS.md)** - List of contributors
- **[ROADMAP.md](ROADMAP.md)** - Future development plans
- **[CHANGELOG.md](CHANGELOG.md)** - Version history

---

## 📊 Project Status

### Summary Files
- **[FINAL_SUMMARY.md](FINAL_SUMMARY.md)** - Complete project summary
- **[PROJECT_COMPLETE.md](PROJECT_COMPLETE.md)** - Completion status
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Project overview

---

## 🔧 Configuration

### Setup Files
- **[.env.example](.env.example)** - Configuration template
- **[config.py](config.py)** - Configuration management
- **[requirements.txt](requirements.txt)** - Python dependencies (full)
- **[requirements-minimal.txt](requirements-minimal.txt)** - Minimal dependencies (recommended)

---

## 🚀 Deployment

### Deployment Files
- **[Makefile](Makefile)** - Make commands
- **[run.sh](run.sh)** - Linux/Mac runner
- **[run.bat](run.bat)** - Windows runner

---

## 📁 File Structure

```
FarmAster/
│
├── 📄 Main Documentation (14 files)
│   ├── README.md                 ⭐ Start here
│   ├── QUICKSTART.md             ⭐ 5-minute setup
│   ├── INSTALL.md                📥 Installation
│   ├── CHECKLIST.md              ✅ Pre-launch
│   ├── COMMANDS.md               🎮 Commands
│   ├── CONTRIBUTING.md           🤝 Contributing
│   ├── CONTRIBUTORS.md           👥 Contributors
│   ├── ROADMAP.md                🗺️ Future plans
│   ├── CHANGELOG.md              📝 Changes
│   ├── PROJECT_SUMMARY.md        📊 Overview
│   ├── PROJECT_COMPLETE.md       ✅ Completion
│   ├── FINAL_SUMMARY.md          🎊 Summary
│   ├── INDEX.md                  📚 This file
│   └── LICENSE                   📜 MIT License
│
├── 📚 Advanced Docs (6 files)
│   └── docs/
│       ├── FAQ.md                ❓ 50+ Q&A
│       ├── API.md                📖 API reference
│       ├── STRATEGY.md           🎯 Strategy
│       ├── DEPLOYMENT.md         🚀 Deployment
│       └── OPTIMIZATION.md       ⚡ Optimization
│
├── 🤖 Core Bot (3 files)
│   ├── bot.py                    🤖 Main bot
│   ├── config.py                 ⚙️ Config
│   └── run_backtest.py           📈 Backtest
│
├── 🧠 Machine Learning (5 files)
│   └── ml/
│       ├── features.py           🔧 Features
│       ├── lstm_model.py         🧠 LSTM
│       ├── train.py              🎓 Training
│       └── README.md             📖 ML docs
│
├── 💹 Trading (5 files)
│   └── trading/
│       ├── asterdex_client.py    🔌 API client
│       ├── signal_generator.py   📡 Signals
│       ├── risk_manager.py       🛡️ Risk
│       └── README.md             📖 Trading docs
│
├── 📊 Backtesting (2 files)
│   └── backtest/
│       └── backtester.py         📈 Backtest
│
├── 🛠️ Utilities (3 files)
│   └── utils/
│       ├── logger.py             📝 Logging
│       └── data_fetcher.py       📥 Data
│
├── 🔧 Scripts (6 files)
│   └── scripts/
│       ├── check_balance.py      💰 Balance
│       ├── test_signal.py        🧪 Test
│       ├── close_all.py          🛑 Close
│       ├── analyze_performance.py 📊 Analyze
│       └── README.md             📖 Scripts docs
│
└── 🚀 Deployment (4 files)
    ├── Makefile                  🔨 Make
    ├── run.sh                    🐧 Linux/Mac
    ├── run.bat                   🪟 Windows
    └── requirements.txt          📦 Dependencies
```

---

## 🎯 Quick Links by Task

### I want to...

#### Install the bot
1. [INSTALL.md](INSTALL.md) - Detailed installation
2. [QUICKSTART.md](QUICKSTART.md) - Quick setup
3. [requirements.txt](requirements.txt) - Dependencies

#### Understand how it works
1. [README.md](README.md) - Overview
2. [docs/STRATEGY.md](docs/STRATEGY.md) - Strategy
3. [docs/API.md](docs/API.md) - Code reference

#### Configure the bot
1. [.env.example](.env.example) - Config template
2. [config.py](config.py) - Config code
3. [docs/OPTIMIZATION.md](docs/OPTIMIZATION.md) - Tuning

#### Deploy to production
1. [CHECKLIST.md](CHECKLIST.md) - Pre-launch
2. [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) - VPS guide
3. [Makefile](Makefile) - Automation

#### Troubleshoot issues
1. [docs/FAQ.md](docs/FAQ.md) - Common issues
2. [COMMANDS.md](COMMANDS.md) - Useful commands
3. [scripts/](scripts/) - Helper scripts

#### Contribute
1. [CONTRIBUTING.md](CONTRIBUTING.md) - Guidelines
2. [ROADMAP.md](ROADMAP.md) - Future plans
3. [CHANGELOG.md](CHANGELOG.md) - History

#### Learn the code
1. [docs/API.md](docs/API.md) - API reference
2. [ml/README.md](ml/README.md) - ML module
3. [trading/README.md](trading/README.md) - Trading module

---

## 📊 Documentation Statistics

- **Total Documentation Files:** 20+
- **Total Code Files:** 30+
- **Total Lines of Documentation:** 10,000+
- **Total Lines of Code:** 5,000+
- **Languages:** Vietnamese + English

---

## 🔍 Search Tips

### Find by Topic
- **Installation:** INSTALL.md, QUICKSTART.md
- **Configuration:** .env.example, config.py, OPTIMIZATION.md
- **Trading:** STRATEGY.md, trading/README.md
- **ML:** ml/README.md, STRATEGY.md
- **Deployment:** DEPLOYMENT.md, Makefile
- **Troubleshooting:** FAQ.md, COMMANDS.md
- **Contributing:** CONTRIBUTING.md, ROADMAP.md

### Find by Skill Level
- **Beginner:** README.md, QUICKSTART.md, FAQ.md
- **Intermediate:** STRATEGY.md, OPTIMIZATION.md, COMMANDS.md
- **Advanced:** API.md, Module READMEs, Source code

---

## 📞 Need Help?

### Documentation Not Clear?
1. Check [FAQ.md](docs/FAQ.md)
2. Search GitHub issues
3. Ask in community
4. Create new issue

### Want to Improve Docs?
1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Fork repository
3. Make improvements
4. Submit pull request

---

## 🎓 Recommended Reading Order

### For New Users
1. README.md
2. QUICKSTART.md
3. INSTALL.md
4. CHECKLIST.md
5. FAQ.md

### For Developers
1. README.md
2. STRATEGY.md
3. API.md
4. Module READMEs
5. Source code

### For Contributors
1. README.md
2. CONTRIBUTING.md
3. ROADMAP.md
4. Source code

---

## 🌟 Most Important Files

### Must Read (Top 5)
1. **[README.md](README.md)** - Everything overview
2. **[QUICKSTART.md](QUICKSTART.md)** - Get started fast
3. **[CHECKLIST.md](CHECKLIST.md)** - Before going live
4. **[docs/FAQ.md](docs/FAQ.md)** - Common questions
5. **[docs/STRATEGY.md](docs/STRATEGY.md)** - How it works

### Reference (Top 5)
1. **[COMMANDS.md](COMMANDS.md)** - All commands
2. **[docs/API.md](docs/API.md)** - Code reference
3. **[docs/OPTIMIZATION.md](docs/OPTIMIZATION.md)** - Tuning
4. **[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)** - Production
5. **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contributing

---

**Last Updated:** 2024  
**Total Files:** 50+  
**Status:** Complete ✅

---

**Happy Reading! 📚**

