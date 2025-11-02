#!/usr/bin/env python3
"""
Check if balance is sufficient for minimum order sizes
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import Config
from trading.asterdex_client import AsterDEXClient
from trading.risk_manager import RiskManager

def main():
    print("=" * 70)
    print("💰 BALANCE & ORDER SIZE CHECK")
    print("=" * 70)
    
    # Initialize
    client = AsterDEXClient(Config.API_KEY, Config.API_SECRET)
    risk_manager = RiskManager()
    
    # Get balance
    balance = client.get_balance()
    
    if balance is None:
        print("\n❌ Failed to get balance!")
        return
    
    print(f"\n📊 Account Info:")
    print(f"   Total Balance: ${balance:.2f} USDT")

    if Config.POSITION_SIZE_USDT is not None:
        print(f"   Position Size: ${Config.POSITION_SIZE_USDT:.2f} USDT (fixed)")
        print(f"   Leverage: {Config.LEVERAGE}x")
        print(f"   Capital per trade: ${Config.POSITION_SIZE_USDT:.2f}")
        print(f"   Buying power: ${Config.POSITION_SIZE_USDT * Config.LEVERAGE:.2f}")
    else:
        print(f"   Position Size: {Config.SIZE_PCT * 100}%")
        print(f"   Leverage: {Config.LEVERAGE}x")
        print(f"   Capital per trade: ${balance * Config.SIZE_PCT:.2f}")
        print(f"   Buying power: ${balance * Config.SIZE_PCT * Config.LEVERAGE:.2f}")
    
    # Check each symbol
    symbols = Config.SYMBOLS.split(',')
    
    print(f"\n📋 Checking {len(symbols)} symbols:")
    print("=" * 70)
    
    valid_symbols = []
    invalid_symbols = []
    
    for symbol in symbols:
        try:
            # Get price
            price = client.get_ticker_price(symbol)
            
            if price is None:
                print(f"\n❌ {symbol}: Failed to get price")
                invalid_symbols.append(symbol)
                continue
            
            # Calculate quantity
            raw_quantity = risk_manager.calculate_position_size(
                balance, price, Config.LEVERAGE
            )
            
            # Format quantity
            formatted_quantity = client.format_quantity(symbol, raw_quantity)
            
            # Get symbol info for minimum notional
            symbol_info = client._get_symbol_info(symbol)
            
            min_notional = 0
            min_qty = 0
            
            if symbol_info:
                # Get MIN_NOTIONAL filter
                min_notional_filter = next(
                    (f for f in symbol_info['filters'] if f['filterType'] == 'MIN_NOTIONAL'),
                    None
                )
                if min_notional_filter:
                    min_notional = float(min_notional_filter.get('notional', 0))
                
                # Get LOT_SIZE filter
                lot_size_filter = next(
                    (f for f in symbol_info['filters'] if f['filterType'] == 'LOT_SIZE'),
                    None
                )
                if lot_size_filter:
                    min_qty = float(lot_size_filter.get('minQty', 0))
            
            # Calculate notional value
            notional_value = formatted_quantity * price
            
            # Check if valid
            is_valid = (
                formatted_quantity > 0 and
                formatted_quantity >= min_qty and
                notional_value >= min_notional
            )
            
            # Print result
            status = "✅" if is_valid else "❌"
            print(f"\n{status} {symbol}:")
            print(f"   Price: ${price:.2f}")
            print(f"   Raw quantity: {raw_quantity:.8f}")
            print(f"   Formatted quantity: {formatted_quantity:.8f}")
            print(f"   Notional value: ${notional_value:.2f}")
            
            if min_qty > 0:
                print(f"   Min quantity: {min_qty:.8f} {'✅' if formatted_quantity >= min_qty else '❌'}")
            
            if min_notional > 0:
                print(f"   Min notional: ${min_notional:.2f} {'✅' if notional_value >= min_notional else '❌'}")
            
            if is_valid:
                valid_symbols.append(symbol)
            else:
                invalid_symbols.append(symbol)
                
                # Suggest fix
                if notional_value < min_notional:
                    required_balance = (min_notional / Config.LEVERAGE / Config.SIZE_PCT)
                    print(f"   💡 Need balance: ${required_balance:.2f} (current: ${balance:.2f})")
                
        except Exception as e:
            print(f"\n❌ {symbol}: Error - {e}")
            invalid_symbols.append(symbol)
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    
    print(f"\n✅ Valid symbols ({len(valid_symbols)}):")
    if valid_symbols:
        for symbol in valid_symbols:
            print(f"   - {symbol}")
    else:
        print("   None")
    
    if invalid_symbols:
        print(f"\n❌ Invalid symbols ({len(invalid_symbols)}):")
        for symbol in invalid_symbols:
            print(f"   - {symbol}")
        
        print("\n💡 SOLUTIONS:")
        print("   1. Increase balance (deposit more USDT)")
        print("   2. Increase SIZE_PCT in .env (e.g., SIZE_PCT=0.2 for 20%)")
        print("   3. Remove invalid symbols from SYMBOLS in .env")
        print("   4. Use higher leverage (risky!)")
    
    print("\n" + "=" * 70)
    
    if len(valid_symbols) == 0:
        print("⚠️  WARNING: No valid symbols! Bot cannot trade!")
        print("\n🔧 Quick fix:")
        print(f"   Current balance: ${balance:.2f}")
        print(f"   Recommended minimum: $100 USDT")
        print(f"   Or increase SIZE_PCT to 0.2 (20%)")
    elif len(valid_symbols) < len(symbols):
        print(f"⚠️  WARNING: Only {len(valid_symbols)}/{len(symbols)} symbols are valid")
    else:
        print("✅ All symbols are valid! Bot ready to trade!")

if __name__ == '__main__':
    main()

