#!/bin/bash
# ============================================
# Linux/Mac Shell Script to Run Bot
# ============================================

echo ""
echo "========================================"
echo "  AsterDEX Perp Farm Bot - Unix"
echo "========================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 not found!"
    echo "Please install Python 3.8+"
    exit 1
fi

# Check .env
if [ ! -f .env ]; then
    echo "WARNING: .env file not found!"
    echo "Creating from .env.example..."
    cp .env.example .env
    echo ""
    echo "Please edit .env with your API keys!"
    exit 1
fi

# Create directories
mkdir -p logs models

# Check if model exists
if [ ! -f models/lstm_model.pt ]; then
    echo ""
    echo "WARNING: LSTM model not found!"
    echo ""
    read -p "Do you want to train now? (y/n): " train
    if [ "$train" = "y" ] || [ "$train" = "Y" ]; then
        echo ""
        echo "Training model..."
        python3 ml/train.py
        if [ $? -ne 0 ]; then
            echo ""
            echo "ERROR: Training failed!"
            exit 1
        fi
    else
        echo ""
        echo "Please run: python3 ml/train.py"
        exit 1
    fi
fi

# Run bot
echo ""
echo "Starting bot..."
echo ""
python3 bot.py

