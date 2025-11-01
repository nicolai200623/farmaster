import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from config import Config
from trading.asterdex_client import AsterDEXClient

client = AsterDEXClient()

print("\nTesting symbols from .env:")
print(f"Symbols: {Config.SYMBOLS}\n")

for symbol in Config.SYMBOLS:
    try:
        ticker = client.client.futures_symbol_ticker(symbol=symbol)
        print(f"✅ {symbol:12} - ${float(ticker['price']):,.2f}")
    except Exception as e:
        print(f"❌ {symbol:12} - {str(e)[:60]}")

print("\nDone!")

