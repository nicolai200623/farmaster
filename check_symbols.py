#!/usr/bin/env python3
"""Check which symbols are available for trading on AsterDEX"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from config import Config
from trading.asterdex_client import AsterDEXClient
from binance.exceptions import BinanceAPIException

def check_symbols():
    """Check which symbols are tradeable"""
    print("\n" + "="*60)
    print("🔍 CHECKING AVAILABLE SYMBOLS ON ASTERDEX")
    print("="*60)
    
    client = AsterDEXClient()
    
    # Get exchange info
    try:
        print("\n📡 Fetching exchange info...")
        exchange_info = client.client.futures_exchange_info()
        
        # Filter tradeable symbols
        tradeable = []
        for symbol_info in exchange_info['symbols']:
            symbol = symbol_info['symbol']
            status = symbol_info['status']
            
            # Only show USDT pairs
            if symbol.endswith('USDT'):
                is_trading = status == 'TRADING'
                tradeable.append({
                    'symbol': symbol,
                    'status': status,
                    'tradeable': is_trading
                })
        
        # Sort by symbol name
        tradeable.sort(key=lambda x: x['symbol'])
        
        print(f"\n✅ Found {len(tradeable)} USDT pairs")
        print("\n" + "="*60)
        print("SYMBOL STATUS")
        print("="*60)
        
        trading_count = 0
        for s in tradeable:
            status_icon = "✅" if s['tradeable'] else "❌"
            print(f"{status_icon} {s['symbol']:15} - {s['status']}")
            if s['tradeable']:
                trading_count += 1
        
        print("\n" + "="*60)
        print(f"📊 SUMMARY")
        print("="*60)
        print(f"Total USDT pairs: {len(tradeable)}")
        print(f"Trading: {trading_count}")
        print(f"Not trading: {len(tradeable) - trading_count}")
        
        # Check configured symbols
        print("\n" + "="*60)
        print(f"🔧 CONFIGURED SYMBOLS IN .env")
        print("="*60)
        
        for symbol in Config.SYMBOLS:
            symbol_data = next((s for s in tradeable if s['symbol'] == symbol), None)
            if symbol_data:
                if symbol_data['tradeable']:
                    print(f"✅ {symbol} - OK (TRADING)")
                else:
                    print(f"❌ {symbol} - NOT AVAILABLE ({symbol_data['status']})")
            else:
                print(f"❌ {symbol} - NOT FOUND")
        
        # Suggest popular trading pairs
        print("\n" + "="*60)
        print(f"💡 SUGGESTED SYMBOLS (TRADING)")
        print("="*60)
        
        popular = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'SOLUSDT', 'XRPUSDT', 
                   'ADAUSDT', 'DOGEUSDT', 'MATICUSDT', 'DOTUSDT', 'AVAXUSDT']
        
        suggested = []
        for symbol in popular:
            symbol_data = next((s for s in tradeable if s['symbol'] == symbol), None)
            if symbol_data and symbol_data['tradeable']:
                suggested.append(symbol)
                print(f"✅ {symbol}")
        
        if suggested:
            print(f"\n💡 Recommended .env config:")
            print(f"SYMBOLS={','.join(suggested[:5])}")
        
    except BinanceAPIException as e:
        print(f"❌ API Error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    check_symbols()

