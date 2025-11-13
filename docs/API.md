# 🔌 API Documentation

## AsterDEX Client API

### Initialization

```python
from trading.asterdex_client import AsterDEXClient

# Initialize with default config
client = AsterDEXClient()

# Or with custom params
client = AsterDEXClient(
    api_key='your_key',
    api_secret='your_secret',
    testnet=True
)
```

### Account Methods

#### `get_account_balance()`
Lấy USDT balance.

**Returns:** `float` - USDT balance

**Example:**
```python
balance = client.get_account_balance()
print(f"Balance: ${balance:.2f}")
```

---

#### `get_position(symbol)`
Lấy thông tin position hiện tại.

**Parameters:**
- `symbol` (str): Trading pair (e.g., 'BTCUSDT')

**Returns:** `dict` or `None`
```python
{
    'side': 'LONG' | 'SHORT',
    'amount': float,
    'entry_price': float,
    'mark_price': float,
    'pnl_pct': float,
    'pnl_usdt': float
}
```

**Example:**
```python
pos = client.get_position('BTCUSDT')
if pos:
    print(f"Position: {pos['side']} {pos['amount']}")
    print(f"PnL: {pos['pnl_pct']*100:.2f}%")
```

---

### Market Data Methods

#### `get_klines(symbol, interval='1m', limit=100)`
Lấy candlestick data.

**Parameters:**
- `symbol` (str): Trading pair
- `interval` (str): Timeframe ('1m', '5m', '15m', '1h', etc.)
- `limit` (int): Number of candles

**Returns:** `list` - Klines data

**Example:**
```python
klines = client.get_klines('BTCUSDT', interval='5m', limit=50)
for k in klines:
    print(f"Time: {k[0]}, Close: {k[4]}")
```

---

#### `get_orderbook(symbol, limit=10)`
Lấy order book.

**Parameters:**
- `symbol` (str): Trading pair
- `limit` (int): Depth level

**Returns:** `dict`
```python
{
    'bids': [[price, quantity], ...],
    'asks': [[price, quantity], ...]
}
```

**Example:**
```python
ob = client.get_orderbook('BTCUSDT', limit=5)
print(f"Best bid: {ob['bids'][0]}")
print(f"Best ask: {ob['asks'][0]}")
```

---

#### `get_ticker_price(symbol)`
Lấy giá hiện tại.

**Parameters:**
- `symbol` (str): Trading pair

**Returns:** `float` - Current price

**Example:**
```python
price = client.get_ticker_price('BTCUSDT')
print(f"BTC Price: ${price:.2f}")
```

---

### Trading Methods

#### `set_leverage(symbol, leverage)`
Set đòn bẩy.

**Parameters:**
- `symbol` (str): Trading pair
- `leverage` (int): Leverage (1-125)

**Returns:** `bool` - Success status

**Example:**
```python
client.set_leverage('BTCUSDT', 10)
```

---

#### `set_margin_type(symbol, margin_type='ISOLATED')`
Set margin type.

**Parameters:**
- `symbol` (str): Trading pair
- `margin_type` (str): 'ISOLATED' or 'CROSSED'

**Returns:** `bool` - Success status

**Example:**
```python
client.set_margin_type('BTCUSDT', 'ISOLATED')
```

---

#### `create_market_order(symbol, side, quantity, reduce_only=False)`
Tạo market order.

**Parameters:**
- `symbol` (str): Trading pair
- `side` (str): 'BUY' or 'SELL'
- `quantity` (float): Order quantity
- `reduce_only` (bool): True for closing position

**Returns:** `dict` or `None` - Order info

**Example:**
```python
# Open LONG
order = client.create_market_order(
    symbol='BTCUSDT',
    side='BUY',
    quantity=0.01
)

# Close position
order = client.create_market_order(
    symbol='BTCUSDT',
    side='SELL',
    quantity=0.01,
    reduce_only=True
)
```

---

#### `close_position(symbol)`
Đóng toàn bộ position.

