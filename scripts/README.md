# 🛠️ Utility Scripts

Helper scripts cho monitoring và management.

## Scripts

### `check_balance.py`
Kiểm tra balance và positions.

**Usage:**
```bash
python scripts/check_balance.py
```

**Output:**
```
💰 ACCOUNT STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💵 USDT Balance: $1000.00

📊 POSITIONS:
BTCUSDT:
  Side: LONG
  Amount: 0.01
  Entry: $50000.00
  Mark: $51000.00
  PnL: 2.00% ($20.00)
```

### `close_all.py`
Emergency close tất cả positions.

**Usage:**
```bash
python scripts/close_all.py
```

**Warning:** Sẽ đóng TẤT CẢ positions ngay lập tức!

### `test_signal.py`
Test signal generation.

**Usage:**
```bash
python scripts/test_signal.py
```

**Output:**
```
🧪 TESTING SIGNAL GENERATOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📡 BTCUSDT Signal: LONG
   LSTM: 0.723 | RSI: 28.5 | OB: 1.82
   Score LONG: 3 | SHORT: 0
```

### `analyze_performance.py`
Phân tích performance từ logs.

**Usage:**
```bash
python scripts/analyze_performance.py
```

**Output:**
```
📊 PERFORMANCE REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📈 OVERALL STATS
Total Trades: 45
Win Rate: 62.22%

💰 PNL STATS
Total PnL: +18.4%
Profit Factor: 1.85

📊 BY SYMBOL
BTCUSDT: 25 trades | 64% WR | +12.3%
ETHUSDT: 20 trades | 60% WR | +6.1%
```

## Creating New Scripts

### Template

```python
#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config
from utils.logger import logger

def main():
    """Main function"""
    Config.validate()
    
    # Your code here
    logger.info("Script running...")

if __name__ == '__main__':
    main()
```

### Example: Volume Tracker

```python
#!/usr/bin/env python3
# scripts/track_volume.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from trading.asterdex_client import AsterDEXClient
from utils.logger import logger

def main():
    client = AsterDEXClient()
    
    total_volume = 0
    
    for symbol in ['BTCUSDT', 'ETHUSDT']:
        # Get recent trades
        # Calculate volume
        # ...
        
    logger.info(f"Total Volume: ${total_volume/1e6:.2f}M")

if __name__ == '__main__':
    main()
```

## Automation

### Cron Jobs

```bash
# Daily balance check
0 0 * * * cd /path/to/bot && python scripts/check_balance.py >> logs/daily.log

# Hourly performance analysis
0 * * * * cd /path/to/bot && python scripts/analyze_performance.py >> logs/perf.log
```

### Systemd Timer

```ini
# /etc/systemd/system/daily-report.timer
[Unit]
Description=Daily Bot Report

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```

## Tips

- Always test scripts on testnet first
- Check logs for errors
- Use try/except for error handling
- Add logging for debugging

