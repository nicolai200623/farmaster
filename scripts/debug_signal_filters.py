#!/usr/bin/env python3
"""
Debug script to verify signal filters are working correctly
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config
from trading.signal_cooldown import SignalCooldownTracker

def main():
    print("=" * 60)
    print("🔍 SIGNAL FILTER DEBUG")
    print("=" * 60)
    
    # 1. Check Config values
    print("\n📋 CONFIG VALUES:")
    print(f"   USE_SMART_ENTRY_V2: {Config.USE_SMART_ENTRY_V2}")
    print(f"   USE_ADVANCED_ENTRY: {Config.USE_ADVANCED_ENTRY}")
    print(f"   MIN_ENTRY_SCORE: {Config.MIN_ENTRY_SCORE}")
    print(f"   MIN_RR_RATIO: {Config.MIN_RR_RATIO}")
    print(f"   USE_ML_CONVICTION_FILTER: {Config.USE_ML_CONVICTION_FILTER}")
    print(f"   MIN_ML_CONVICTION: {Config.MIN_ML_CONVICTION}")
    print(f"   USE_SIGNAL_COOLDOWN: {Config.USE_SIGNAL_COOLDOWN}")
    print(f"   SIGNAL_COOLDOWN_MINUTES: {Config.SIGNAL_COOLDOWN_MINUTES}")
    print(f"   REQUIRE_HTF_TREND_ALIGNMENT: {Config.REQUIRE_HTF_TREND_ALIGNMENT}")
    print(f"   USE_MULTI_TIMEFRAME: {Config.USE_MULTI_TIMEFRAME}")
    
    # 2. Check cooldown tracker data
    print("\n🚫 COOLDOWN TRACKER STATUS:")
    tracker = SignalCooldownTracker(cooldown_minutes=Config.SIGNAL_COOLDOWN_MINUTES)
    
    if not tracker.last_signals:
        print("   ❌ NO COOLDOWNS RECORDED!")
        print("   This means signals have never been recorded")
        print("   Check if cooldown.record_signal() is being called")
    else:
        print(f"   ✅ Found {len(tracker.last_signals)} cooldown records:")
        for symbol, info in tracker.last_signals.items():
            cooldown_info = tracker.get_cooldown_info(symbol)
            can_signal = "✅ CAN signal" if cooldown_info['can_signal'] else "🚫 BLOCKED"
            print(f"      {symbol}: {info['signal']} at {info['time'].strftime('%H:%M:%S')}")
            print(f"         Minutes since: {cooldown_info['minutes_since']:.1f} | {can_signal}")
    
    # 3. Check if cooldown file exists
    print("\n📁 COOLDOWN FILE:")
    cooldown_file = 'data/signal_cooldown.json'
    if os.path.exists(cooldown_file):
        print(f"   ✅ File exists: {cooldown_file}")
        with open(cooldown_file, 'r') as f:
            print(f"   Content: {f.read()}")
    else:
        print(f"   ❌ File NOT found: {cooldown_file}")
        print("   Cooldown is not persisted to disk!")
    
    # 4. Test cooldown logic
    print("\n🧪 COOLDOWN LOGIC TEST:")
    test_symbol = "TESTUSDT"
    
    # Test 1: New symbol should be able to signal
    can_signal, reason = tracker.can_signal(test_symbol, "LONG")
    print(f"   New symbol can signal: {can_signal} | Reason: {reason}")
    
    # Test 2: Record and immediately try to signal
    tracker.record_signal(test_symbol, "LONG")
    can_signal, reason = tracker.can_signal(test_symbol, "LONG")
    print(f"   After record, can signal: {can_signal}")
    print(f"   Reason: {reason}")
    
    # 5. Summary
    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    
    issues = []
    
    if not os.path.exists(cooldown_file):
        issues.append("❌ Cooldown file missing - signals not persisted")
    
    if not tracker.last_signals:
        issues.append("❌ No cooldown records - record_signal() not being called")
    
    if not issues:
        print("✅ All filters appear to be configured correctly")
    else:
        print("⚠️ ISSUES FOUND:")
        for issue in issues:
            print(f"   {issue}")
    
    print("\n💡 RECOMMENDATIONS:")
    print("   1. Ensure record_signal() is called BEFORE placing orders")
    print("   2. Check if order failures prevent cooldown from being recorded")
    print("   3. Verify VPS has write permissions to data/ folder")

if __name__ == "__main__":
    main()

