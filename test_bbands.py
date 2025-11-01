#!/usr/bin/env python3
"""Test Bollinger Bands column names"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pandas as pd
import pandas_ta as ta

# Create sample data
data = {
    'close': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
              110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
              120, 121, 122, 123, 124, 125]
}
df = pd.DataFrame(data)

print("Testing Bollinger Bands...")
print(f"pandas-ta version: {ta.__version__ if hasattr(ta, '__version__') else 'unknown'}")

# Calculate BB
bbands = ta.bbands(df['close'], length=20, std=2)

if bbands is not None:
    print(f"\nBollinger Bands columns: {bbands.columns.tolist()}")
    print(f"\nFirst few rows:")
    print(bbands.head())
    print(f"\nLast few rows:")
    print(bbands.tail())
else:
    print("ERROR: Bollinger Bands returned None!")

