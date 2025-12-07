@echo off
REM ============================================
REM Quick Setup for Grok AI Validator
REM ============================================

echo.
echo ============================================
echo  Setting up Grok AI Validator
echo ============================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Error: Virtual environment not found!
    echo Please run: python -m venv venv
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Grok only needs requests (already in requirements.txt)
echo.
echo Checking dependencies...
pip show requests >nul 2>&1
if errorlevel 1 (
    echo Installing requests...
    pip install requests
) else (
    echo ✓ requests already installed
)

echo.
echo ============================================
echo  Grok Setup Complete!
echo ============================================
echo.
echo Next steps:
echo 1. Get API key from https://console.x.ai/
echo 2. Add to .env: XAI_API_KEY=your-key-here
echo 3. Run test: python scripts\test_ai_validator.py
echo 4. Start bot: python bot.py
echo.

pause
