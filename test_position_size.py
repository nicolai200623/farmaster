#!/usr/bin/env python3
"""Test position size configuration"""

from config import Config

print("=" * 60)
print("🧪 POSITION SIZE CONFIG TEST")
print("=" * 60)

print(f"\n📊 Current Config:")
print(f"   SIZE_PCT: {Config.SIZE_PCT}")
print(f"   POSITION_SIZE_USDT: {Config.POSITION_SIZE_USDT}")
print(f"   LEVERAGE: {Config.LEVERAGE}")

print("\n" + "=" * 60)
Config.validate()
print("=" * 60)

# Test calculation
print("\n💰 Position Size Calculation Test:")
print("=" * 60)

test_balance = 100.0
test_price = 70000.0

if Config.POSITION_SIZE_USDT is not None:
    capital = Config.POSITION_SIZE_USDT
    print(f"Mode: Fixed USDT")
    print(f"Capital: ${capital:.2f} (fixed)")
else:
    capital = test_balance * Config.SIZE_PCT
    print(f"Mode: Percentage")
    print(f"Capital: ${capital:.2f} ({Config.SIZE_PCT*100}% of ${test_balance})")

buying_power = capital * Config.LEVERAGE
quantity = buying_power / test_price

print(f"\nTest scenario:")
print(f"   Balance: ${test_balance:.2f}")
print(f"   BTC Price: ${test_price:.2f}")
print(f"   Capital: ${capital:.2f}")
print(f"   Leverage: {Config.LEVERAGE}x")
print(f"   Buying power: ${buying_power:.2f}")
print(f"   Quantity: {quantity:.8f} BTC")
print(f"   Notional value: ${quantity * test_price:.2f}")

print("\n" + "=" * 60)
print("✅ Test completed!")

