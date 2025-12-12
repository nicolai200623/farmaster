# 🔄 Multi-Exchange Trading Guide

## Tổng quan

Bot giờ đã hỗ trợ giao dịch trên **nhiều exchanges đồng thời**:
- **AsterDEX** - Exchange hiện tại đang dùng (12 symbols)
- **Binance Futures** - Exchange lớn nhất thế giới (nhiều coins, thanh khoản cao)

## ✨ Tính năng mới

### 1. Multi-Exchange Architecture
- **Modular Design**: Mỗi exchange có client riêng kế thừa từ `BaseExchangeClient`
- **Independent Trading**: Bot quản lý positions độc lập cho từng exchange
- **Unified Risk Management**: Tổng hợp PnL từ tất cả exchanges để quản lý rủi ro

### 2. Flexible Configuration
- Có thể chọn dùng 1 hoặc nhiều exchanges
- Mỗi exchange có danh sách symbols riêng
- Leverage riêng cho từng exchange
- Balance tracking tách biệt

### 3. Backward Compatible
- Code cũ vẫn chạy bình thường nếu chỉ dùng AsterDEX
- Không cần thay đổi gì nếu không muốn thêm Binance

## 📁 Cấu trúc Files Mới

```
FarmAster/
├── trading/
│   ├── base_exchange.py          # ⭐ NEW: Abstract base class
│   ├── asterdex_client.py         # ✏️ UPDATED: Kế thừa BaseExchangeClient
│   └── binance_client.py          # ⭐ NEW: Binance Futures client
├── config.py                      # ✏️ UPDATED: Multi-exchange config
├── bot.py                         # ✏️ UPDATED: Xử lý nhiều exchanges
├── .env.binance.example           # ⭐ NEW: Config template
└── MULTI_EXCHANGE_GUIDE.md        # ⭐ NEW: Guide này
```

## 🚀 Quick Start

### Bước 1: Tạo Binance API Keys

