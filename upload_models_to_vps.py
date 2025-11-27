#!/usr/bin/env python3
"""
📤 UPLOAD MODELS TO VPS
Tự động upload trained models từ local lên VPS
"""

import os
import sys
import subprocess
from pathlib import Path

# ============================================
# CẤU HÌNH VPS - SỬA PHẦN NÀY
# ============================================
VPS_USER = "your-username"  # Thay bằng username VPS
VPS_HOST = "your-vps-ip"    # Thay bằng IP VPS
VPS_PATH = "/home/farmaster/farmaster/models"  # Đường dẫn models trên VPS
VPS_PORT = 22  # SSH port (thường là 22)

# ============================================
# MODELS CẦN UPLOAD
# ============================================
MODELS_DIR = "models"
REQUIRED_MODELS = [
    "lstm_model.pt",
    "xgboost_model.json",
    "lightgbm_model.txt",
    "catboost_model.cbm"
]

def check_models_exist():
    """Kiểm tra xem models có tồn tại trên local không"""
    print("🔍 Checking local models...")
    missing = []
    
    for model in REQUIRED_MODELS:
        model_path = os.path.join(MODELS_DIR, model)
        if not os.path.exists(model_path):
            missing.append(model)
        else:
            size = os.path.getsize(model_path) / (1024 * 1024)  # MB
            print(f"   ✅ {model:<25} {size:>8.2f} MB")
    
    if missing:
        print(f"\n❌ Missing models: {', '.join(missing)}")
        print("   Please train models first: python scripts/auto_retrain.py --days 180")
        return False
    
    print(f"\n✅ All {len(REQUIRED_MODELS)} models found!")
    return True

def check_vps_config():
    """Kiểm tra cấu hình VPS"""
    print("\n🔧 Checking VPS configuration...")
    
    if VPS_USER == "your-username" or VPS_HOST == "your-vps-ip":
        print("❌ Please configure VPS settings in this script:")
        print("   1. Open: upload_models_to_vps.py")
        print("   2. Edit lines 12-14:")
        print(f"      VPS_USER = '{VPS_USER}'  # Your VPS username")
        print(f"      VPS_HOST = '{VPS_HOST}'  # Your VPS IP")
        print(f"      VPS_PATH = '{VPS_PATH}'")
        return False
    
    print(f"   VPS User: {VPS_USER}")
    print(f"   VPS Host: {VPS_HOST}")
    print(f"   VPS Path: {VPS_PATH}")
    print(f"   SSH Port: {VPS_PORT}")
    return True

def test_ssh_connection():
    """Test SSH connection to VPS"""
    print("\n🔌 Testing SSH connection...")
    
    try:
        # Test connection with timeout
        cmd = [
            "ssh",
            "-p", str(VPS_PORT),
            "-o", "ConnectTimeout=10",
            "-o", "BatchMode=yes",  # No password prompt
            f"{VPS_USER}@{VPS_HOST}",
            "echo 'Connection OK'"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        
        if result.returncode == 0:
            print("   ✅ SSH connection successful!")
            return True
        else:
            print("   ❌ SSH connection failed!")
            print(f"   Error: {result.stderr}")
            print("\n💡 Troubleshooting:")
            print("   1. Check VPS_USER and VPS_HOST are correct")
            print("   2. Make sure you can SSH manually: ssh user@vps-ip")
            print("   3. Setup SSH key authentication (recommended)")
            return False
    except subprocess.TimeoutExpired:
        print("   ❌ Connection timeout!")
        return False
    except FileNotFoundError:
        print("   ❌ SSH command not found!")
        print("   Please install OpenSSH client")
        return False

def upload_models():
    """Upload models to VPS using SCP"""
    print("\n📤 Uploading models to VPS...")
    print("=" * 70)
    
    success_count = 0
    
    for model in REQUIRED_MODELS:
        local_path = os.path.join(MODELS_DIR, model)
        remote_path = f"{VPS_USER}@{VPS_HOST}:{VPS_PATH}/{model}"
        
        print(f"\n📦 Uploading {model}...")
        
        try:
            cmd = [
                "scp",
                "-P", str(VPS_PORT),
                local_path,
                remote_path
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"   ✅ {model} uploaded successfully!")
                success_count += 1
            else:
                print(f"   ❌ Failed to upload {model}")
                print(f"   Error: {result.stderr}")
        
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 70)
    print(f"📊 Upload Summary: {success_count}/{len(REQUIRED_MODELS)} models uploaded")
    
    return success_count == len(REQUIRED_MODELS)

def verify_on_vps():
    """Verify models on VPS"""
    print("\n🔍 Verifying models on VPS...")
    
    try:
        cmd = [
            "ssh",
            "-p", str(VPS_PORT),
            f"{VPS_USER}@{VPS_HOST}",
            f"ls -lh {VPS_PATH}/*.{{pt,json,txt,cbm}} 2>/dev/null"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("   ✅ Models on VPS:")
            print(result.stdout)
            return True
        else:
            print("   ⚠️ Could not verify models on VPS")
            return False
    
    except Exception as e:
        print(f"   ⚠️ Verification error: {e}")
        return False

def main():
    print("=" * 70)
    print("📤 UPLOAD MODELS TO VPS")
    print("=" * 70)
    
    # Step 1: Check local models
    if not check_models_exist():
        sys.exit(1)
    
    # Step 2: Check VPS config
    if not check_vps_config():
        sys.exit(1)
    
    # Step 3: Test SSH connection
    if not test_ssh_connection():
        print("\n💡 Tip: Setup SSH key for passwordless login:")
        print("   ssh-keygen -t rsa")
        print("   ssh-copy-id user@vps-ip")
        sys.exit(1)
    
    # Step 4: Confirm upload
    print("\n" + "=" * 70)
    print("⚠️ READY TO UPLOAD")
    print("=" * 70)
    print(f"From: {os.path.abspath(MODELS_DIR)}")
    print(f"To:   {VPS_USER}@{VPS_HOST}:{VPS_PATH}")
    print(f"Files: {len(REQUIRED_MODELS)} models (~50 MB total)")
    
    confirm = input("\n❓ Continue? (yes/no): ").strip().lower()
    
    if confirm not in ['yes', 'y']:
        print("❌ Upload cancelled")
        sys.exit(0)
    
    # Step 5: Upload
    if not upload_models():
        print("\n❌ Upload failed!")
        sys.exit(1)
    
    # Step 6: Verify
    verify_on_vps()
    
    # Success
    print("\n" + "=" * 70)
    print("✅ UPLOAD COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print("\n🚀 Next steps on VPS:")
    print("   1. SSH to VPS: ssh user@vps-ip")
    print("   2. Test models: python3 -c 'import torch; torch.load(\"models/lstm_model.pt\")'")
    print("   3. Run bot: python3 bot.py")
    print("=" * 70)

if __name__ == '__main__':
    main()

