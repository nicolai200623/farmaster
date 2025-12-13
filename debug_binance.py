#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================
# DEBUG BINANCE API & BALANCE
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
from binance.client import Client
from binance.exceptions import BinanceAPIException

def debug_binance():
    """Debug Binance API connection và balance"""

    print("=" * 70)
    print("🔍 BINANCE API DEBUG")
    print("=" * 70)
    print()

    # Step 1: Check config
    print("📋 Step 1: Checking Configuration")
    print("-" * 70)

    exchanges = Config.EXCHANGES
    print(f"EXCHANGES config: {exchanges}")

    if 'binance' not in exchanges:
        print("❌ ERROR: 'binance' not in EXCHANGES!")
        print("   Add to .env: EXCHANGES=asterdex,binance")
        return

    print(f"✅ Binance is enabled in EXCHANGES")
    print()

    # Step 2: Check API credentials
    print("🔑 Step 2: Checking API Credentials")
    print("-" * 70)

    api_key = Config.BINANCE_API_KEY
    api_secret = Config.BINANCE_API_SECRET
    testnet = Config.BINANCE_TESTNET_MODE

    if not api_key or not api_secret:
        print("❌ ERROR: BINANCE_API_KEY or BINANCE_API_SECRET is empty!")
        print("   Check your .env file")
        return

    print(f"API Key: {api_key[:10]}...{api_key[-5:]}")
    print(f"API Secret: {api_secret[:10]}...***")
    print(f"Testnet Mode: {testnet}")
    print()

    # Step 3: Test basic connection
    print("🔌 Step 3: Testing API Connection")
    print("-" * 70)

    try:
        client = Client(api_key, api_secret)

        # Set correct URL
        if not testnet:
            # Mainnet - no need to change URL
            print("Using Binance MAINNET")
        else:
            client.FUTURES_URL = 'https://testnet.binancefuture.com'
            print("Using Binance TESTNET")

        # Test server time
        server_time = client.get_server_time()
        print(f"✅ Connected to Binance API")
        print(f"   Server time: {server_time}")
        print()

    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return

    # Step 4: Check API permissions
    print("🔐 Step 4: Checking API Permissions")
    print("-" * 70)

    has_trading_permission = False

    try:
        # Try to get account info (requires READ permission)
        account = client.futures_account()
        print("✅ API has READ permission")

        # Check if can update position mode (requires TRADING permission)
        try:
            # This is a read-only check, won't change anything
            position_mode = client.futures_get_position_mode()
            print(f"✅ API has TRADING permission (dual position mode: {position_mode})")
            has_trading_permission = True
        except BinanceAPIException as e:
            if e.code == -2015:
                print("❌ API does NOT have TRADING permission!")
                print("   Error: Invalid API-key, IP, or permissions for action")
                print()
                print("   🔧 FIX:")
                print("   1. Go to: https://www.binance.com/en/my/settings/api-management")
                print("   2. Edit your API key")
                print("   3. Enable 'Enable Spot & Margin Trading'")
                print("   4. Enable 'Enable Futures'")
                print("   5. Save and try again")
                print()
                has_trading_permission = False
            else:
                print(f"⚠️  Permission check warning: {e}")

        print()

    except Exception as e:
        print(f"❌ Failed to check permissions: {e}")
        print("   Continuing to check balance...")
        print()

    # Step 5: Get Futures account balance
    print("💰 Step 5: Getting Futures Balance")
    print("-" * 70)

    try:
        # Method 1: futures_account_balance()
        print("Method 1: futures_account_balance()")
        balances = client.futures_account_balance()

        print(f"Total assets: {len(balances)}")

        # Find USDT
        usdt_balance = None
        for b in balances:
            if b['asset'] == 'USDT':
                usdt_balance = b
                break

        if usdt_balance:
            balance = float(usdt_balance['balance'])
            available = float(usdt_balance['availableBalance'])
            print(f"✅ USDT Balance: ${balance:.2f}")
            print(f"   Available: ${available:.2f}")
            print(f"   Raw data: {usdt_balance}")

            if balance == 0:
                print()
                print("⚠️  Balance is $0!")
                print("   Possible reasons:")
                print("   1. USDT is in Spot wallet, not Futures wallet")
                print("   2. Need to transfer: Wallet → Transfer → To USDⓈ-M Futures")
                print("   3. Using wrong API key (testnet vs mainnet)")
        else:
            print("❌ USDT not found in balance!")
            print("   Available assets:")
            for b in balances[:5]:
                print(f"   - {b['asset']}: {b['balance']}")

        print()

    except Exception as e:
        print(f"❌ Failed to get balance (Method 1): {e}")
        print()

    # Method 2: futures_account()
    try:
        print("Method 2: futures_account() - Full account info")
        account = client.futures_account()

        total_wallet_balance = float(account.get('totalWalletBalance', 0))
        available_balance = float(account.get('availableBalance', 0))
        total_unrealized_profit = float(account.get('totalUnrealizedProfit', 0))

        print(f"Total Wallet Balance: ${total_wallet_balance:.2f}")
        print(f"Available Balance: ${available_balance:.2f}")
        print(f"Unrealized P&L: ${total_unrealized_profit:.2f}")

        if total_wallet_balance == 0:
            print()
            print("⚠️  Total wallet balance is $0!")
            print()
            print("🔧 SOLUTION:")
            print("   1. Go to Binance → Wallet → Overview")
            print("   2. Click 'Transfer'")
            print("   3. From: Spot Wallet")
            print("   4. To: USDⓈ-M Futures")
            print("   5. Coin: USDT")
            print("   6. Amount: 110 (or whatever amount you want)")
            print("   7. Confirm transfer")
            print()

        print()

    except Exception as e:
        print(f"❌ Failed to get account info (Method 2): {e}")
        print()

    # Step 6: Check open positions
    print("📊 Step 6: Checking Open Positions")
    print("-" * 70)

    try:
        positions = client.futures_position_information()

        open_positions = [p for p in positions if float(p['positionAmt']) != 0]

        if open_positions:
            print(f"Found {len(open_positions)} open positions:")
            for p in open_positions:
                print(f"  {p['symbol']}: {p['positionAmt']} @ {p['entryPrice']}")
        else:
            print("No open positions")

        print()

    except Exception as e:
        print(f"❌ Failed to get positions: {e}")
        print()

    # Step 7: Recommendations
    print("=" * 70)
    print("📝 SUMMARY & RECOMMENDATIONS")
    print("=" * 70)
    print()
    print("Common issues and solutions:")
    print()
    print("1. Balance shows $0:")
    print("   → Transfer USDT from Spot to USDⓈ-M Futures wallet")
    print()
    print("2. API permission error (-2015):")
    print("   → Enable 'Enable Spot & Margin Trading' in API settings")
    print()
    print("3. Wrong balance shown:")
    print("   → Check if using correct API key (not testnet key)")
    print()
    print("4. VPS can't start bot:")
    print("   → Check if .env file exists and has correct config")
    print("   → Run: cat .env | grep BINANCE")
    print()

if __name__ == '__main__':
    debug_binance()
