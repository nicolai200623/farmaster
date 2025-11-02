#!/usr/bin/env python3
"""
Test Coingecko API rate limits and data fetching
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.data_fetcher import DataFetcher
from config import Config

def test_single_symbol():
    """Test fetching single symbol"""
    print("=" * 60)
    print("🧪 TEST 1: Single Symbol Fetch")
    print("=" * 60)
    
    df = DataFetcher.fetch_historical_ohlcv('BTCUSDT', days=30)
    
    if not df.empty:
        print(f"✅ Success! Fetched {len(df)} candles")
        print(f"\nFirst 3 rows:")
        print(df.head(3))
        print(f"\nLast 3 rows:")
        print(df.tail(3))
    else:
        print("❌ Failed to fetch data")
    
    return not df.empty

def test_multiple_symbols():
    """Test fetching multiple symbols with rate limiting"""
    print("\n" + "=" * 60)
    print("🧪 TEST 2: Multiple Symbols Fetch (with rate limiting)")
    print("=" * 60)
    
    # Test with 3 symbols only to avoid rate limit
    test_symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']
    
    print(f"\nFetching {len(test_symbols)} symbols: {test_symbols}")
    print("This will take ~10 seconds due to rate limiting...\n")
    
    data_dict = DataFetcher.fetch_multiple_symbols(test_symbols, days=30)
    
    print(f"\n✅ Successfully fetched {len(data_dict)}/{len(test_symbols)} symbols")
    
    for symbol, df in data_dict.items():
        print(f"   {symbol}: {len(df)} candles")
    
    return len(data_dict) > 0

def test_coin_map():
    """Test COIN_MAP coverage"""
    print("\n" + "=" * 60)
    print("🧪 TEST 3: COIN_MAP Coverage")
    print("=" * 60)
    
    symbols = Config.SYMBOLS.split(',')
    
    print(f"\nConfigured symbols: {len(symbols)}")
    
    mapped = []
    unmapped = []
    
    for symbol in symbols:
        if symbol in DataFetcher.COIN_MAP:
            mapped.append(symbol)
        else:
            unmapped.append(symbol)
    
    print(f"\n✅ Mapped ({len(mapped)}):")
    for symbol in mapped:
        coin_id = DataFetcher.COIN_MAP[symbol]
        print(f"   {symbol} -> {coin_id}")
    
    if unmapped:
        print(f"\n⚠️  Unmapped ({len(unmapped)}) - will use 'bitcoin' as fallback:")
        for symbol in unmapped:
            print(f"   {symbol} -> bitcoin (fallback)")
    
    return True

if __name__ == '__main__':
    print("🚀 Coingecko API Test Suite")
    print("=" * 60)
    
    results = []
    
    # Test 1
    results.append(("Single Symbol", test_single_symbol()))
    
    # Test 2
    results.append(("Multiple Symbols", test_multiple_symbols()))
    
    # Test 3
    results.append(("COIN_MAP Coverage", test_coin_map()))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    all_passed = all(result[1] for result in results)
    
    if all_passed:
        print("\n🎉 All tests passed!")
    else:
        print("\n⚠️  Some tests failed")
    
    print("\n💡 Tips:")
    print("   - Coingecko free tier: ~10-30 calls/minute")
    print("   - Bot uses 3s delay between requests (safe)")
    print("   - Retry logic handles rate limits automatically")
    print("   - Unmapped symbols fallback to 'bitcoin' data")