1. Đăng nhập [Binance](https://www.binance.com)
2. Vào **Account** → **API Management**
3. Tạo API key mới:
   - ✅ Enable Futures Trading
   - ✅ Enable Reading (để đọc balance, positions)
   - ❌ KHÔNG enable Withdrawals (bảo mật)
4. Whitelist IP nếu cần (khuyến nghị)
5. Copy API Key và Secret Key

### Bước 2: Cấu hình Bot

**Option 1: Dùng cả AsterDEX và Binance**

```bash
# Copy file example
cp .env.binance.example .env

# Chỉnh sửa .env
EXCHANGES=asterdex,binance

# AsterDEX config
API_KEY=your_asterdex_key
API_SECRET=your_asterdex_secret
SYMBOLS=BTCUSDT,ETHUSDT,SOLUSDT,...
LEVERAGE=10

# Binance config
BINANCE_API_KEY=your_binance_key
BINANCE_API_SECRET=your_binance_secret
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT,XRPUSDT,...
BINANCE_LEVERAGE=10
```

**Option 2: Chỉ dùng Binance**

```bash
EXCHANGES=binance

# Chỉ cần config Binance
BINANCE_API_KEY=your_binance_key
BINANCE_API_SECRET=your_binance_secret
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,...
BINANCE_LEVERAGE=10
```

**Option 3: Chỉ dùng AsterDEX (giữ nguyên như cũ)**

```bash
EXCHANGES=asterdex

# Config như cũ
API_KEY=your_asterdex_key
API_SECRET=your_asterdex_secret
SYMBOLS=BTCUSDT,ETHUSDT,...
LEVERAGE=10
```

### Bước 3: Chạy Bot

```bash
# Train models (nếu chưa train)
python ml/train_ensemble.py

# Chạy bot
python bot.py
```

## ⚙️ Configuration Chi Tiết

### Exchange Selection

```bash
# Syntax
EXCHANGES=exchange1,exchange2,...

# Examples
EXCHANGES=asterdex              # Chỉ AsterDEX
EXCHANGES=binance               # Chỉ Binance
EXCHANGES=asterdex,binance      # Cả hai
```

### Binance Symbols

Binance có **rất nhiều** trading pairs. Đây là một số coins phổ biến với thanh khoản cao:

**Top 20 Recommended:**
```bash
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT,XRPUSDT,ADAUSDT,DOGEUSDT,AVAXUSDT,DOTUSDT,LINKUSDT,UNIUSDT,NEARUSDT,MATICUSDT,LTCUSDT,ATOMUSDT,FILUSDT,ARBUSDT,OPUSDT,SHIBUSDT,APTUSDT
```

**Top 10 (Conservative):**
```bash
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT,XRPUSDT,ADAUSDT,AVAXUSDT,DOTUSDT,LINKUSDT,MATICUSDT
```

**Top 5 (Safest):**
```bash
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT,XRPUSDT
```

### Leverage Settings

Mỗi exchange có leverage riêng:

```bash
# AsterDEX leverage
LEVERAGE=10

# Binance leverage
BINANCE_LEVERAGE=10
```

⚠️ **Lưu ý**: Binance hỗ trợ leverage tối đa **125x** (tùy symbol), nhưng khuyến nghị dùng **5-20x** cho an toàn.

### Position Sizing

**Recommended cho Multi-Exchange: Dùng Fixed USDT**

```bash
POSITION_SIZE_USDT=10
```

Với config này:
- Mỗi trade = $10 USDT (trên bất kỳ exchange nào)
- Dễ quản lý risk khi có nhiều exchanges
- Tổng capital = số lệnh × $10

**Alternative: Percentage-based**

```bash
SIZE_PCT=0.2  # 20% của balance
```

⚠️ Với percentage mode, balance được tính **tổng từ tất cả exchanges**, nên mỗi exchange sẽ dùng 20% của **tổng balance**.

## 📊 Bot Behavior với Multi-Exchange

### Trading Loop

```
Loop #1:
├── Get balance từ tất cả exchanges
│   ├── AsterDEX: $100
│   └── Binance: $200
│   └── Total: $300
│
├── Check daily loss limit (trên tổng $300)
│
├── Process AsterDEX
│   ├── Check BTCUSDT
│   ├── Check ETHUSDT
│   └── ...
│
└── Process Binance
    ├── Check BTCUSDT
    ├── Check ETHUSDT
    └── ...
```

### Position Management

Bot quản lý positions **độc lập** cho từng exchange:

```
AsterDEX Positions:
├── BTCUSDT LONG (Entry: $45,000, PnL: +2.5%)
└── ETHUSDT SHORT (Entry: $2,400, PnL: -1.2%)

Binance Positions:
├── SOLUSDT LONG (Entry: $110, PnL: +5.3%)
└── BNBUSDT LONG (Entry: $320, PnL: +1.8%)
```

### Telegram Notifications

Logs sẽ có prefix để phân biệt exchange:

```
[ASTERDEX] OPEN LONG BTCUSDT | Qty: 0.002 | Price: $45,000
[BINANCE] OPEN LONG SOLUSDT | Qty: 0.9 | Price: $110
[BINANCE] CLOSE LONG SOLUSDT | TP Hit | PnL: 5.3%
```

## 🎯 Use Cases

### Use Case 1: Maximize Opportunities

**Scenario**: Bạn muốn trade nhiều coins nhất có thể

**Config**:
```bash
EXCHANGES=asterdex,binance

# AsterDEX: 12 symbols
SYMBOLS=ADAUSDT,BNBUSDT,DOGEUSDT,UNIUSDT,LINKUSDT,BTCUSDT,ETHUSDT,SOLUSDT,XRPUSDT,DOTUSDT,AVAXUSDT,NEARUSDT

# Binance: 20 symbols (nhiều coins độc quyền)
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT,XRPUSDT,ADAUSDT,DOGEUSDT,AVAXUSDT,DOTUSDT,LINKUSDT,UNIUSDT,NEARUSDT,MATICUSDT,LTCUSDT,ATOMUSDT,FILUSDT,ARBUSDT,OPUSDT,SHIBUSDT,APTUSDT

POSITION_SIZE_USDT=5  # Nhỏ để spread risk
```

**Result**: Trade lên đến **32 symbols** với cơ hội tìm signals cao hơn

### Use Case 2: Focus on Liquidity

**Scenario**: Chỉ quan tâm thanh khoản tốt nhất

**Config**:
```bash
EXCHANGES=binance

BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT
BINANCE_LEVERAGE=15
POSITION_SIZE_USDT=20
```

**Result**: Focus vào top coins, spread thấp, execution nhanh

### Use Case 3: Arbitrage Monitoring

**Scenario**: Theo dõi giá trên cả 2 exchanges, trade nơi nào có signal tốt hơn

**Config**:
```bash
EXCHANGES=asterdex,binance

# Cùng symbols trên 2 exchanges
SYMBOLS=BTCUSDT,ETHUSDT,SOLUSDT
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,SOLUSDT

POSITION_SIZE_USDT=15
```

**Result**: Nếu BTCUSDT có signal tốt trên Binance nhưng không tốt trên AsterDEX, bot chỉ trade trên Binance

## 🛡️ Risk Management

### Daily Loss Limit

Daily loss limit áp dụng cho **tổng PnL** của tất cả exchanges:

```bash
DAILY_LOSS_LIMIT=0.15  # 15%
```

Ví dụ:
- AsterDEX balance: $100 → PnL: -$10
- Binance balance: $200 → PnL: -$20
- **Total PnL**: -$30 / $300 = **-10%** ✅ (tiếp tục trade)

Nếu total PnL < -15%, bot sẽ **dừng trade trên tất cả exchanges**.

### Position Limits

Config hiện tại không giới hạn số positions per exchange. Bạn có thể thêm limit bằng cách điều chỉnh `MAX_POSITIONS` trong config.

### Margin Mode

Bot tự động set **ISOLATED margin** cho tất cả positions trên cả 2 exchanges:
- Risk của mỗi position bị cô lập
- Liquidation 1 position không ảnh hưởng đến positions khác

## 🔧 Advanced Configuration

### Per-Exchange Settings

Nếu muốn settings khác nhau cho từng exchange, có thể:

**Example: Aggressive Binance, Conservative AsterDEX**

```bash
EXCHANGES=asterdex,binance

# AsterDEX: Conservative
LEVERAGE=5
SYMBOLS=BTCUSDT,ETHUSDT  # Ít symbols

# Binance: Aggressive
BINANCE_LEVERAGE=15
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,BNBUSDT,SOLUSDT,XRPUSDT,...  # Nhiều symbols

POSITION_SIZE_USDT=10  # Shared
```

### Testnet vs Mainnet

Có thể dùng testnet cho 1 exchange và mainnet cho exchange khác:

```bash
# AsterDEX mainnet
TESTNET_MODE=false

# Binance testnet (để test)
BINANCE_TESTNET_MODE=true
```

⚠️ **Không khuyến nghị** mix testnet/mainnet vì sẽ gây nhầm lẫn.

## 📈 Performance Considerations

### API Rate Limits

- **AsterDEX**: ~1 request/second
- **Binance**: ~1200 requests/minute (weight-based)

Bot có delay 0.5s giữa các symbols để tránh rate limit.

Với 12 symbols AsterDEX + 20 symbols Binance = 32 symbols:
- Time per loop: ~16 seconds (symbols) + 180s (sleep) = **196 seconds/loop**

### Memory Usage

Multi-exchange tăng memory usage không đáng kể:
- Mỗi client ~5 MB
- Position tracking shared
- ML models shared (không duplicate)

Expected: **+10 MB** khi thêm Binance

### Log Files

Logs sẽ lớn hơn vì có nhiều symbols:
- **1 exchange (12 symbols)**: ~5 MB/day
- **2 exchanges (32 symbols)**: ~12 MB/day

Log files tự động rotate theo ngày (`bot_YYYYMMDD.log`).

## 🐛 Troubleshooting

### Issue 1: "BINANCE_API_KEY not found"

**Cause**: Chưa set Binance credentials trong `.env`

**Fix**:
```bash
BINANCE_API_KEY=your_key_here
BINANCE_API_SECRET=your_secret_here
```

### Issue 2: "Exchange không hợp lệ: xxx"

**Cause**: Typo trong EXCHANGES

**Fix**: Chỉ dùng `asterdex` hoặc `binance` (lowercase)
```bash
EXCHANGES=asterdex,binance  # ✅
EXCHANGES=AsterDEX,Binance  # ❌
```

### Issue 3: Binance API Error -1121 "Invalid symbol"

**Cause**: Symbol không tồn tại trên Binance hoặc không hỗ trợ futures

**Fix**: Kiểm tra danh sách symbols hỗ trợ tại [Binance Futures](https://www.binance.com/en/futures/BTCUSDT)

Common valid symbols:
```
BTCUSDT ✅
ETHUSDT ✅
BTC-USDT ❌ (sai format)
BTCUSD ❌ (không phải USDT futures)
```

### Issue 4: "Insufficient balance" trên Binance

**Cause**:
- Balance không đủ cho position size
- Chưa transfer USDT vào Futures wallet

**Fix**:
1. Transfer USDT từ Spot → Futures wallet
2. Hoặc giảm `POSITION_SIZE_USDT`

### Issue 5: Positions không được track đúng

**Cause**: Symbol bị duplicate giữa 2 exchanges

**Fix**: Position tracker dùng symbol làm key, nên **tránh trade cùng symbol trên 2 exchanges đồng thời** (sẽ ghi đè lẫn nhau).

Nếu muốn trade BTCUSDT trên cả 2 exchanges, cần update position tracker để dùng `(exchange, symbol)` làm key.

## 🔮 Future Enhancements

### Planned Features

1. **More Exchanges**: OKX, Bybit, Gate.io
2. **Exchange-Specific Strategies**: Khác nhau cho từng exchange
3. **Cross-Exchange Arbitrage**: Phát hiện chênh lệch giá
4. **Position Correlation**: Tránh overexposure trên cùng coin
5. **Exchange Priority**: Ưu tiên trade trên exchange nào trước

### How to Request Features

Tạo issue trên GitHub hoặc liên hệ qua Telegram.

## 📚 API Reference

### BaseExchangeClient

Abstract class định nghĩa interface chung:

```python
class BaseExchangeClient(ABC):
    @abstractmethod
    def get_account_balance(self) -> float

    @abstractmethod
    def get_position(self, symbol: str) -> Optional[Dict]

    @abstractmethod
    def get_klines(self, symbol: str, interval: str, limit: int) -> List

    @abstractmethod
    def create_market_order(self, symbol: str, side: str, quantity: float) -> Dict

    # ... và nhiều methods khác
```

### AsterDEXClient

```python
from trading.asterdex_client import AsterDEXClient

client = AsterDEXClient()
balance = client.get_account_balance()
position = client.get_position('BTCUSDT')
```

### BinanceClient

```python
from trading.binance_client import BinanceClient

client = BinanceClient()
balance = client.get_account_balance()
position = client.get_position('BTCUSDT')
```

Cả 2 clients có **cùng interface** nên code có thể thay thế lẫn nhau.

## ✅ Checklist Before Going Live

Multi-exchange trading tăng complexity. Trước khi chạy mainnet, check:

- [ ] API keys được tạo đúng cho cả 2 exchanges
- [ ] Futures trading đã được enable
- [ ] Balance đủ trên cả 2 exchanges
- [ ] Test kết nối thành công
- [ ] Config leverage hợp lý (không quá cao)
- [ ] Position size phù hợp với capital
- [ ] Daily loss limit đã set
- [ ] Telegram notifications hoạt động
- [ ] ML models đã được train
- [ ] Backtest kết quả khả quan
- [ ] Hiểu rõ risk khi dùng nhiều exchanges

## 📞 Support

- **GitHub Issues**: Báo bugs và feature requests
- **Telegram**: Real-time support
- **Documentation**: Đọc các guides khác trong repo

---

**Happy Trading! 🚀**

_Bot được thiết kế để tối đa hóa cơ hội trading bằng cách kết hợp nhiều exchanges, nhưng luôn nhớ: Higher opportunities = Higher risks. Trade responsibly!_
