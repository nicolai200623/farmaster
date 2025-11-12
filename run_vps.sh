#!/bin/bash
# VPS Helper Script for FarmAster Bot

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Set PYTHONPATH
export PYTHONPATH="$SCRIPT_DIR:$PYTHONPATH"

echo -e "${GREEN}============================================================${NC}"
echo -e "${GREEN}🚀 FARMASTER BOT - VPS HELPER${NC}"
echo -e "${GREEN}============================================================${NC}"
echo -e "Working Directory: ${YELLOW}$SCRIPT_DIR${NC}"
echo -e "PYTHONPATH: ${YELLOW}$PYTHONPATH${NC}"
echo ""

# Function to show menu
show_menu() {
    echo -e "${GREEN}Chọn hành động:${NC}"
    echo "1. Train Models (ml/train_ensemble.py)"
    echo "2. Run Backtest (run_backtest.py)"
    echo "3. Run Bot Live (main.py)"
    echo "4. Run Bot in Background (nohup)"
    echo "5. Check Bot Status"
    echo "6. View Bot Logs"
    echo "7. Stop Bot"
    echo "8. Install Dependencies"
    echo "9. Verify Installation"
    echo "0. Exit"
    echo ""
    read -p "Nhập lựa chọn (0-9): " choice
}

# Function to train models
train_models() {
    echo -e "${GREEN}📚 Training Ensemble Models...${NC}"
    python ml/train_ensemble.py
}

# Function to run backtest
run_backtest() {
    echo -e "${GREEN}📊 Running Backtest...${NC}"
    python run_backtest.py
}

# Function to run bot live
run_bot_live() {
    echo -e "${GREEN}🤖 Starting Bot (Live Mode)...${NC}"
    python main.py
}

# Function to run bot in background
run_bot_background() {
    echo -e "${GREEN}🤖 Starting Bot in Background...${NC}"
    nohup python main.py > bot.log 2>&1 &
    BOT_PID=$!
    echo $BOT_PID > bot.pid
    echo -e "${GREEN}✅ Bot started with PID: ${YELLOW}$BOT_PID${NC}"
    echo -e "Log file: ${YELLOW}bot.log${NC}"
    echo -e "PID file: ${YELLOW}bot.pid${NC}"
}

# Function to check bot status
check_status() {
    if [ -f bot.pid ]; then
        BOT_PID=$(cat bot.pid)
        if ps -p $BOT_PID > /dev/null; then
            echo -e "${GREEN}✅ Bot is running (PID: ${YELLOW}$BOT_PID${NC}${GREEN})${NC}"
        else
            echo -e "${RED}❌ Bot is not running (stale PID file)${NC}"
            rm bot.pid
        fi
    else
        echo -e "${YELLOW}⚠️ No PID file found. Bot may not be running.${NC}"
    fi
    
    # Check for any python main.py process
    MAIN_PID=$(pgrep -f "python main.py")
    if [ ! -z "$MAIN_PID" ]; then
        echo -e "${GREEN}Found main.py process: ${YELLOW}$MAIN_PID${NC}"
    fi
}

# Function to view logs
view_logs() {
    if [ -f bot.log ]; then
        echo -e "${GREEN}📋 Bot Logs (last 50 lines):${NC}"
        tail -n 50 bot.log
        echo ""
        read -p "Press Enter to continue or 'f' to follow logs: " follow
        if [ "$follow" = "f" ]; then
            tail -f bot.log
        fi
    else
        echo -e "${RED}❌ No log file found${NC}"
    fi
}

# Function to stop bot
stop_bot() {
    if [ -f bot.pid ]; then
        BOT_PID=$(cat bot.pid)
        echo -e "${YELLOW}Stopping bot (PID: $BOT_PID)...${NC}"
        kill $BOT_PID 2>/dev/null
        sleep 2
        if ps -p $BOT_PID > /dev/null; then
            echo -e "${RED}Bot still running, force killing...${NC}"
            kill -9 $BOT_PID 2>/dev/null
        fi
        rm bot.pid
        echo -e "${GREEN}✅ Bot stopped${NC}"
    else
        # Try to find and kill any main.py process
        MAIN_PID=$(pgrep -f "python main.py")
        if [ ! -z "$MAIN_PID" ]; then
            echo -e "${YELLOW}Found main.py process: $MAIN_PID${NC}"
            read -p "Kill this process? (y/n): " confirm
            if [ "$confirm" = "y" ]; then
                kill $MAIN_PID
                echo -e "${GREEN}✅ Process killed${NC}"
            fi
        else
            echo -e "${YELLOW}⚠️ No running bot found${NC}"
        fi
    fi
}