**Parameters:**
- `symbol` (str): Trading pair

**Returns:** `bool` - Success status

**Example:**
```python
if client.close_position('BTCUSDT'):
    print("Position closed!")
```

---

## Signal Generator API

### Initialization

```python
from trading.signal_generator import SignalGenerator
from ml.lstm_model import LSTMTrainer

lstm_trainer = LSTMTrainer(input_size=14)
lstm_trainer.load()

signal_gen = SignalGenerator(lstm_trainer)
```

### Methods

#### `generate_signal(client, symbol)`
Tạo trading signal.

**Parameters:**
- `client` (AsterDEXClient): Client instance
- `symbol` (str): Trading pair

**Returns:** `str` - 'LONG', 'SHORT', or 'HOLD'

**Example:**
```python
signal = signal_gen.generate_signal(client, 'BTCUSDT')
print(f"Signal: {signal}")
```

---

#### `should_close_position(position, tp_pct=None, sl_pct=None)`
Kiểm tra có nên đóng position.

**Parameters:**
- `position` (dict): Position info from `get_position()`
- `tp_pct` (float): Take profit %
- `sl_pct` (float): Stop loss %

**Returns:** `tuple` - (should_close: bool, reason: str)

**Example:**
```python
pos = client.get_position('BTCUSDT')
should_close, reason = signal_gen.should_close_position(pos)

if should_close:
    print(f"Close position: {reason}")
```

---

## Risk Manager API

### Initialization

```python
from trading.risk_manager import RiskManager

risk_mgr = RiskManager()
```

### Methods

#### `set_daily_start(balance)`
Set balance đầu ngày.

**Parameters:**
- `balance` (float): Starting balance

**Example:**
```python
risk_mgr.set_daily_start(1000.0)
```

---

#### `check_daily_loss_limit(current_balance)`
Kiểm tra daily loss limit.

**Parameters:**
- `current_balance` (float): Current balance

**Returns:** `tuple` - (exceeded: bool, pnl_pct: float)

**Example:**
```python
exceeded, pnl = risk_mgr.check_daily_loss_limit(900.0)
if exceeded:
    print(f"Loss limit exceeded: {pnl*100:.2f}%")
```

---

#### `calculate_position_size(balance, price, leverage=None)`
Tính position size.

**Parameters:**
- `balance` (float): Account balance
- `price` (float): Current price
- `leverage` (int): Leverage

**Returns:** `float` - Quantity to trade

**Example:**
```python
qty = risk_mgr.calculate_position_size(
    balance=1000,
    price=50000,
    leverage=5
)
print(f"Quantity: {qty}")
```

---

#### `record_trade(symbol, side, quantity, price, pnl_pct=None)`
Ghi nhận trade.

**Parameters:**
- `symbol` (str): Trading pair
- `side` (str): 'LONG' or 'SHORT'
- `quantity` (float): Trade quantity
- `price` (float): Trade price
- `pnl_pct` (float): PnL percentage (optional)

**Example:**
```python
risk_mgr.record_trade(
    symbol='BTCUSDT',
    side='LONG',
    quantity=0.01,
    price=50000,
    pnl_pct=0.02
)
```

---

#### `get_daily_stats()`
Lấy statistics trong ngày.

**Returns:** `dict`
```python
{
    'trades': int,
    'volume': float,
    'pnl': float,
    'total_trades': int,
    'win_rate': float,
    'winning_trades': int,
    'losing_trades': int
}
```

**Example:**
```python
stats = risk_mgr.get_daily_stats()
print(f"Win Rate: {stats['win_rate']:.2f}%")
```

---

## LSTM Model API

### Initialization

```python
from ml.lstm_model import LSTMTrainer

trainer = LSTMTrainer(input_size=14)
```

### Methods

#### `train(X_train, y_train, epochs=None, batch_size=32, lr=0.001)`
Train model.

