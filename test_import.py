#!/usr/bin/env python3
"""Test imports"""

import sys
import os

print("Python version:", sys.version)
print("Current dir:", os.getcwd())
print("Script dir:", os.path.dirname(os.path.abspath(__file__)))
print("\nPython path:")
for p in sys.path:
    print(f"  - {p}")

# Add project root
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

print("\nAfter adding project root:")
for p in sys.path:
    print(f"  - {p}")

# Try import
try:
    from config import Config
    print("\n✅ Successfully imported Config!")
    print(f"Config loaded: {Config}")
except Exception as e:
    print(f"\n❌ Failed to import Config: {e}")

try:
    from utils.logger import logger
    print("✅ Successfully imported logger!")
except Exception as e:
    print(f"❌ Failed to import logger: {e}")

