# 🚀 Quick Start: Grok AI Validator

Hướng dẫn nhanh để setup và sử dụng Grok AI Validator.

---

## ⚡ 3-Step Setup

### Step 1: Get API Key

1. Truy cập: https://console.x.ai/
2. Sign up / Login
3. Tạo API key
4. Copy key (dạng: `xai-...`)

### Step 2: Configure

Thêm vào file `.env`:

```env
# AI Validator
USE_AI_VALIDATOR=True
AI_PROVIDER=grok
XAI_API_KEY=xai-your-api-key-here

# Mode (optional - default is borderline)
AI_VALIDATOR_MODE=borderline
```

### Step 3: Test

```bash
# Windows
python scripts\test_ai_validator.py

# Linux/Mac
python scripts/test_ai_validator.py
```

**Expected output:**
```
🧪 TESTING AI VALIDATOR
✅ Available providers: grok

Testing GROK provider
🤖 Calling GROK API... (1.8s)

✅ AI Response:
   Decision: APPROVE ✅
   Confidence: 75%
   Reasoning: Clean technical setup...
```

---

## ✅ You're Ready!

Start trading:
```bash
python bot.py
```

---

## ❌ Troubleshooting

### Error: "No module named 'anthropic'"

**Cause:** Test script imports all providers

**Fix:** Bạn đang dùng Grok, không cần anthropic. Code đã được update để handle optional imports.

**Verify fix worked:**
```bash
python scripts/test_ai_validator.py
```

Bây giờ sẽ chỉ test Grok và skip Claude.

---

### Error: "No API key found"

**Cause:** Missing `XAI_API_KEY` in `.env`

**Fix:**
```env
# Add to .env
XAI_API_KEY=xai-your-key-here
```

---

### Error: "Model not found"

**Cause:** Wrong model name

**Fix:** Không cần set `AI_MODEL` - tự động dùng `grok-4-1-fast-reasoning`

```env
# Remove this line if you have it:
# AI_MODEL=grok-beta

# Or set explicitly:
AI_MODEL=grok-4-1-fast-reasoning
```

---

## 📊 Verify Setup

```bash
python scripts/verify_grok_model.py
```

**Expected:**
```
✅ VERIFYING GROK MODEL CONFIGURATION
1. AI Validator: ENABLED ✅
2. Provider: Grok ✅
3. API Key: Found ✅
4. Model: grok-4-1-fast-reasoning ✅

✅ READY TO USE GROK AI VALIDATOR
```

---

## 🎯 Configuration Examples

### Minimal (Recommended)
```env
USE_AI_VALIDATOR=True
AI_PROVIDER=grok
XAI_API_KEY=xai-xxx
```

### Conservative (High Quality)
```env
USE_AI_VALIDATOR=True
AI_PROVIDER=grok
XAI_API_KEY=xai-xxx
AI_VALIDATOR_MODE=all  # Check every signal
AI_MIN_CONFIDENCE=0.7  # Require 70%+ confidence
```

### Balanced (Default)
```env
USE_AI_VALIDATOR=True
AI_PROVIDER=grok
XAI_API_KEY=xai-xxx
AI_VALIDATOR_MODE=borderline  # Only scores 7-10
AI_MIN_CONFIDENCE=0.6
```

### Aggressive (Minimal AI)
```env
USE_AI_VALIDATOR=True
AI_PROVIDER=grok
XAI_API_KEY=xai-xxx
AI_VALIDATOR_MODE=tiebreaker  # Only when needed
```

---

## 💰 Cost

**Borderline mode (recommended):**
- ~15 AI calls/day
- ~$0.015/day
- **~$0.45/month**

**All mode:**
- ~50 AI calls/day
- ~$0.05/day
- **~$1.50/month**

Very affordable! 💰

---

## 📚 Documentation

**Quick Guides:**
- [GROK_MODELS_GUIDE.md](docs/GROK_MODELS_GUIDE.md) - Model details
- [GROK_MODEL_UPDATE.md](GROK_MODEL_UPDATE.md) - What changed

**Complete Guides:**
- [AI_VALIDATOR_GUIDE.md](docs/AI_VALIDATOR_GUIDE.md) - Full guide
- [AI_VALIDATOR_FLOW.md](docs/AI_VALIDATOR_FLOW.md) - Visual flows

---

## 🎯 What AI Does

**Example Signal:**
```
DOTUSDT SHORT
Score: 13/15 (Very strong)
ML: 0.35 (Weak conviction) ⚠️
```

**Without AI:**
```
→ HOLD (filtered by ML conviction filter)
→ Miss potential good trade
```

**With AI:**
```
→ AI analyzes: "Setup is clean but entry at support is risky"
→ AI suggests: Reduce position to 60%, tight SL
→ ENTER with adjustments ✅
→ Better risk management
```

---

## ⚙️ Advanced Options

### Custom Model
```env
AI_MODEL=grok-4-1-fast-reasoning  # Default (recommended)
# AI_MODEL=grok-beta              # Legacy
# AI_MODEL=grok-2-latest          # Older
```

### Timeouts
```env
AI_TIMEOUT_SECONDS=5  # Default
AI_MAX_RETRIES=2      # Default
```

### Score Range (Borderline Mode)
```env
AI_MIN_SCORE_FOR_CHECK=7   # Min score to trigger AI
AI_MAX_SCORE_FOR_CHECK=10  # Max score to trigger AI
```

---

## 🔍 Monitor Performance

**View AI decisions:**
```bash
cat logs/ai_validator_history.json
```

**Check accuracy:**
```python
from trading.ai_validator import AIAccuracyTracker

tracker = AIAccuracyTracker()
tracker.print_statistics()
```

---

## ✅ Checklist

- [ ] Got API key from https://console.x.ai/
- [ ] Added `XAI_API_KEY` to `.env`
- [ ] Set `USE_AI_VALIDATOR=True`
- [ ] Set `AI_PROVIDER=grok`
- [ ] Tested: `python scripts/test_ai_validator.py` ✅
- [ ] Verified: `python scripts/verify_grok_model.py` ✅
- [ ] Started bot: `python bot.py` 🚀

---

## 🎉 That's It!

You're now using **grok-4-1-fast-reasoning** for AI-powered trade validation!

**Benefits:**
- ⚡ Fast (1.8s responses)
- 🎯 Accurate (78%+ correct)
- 🧠 Smart reasoning
- 💰 Affordable ($0.45/month)

Happy trading! 🚀
