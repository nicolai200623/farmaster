#!/bin/bash
# Quick install script for VPS deployment
# Usage: bash install-vps.sh

set -e  # Exit on error

echo "🚀 AsterDEX Bot - VPS Installation"
echo "===================================="
echo ""

# Check Python version
echo "📋 Checking Python version..."
python3 --version || { echo "❌ Python 3 not found!"; exit 1; }

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo ""
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install core dependencies
echo ""
echo "📥 Installing core dependencies..."
pip install -r requirements-vps.txt

# Try to install pandas-ta (optional)
echo ""
echo "📥 Attempting to install pandas-ta (optional)..."
if pip install git+https://github.com/twopirllc/pandas-ta.git; then
    echo "✅ pandas-ta installed successfully!"
else
    echo "⚠️  pandas-ta installation failed - bot will use manual calculation"
    echo "   This is OK! Bot will work fine with manual indicators."
fi

# Verify installations
echo ""
echo "🔍 Verifying installations..."
python -c "import torch; print('✅ PyTorch:', torch.__version__)"
python -c "import pandas; print('✅ Pandas:', pandas.__version__)"
python -c "import binance; print('✅ python-binance: OK')"
python -c "import telegram; print('✅ python-telegram-bot: OK')"

# Check pandas-ta
if python -c "import pandas_ta" 2>/dev/null; then
    echo "✅ pandas-ta: OK (using pandas-ta)"
else
    echo "⚠️  pandas-ta: Not installed (using manual calculation)"
fi

# Create .env if not exists
echo ""
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "✅ .env created from .env.example"
        echo "⚠️  Please edit .env with your API keys:"
        echo "   nano .env"
    else
        echo "⚠️  .env.example not found, please create .env manually"
    fi
else
    echo "✅ .env already exists"
fi

echo ""
echo "===================================="
echo "✅ Installation complete!"
echo "===================================="
echo ""
echo "📋 Next steps:"
echo "1. Edit .env with your API keys:"
echo "   nano .env"
echo ""
echo "2. Train LSTM model:"
echo "   source venv/bin/activate"
echo "   python scripts/train_lstm.py"
echo ""
echo "3. Test connection:"
echo "   python scripts/check_balance.py"
echo ""
echo "4. Run bot:"
echo "   python bot.py"
echo ""
echo "5. Run in background (recommended):"
echo "   screen -S asterdex"
echo "   python bot.py"
echo "   # Press Ctrl+A+D to detach"
echo ""

