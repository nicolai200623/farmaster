@echo off
REM ============================================
REM Windows Batch Script to Run Bot
REM ============================================

echo.
echo ========================================
echo   AsterDEX Perp Farm Bot - Windows
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.8+
    pause
    exit /b 1
)

REM Check .env
if not exist .env (
    echo WARNING: .env file not found!
    echo Creating from .env.example...
    copy .env.example .env
    echo.
    echo Please edit .env with your API keys!
    pause
    exit /b 1
)

REM Create directories
if not exist logs mkdir logs
if not exist models mkdir models

REM Check if model exists
if not exist models\lstm_model.pt (
    echo.
    echo WARNING: LSTM model not found!
    echo.
    set /p train="Do you want to train now? (y/n): "
    if /i "%train%"=="y" (
        echo.
        echo Training model...
        python ml\train.py
        if errorlevel 1 (
            echo.
            echo ERROR: Training failed!
            pause
            exit /b 1
        )
    ) else (
        echo.
        echo Please run: python ml\train.py
        pause
        exit /b 1
    )
)

REM Run bot
echo.
echo Starting bot...
echo.
python bot.py

pause

