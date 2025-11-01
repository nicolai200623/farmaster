# ============================================
# 🚀 AsterDEX Bot Makefile
# ============================================

.PHONY: help install setup train backtest run test clean

help:
	@echo "🚀 AsterDEX Perp Farm Bot"
	@echo ""
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make setup      - Setup environment (.env)"
	@echo "  make train      - Train LSTM model"
	@echo "  make backtest   - Run backtest"
	@echo "  make run        - Run bot"
	@echo "  make test       - Test signals"
	@echo "  make balance    - Check balance"
	@echo "  make close      - Close all positions"
	@echo "  make clean      - Clean cache files"
	@echo ""

install:
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt
	@echo "✅ Installation complete!"

setup:
	@echo "🔧 Setting up environment..."
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "✅ Created .env file"; \
		echo "⚠️  Please edit .env with your API keys!"; \
	else \
		echo "⚠️  .env already exists"; \
	fi
	@mkdir -p logs models
	@echo "✅ Setup complete!"

train:
	@echo "🎓 Training LSTM model..."
	python ml/train.py
	@echo "✅ Training complete!"

backtest:
	@echo "📈 Running backtest..."
	python run_backtest.py
	@echo "✅ Backtest complete!"

run:
	@echo "🚀 Starting bot..."
	python bot.py

test:
	@echo "🧪 Testing signals..."
	python scripts/test_signal.py

balance:
	@echo "💰 Checking balance..."
	python scripts/check_balance.py

close:
	@echo "🔴 Closing all positions..."
	python scripts/close_all.py

clean:
	@echo "🧹 Cleaning cache..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@echo "✅ Clean complete!"

# Quick start workflow
quickstart: install setup
	@echo ""
	@echo "✅ Quick setup complete!"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Edit .env with your API keys"
	@echo "  2. make train"
	@echo "  3. make backtest"
	@echo "  4. make run"
	@echo ""

