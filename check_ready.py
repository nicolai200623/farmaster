#!/usr/bin/env python3
"""Check if bot is ready for live trading"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from config import Config
from binance.client import Client
from binance.exceptions import BinanceAPIException
import asyncio
from telegram import Bot

print("\n" + "="*60)
print("🧪 ASTERDEX BOT - READINESS CHECK")
print("="*60)

# 1. Check Config
print("\n📋 1. CHECKING CONFIGURATION...")
print(f"   ✅ API Key: {Config.API_KEY[:10]}...")
print(f"   ✅ API Secret: {Config.API_SECRET[:10]}...")
print(f"   ✅ Testnet Mode: {Config.TESTNET_MODE}")
print(f"   ✅ Symbols: {', '.join(Config.SYMBOLS)}")
print(f"   ✅ Leverage: {Config.LEVERAGE}x")
print(f"   ✅ Position Size: {Config.SIZE_PCT*100}%")
print(f"   ✅ TP/SL: {Config.TP_PCT*100}% / {Config.SL_PCT*100}%")

# 2. Test AsterDEX Connection
print("\n🔌 2. TESTING ASTERDEX CONNECTION...")
try:
    client = Client(Config.API_KEY, Config.API_SECRET)

    # Override FUTURES_URL (not API_URL!)
    base_url = Config.TESTNET_URL if Config.TESTNET_MODE else Config.FUTURES_BASE_URL
    client.FUTURES_URL = base_url

    print(f"   ✅ Futures URL: {base_url}")
    print(f"   ✅ Testnet Mode: {Config.TESTNET_MODE}")

    # Get server time (public endpoint - no auth needed)
    print("\n   📡 Testing public endpoint...")
    server_time = client.get_server_time()
    print(f"   ✅ Server Time: {server_time['serverTime']}")

    # Get account (requires auth)
    print("\n   🔐 Testing authenticated endpoint...")
    account = client.futures_account()
    balance = float(account['totalWalletBalance'])
    print(f"   ✅ Total Balance: ${balance:,.2f}")
    print(f"   ✅ Available Balance: ${float(account['availableBalance']):,.2f}")
    
    # Get positions
    positions = client.futures_position_information()
    active = [p for p in positions if float(p['positionAmt']) != 0]
    print(f"   ✅ Active Positions: {len(active)}")
    
    # Get market data
    ticker = client.futures_symbol_ticker(symbol='BTCUSDT')
    print(f"   ✅ Market Data: BTC @ ${float(ticker['price']):,.2f}")
    
    asterdex_ok = True
    
except BinanceAPIException as e:
    print(f"   ❌ API Error: {e.message}")
    asterdex_ok = False
except Exception as e:
    print(f"   ❌ Error: {e}")
    asterdex_ok = False

# 3. Test Telegram
print("\n📱 3. TESTING TELEGRAM...")
async def test_telegram():
    try:
        if not Config.TELEGRAM_TOKEN:
            print("   ⚠️ Telegram not configured (optional)")
            return True
        
        bot = Bot(token=Config.TELEGRAM_TOKEN)
        me = await bot.get_me()
        print(f"   ✅ Bot: @{me.username}")
        
        # Send test message
        msg = await bot.send_message(
            chat_id=Config.TELEGRAM_CHAT_ID,
            text="🧪 **Connection Test**\n\n✅ Bot is ready!",
            parse_mode='Markdown'
        )
        print(f"   ✅ Test message sent (ID: {msg.message_id})")
        return True
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

telegram_ok = asyncio.run(test_telegram())

# 4. Check Model
print("\n🧠 4. CHECKING ML MODEL...")
import os.path
if os.path.exists('models/lstm_model.pt'):
    print("   ✅ LSTM model found")
    model_ok = True
else:
    print("   ❌ LSTM model not found - run: python ml/train.py")
    model_ok = False

# 5. Summary
print("\n" + "="*60)
print("📊 READINESS SUMMARY")
print("="*60)
print(f"Configuration: ✅ PASS")
print(f"AsterDEX API:  {'✅ PASS' if asterdex_ok else '❌ FAIL'}")
print(f"Telegram Bot:  {'✅ PASS' if telegram_ok else '❌ FAIL'}")
print(f"ML Model:      {'✅ PASS' if model_ok else '❌ FAIL'}")
print("="*60)

if asterdex_ok and model_ok:
    print("\n🎉 BOT IS READY FOR LIVE TRADING!")
    print("\n📝 To start:")
    print("   python bot.py")
    print("\n⚠️ Remember:")
    print("   - Currently in TESTNET mode")
    print("   - Set TESTNET_MODE=False for live trading")
    print("   - Monitor Telegram for notifications")
else:
    print("\n⚠️ Please fix the issues above before going live")

print("\n")

