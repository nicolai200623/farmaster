#!/usr/bin/env python3
"""
VPS Helper Script for FarmAster Bot
Cross-platform Python version
"""

import os
import sys
import subprocess
import signal
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))

# Colors for terminal output
class Colors:
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    RED = '\033[0;31m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'  # No Color

def print_header():
    """Print header"""
    print(f"{Colors.GREEN}============================================================{Colors.NC}")
    print(f"{Colors.GREEN}🚀 FARMASTER BOT - VPS HELPER{Colors.NC}")
    print(f"{Colors.GREEN}============================================================{Colors.NC}")
    print(f"Working Directory: {Colors.YELLOW}{PROJECT_ROOT}{Colors.NC}")
    print(f"Python Path: {Colors.YELLOW}{sys.executable}{Colors.NC}")
    print()

def show_menu():
    """Show main menu"""
    print(f"{Colors.GREEN}Chọn hành động:{Colors.NC}")
    print("1. Train Models (ml/train_ensemble.py)")
    print("2. Run Backtest (run_backtest.py)")
    print("3. Run Bot Live (bot.py)")
    print("4. Run Bot in Background")
    print("5. Check Bot Status")
    print("6. View Bot Logs")
    print("7. Stop Bot")
    print("8. Install Dependencies")
    print("9. Verify Installation")
    print("0. Exit")
    print()
    return input("Nhập lựa chọn (0-9): ")

def run_command(cmd, description):
    """Run a command"""
    print(f"{Colors.GREEN}{description}...{Colors.NC}")
    try:
        result = subprocess.run(
            cmd,
            cwd=PROJECT_ROOT,
            shell=True,
            check=True
        )
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.NC}")
        return False

def train_models():
    """Train ensemble models"""
    return run_command(
        f"{sys.executable} ml/train_ensemble.py",
        "📚 Training Ensemble Models"
    )

def run_backtest():
    """Run backtest"""
    return run_command(
        f"{sys.executable} run_backtest.py",
        "📊 Running Backtest"
    )

def run_bot_live():
    """Run bot in foreground"""
    return run_command(
        f"{sys.executable} bot.py",
        "🤖 Starting Bot (Live Mode)"
    )

def run_bot_background():
    """Run bot in background"""
    print(f"{Colors.GREEN}🤖 Starting Bot in Background...{Colors.NC}")
    
    pid_file = PROJECT_ROOT / "bot.pid"
    log_file = PROJECT_ROOT / "bot.log"
    
    # Check if already running
    if pid_file.exists():
        with open(pid_file, 'r') as f:
            old_pid = int(f.read().strip())
        try:
            os.kill(old_pid, 0)  # Check if process exists
            print(f"{Colors.YELLOW}⚠️ Bot already running (PID: {old_pid}){Colors.NC}")
            return False
        except OSError:
            # Process doesn't exist, remove stale PID file
            pid_file.unlink()
    
    # Start bot in background
    with open(log_file, 'w') as log:
        process = subprocess.Popen(
            [sys.executable, "bot.py"],
            cwd=PROJECT_ROOT,
            stdout=log,
            stderr=subprocess.STDOUT,
            start_new_session=True
        )
    
    # Save PID
    with open(pid_file, 'w') as f:
        f.write(str(process.pid))
    
    print(f"{Colors.GREEN}✅ Bot started with PID: {Colors.YELLOW}{process.pid}{Colors.NC}")
    print(f"Log file: {Colors.YELLOW}{log_file}{Colors.NC}")
    print(f"PID file: {Colors.YELLOW}{pid_file}{Colors.NC}")
    return True

def check_status():
    """Check bot status"""
    pid_file = PROJECT_ROOT / "bot.pid"
    
    if pid_file.exists():
        with open(pid_file, 'r') as f:
            pid = int(f.read().strip())
        
        try:
            os.kill(pid, 0)  # Check if process exists
            print(f"{Colors.GREEN}✅ Bot is running (PID: {Colors.YELLOW}{pid}{Colors.NC}{Colors.GREEN}){Colors.NC}")
        except OSError:
            print(f"{Colors.RED}❌ Bot is not running (stale PID file){Colors.NC}")
            pid_file.unlink()
    else:
        print(f"{Colors.YELLOW}⚠️ No PID file found. Bot may not be running.{Colors.NC}")

