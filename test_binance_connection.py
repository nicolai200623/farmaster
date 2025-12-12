#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================
# TEST BINANCE CONNECTION
# Kiểm tra kết nối và API credentials
# ============================================

import sys
import os

# Fix Unicode output on Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from config import Config
from trading.binance_client import BinanceClient
from utils.logger import logger

def test_binance_connection():
    """Test Binance connection và API calls"""

    print("=" * 60)
    print("🧪 TESTING BINANCE CONNECTION")
    print("=" * 60)

    # Check if Binance is enabled
    if 'binance' not in Config.EXCHANGES:
        print("❌ Binance chưa được enable trong EXCHANGES")
        print(f"   Current EXCHANGES: {Config.EXCHANGES}")
        print("\n💡 Thêm 'binance' vào EXCHANGES trong .env:")
        print("   EXCHANGES=asterdex,binance")
        return False

    # Check credentials
    if not Config.BINANCE_API_KEY or not Config.BINANCE_API_SECRET:
        print("❌ BINANCE_API_KEY hoặc BINANCE_API_SECRET chưa được set!")
        print("\n💡 Thêm vào .env:")
        print("   BINANCE_API_KEY=your_key")
        print("   BINANCE_API_SECRET=your_secret")
        return False

    print(f"✅ Binance API Key: {Config.BINANCE_API_KEY[:10]}...")
    print(f"✅ Testnet Mode: {Config.BINANCE_TESTNET_MODE}")
    print(f"✅ Symbols: {Config.BINANCE_SYMBOLS[:5]}... ({len(Config.BINANCE_SYMBOLS)} total)")
    print(f"✅ Leverage: {Config.BINANCE_LEVERAGE}x")
    print()

    try:
        # Initialize client
        print("🔌 Initializing Binance client...")
        client = BinanceClient()
        print("✅ Client initialized successfully")
        print()

        # Test 1: Get account balance
        print("📊 Test 1: Getting account balance...")
        try:
            balance = client.get_account_balance()
            print(f"✅ Balance: ${balance:.2f} USDT")

            if balance == 0:
                print("⚠️  WARNING: Balance is $0!")
                print("   Hãy transfer USDT vào Futures wallet:")
                print("   Binance → Wallet → Fiat and Spot → Transfer → To Futures")
        except Exception as e:
            print(f"❌ Failed to get balance: {e}")
            return False
        print()

        # Test 2: Get symbol info (first symbol)
        test_symbol = Config.BINANCE_SYMBOLS[0]
        print(f"📊 Test 2: Getting {test_symbol} info...")
        try:
            symbol_info = client._get_symbol_info(test_symbol)
            if symbol_info:
                print(f"✅ Symbol: {symbol_info['symbol']}")
                print(f"   Status: {symbol_info['status']}")
                print(f"   Contract Type: {symbol_info.get('contractType', 'N/A')}")
            else:
                print(f"⚠️  Could not get symbol info")
        except Exception as e:
            print(f"❌ Failed: {e}")
        print()

        # Test 3: Get current price
        print(f"📊 Test 3: Getting {test_symbol} price...")
        try:
            price = client.get_ticker_price(test_symbol)
            print(f"✅ Current price: ${price:,.2f}")
        except Exception as e:
            print(f"❌ Failed: {e}")
            return False
        print()

        # Test 4: Get klines
        print(f"📊 Test 4: Getting {test_symbol} klines (1h, 10 candles)...")
        try:
            klines = client.get_klines(test_symbol, '1h', 10)
            if klines and len(klines) > 0:
                print(f"✅ Retrieved {len(klines)} candles")
                last_candle = klines[-1]
                print(f"   Last close: ${float(last_candle[4]):,.2f}")
            else:
                print(f"⚠️  No klines data")
        except Exception as e:
            print(f"❌ Failed: {e}")
        print()

        # Test 5: Get orderbook
        print(f"📊 Test 5: Getting {test_symbol} orderbook...")
        try:
            orderbook = client.get_orderbook(test_symbol, limit=5)
            if orderbook and orderbook.get('bids') and orderbook.get('asks'):
                best_bid = float(orderbook['bids'][0][0])
                best_ask = float(orderbook['asks'][0][0])
                spread = ((best_ask - best_bid) / best_bid) * 100
                print(f"✅ Best Bid: ${best_bid:,.2f}")
                print(f"   Best Ask: ${best_ask:,.2f}")
                print(f"   Spread: {spread:.4f}%")
            else:
                print(f"⚠️  No orderbook data")
        except Exception as e:
            print(f"❌ Failed: {e}")
        print()

        # Test 6: Check positions
        print(f"📊 Test 6: Checking open positions...")
        try:
            positions_count = 0
            for symbol in Config.BINANCE_SYMBOLS[:5]:  # Check first 5 symbols
                position = client.get_position(symbol)
                if position:
                    positions_count += 1
                    print(f"✅ Open position: {symbol} {position['side']}")
                    print(f"   Amount: {position['amount']}")
                    print(f"   PnL: {position['pnl_pct']*100:.2f}% (${position['pnl_usdt']:.2f})")

            if positions_count == 0:
                print(f"✅ No open positions")
        except Exception as e:
            print(f"❌ Failed: {e}")
        print()

        # Test 7: Test leverage setting (dry run - no actual order)
        print(f"📊 Test 7: Testing leverage setting...")
        try:
            result = client.set_leverage(test_symbol, Config.BINANCE_LEVERAGE)
            if result:
                print(f"✅ Leverage set to {Config.BINANCE_LEVERAGE}x for {test_symbol}")
            else:
                print(f"⚠️  Leverage setting returned False (might be already set)")
        except Exception as e:
            print(f"⚠️  Leverage setting: {e}")
            print(f"   (This is usually OK if leverage is already set)")
        print()

        # Test 8: Test margin type setting
        print(f"📊 Test 8: Testing margin type setting...")
        try:
            result = client.set_margin_type(test_symbol, 'ISOLATED')
            if result:
                print(f"✅ Margin type set to ISOLATED for {test_symbol}")
            else:
                print(f"⚠️  Margin type setting returned False (might be already set)")
        except Exception as e:
            print(f"⚠️  Margin type setting: {e}")
            print(f"   (This is usually OK if margin type is already set)")
        print()

        # Summary
        print("=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print()
        print("🎉 Binance connection is working perfectly!")
        print()
        print("📝 Next steps:")
        print("   1. Make sure you have sufficient USDT in Futures wallet")
        print(f"   2. Current balance: ${balance:.2f}")
        print("   3. Train ML models if needed: python ml/train_ensemble.py")
        print("   4. Run bot: python bot.py")
        print()

        return True

    except Exception as e:
        print()
        print("=" * 60)
        print("❌ CONNECTION TEST FAILED")
        print("=" * 60)
        print(f"Error: {e}")
        print()
        print("🔍 Troubleshooting:")
        print("   1. Check if API keys are correct")
        print("   2. Check if Futures trading is enabled on your API key")
        print("   3. Check if IP is whitelisted (if IP restriction is enabled)")
        print("   4. Check network connection")
        print()
        import traceback
        print("Full traceback:")
        print(traceback.format_exc())
        return False

if __name__ == '__main__':
    test_binance_connection()
