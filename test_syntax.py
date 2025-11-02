#!/usr/bin/env python3
"""Test bot.py syntax"""

try:
    import bot
    print("✅ bot.py syntax is OK!")
except SyntaxError as e:
    print(f"❌ Syntax error: {e}")
except Exception as e:
    print(f"⚠️ Import error (but syntax OK): {e}")

