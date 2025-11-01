#!/usr/bin/env python3
"""Test which symbols are working on AsterDEX"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from config import Config
from trading.asterdex_client import AsterDEXClient
from binance.exceptions import BinanceAPIException

def test_symbol(client, symbol):
    """Test if a symbol is tradeable"""
    try:
        # Test 1: Get ticker
        ticker = client.client.futures_symbol_ticker(symbol=symbol)
        price = float(ticker['price'])
        
        # Test 2: Get orderbook
        orderbook = client.client.futures_order_book(symbol=symbol, limit=5)
        
        # Test 3: Get klines
        klines = client.client.futures_klines(symbol=symbol, interval='1m', limit=5)
        
        return {
            'symbol': symbol,
            'status': 'OK',
            'price': price,
            'error': None
        }
    except BinanceAPIException as e:
        return {
            'symbol': symbol,
            'status': 'ERROR',
            'price': 0,
            'error': f"{e.code}: {e.message}"
        }
    except Exception as e:
        return {
            'symbol': symbol,
            'status': 'ERROR',
            'price': 0,
            'error': str(e)
        }

def main():
    print("\n" + "="*70)
    print("🧪 TESTING SYMBOLS ON ASTERDEX")
    print("="*70)
    
    client = AsterDEXClient()
    
    print(f"\n📋 Testing {len(Config.SYMBOLS)} symbols from .env...")
    print()
    
    results = []
    for symbol in Config.SYMBOLS:
        print(f"Testing {symbol}...", end=" ")
        result = test_symbol(client, symbol)
        results.append(result)
        
        if result['status'] == 'OK':
            print(f"✅ OK (${result['price']:,.2f})")
        else:
            print(f"❌ FAILED - {result['error']}")
    
    # Summary
    print("\n" + "="*70)
    print("📊 SUMMARY")
    print("="*70)
    
    working = [r for r in results if r['status'] == 'OK']
    failed = [r for r in results if r['status'] == 'ERROR']
    
    print(f"\n✅ Working symbols: {len(working)}/{len(results)}")
    if working:
        for r in working:
            print(f"   ✅ {r['symbol']:12} @ ${r['price']:,.2f}")
    
    print(f"\n❌ Failed symbols: {len(failed)}/{len(results)}")
    if failed:
        for r in failed:
            print(f"   ❌ {r['symbol']:12} - {r['error']}")
    
    # Recommendation
    if working:
        print("\n" + "="*70)
        print("💡 RECOMMENDED .env CONFIG")
        print("="*70)
        working_symbols = [r['symbol'] for r in working]
        print(f"\nSYMBOLS={','.join(working_symbols)}")
        
        # Prioritize BTC/ETH for airdrop boost
        priority = []
        for sym in ['BTCUSDT', 'ETHUSDT']:
            if sym in working_symbols:
                priority.append(sym)
        
        # Add other working symbols
        for sym in working_symbols:
            if sym not in priority:
                priority.append(sym)
        
        if len(priority) > 5:
            priority = priority[:5]
        
        print(f"\n💎 Top 5 (BTC/ETH prioritized for 2x boost):")
        print(f"SYMBOLS={','.join(priority)}")
    else:
        print("\n⚠️ No working symbols found! Check AsterDEX status.")
    
    print()

if __name__ == '__main__':
    main()

