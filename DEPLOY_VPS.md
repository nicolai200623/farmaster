# 🚀 Deploy Bot với Grok AI lên VPS

## ⚠️ VẤN ĐỀ HIỆN TẠI

Bot trên VPS **KHÔNG** gọi Grok AI vì:
- `.env` trên VPS thiếu `XAI_API_KEY` và các config Grok AI mới
- Log hiển thị: `⚠️ AI Check enabled but grok client not available`

---

## ✅ GIẢI PHÁP: Deploy .env mới lên VPS

### Bước 1: Chuẩn bị

1. **Kiểm tra .env local** có đầy đủ config:
   ```bash
   grep -E "XAI_API_KEY|GROK_MODEL|AI_VALIDATOR_MODE|USE_ENTRY_PIPELINE|USE_AI_CHECK" .env
   ```

   Phải thấy:
   ```env
   USE_ENTRY_PIPELINE=True
   USE_AI_CHECK=True
   AI_PROVIDER=grok
   GROK_MODEL=grok-4-1-fast-reasoning
   AI_VALIDATOR_MODE=all
   AI_CHECK_BORDERLINE_ONLY=False
   XAI_API_KEY=xai-xxx...xxx  # API key của bạn
   ```

2. **Sửa thông tin VPS** trong script upload:
   - File Windows: `upload_env_to_vps.bat`
   - File Linux/Mac: `upload_env_to_vps.sh`

   Sửa 3 dòng:
   ```bash
   VPS_USER="root"           # Thay bằng username VPS của bạn
   VPS_HOST="your_vps_ip"    # Thay bằng IP VPS
   VPS_PATH="/root/FarmAster" # Thay bằng đường dẫn bot trên VPS
   ```

---

### Bước 2: Upload .env lên VPS

**Windows:**
```cmd
upload_env_to_vps.bat
```

**Linux/Mac:**
```bash
chmod +x upload_env_to_vps.sh
./upload_env_to_vps.sh
```

**Hoặc upload thủ công:**
```bash
scp .env root@your_vps_ip:/root/FarmAster/.env
```

---

### Bước 3: Pull code mới và restart bot

SSH vào VPS:
```bash
ssh root@your_vps_ip
```

Trong VPS:
```bash
cd /root/FarmAster  # Đường dẫn bot trên VPS

# Pull code mới từ GitHub
git pull origin master

# Stop bot cũ
pkill -f bot.py

# Khởi động bot mới
nohup python bot.py > bot.log 2>&1 &

# Monitor log
tail -f bot.log
```

---

### Bước 4: Kiểm tra Grok AI hoạt động

Trong log bạn phải thấy:

#### ✅ Khi bot khởi động:
```
🚀 Entry Pipeline enabled (5-stage validation)
🤖 AIEntryAnalyzer initialized (provider: grok)  # ← QUAN TRỌNG!
   Stages enabled: ML=True, SmartEntry=False, PA=False, HTF=False, AI=True
```

#### ✅ Khi có signal:
```
[PASS] ml_ensemble: XGB:0.72, LGB:0.68, CB:0.65 → LONG (0.68)
🤖 Calling Grok AI...
✅ AI approved: High ML confidence, aligned models, strong momentum
✅ BTCUSDT ENTRY APPROVED: LONG
   Stages passed: ['ml_ensemble', 'ai_check']  # ← Phải có 'ai_check'!
```

#### ❌ Nếu thấy (LỖI):
```
⚠️ AI Check enabled but grok client not available  # ← Config sai!
```

Nghĩa là `.env` chưa được upload đúng. Kiểm tra lại:
```bash
grep XAI_API_KEY /root/FarmAster/.env
```

---

## 🔍 Troubleshooting

### Lỗi 1: "grok client not available"

**Nguyên nhân:** `XAI_API_KEY` trống hoặc không có trong `.env`

**Giải pháp:**
```bash
# Trên VPS, kiểm tra .env
cat /root/FarmAster/.env | grep XAI_API_KEY

# Nếu không có hoặc trống, upload lại .env từ local
scp .env root@vps_ip:/root/FarmAster/.env

# Restart bot
pkill -f bot.py && nohup python bot.py > bot.log 2>&1 &
```

---

### Lỗi 2: Pipeline enabled nhưng không gọi AI

**Nguyên nhân:** Thiếu package `openai`

**Giải pháp:**
```bash
# Trên VPS
pip install openai

# Hoặc cài từ requirements
pip install -r requirements.txt
```

---

### Lỗi 3: "OPENAI_AVAILABLE = False"

**Nguyên nhân:** Package `openai` chưa cài hoặc version quá cũ

**Giải pháp:**
```bash
pip install --upgrade openai
```

Cần version >= 1.0.0 để dùng Grok API (OpenAI-compatible)

---

## 📊 Flow hoạt động sau khi deploy

```
📊 Lấy data OHLCV (1H timeframe)
    ↓
🎭 ML Ensemble (XGBoost + LightGBM + CatBoost)
    ├─ Nếu confidence < 0.65 → REJECT
    └─ Nếu PASS → Tiếp
           ↓
🤖 GROK AI TIER 2 VALIDATION
    ├─ Model: grok-4-1-fast-reasoning
    ├─ Phân tích: ML confidence, indicators, candles, volume
    ├─ Decision: ENTER (confidence >= 60%) hoặc SKIP
    └─ Reason: Giải thích chi tiết
           ↓
    ✅ Nếu ENTER → EXECUTE TRADE
    ❌ Nếu SKIP → BỎ QUA
```

---

## 🎯 Kết quả mong đợi

Sau khi deploy đúng, trong **mỗi** signal bạn sẽ thấy log:

```
🎭 ML Ensemble: PASS (confidence 0.72)
🤖 Calling Grok AI...
🤖 Grok AI response: ENTER (confidence 85%)
✅ ENTRY APPROVED
   Stages: ['ml_ensemble', 'ai_check']
```

Nếu Grok reject:
```
🎭 ML Ensemble: PASS (confidence 0.68)
🤖 Calling Grok AI...
🤖 Grok AI response: SKIP (confidence 92%) - Weak volume, potential fake breakout
❌ ENTRY REJECTED: AI rejected
```

---

## 📞 Hỗ trợ

Nếu gặp vấn đề, cung cấp:
1. Log khi bot khởi động (từ "Bot initialized" đến "Trading loop started")
2. Log của 1 signal bị reject/approve
3. Kết quả của: `grep XAI_API_KEY .env` (trên VPS)
