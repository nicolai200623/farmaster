# 💰 Trading Module

Module chứa trading logic và risk management.

## Files

### `asterdex_client.py`
AsterDEX API client wrapper.

**Features:**
- Binance-compatible API
- URL override for AsterDEX
- Account management
- Market data
- Order execution

**Usage:**
```python
from trading.asterdex_client import AsterDEXClient

client = AsterDEXClient()

# Get balance
balance = client.get_account_balance()

# Get position
pos = client.get_position('BTCUSDT')

# Create order
order = client.create_market_order(
    symbol='BTCUSDT',
    side='BUY',
    quantity=0.01
)

# Close position
client.close_position('BTCUSDT')
```

### `signal_generator.py`
Trading signal generation.

**Signals:**
1. LSTM prediction
2. RSI oversold/overbought
3. Order Book imbalance

**Usage:**
```python
from trading.signal_generator import SignalGenerator

signal_gen = SignalGenerator(lstm_trainer)

# Generate signal
signal = signal_gen.generate_signal(client, 'BTCUSDT')
# Returns: 'LONG', 'SHORT', or 'HOLD'

# Check if should close
should_close, reason = signal_gen.should_close_position(position)
```

### `risk_manager.py`
Risk management and position sizing.

**Features:**
- Position sizing
- Daily loss limit
- Trade tracking
- Statistics

**Usage:**
```python
from trading.risk_manager import RiskManager

risk_mgr = RiskManager()

# Set daily start
risk_mgr.set_daily_start(balance)

# Check if can trade
can_trade, reason = risk_mgr.should_trade(current_balance)

# Calculate position size
qty = risk_mgr.calculate_position_size(balance, price, leverage)

# Record trade
risk_mgr.record_trade(symbol, side, quantity, price, pnl_pct)

# Get stats
stats = risk_mgr.get_daily_stats()
```

## Configuration

### Trading Parameters
```env
SYMBOLS=BTCUSDT,ETHUSDT
LEVERAGE=5
SIZE_PCT=0.1
TP_PCT=0.02
SL_PCT=0.01
DAILY_LOSS_LIMIT=0.2
```

### Signal Thresholds
```env
LSTM_THRESHOLD=0.6
RSI_OVERSOLD=30
RSI_OVERBOUGHT=70
OB_IMBALANCE_LONG=1.5
MIN_SIGNAL_SCORE=2
```

## Safety Features

1. **Isolated Margin:** Each position isolated
2. **Daily Loss Limit:** Auto-stop at 20% loss
3. **TP/SL:** Automatic exit
4. **Position Sizing:** Max 10% per trade
5. **Error Handling:** Retry and recovery

## Customization

### Add New Signal Source

Edit `signal_generator.py`:
```python
def generate_signal(self, client, symbol):
    # ... existing code ...
    
    # Add Volume signal
    volume_ratio = current_volume / avg_volume
    if volume_ratio > 2:
        score_long += 1
    
    # ... rest of code ...
```

### Adjust Risk Parameters

Edit `.env`:
```env
SIZE_PCT=0.05      # More conservative
LEVERAGE=3         # Lower leverage
TP_PCT=0.03        # Higher TP
SL_PCT=0.005       # Tighter SL
```

