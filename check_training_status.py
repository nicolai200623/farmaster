#!/usr/bin/env python3
"""
🔍 CHECK TRAINING STATUS
Kiểm tra xem auto_retrain.py đã chạy xong chưa
"""

import os
import sys
import glob
from datetime import datetime
import json

def check_process_running():
    """Kiểm tra xem process auto_retrain.py có đang chạy không"""
    try:
        import psutil
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                cmdline = proc.info.get('cmdline', [])
                if cmdline and 'auto_retrain.py' in ' '.join(cmdline):
                    return True, proc.info['pid']
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return False, None
    except ImportError:
        # Fallback nếu không có psutil
        import subprocess
        try:
            # Linux/Mac
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            if 'auto_retrain.py' in result.stdout:
                return True, "unknown"
        except:
            # Windows
            try:
                result = subprocess.run(['tasklist'], capture_output=True, text=True)
                if 'python' in result.stdout.lower():
                    return True, "unknown"
            except:
                pass
        return False, None

def check_models_exist():
    """Kiểm tra xem models đã được tạo chưa"""
    models_dir = 'models'
    required_models = [
        'lstm_model.pt',
        'xgboost_model.json',
        'lightgbm_model.txt',
        'catboost_model.cbm'
    ]
    
    if not os.path.exists(models_dir):
        return False, []
    
    existing_models = []
    for model in required_models:
        model_path = os.path.join(models_dir, model)
        if os.path.exists(model_path):
            # Get file modification time
            mtime = os.path.getmtime(model_path)
            mtime_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
            size = os.path.getsize(model_path)
            existing_models.append({
                'name': model,
                'modified': mtime_str,
                'size': size
            })
    
    return len(existing_models) == len(required_models), existing_models

def check_latest_log():
    """Kiểm tra log file mới nhất"""
    logs_dir = 'logs'
    if not os.path.exists(logs_dir):
        return None
    
    # Find latest log file
    log_files = glob.glob(os.path.join(logs_dir, 'bot_*.log'))
    if not log_files:
        return None
    
    latest_log = max(log_files, key=os.path.getmtime)
    
    # Read last 50 lines
    try:
        with open(latest_log, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            last_lines = lines[-50:] if len(lines) > 50 else lines
            
            # Check for completion messages
            log_text = ''.join(last_lines)
            
            if 'RETRAINING COMPLETED SUCCESSFULLY' in log_text:
                return {
                    'status': 'completed',
                    'file': latest_log,
                    'last_lines': last_lines[-10:]
                }
            elif 'Training' in log_text or 'Epoch' in log_text:
                return {
                    'status': 'running',
                    'file': latest_log,
                    'last_lines': last_lines[-10:]
                }
            elif 'ERROR' in log_text or 'FAILED' in log_text:
                return {
                    'status': 'failed',
                    'file': latest_log,
                    'last_lines': last_lines[-10:]
                }
            else:
                return {
                    'status': 'unknown',
                    'file': latest_log,
                    'last_lines': last_lines[-10:]
                }
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

def main():
    print("=" * 70)
    print("🔍 CHECKING TRAINING STATUS")
    print("=" * 70)
    print()
    
    # 1. Check if process is running
    print("1️⃣ Checking if auto_retrain.py is running...")
    is_running, pid = check_process_running()
    if is_running:
        print(f"   ✅ Process is RUNNING (PID: {pid})")
    else:
        print(f"   ⏸️ Process is NOT running")
    print()
    
    # 2. Check models
    print("2️⃣ Checking models...")
    all_exist, models = check_models_exist()
    if all_exist:
        print(f"   ✅ All 4 models exist:")
        for model in models:
            size_mb = model['size'] / (1024 * 1024)
            print(f"      • {model['name']:<25} {size_mb:>8.2f} MB   {model['modified']}")
    else:
        print(f"   ⚠️ Only {len(models)}/4 models found:")
        for model in models:
            print(f"      • {model['name']}")
    print()
    
    # 3. Check logs
    print("3️⃣ Checking latest log...")
    log_info = check_latest_log()
    if log_info:
        print(f"   📄 Log file: {log_info.get('file', 'N/A')}")
        print(f"   📊 Status: {log_info.get('status', 'unknown').upper()}")
        
        if log_info.get('status') == 'completed':
            print(f"   ✅ Training COMPLETED!")
        elif log_info.get('status') == 'running':
            print(f"   🔄 Training is RUNNING...")
        elif log_info.get('status') == 'failed':
            print(f"   ❌ Training FAILED!")
        
        print(f"\n   📝 Last 10 lines:")
        for line in log_info.get('last_lines', []):
            print(f"      {line.rstrip()}")
    else:
        print(f"   ⚠️ No log files found")
    print()
    
    # 4. Summary
    print("=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    
    if log_info and log_info.get('status') == 'completed' and all_exist:
        print("✅ Training is COMPLETE and all models are ready!")
        print("\n🚀 Next steps:")
        print("   1. Run backtest: python run_backtest_90days.py")
        print("   2. Or start bot: python bot.py")
    elif is_running:
        print("🔄 Training is STILL RUNNING...")
        print("\n⏰ Estimated time remaining:")
        print("   • Check log for current epoch/progress")
        print("   • LSTM usually takes 30-40 minutes")
        print("   • Total: 45-60 minutes for 180 days")
        print("\n💡 To monitor in real-time:")
        print("   tail -f logs/bot_*.log")
    elif log_info and log_info.get('status') == 'failed':
        print("❌ Training FAILED!")
        print("\n🔧 Check the error in logs:")
        print(f"   cat {log_info.get('file')}")
    else:
        print("⚠️ Status UNCLEAR - check manually")
        print("\n💡 Commands to check:")
        print("   • ps aux | grep auto_retrain")
        print("   • ls -lh models/")
        print("   • tail -50 logs/bot_*.log")
    
    print("=" * 70)

if __name__ == '__main__':
    main()

