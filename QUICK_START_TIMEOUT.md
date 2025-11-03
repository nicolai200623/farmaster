# ⏱️ Position Timeout - Quick Start Guide

## What's New?

Your trading bot now automatically closes any position that has been open for **24+ hours** without reaching the 1% take profit target.

## Why This Matters

- ✅ **Risk Management**: Prevents positions from staying open indefinitely
- ✅ **Capital Efficiency**: Frees up capital from stagnant positions
- ✅ **Strategy Alignment**: Keeps focus on high-frequency, quick profits
- ✅ **Automated**: No manual intervention needed

## How It Works

```
Position Opens → Timer Starts → 24 Hours Pass → Auto-Close at Market Price
                              ↓
                         TP Hit? → Close with Profit ✅
```

## Configuration (Optional)

The default timeout is **24 hours**. To customize, add to your `.env` file:

```bash
# Position timeout in hours (default: 24)
POSITION_TIMEOUT_HOURS=24
```

Examples:
- `POSITION_TIMEOUT_HOURS=12` - More aggressive (12 hours)
- `POSITION_TIMEOUT_HOURS=48` - More lenient (48 hours)
- `POSITION_TIMEOUT_HOURS=24` - Default (recommended)

## What You'll See in Logs

### Position Age Display
```
📊 Processing BTCUSDT...
   Current position: LONG 0.002
   Entry: $50000.00 | Mark: $50100.00
   PnL: 0.20% ($1.00)
   Age: 23.5h / 24.0h  ← Position age tracking
```

### Timeout Closure
```
🔴 Closing position: TIMEOUT (24.5h, PnL: 0.20%)
CLOSE LONG BTCUSDT | TIMEOUT (24.5h, PnL: 0.20%) | PnL: 0.20%
⏱️ Cleared position tracking for BTCUSDT
```

### Normal TP Closure (Still Works!)
```
🔴 Closing position: TP (1.00%)
CLOSE LONG BTCUSDT | TP (1.00%) | PnL: 1.00%
```

## Testing the Feature

Run the test suite to verify everything works:

```bash
python test_position_timeout.py
```

Expected output:
```
✅ ALL TESTS PASSED!
```

## Starting the Bot

No changes needed! Just start as usual:

```bash
python bot.py
```

The timeout feature is automatically active.

## Monitoring

### Check Position Tracking
View currently tracked positions:
```bash
cat data/position_times.json
```

### Review Timeout Closures
Search logs for timeout events:
```bash
grep "TIMEOUT" logs/bot_*.log
```

## Example Scenarios

### ✅ Scenario 1: Position Hits TP (Normal)
```
Hour 0:  Open LONG BTCUSDT at $50,000
Hour 2:  Price reaches $50,500 (1% profit)
Action:  Close with TP ✅
Result:  +1% profit in 2 hours
```

### ⏱️ Scenario 2: Position Times Out (Profitable)
```
Hour 0:   Open LONG BTCUSDT at $50,000
Hour 24:  Price at $50,100 (0.2% profit, below TP)
Action:   Close with TIMEOUT ⏱️
Result:   +0.2% profit, capital freed for new trades
```

### ⏱️ Scenario 3: Position Times Out (Loss)
```
Hour 0:   Open SHORT ETHUSDT at $3,000
Hour 25:  Price at $3,015 (-0.5% loss)
Action:   Close with TIMEOUT ⏱️
Result:   -0.5% loss, prevents further losses
```

## Key Points

### ✅ What Works
- Positions tracked automatically when opened
- Timeout check runs every loop
- Works with multiple wallets/symbols independently
- Persists across bot restarts
- No manual intervention needed

### 📋 Priority Order
1. **Take Profit (1%)** - Closes immediately ✅
2. **Stop Loss (0%)** - Currently disabled
3. **Timeout (24h)** - Closes if TP not hit ⏱️

### 🔄 Data Persistence
- Position times saved to `data/position_times.json`
- Survives bot restarts
- Automatic cleanup of old data

## Troubleshooting

### Q: Position not showing age?
**A:** Position was opened before timeout feature. Will track from next opening.

### Q: Timeout not triggering?
**A:** Check if position already hit TP (1%). TP takes priority over timeout.

### Q: Want to disable timeout?
**A:** Set very high value: `POSITION_TIMEOUT_HOURS=999999`

### Q: Want shorter timeout?
**A:** Set lower value: `POSITION_TIMEOUT_HOURS=12`

## Summary

The Position Timeout feature is now active and working! It will:

✅ Track all position opening times
✅ Monitor position age continuously  
✅ Auto-close positions after 24 hours if TP not hit
✅ Work independently for each wallet
✅ Persist across bot restarts
✅ Require zero manual intervention

Your high-frequency trading strategy (1% TP, 10x leverage, $10 position size) now has an additional safety mechanism to prevent positions from staying open too long.

## Need Help?

- **Full Documentation**: See `docs/POSITION_TIMEOUT.md`
- **Implementation Details**: See `POSITION_TIMEOUT_IMPLEMENTATION.md`
- **Test Suite**: Run `python test_position_timeout.py`

---

**Happy Trading! 🚀**

