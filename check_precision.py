import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from config import Config
from trading.asterdex_client import AsterDEXClient

client = AsterDEXClient()

print("\nChecking precision for symbols...")
print()

# Get exchange info
exchange_info = client.client.futures_exchange_info()

for symbol_name in Config.SYMBOLS:
    symbol_info = next((s for s in exchange_info['symbols'] if s['symbol'] == symbol_name), None)
    
    if symbol_info:
        # Get filters
        qty_precision = symbol_info.get('quantityPrecision', 3)
        price_precision = symbol_info.get('pricePrecision', 2)
        
        # LOT_SIZE filter
        lot_size = next((f for f in symbol_info['filters'] if f['filterType'] == 'LOT_SIZE'), None)
        
        if lot_size:
            min_qty = float(lot_size['minQty'])
            max_qty = float(lot_size['maxQty'])
            step_size = float(lot_size['stepSize'])
            
            print(f"{symbol_name}:")
            print(f"  Qty Precision: {qty_precision}")
            print(f"  Price Precision: {price_precision}")
            print(f"  Min Qty: {min_qty}")
            print(f"  Max Qty: {max_qty}")
            print(f"  Step Size: {step_size}")
            print()

print("\nExample for ADAUSDT with $3.52 @ $0.61:")
price = 0.61
notional = 3.52
qty = notional / price
print(f"  Raw quantity: {qty}")
print(f"  Rounded to 0 decimals: {round(qty, 0)}")
print(f"  Rounded to 1 decimals: {round(qty, 1)}")
print(f"  Rounded to 2 decimals: {round(qty, 2)}")

