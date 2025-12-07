#!/bin/bash
# ============================================
# Quick Setup for Grok AI Validator
# ============================================

echo ""
echo "============================================"
echo " Setting up Grok AI Validator"
echo "============================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Error: Virtual environment not found!"
    echo "Please run: python -m venv venv"
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Grok only needs requests (already in requirements.txt)
echo ""
echo "Checking dependencies..."
if pip show requests > /dev/null 2>&1; then
    echo "✓ requests already installed"
else
    echo "Installing requests..."
    pip install requests
fi

echo ""
echo "============================================"
echo " ✅ Grok Setup Complete!"
echo "============================================"
echo ""
echo "Next steps:"
echo "1. Get API key from https://console.x.ai/"
echo "2. Add to .env: XAI_API_KEY=your-key-here"
echo "3. Run test: python scripts/test_ai_validator.py"
echo "4. Start bot: python bot.py"
echo ""
