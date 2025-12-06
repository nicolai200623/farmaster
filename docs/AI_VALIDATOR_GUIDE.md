# 🤖 AI Validator Guide

## Overview

AI Validator là một lớp validation thông minh sử dụng AI (Grok, Claude, GPT, Gemini) để phân tích và xác nhận trading signals trước khi entry.

## Features

✅ **Multi-Provider Support**
- **Grok (xAI)** - Recommended for crypto market analysis
- **Claude (Anthropic)** - Fast and accurate with Haiku model
- **GPT (OpenAI)** - gpt-4o-mini for cost-effective analysis
- **Gemini (Google)** - gemini-1.5-flash for quick responses

✅ **Flexible Validation Modes**
- **All Mode** - Analyze every signal
- **Borderline Mode** - Only signals with score 7-10 (grey zone)
- **Tiebreaker Mode** - When filters conflict

✅ **Accuracy Tracking**
- Record all AI decisions
- Track win/loss outcomes
- Calculate AI accuracy over time
- Export history to JSON

---

## Installation

### 1. Install Required Packages

```bash
# For Claude (Anthropic)
pip install anthropic

# For Grok/GPT (OpenAI-compatible)
pip install openai

# For Gemini (Google)
pip install google-generativeai
```

### 2. Configure API Keys

Add to your `.env` file:

```env
# AI Validator Settings
USE_AI_VALIDATOR=True
AI_PROVIDER=grok  # or claude, openai, gemini
AI_VALIDATOR_MODE=borderline  # all, borderline, tiebreaker

# API Keys (choose one or more)
XAI_API_KEY=your_grok_api_key_here
ANTHROPIC_API_KEY=your_claude_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_gemini_api_key_here

# Advanced Settings
AI_MIN_SCORE_FOR_CHECK=7  # Min score to trigger AI (borderline mode)
AI_MAX_SCORE_FOR_CHECK=10  # Max score to trigger AI (borderline mode)
AI_TIMEOUT_SECONDS=5
AI_MAX_RETRIES=2
AI_MIN_CONFIDENCE=0.6  # Min AI confidence to approve (60%)

# Accuracy Tracking
TRACK_AI_ACCURACY=True
AI_HISTORY_FILE=logs/ai_validator_history.json
```

---

## How It Works

### Signal Flow with AI Validator

```
1. ML Ensemble → Predicts direction
         ↓
2. Smart Entry → Score 13/15 ✅
         ↓
3. Filters → HTF, Cooldown, etc.
         ↓
4. 🤖 AI Validator → Analyzes setup
         ↓
   - Checks technical quality
   - Identifies traps
   - Assesses risk/reward
         ↓
5. Final Decision → ENTER or HOLD
```

### When AI is Triggered

**Borderline Mode (Default):**
```
Score 1-6   → ❌ Auto HOLD (too weak)
Score 7-10  → 🤖 Ask AI (grey zone)
Score 11-15 → ✅ Auto ENTER (very strong)
```

**All Mode:**
```
Every signal → 🤖 Ask AI
```

**Tiebreaker Mode:**
```
Filters conflict → 🤖 Ask AI
Score borderline → 🤖 Ask AI
Clear signals → Skip AI
```

---

## Usage Examples

### Example 1: Using Grok (Recommended)

```env
USE_AI_VALIDATOR=True
AI_PROVIDER=grok
XAI_API_KEY=xai-xxxxxxxxxxxxx
AI_VALIDATOR_MODE=borderline
```

**What happens:**
- Bot detects signal with score 8/15
- AI Validator calls Grok API
- Grok analyzes: "Pullback looks clean, but volume is weak. SKIP."
- Bot holds, avoids potential loss

### Example 2: Using Claude for Fast Decisions

```env
USE_AI_VALIDATOR=True
AI_PROVIDER=claude
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
AI_MODEL=claude-3-haiku-20240307
AI_TIMEOUT_SECONDS=3  # Fast responses
```

**What happens:**
- Claude Haiku responds in ~1-2 seconds
- Low latency, good for high-frequency signals

### Example 3: Analyze All Signals

```env
USE_AI_VALIDATOR=True
AI_VALIDATOR_MODE=all
AI_PROVIDER=grok
```

**What happens:**
- Every signal (score 1-15) goes through AI
- More conservative, fewer entries
- Higher quality trades

---

## AI Decision Examples

### Example Signal: DOTUSDT SHORT (Score 13/15)

**Input to AI:**
```
Symbol: DOTUSDT
Direction: SHORT
Score: 13/15

Reasons:
- Perfect alignment: All TFs DOWN
- Perfect pullback to EMA21
- At swing low (support)
- RSI neutral (good for entry)
- London session (high liquidity)

Technical:
- Price: $6.234
- EMA21: $6.240
- RSI: 45.2
- ML Prob: 0.35 (bearish)

Filters:
- HTF Alignment: PASS
- Cooldown: PASS
- ML Conviction: WEAK ⚠️
```

**AI Response:**
```
DECISION: APPROVE
CONFIDENCE: 75%
REASONING: Strong technical setup with perfect pullback.
However, ML conviction is weak. Suggest smaller position size.
```

**Bot Action:**
- ✅ Enter SHORT position
- Use suggested adjustments (if any)

---

## AI Prompt Template

The AI receives this structured prompt:

```
You are an expert crypto trading analyst. Evaluate this {SIGNAL} signal.

SIGNAL STRENGTH: {SCORE}/15
ENTRY REASONS: {REASONS}
TECHNICAL DATA: {PRICE, INDICATORS}
FILTERS STATUS: {FILTERS}

Consider:
1. Technical setup quality
2. Risk/Reward ratio
3. Market traps (liquidity sweeps, stop hunts)
4. Timing

Respond:
DECISION: [APPROVE/REJECT]
CONFIDENCE: [0-100]%
REASONING: [1-2 sentences]
```