# Function to install dependencies
install_deps() {
    echo -e "${GREEN}📦 Installing Dependencies...${NC}"
    pip install --upgrade pip
    pip install -r requirements-vps.txt
    echo -e "${GREEN}✅ Dependencies installed${NC}"
}

# Function to verify installation
verify_install() {
    echo -e "${GREEN}🔍 Verifying Installation...${NC}"
    echo ""
    
    echo -e "${YELLOW}Checking Python packages:${NC}"
    python -c "import xgboost; print(f'✅ XGBoost: {xgboost.__version__}')" 2>/dev/null || echo -e "${RED}❌ XGBoost not found${NC}"
    python -c "import torch; print(f'✅ PyTorch: {torch.__version__}')" 2>/dev/null || echo -e "${RED}❌ PyTorch not found${NC}"
    python -c "import sklearn; print(f'✅ Scikit-learn: {sklearn.__version__}')" 2>/dev/null || echo -e "${RED}❌ Scikit-learn not found${NC}"
    python -c "import pandas; print(f'✅ Pandas: {pandas.__version__}')" 2>/dev/null || echo -e "${RED}❌ Pandas not found${NC}"
    python -c "import numpy; print(f'✅ NumPy: {numpy.__version__}')" 2>/dev/null || echo -e "${RED}❌ NumPy not found${NC}"
    
    echo ""
    echo -e "${YELLOW}Checking project modules:${NC}"
    python -c "from ml.ensemble import EnsembleModel; print('✅ Ensemble module OK')" 2>/dev/null || echo -e "${RED}❌ Ensemble module failed${NC}"
    python -c "from utils.data_fetcher import DataFetcher; print('✅ DataFetcher module OK')" 2>/dev/null || echo -e "${RED}❌ DataFetcher module failed${NC}"
    python -c "from trading.signal_generator import SignalGenerator; print('✅ SignalGenerator module OK')" 2>/dev/null || echo -e "${RED}❌ SignalGenerator module failed${NC}"
    
    echo ""
    echo -e "${YELLOW}Checking required files:${NC}"
    [ -f .env ] && echo -e "✅ .env" || echo -e "${RED}❌ .env not found${NC}"
    [ -f config.py ] && echo -e "✅ config.py" || echo -e "${RED}❌ config.py not found${NC}"
    [ -f models/lstm_model.pt ] && echo -e "✅ models/lstm_model.pt" || echo -e "${YELLOW}⚠️ models/lstm_model.pt not found (run training)${NC}"
    [ -f models/xgboost_model.json ] && echo -e "✅ models/xgboost_model.json" || echo -e "${YELLOW}⚠️ models/xgboost_model.json not found (run training)${NC}"
    [ -f config/symbol_params.json ] && echo -e "✅ config/symbol_params.json" || echo -e "${YELLOW}⚠️ config/symbol_params.json not found (will be auto-created)${NC}"
}

# Main loop
while true; do
    show_menu
    
    case $choice in
        1)
            train_models
            ;;
        2)
            run_backtest
            ;;
        3)
            run_bot_live
            ;;
        4)
            run_bot_background
            ;;
        5)
            check_status
            ;;
        6)
            view_logs
            ;;
        7)
            stop_bot
            ;;
        8)
            install_deps
            ;;
        9)
            verify_install
            ;;
        0)
            echo -e "${GREEN}Goodbye!${NC}"
            exit 0
            ;;
        *)
            echo -e "${RED}Invalid choice. Please try again.${NC}"
            ;;
    esac
    
    echo ""
    read -p "Press Enter to continue..."
    clear
done