**Parameters:**
- `X_train` (np.array): Training data (n_samples, seq_len, features)
- `y_train` (np.array): Labels (n_samples,)
- `epochs` (int): Number of epochs
- `batch_size` (int): Batch size
- `lr` (float): Learning rate

**Example:**
```python
trainer.train(X_train, y_train, epochs=50)
```

---

#### `predict(X)`
Dự đoán.

**Parameters:**
- `X` (np.array): Input data (seq_len, features) or (batch, seq_len, features)

**Returns:** `np.array` - Probabilities

**Example:**
```python
prob = trainer.predict(X_test)
print(f"Probability UP: {prob[0]:.3f}")
```

---

#### `save(model_path=None, scaler_path=None)`
Lưu model.

**Example:**
```python
trainer.save()
```

---

#### `load(model_path=None, scaler_path=None)`
Load model.

**Returns:** `bool` - Success status

**Example:**
```python
if trainer.load():
    print("Model loaded!")
```

---

## Feature Engine API

### Methods

#### `calculate_indicators(df)`
Tính toán indicators.

**Parameters:**
- `df` (DataFrame): OHLCV data

**Returns:** `DataFrame` - Data with indicators

**Example:**
```python
from ml.features import FeatureEngine

df = FeatureEngine.calculate_indicators(df)
print(df[['rsi', 'macd', 'bb_upper']].tail())
```

---

#### `prepare_features(df, feature_cols=None)`
Chuẩn bị features.

**Parameters:**
- `df` (DataFrame): Data with indicators
- `feature_cols` (list): Feature columns

**Returns:** `DataFrame` - Feature matrix

**Example:**
```python
features = FeatureEngine.prepare_features(df)
```

---

#### `create_sequences(data, seq_length=60)`
Tạo sequences cho LSTM.

**Parameters:**
- `data` (np.array): Feature matrix
- `seq_length` (int): Sequence length

**Returns:** `tuple` - (X, y)

**Example:**
```python
X, y = FeatureEngine.create_sequences(data, seq_length=60)
```

---

## Backtester API

### Initialization

```python
from backtest.backtester import Backtester

backtester = Backtester(
    lstm_trainer=trainer,
    initial_capital=1000
)
```

### Methods

#### `run_backtest(symbols=None, days=30)`
Chạy backtest.

**Parameters:**
- `symbols` (list): Trading pairs
- `days` (int): Number of days

**Returns:** `dict` - Backtest results

**Example:**
```python
results = backtester.run_backtest(
    symbols=['BTCUSDT', 'ETHUSDT'],
    days=30
)

print(f"Win Rate: {results['win_rate']:.2f}%")
print(f"Total PnL: {results['total_pnl_pct']:.2f}%")
```

---

## Configuration API

### Access Config

```python
from config import Config

# Get values
print(Config.SYMBOLS)
print(Config.LEVERAGE)
print(Config.TP_PCT)

# Validate
Config.validate()
```

### Available Settings

```python
# API
Config.API_KEY
Config.API_SECRET
Config.FUTURES_BASE_URL

# Trading
Config.SYMBOLS
Config.LEVERAGE
Config.SIZE_PCT
Config.TP_PCT
Config.SL_PCT
Config.LOOP_SLEEP
Config.DAILY_LOSS_LIMIT

# ML
Config.LSTM_HIDDEN_SIZE
Config.LSTM_NUM_LAYERS
Config.LSTM_EPOCHS
Config.SEQUENCE_LENGTH
Config.LSTM_THRESHOLD

# Signals
Config.RSI_OVERSOLD
Config.RSI_OVERBOUGHT
Config.OB_IMBALANCE_LONG
Config.OB_IMBALANCE_SHORT
Config.MIN_SIGNAL_SCORE
```

---

## Logger API

### Usage

```python
from utils.logger import logger

# Log levels
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")

# With Telegram
logger.info("Message", send_tg=True)
logger.trade("Trade executed!")
```

---

**For more examples, see the source code! 🚀**