def view_logs():
    """View bot logs"""
    log_file = PROJECT_ROOT / "bot.log"
    
    if log_file.exists():
        print(f"{Colors.GREEN}📋 Bot Logs (last 50 lines):{Colors.NC}")
        with open(log_file, 'r') as f:
            lines = f.readlines()
            for line in lines[-50:]:
                print(line.rstrip())
        print()
    else:
        print(f"{Colors.RED}❌ No log file found{Colors.NC}")

def stop_bot():
    """Stop bot"""
    pid_file = PROJECT_ROOT / "bot.pid"
    
    if pid_file.exists():
        with open(pid_file, 'r') as f:
            pid = int(f.read().strip())
        
        print(f"{Colors.YELLOW}Stopping bot (PID: {pid})...{Colors.NC}")
        
        try:
            os.kill(pid, signal.SIGTERM)
            import time
            time.sleep(2)
            
            # Check if still running
            try:
                os.kill(pid, 0)
                print(f"{Colors.RED}Bot still running, force killing...{Colors.NC}")
                os.kill(pid, signal.SIGKILL)
            except OSError:
                pass
            
            pid_file.unlink()
            print(f"{Colors.GREEN}✅ Bot stopped{Colors.NC}")
        except OSError:
            print(f"{Colors.RED}❌ Process not found{Colors.NC}")
            pid_file.unlink()
    else:
        print(f"{Colors.YELLOW}⚠️ No running bot found{Colors.NC}")

def install_deps():
    """Install dependencies"""
    return run_command(
        f"{sys.executable} -m pip install --upgrade pip && {sys.executable} -m pip install -r requirements-vps.txt",
        "📦 Installing Dependencies"
    )

def verify_install():
    """Verify installation"""
    print(f"{Colors.GREEN}🔍 Verifying Installation...{Colors.NC}")
    print()
    
    print(f"{Colors.YELLOW}Checking Python packages:{Colors.NC}")
    
    packages = [
        ('xgboost', 'XGBoost'),
        ('torch', 'PyTorch'),
        ('sklearn', 'Scikit-learn'),
        ('pandas', 'Pandas'),
        ('numpy', 'NumPy'),
    ]
    
    for module, name in packages:
        try:
            mod = __import__(module)
            version = getattr(mod, '__version__', 'unknown')
            print(f"✅ {name}: {version}")
        except ImportError:
            print(f"{Colors.RED}❌ {name} not found{Colors.NC}")
    
    print()
    print(f"{Colors.YELLOW}Checking project modules:{Colors.NC}")
    
    modules = [
        ('ml.ensemble', 'EnsembleModel', 'Ensemble module'),
        ('utils.data_fetcher', 'DataFetcher', 'DataFetcher module'),
        ('trading.signal_generator', 'SignalGenerator', 'SignalGenerator module'),
    ]
    
    for module, cls, desc in modules:
        try:
            mod = __import__(module, fromlist=[cls])
            print(f"✅ {desc} OK")
        except ImportError as e:
            print(f"{Colors.RED}❌ {desc} failed: {e}{Colors.NC}")
    
    print()
    print(f"{Colors.YELLOW}Checking required files:{Colors.NC}")
    
    files = [
        ('.env', True),
        ('config.py', True),
        ('models/lstm_model.pt', False),
        ('models/xgboost_model.json', False),
        ('config/symbol_params.json', False),
    ]
    
    for file, required in files:
        file_path = PROJECT_ROOT / file
        if file_path.exists():
            print(f"✅ {file}")
        elif required:
            print(f"{Colors.RED}❌ {file} not found{Colors.NC}")
        else:
            print(f"{Colors.YELLOW}⚠️ {file} not found (will be auto-created){Colors.NC}")

def main():
    """Main function"""
    os.chdir(PROJECT_ROOT)
    
    while True:
        print_header()
        choice = show_menu()
        
        if choice == '1':
            train_models()
        elif choice == '2':
            run_backtest()
        elif choice == '3':
            run_bot_live()
        elif choice == '4':
            run_bot_background()
        elif choice == '5':
            check_status()
        elif choice == '6':
            view_logs()
        elif choice == '7':
            stop_bot()
        elif choice == '8':
            install_deps()
        elif choice == '9':
            verify_install()
        elif choice == '0':
            print(f"{Colors.GREEN}Goodbye!{Colors.NC}")
            break
        else:
            print(f"{Colors.RED}Invalid choice. Please try again.{Colors.NC}")
        
        print()
        input("Press Enter to continue...")
        
        # Clear screen (cross-platform)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()

