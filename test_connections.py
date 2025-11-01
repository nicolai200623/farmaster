#!/usr/bin/env python3
"""Test AsterDEX and Telegram connections"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from config import Config
from utils.logger import logger
from binance.client import Client
from binance.exceptions import BinanceAPIException
import asyncio
from telegram import Bot

def test_asterdex():
    """Test AsterDEX API connection"""
    print("\n" + "="*60)
    print("🔍 TESTING ASTERDEX CONNECTION")
    print("="*60)

    try:
        # Initialize client (same way as AsterDEXClient)
        client = Client(Config.API_KEY, Config.API_SECRET)

        # Override FUTURES_URL (not API_URL!)
        base_url = Config.TESTNET_URL if Config.TESTNET_MODE else Config.FUTURES_BASE_URL
        client.FUTURES_URL = base_url

        print(f"✅ Futures URL: {base_url}")
        print(f"✅ Testnet Mode: {Config.TESTNET_MODE}")
        
        # Test 1: Get server time
        print("\n📡 Test 1: Server Time...")
        server_time = client.get_server_time()
        print(f"   ✅ Server Time: {server_time}")
        
        # Test 2: Get account info
        print("\n💰 Test 2: Account Info...")
        account = client.futures_account()
        balance = float(account['totalWalletBalance'])
        print(f"   ✅ Total Balance: ${balance:,.2f}")
        print(f"   ✅ Available Balance: ${float(account['availableBalance']):,.2f}")
        
        # Test 3: Get positions
        print("\n📊 Test 3: Current Positions...")
        positions = client.futures_position_information()
        active_positions = [p for p in positions if float(p['positionAmt']) != 0]
        print(f"   ✅ Active Positions: {len(active_positions)}")
        
        if active_positions:
            for pos in active_positions:
                print(f"      - {pos['symbol']}: {pos['positionAmt']} @ ${pos['entryPrice']}")
        
        # Test 4: Get market data
        print("\n📈 Test 4: Market Data...")
        for symbol in Config.SYMBOLS:
            ticker = client.futures_symbol_ticker(symbol=symbol)
            print(f"   ✅ {symbol}: ${float(ticker['price']):,.2f}")
        
        print("\n" + "="*60)
        print("✅ ASTERDEX CONNECTION: SUCCESS!")
        print("="*60)
        return True
        
    except BinanceAPIException as e:
        print(f"\n❌ AsterDEX API Error: {e}")
        print(f"   Status Code: {e.status_code}")
        print(f"   Message: {e.message}")
        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

async def test_telegram():
    """Test Telegram bot connection"""
    print("\n" + "="*60)
    print("🔍 TESTING TELEGRAM CONNECTION")
    print("="*60)
    
    try:
        if not Config.TELEGRAM_TOKEN or not Config.TELEGRAM_CHAT_ID:
            print("⚠️ Telegram not configured (optional)")
            return True
        
        # Initialize bot
        bot = Bot(token=Config.TELEGRAM_TOKEN)
        
        # Test 1: Get bot info
        print("\n🤖 Test 1: Bot Info...")
        me = await bot.get_me()
        print(f"   ✅ Bot Username: @{me.username}")
        print(f"   ✅ Bot Name: {me.first_name}")
        
        # Test 2: Send test message
        print("\n📨 Test 2: Sending Test Message...")
        message = await bot.send_message(
            chat_id=Config.TELEGRAM_CHAT_ID,
            text="🧪 **AsterDEX Bot - Connection Test**\n\n"
                 "✅ Telegram connection successful!\n"
                 "✅ Bot is ready to send notifications\n\n"
                 f"📊 Monitoring: {', '.join(Config.SYMBOLS)}\n"
                 f"⚡ Leverage: {Config.LEVERAGE}x\n"
                 f"💰 Position Size: {Config.SIZE_PCT*100}%",
            parse_mode='Markdown'
        )
        print(f"   ✅ Message sent! ID: {message.message_id}")
        
        print("\n" + "="*60)
        print("✅ TELEGRAM CONNECTION: SUCCESS!")
        print("="*60)
        return True
        
    except Exception as e:
        print(f"\n❌ Telegram Error: {e}")
        return False

async def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("🧪 ASTERDEX BOT - CONNECTION TEST")
    print("="*60)
    print(f"📍 Config File: .env")
    print(f"🔑 API Key: {Config.API_KEY[:10]}...")
    print(f"📱 Telegram: {'Configured' if Config.TELEGRAM_TOKEN else 'Not configured'}")
    
    # Test AsterDEX
    asterdex_ok = test_asterdex()
    
    # Test Telegram
    telegram_ok = await test_telegram()
    
    # Summary
    print("\n" + "="*60)
    print("📊 TEST SUMMARY")
    print("="*60)
    print(f"AsterDEX API: {'✅ PASS' if asterdex_ok else '❌ FAIL'}")
    print(f"Telegram Bot: {'✅ PASS' if telegram_ok else '❌ FAIL'}")
    print("="*60)
    
    if asterdex_ok and telegram_ok:
        print("\n🎉 ALL TESTS PASSED! Bot is ready for live trading!")
        print("\n📝 Next steps:")
        print("   1. Review your balance and risk settings")
        print("   2. Start bot: python bot.py")
        print("   3. Monitor Telegram for notifications")
    else:
        print("\n⚠️ Some tests failed. Please check configuration.")
    
    print("\n")

if __name__ == "__main__":
    asyncio.run(main())