---

## Accuracy Tracking

### Viewing AI Statistics

```python
from trading.ai_validator import AIAccuracyTracker

tracker = AIAccuracyTracker()
tracker.print_statistics()
```

**Output:**
```
============================================================
🤖 AI VALIDATOR STATISTICS
============================================================
Total Decisions: 127
Completed Trades: 89
AI Accuracy: 73.0%
Avg Confidence: 68.5%
Approval Rate: 42.5%
AI-Approved Win Rate: 78.2%
============================================================
```

### Interpreting Results

- **AI Accuracy 73%** - AI correctly predicted 73% of outcomes
- **Approval Rate 42.5%** - AI approved 42.5% of signals (conservative)
- **AI-Approved Win Rate 78.2%** - Trades approved by AI won 78.2% of the time

---

## Testing

### Run Test Script

```bash
python scripts/test_ai_validator.py
```

This will:
1. Test all configured AI providers
2. Run sample signal validation
3. Test accuracy tracker
4. Display results

### Sample Test Output

```
🧪 TESTING AI VALIDATOR
✅ Available providers: grok, claude

Testing GROK provider
📊 Test Signal:
   Symbol: DOTUSDT
   Direction: SHORT
   Score: 13/15

🤖 Calling GROK API...

✅ AI Response:
   Decision: APPROVE ✅
   Confidence: 75%
   Reasoning: Clean pullback setup with good R:R.
   Watch for support bounce.
```

---

## Best Practices

### 1. Start with Borderline Mode
```env
AI_VALIDATOR_MODE=borderline
AI_MIN_SCORE_FOR_CHECK=7
AI_MAX_SCORE_FOR_CHECK=10
```
- Focuses AI on uncertain signals
- Saves API costs
- Lets clear signals pass through

### 2. Choose Right Provider

**For Speed:** Claude Haiku (1-2s response)
```env
AI_PROVIDER=claude
AI_MODEL=claude-3-haiku-20240307
```

**For Crypto Expertise:** Grok
```env
AI_PROVIDER=grok
AI_MODEL=grok-2-latest
```

**For Cost:** GPT-4o-mini
```env
AI_PROVIDER=openai
AI_MODEL=gpt-4o-mini
```

### 3. Set Appropriate Timeouts

```env
AI_TIMEOUT_SECONDS=5  # Recommended
AI_MAX_RETRIES=2
```
- Too low: May miss responses
- Too high: Delays trading

### 4. Monitor Accuracy

Review AI history regularly:
```bash
cat logs/ai_validator_history.json | jq '.[-10:]'
```

---

## Troubleshooting

### AI Not Triggering

**Check:**
1. `USE_AI_VALIDATOR=True` in config
2. API key is set
3. Score is in range (for borderline mode)
4. Provider client is available

**Debug:**
```bash
python scripts/test_ai_validator.py
```

### API Timeouts

**Solution:**
```env
AI_TIMEOUT_SECONDS=10  # Increase timeout
AI_MAX_RETRIES=3       # More retries
```

### Wrong Provider

**Check logs:**
```
⚠️ AI Check enabled but grok client not available
```

**Fix:**
```bash
pip install openai  # For Grok/GPT
```

---

## Cost Considerations

### API Costs per Request

| Provider | Model | Cost/Request | Speed |
|----------|-------|--------------|-------|
| Claude | Haiku | ~$0.0001 | 1-2s |
| Grok | Grok-2 | ~$0.001 | 2-3s |
| OpenAI | gpt-4o-mini | ~$0.0002 | 2-4s |
| Gemini | Flash | ~$0.00005 | 1-2s |

### Monthly Cost Estimate

**Borderline Mode (30 signals/day):**
- Claude: ~$0.09/month
- Grok: ~$0.90/month
- GPT: ~$0.18/month
- Gemini: ~$0.05/month

**All Mode (100 signals/day):**
- Claude: ~$0.30/month
- Grok: ~$3.00/month
- GPT: ~$0.60/month
- Gemini: ~$0.15/month

---

## Advanced Configuration

### Custom AI Model

```env
AI_MODEL=grok-beta  # Custom model
```

### Adjust Confidence Threshold

```env
AI_MIN_CONFIDENCE=0.7  # Require 70% AI confidence
```

### Multiple Providers Fallback

Coming soon: Auto-fallback if primary provider fails.

---

## FAQ

**Q: Should I use AI for every signal?**
A: Start with borderline mode. Use "all" mode if you want maximum safety.

**Q: Which provider is best?**
A: Grok for crypto expertise, Claude for speed, Gemini for cost.

**Q: How accurate is AI?**
A: Typically 65-75% accuracy. Track your own results with AIAccuracyTracker.

**Q: Does AI slow down trading?**
A: ~1-5 seconds per call. Use borderline mode to minimize calls.

**Q: Can I use multiple providers?**
A: Currently one at a time. Ensemble AI coming soon.

---

## Changelog

### v1.0.0 (2025-12-06)
- ✅ Multi-provider support (Grok, Claude, GPT, Gemini)
- ✅ Three validation modes (all, borderline, tiebreaker)
- ✅ AI accuracy tracking
- ✅ Detailed logging
- ✅ Test script

---

## Next Steps

1. **Set up API key** in `.env`
2. **Run test script** to verify
3. **Start with borderline mode**
4. **Monitor accuracy** after 20+ trades
5. **Adjust settings** based on results

Good luck with AI-powered trading! 🚀
