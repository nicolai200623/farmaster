"""
Script kiểm tra lịch sử giao dịch XRPUSDT
"""
import sys
sys.path.insert(0, '.')

from trading.asterdex_client import AsterDEXClient
from datetime import datetime, timedelta

def main():
    client = AsterDEXClient()
    
    print('='*60)
    print('📜 LỊCH SỬ GIAO DỊCH XRPUSDT (7 ngày gần nhất):')
    print('='*60)
    
    try:
        # Get trades for XRPUSDT
        trades = client.client.futures_account_trades(symbol='XRPUSDT', limit=50)
        
        if not trades:
            print('❌ Không tìm thấy giao dịch XRPUSDT nào trong lịch sử.')
            print('   -> Vị thế này có thể được mở thủ công trên sàn.')
        else:
            print(f'Tìm thấy {len(trades)} giao dịch:\n')
            for trade in trades[-10:]:  # Last 10 trades
                time_ms = trade.get('time', 0)
                time_str = datetime.fromtimestamp(time_ms/1000).strftime('%Y-%m-%d %H:%M:%S')
                side = trade.get('side', 'N/A')
                price = float(trade.get('price', 0))
                qty = float(trade.get('qty', 0))
                realized_pnl = float(trade.get('realizedPnl', 0))
                commission = float(trade.get('commission', 0))
                
                print(f'  {time_str}: {side}')
                print(f'    Price: ${price:.4f} | Qty: {qty}')
                print(f'    Realized PnL: ${realized_pnl:.4f} | Fee: ${commission:.6f}')
                print()
                
    except Exception as e:
        print(f'❌ Lỗi khi lấy lịch sử giao dịch: {e}')
    
    # Also check if XRPUSDT was ever in any old config
    print('='*60)
    print('📋 KIỂM TRA CẤU HÌNH TRƯỚC ĐÓ:')
    print('='*60)
    
    # Check .env file for any mention of XRP
    try:
        with open('.env', 'r') as f:
            env_content = f.read()
            if 'XRP' in env_content:
                print('⚠️ Tìm thấy XRP trong file .env hiện tại!')
                for line in env_content.split('\n'):
                    if 'XRP' in line:
                        print(f'   {line}')
            else:
                print('✅ Không có XRP trong file .env hiện tại')
    except:
        pass

if __name__ == '__main__':
    main()

