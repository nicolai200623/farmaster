#!/usr/bin/env python3
"""
Quick Telegram Configuration Tester
"""
import os
import sys
from dotenv import load_dotenv

# Load .env
load_dotenv()

print("=" * 60)
print("🔍 TELEGRAM CONFIGURATION CHECK")
print("=" * 60)

# Check if .env exists
if os.path.exists('.env'):
    print("✅ .env file found")
else:
    print("❌ .env file NOT found")
    print("   Please create .env from .env.example")
    sys.exit(1)

# Check Telegram Token
telegram_token = os.getenv('TELEGRAM_TOKEN', '')
if telegram_token and telegram_token != 'your_telegram_bot_token':
    print(f"✅ TELEGRAM_TOKEN: {telegram_token[:10]}...{telegram_token[-5:]}")
else:
    print("❌ TELEGRAM_TOKEN not configured")
    print("   Set TELEGRAM_TOKEN in .env")

# Check Telegram Chat ID
telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID', '')
if telegram_chat_id and telegram_chat_id != 'your_chat_id':
    print(f"✅ TELEGRAM_CHAT_ID: {telegram_chat_id}")
else:
    print("❌ TELEGRAM_CHAT_ID not configured")
    print("   Set TELEGRAM_CHAT_ID in .env")

print()

# Try to send test message if both are configured
if telegram_token and telegram_chat_id and \
   telegram_token != 'your_telegram_bot_token' and \
   telegram_chat_id != 'your_chat_id':
    print("📱 Testing Telegram notification...")

    try:
        from telegram import Bot
        import asyncio

        bot = Bot(token=telegram_token)

        # Test send message
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(
            bot.send_message(
                chat_id=telegram_chat_id,
                text="✅ Test message from FarmAster Bot\n\nTelegram notifications are working!"
            )
        )
        loop.close()

        print("✅ Test message sent successfully!")
        print("   Check your Telegram to confirm.")

    except Exception as e:
        print(f"❌ Failed to send test message: {e}")
        print("   Please check:")
        print("   1. Bot token is correct")
        print("   2. Chat ID is correct")
        print("   3. You have started the bot in Telegram")
else:
    print("⚠️ Cannot test - Telegram not fully configured")
    print("\n📝 To configure Telegram:")
    print("1. Create a bot via @BotFather on Telegram")
    print("2. Get bot token from @BotFather")
    print("3. Start your bot in Telegram")
    print("4. Get your chat ID from @userinfobot")
    print("5. Update .env with TELEGRAM_TOKEN and TELEGRAM_CHAT_ID")

print("=" * 60)
