#!/usr/bin/env python3
# ============================================
# 🚀 APPLY VOLUME FARMING CONFIGURATION
# Script để áp dụng cấu hình tối ưu cho farming volume
# ============================================

import os
import shutil
from datetime import datetime

def backup_current_env():
    """Backup file .env hiện tại"""
    if os.path.exists('.env'):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = f'.env.backup_{timestamp}'
        shutil.copy('.env', backup_file)
        print(f"✅ Đã backup .env hiện tại -> {backup_file}")
        return backup_file
    return None

def apply_volume_farming_config():
    """Áp dụng cấu hình volume farming"""
    if not os.path.exists('.env.volume_farming'):
        print("❌ Không tìm thấy file .env.volume_farming")
        return False
    
    # Backup current config
    backup_file = backup_current_env()
    
    # Copy volume farming config
    shutil.copy('.env.volume_farming', '.env')
    print("✅ Đã áp dụng cấu hình volume farming")
    
    return True

def show_config_comparison():
    """Hiển thị so sánh cấu hình"""
    print("\n" + "="*60)
    print("📊 SO SÁNH CÁC THAY ĐỔI CHÍNH")
    print("="*60)
    
    changes = [
        ("SYMBOLS", "6 pairs", "8 pairs", "Tăng cơ hội giao dịch"),
        ("LOOP_SLEEP", "60s", "30s", "Kiểm tra thường xuyên hơn"),
        ("LSTM_THRESHOLD", "0.45", "0.40", "Dễ tạo tín hiệu hơn"),
        ("MIN_CONFLUENCE_SCORE", "4", "3", "Giảm yêu cầu confluence"),
        ("WAIT_FOR_CONFIRMATION", "True", "False", "Entry nhanh hơn"),
        ("USE_TREND_FILTER", "True", "False", "Ít filter hơn"),
        ("USE_VOLUME_FILTER", "True", "False", "Ít filter hơn"),
        ("MIN_SIGNAL_QUALITY_SCORE", "50", "30", "Chấp nhận tín hiệu yếu hơn"),
        ("USE_TRAILING_STOP", "True", "False", "Chỉ dùng TP 1%"),
        ("USE_BREAKEVEN_STOP", "True", "False", "Đơn giản hóa"),
        ("USE_MARKET_REGIME", "True", "False", "Trade mọi điều kiện"),
        ("POSITION_TIMEOUT_HOURS", "24h", "48h", "Giữ lệnh lâu hơn"),
    ]
    
    print(f"{'Tham số':<25} {'Cũ':<10} {'Mới':<10} {'Lý do'}")
    print("-"*60)
    for param, old, new, reason in changes:
        print(f"{param:<25} {old:<10} {new:<10} {reason}")
    
    print("\n" + "="*60)
    print("🎯 KẾT QUẢ DỰ KIẾN")
    print("="*60)
    print("📈 Số lượng giao dịch: +50-80% (từ 10-15 lên 18-25 trades/tháng)")
    print("💰 Volume: +50-80% (từ $200-300k lên $350-500k/tháng)")
    print("⚠️  Win rate: Có thể giảm 5-10% (vẫn >55%)")
    print("✅ Profit: Tăng nhờ nhiều giao dịch hơn")
    print("="*60)

def validate_config():
    """Kiểm tra cấu hình mới"""
    print("\n🔍 Kiểm tra cấu hình...")
    
    try:
        from config import Config
        Config.validate()
        print("✅ Cấu hình hợp lệ!")
        
        # Show key settings
        print("\n📋 CÁC THIẾT LẬP CHÍNH:")
        print(f"   Symbols: {len(Config.SYMBOLS)} pairs")
        print(f"   Leverage: {Config.LEVERAGE}x")
        print(f"   Position Size: ${Config.POSITION_SIZE_USDT} USDT")
        print(f"   TP: {Config.TP_PCT}%")
        print(f"   SL: {'Disabled' if Config.SL_PCT is None or Config.SL_PCT == 0 else f'{Config.SL_PCT}%'}")
        print(f"   Loop Sleep: {Config.LOOP_SLEEP}s")
        print(f"   LSTM Threshold: {Config.LSTM_THRESHOLD}")
        print(f"   Min Confluence: {Config.MIN_CONFLUENCE_SCORE}")
        
        return True
    except Exception as e:
        print(f"❌ Lỗi cấu hình: {e}")
        return False

def main():
    """Main function"""
    print("="*60)
    print("🚀 VOLUME FARMING CONFIGURATION TOOL")
    print("="*60)
    
    # Show comparison
    show_config_comparison()
    
    # Ask for confirmation
    print("\n⚠️  Bạn có muốn áp dụng cấu hình mới không?")
    print("   File .env hiện tại sẽ được backup tự động.")
    response = input("   Nhập 'yes' để tiếp tục: ").strip().lower()
    
    if response != 'yes':
        print("❌ Đã hủy. Không có thay đổi nào được thực hiện.")
        return
    
    # Apply config
    if apply_volume_farming_config():
        # Validate
        if validate_config():
            print("\n" + "="*60)
            print("✅ HOÀN TẤT!")
            print("="*60)
            print("📝 Các bước tiếp theo:")
            print("   1. Kiểm tra file .env")
            print("   2. Chạy backtest: python run_backtest.py")
            print("   3. Nếu kết quả tốt, khởi động bot: python bot.py")
            print("   4. Theo dõi logs và Telegram")
            print("="*60)
        else:
            print("\n❌ Có lỗi trong cấu hình. Vui lòng kiểm tra lại.")
            print("   Bạn có thể restore từ file backup nếu cần.")
    else:
        print("❌ Không thể áp dụng cấu hình mới.")

if __name__ == '__main__':
    main()

