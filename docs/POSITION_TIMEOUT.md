# ⏱️ Position Timeout Feature

## Overview

The Position Timeout feature automatically closes any open position that has been open for more than 24 hours without reaching the take profit (TP) target. This prevents positions from staying open indefinitely and helps manage risk in the high-frequency trading strategy.

## How It Works

### 1. Position Tracking
- When a position is opened, the bot records the exact timestamp
- Position opening times are stored in `data/position_times.json`
- This data persists across bot restarts, ensuring continuity

### 2. Timeout Monitoring
- Every trading loop, the bot checks the age of each open position
- If a position has been open for ≥24 hours and hasn't hit the 1% TP target
- The position is automatically closed at market price

### 3. Independent Per-Wallet
- Each position (symbol) is tracked independently
- Works seamlessly with multiple wallets/symbols
- Timeout applies to each position individually

## Configuration

### Environment Variable
Add to your `.env` file:

```bash
# Position timeout in hours (default: 24)
POSITION_TIMEOUT_HOURS=24
```

### Customization
You can adjust the timeout period:
- **24 hours** (default) - Recommended for the current strategy
- **12 hours** - More aggressive timeout
- **48 hours** - More lenient timeout

## Integration with Existing Strategy

The timeout feature integrates seamlessly with your existing trading parameters:

- **Take Profit**: 1% (Config.TP_PCT)
- **Stop Loss**: 0% (disabled, Config.SL_PCT)
- **Leverage**: 10x (Config.LEVERAGE)
- **Position Size**: $10 fixed (Config.POSITION_SIZE_USDT)
- **Margin Mode**: Isolated
- **Timeout**: 24 hours (Config.POSITION_TIMEOUT_HOURS)

### Priority Order
When checking if a position should be closed:
1. **Take Profit** - Closes immediately if 1% profit reached
2. **Stop Loss** - Closes if SL threshold reached (currently disabled)
3. **Timeout** - Closes if 24+ hours elapsed without hitting TP

## Example Scenarios

### Scenario 1: Position Hits TP Before Timeout
```
Time 0h:    Open LONG BTCUSDT at $50,000
Time 2h:    Price reaches $50,500 (1% profit)
Action:     ✅ Close position with TP reason
Result:     Position closed after 2 hours with 1% profit
```

### Scenario 2: Position Times Out
```
Time 0h:    Open LONG BTCUSDT at $50,000
Time 24h:   Price at $50,100 (0.2% profit, below TP)
Action:     ⏱️ Close position with TIMEOUT reason
Result:     Position closed after 24 hours with 0.2% profit
```

### Scenario 3: Position Times Out with Loss
```
Time 0h:    Open SHORT ETHUSDT at $3,000
Time 25h:   Price at $3,015 (-0.5% loss)
Action:     ⏱️ Close position with TIMEOUT reason
Result:     Position closed after 25 hours with -0.5% loss
```

## Log Messages

### Position Tracking
```
⏱️ Tracking position open time for BTCUSDT: 2025-11-03T07:30:00.123456
```

### Position Age Display
```
📊 Processing BTCUSDT...
   Current position: LONG 0.002
   Entry: $50000.00 | Mark: $50100.00
   PnL: 0.20% ($1.00)
   Age: 23.5h / 24.0h
```

### Timeout Close
```
🔴 Closing position: TIMEOUT (24.5h, PnL: 0.20%)
CLOSE LONG BTCUSDT | TIMEOUT (24.5h, PnL: 0.20%) | PnL: 0.20%
⏱️ Cleared position tracking for BTCUSDT
```

### Cleanup
```
🧹 Cleaned up 2 stale position trackings
```

## Data Persistence

### Storage Location
Position timestamps are stored in:
```
data/position_times.json
```

### File Format
```json
{
  "BTCUSDT": "2025-11-03T07:30:00.123456",
  "ETHUSDT": "2025-11-03T08:15:30.789012"
}
```

### Automatic Cleanup
- Stale position tracking is cleaned up every 10 loops
- Positions that no longer exist are automatically removed
- Ensures the tracking file stays clean and accurate

## Benefits

### 1. Risk Management
- Prevents positions from staying open indefinitely
- Limits exposure time for each trade
- Helps manage overnight and weekend risk

### 2. Capital Efficiency
- Frees up capital from stagnant positions
- Allows redeployment to new opportunities
- Maintains high trading frequency

### 3. Strategy Alignment
- Complements the high-frequency approach
- Ensures positions don't deviate from the 1% TP target strategy
- Maintains focus on quick, small profits

### 4. Reliability
- Persists across bot restarts
- Works independently for each wallet
- No manual intervention required

## Testing

Run the test suite to verify the feature:

```bash
python test_position_timeout.py
```

Expected output:
```
✅ ALL TESTS PASSED!

💡 The position timeout feature is working correctly!
   - Positions will be tracked when opened
   - Positions will auto-close after 24 hours if TP not hit
   - Tracking persists across bot restarts
```

## Monitoring

### Check Position Ages
The bot displays position age in each loop:
```
Age: 12.3h / 24.0h
```

### Review Timeout Closes
Check logs for TIMEOUT close reasons:
```bash
grep "TIMEOUT" logs/bot_*.log
```

### Verify Tracking File
Inspect current tracked positions:
```bash
cat data/position_times.json
```

## Troubleshooting

### Position Not Tracked
**Symptom**: Position age shows as `None`

**Cause**: Position was opened before the timeout feature was added

**Solution**: The bot will start tracking from the next position opening

### Stale Tracking Data
**Symptom**: Tracking file contains old symbols

**Cause**: Normal - cleanup happens every 10 loops

**Solution**: No action needed, automatic cleanup will handle it

### Timeout Not Triggering
**Symptom**: Position older than 24h not closing

**Cause**: Check if position has already hit TP

**Solution**: Verify TP_PCT configuration and position PnL

## API Reference

### PositionTracker Class

```python
from trading.position_tracker import PositionTracker

tracker = PositionTracker()

# Track new position
tracker.track_position_open('BTCUSDT')

# Get position age
age_hours = tracker.get_position_age_hours('BTCUSDT')

# Check if timed out
is_timeout = tracker.is_position_timeout('BTCUSDT', timeout_hours=24)

# Clear tracking
tracker.clear_position('BTCUSDT')

# Cleanup stale positions
tracker.cleanup_stale_positions(['BTCUSDT', 'ETHUSDT'])
```

### SignalGenerator Update

```python
# Updated method signature
should_close, reason = signal_generator.should_close_position(
    position,
    tp_pct=None,
    sl_pct=None,
    position_age_hours=None  # New parameter
)
```

## Future Enhancements

Potential improvements for future versions:

1. **Dynamic Timeout**: Adjust timeout based on market volatility
2. **Partial Close**: Close portion of position at timeout
3. **Timeout Alerts**: Send Telegram notification before timeout
4. **Statistics**: Track timeout frequency and average PnL at timeout
5. **Per-Symbol Timeout**: Different timeout for different symbols

## Summary

The Position Timeout feature is a critical risk management tool that:
- ✅ Automatically closes positions after 24 hours
- ✅ Works independently for each wallet/position
- ✅ Persists across bot restarts
- ✅ Integrates seamlessly with existing strategy
- ✅ Requires no manual intervention
- ✅ Fully tested and production-ready

This feature ensures your high-frequency trading strategy stays focused on quick, profitable trades while managing risk effectively.

