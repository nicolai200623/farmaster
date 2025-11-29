"""
Script để kiểm tra tất cả vị thế đang mở và so sánh với cấu hình SYMBOLS
"""
import sys
sys.path.insert(0, '.')

from trading.asterdex_client import AsterDEXClient
from config import Config

def main():
    # Initialize client
    client = AsterDEXClient()

    # Get all open positions
    print('='*60)
    print('📊 TẤT CẢ VỊ THẾ ĐANG MỞ TRÊN SÀN:')
    print('='*60)

    # Get positions for all possible symbols (not just config symbols)
    # Use the raw API to get ALL positions
    all_positions = client.client.futures_position_information()
    open_positions = [p for p in all_positions if abs(float(p.get('positionAmt', 0))) > 0]

    symbols_in_positions = set()
    for pos in open_positions:
        symbol = pos.get('symbol', 'N/A')
        symbols_in_positions.add(symbol)
        side = 'LONG' if float(pos.get('positionAmt', 0)) > 0 else 'SHORT'
        amt = abs(float(pos.get('positionAmt', 0)))
        entry = float(pos.get('entryPrice', 0))
        mark = float(pos.get('markPrice', 0))
        pnl = float(pos.get('unRealizedProfit', 0))
        margin_type = pos.get('marginType', 'N/A')
        
        in_config = "✅" if symbol in Config.SYMBOLS else "❌ NOT IN CONFIG"
        
        print(f'  {symbol}: {side} {amt} {in_config}')
        print(f'    Entry: ${entry:.4f} | Mark: ${mark:.4f}')
        print(f'    PnL: ${pnl:.2f} | Margin: {margin_type}')
        print()

    # Check against config
    print('='*60)
    print('⚙️ SYMBOLS TRONG CẤU HÌNH BOT:')
    print('='*60)
    config_symbols = set(Config.SYMBOLS)
    print(f'  {Config.SYMBOLS}')
    print()

    # Find discrepancies
    print('='*60)
    print('🔍 PHÂN TÍCH SỰ KHÔNG KHỚP:')
    print('='*60)

    # Positions not in config
    not_in_config = symbols_in_positions - config_symbols
    if not_in_config:
        print(f'❌ Vị thế KHÔNG trong SYMBOLS config:')
        for s in not_in_config:
            print(f'   - {s}')
        print()
        print('⚠️ CẢNH BÁO: Các vị thế này sẽ KHÔNG được bot quản lý!')
        print('   Bot sẽ không theo dõi TP/SL/Trailing cho các symbol này.')
    else:
        print('✅ Tất cả vị thế đều nằm trong SYMBOLS config')

    print()

    # Config symbols without positions
    no_position = config_symbols - symbols_in_positions
    if no_position:
        print(f'📭 SYMBOLS trong config KHÔNG có vị thế:')
        for s in no_position:
            print(f'   - {s}')

if __name__ == '__main__':
    main()

