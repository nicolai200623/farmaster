# 🚀 TRAIN LOCAL - DEPLOY VPS

## ✅ Lợi Ích

- ⚡ **Nhanh hơn:** CPU/GPU local mạnh hơn VPS
- 💰 **Tiết kiệm:** Không tốn CPU time trên VPS
- 🔧 **Dễ debug:** Có thể monitor trực tiếp
- 📊 **Backtest ngay:** Test models trước khi deploy

---

## 📋 WORKFLOW CHUẨN

### Bước 1: Train Trên Local (Windows)

```powershell
# 1. Đảm bảo code mới nhất
git pull origin master

# 2. Kiểm tra fix warnings
python test_features_fix.py

# 3. Train với 180 ngày (khuyến nghị)
python scripts/auto_retrain.py --days 180

# 4. Đợi ~45-60 phút (theo dõi progress)
# Có thể làm việc khác trong lúc này

# 5. Kiểm tra training đã xong
python check_training_status.py

# 6. Backtest để verify models tốt
python run_backtest_90days.py
```

**Kết quả:** Bạn sẽ có 4 files trong thư mục `models/`:
- `lstm_model.pt` (~45 MB)
- `xgboost_model.json` (~2 MB)
- `lightgbm_model.txt` (~2 MB)
- `catboost_model.cbm` (~3 MB)

---

### Bước 2: Upload Models Lên VPS

#### Cách 1: Dùng SCP (Khuyến Nghị)

```powershell
# Từ máy local (Windows PowerShell)
# Syntax: scp <local_file> <user>@<vps_ip>:<remote_path>

# Upload từng file
scp models/lstm_model.pt user@your-vps-ip:/home/farmaster/farmaster/models/
scp models/xgboost_model.json user@your-vps-ip:/home/farmaster/farmaster/models/
scp models/lightgbm_model.txt user@your-vps-ip:/home/farmaster/farmaster/models/
scp models/catboost_model.cbm user@your-vps-ip:/home/farmaster/farmaster/models/

# Hoặc upload cả thư mục
scp -r models/* user@your-vps-ip:/home/farmaster/farmaster/models/
```

**Lưu ý:**
- Thay `user` bằng username VPS của bạn
- Thay `your-vps-ip` bằng IP VPS
- Thay `/home/farmaster/farmaster` bằng đường dẫn thực tế

#### Cách 2: Dùng WinSCP (GUI - Dễ hơn)

1. **Download WinSCP:** https://winscp.net/eng/download.php
2. **Kết nối VPS:**
   - Host: IP VPS của bạn
   - Username: username VPS
   - Password: password VPS
   - Port: 22
3. **Upload:**
   - Bên trái: Máy local → Navigate đến `C:\LAINP\Augment\FarmAster\models`
   - Bên phải: VPS → Navigate đến `/home/farmaster/farmaster/models`
   - Drag & drop 4 files từ trái sang phải

#### Cách 3: Dùng Git (Nếu Models Nhỏ)

⚠️ **KHÔNG khuyến nghị** vì:
- Models lớn (~50 MB total)
- Git không tối ưu cho binary files
- Làm chậm repository

**Nhưng nếu muốn:**
```powershell
# Local
git add models/*.pt models/*.json models/*.txt models/*.cbm
git commit -m "Update trained models (180 days)"
git push origin master

# VPS
git pull origin master
```

#### Cách 4: Dùng SFTP

```powershell
# Windows PowerShell
sftp user@your-vps-ip

# Trong SFTP session
cd /home/farmaster/farmaster/models
lcd C:\LAINP\Augment\FarmAster\models
put lstm_model.pt
put xgboost_model.json
put lightgbm_model.txt
put catboost_model.cbm
exit
```

---

### Bước 3: Verify Trên VPS

```bash
# SSH vào VPS
ssh user@your-vps-ip

# Navigate đến project
cd /home/farmaster/farmaster

# Kiểm tra models đã upload
ls -lh models/

# Phải thấy 4 files:
# -rw-r--r-- 1 user user  45M Nov 26 16:00 lstm_model.pt
# -rw-r--r-- 1 user user 2.2M Nov 26 16:00 xgboost_model.json
# -rw-r--r-- 1 user user 1.9M Nov 26 16:00 lightgbm_model.txt
# -rw-r--r-- 1 user user 3.2M Nov 26 16:00 catboost_model.cbm

# Kiểm tra file size (phải giống local)
du -sh models/*

# Test load models
python3 -c "
import torch
from xgboost import XGBClassifier
import lightgbm as lgb
from catboost import CatBoostClassifier

# Test LSTM
model = torch.load('models/lstm_model.pt')
print('✅ LSTM loaded')

# Test XGBoost
xgb = XGBClassifier()
xgb.load_model('models/xgboost_model.json')
print('✅ XGBoost loaded')

# Test LightGBM
lgbm = lgb.Booster(model_file='models/lightgbm_model.txt')
print('✅ LightGBM loaded')

# Test CatBoost
cat = CatBoostClassifier()
cat.load_model('models/catboost_model.cbm')
print('✅ CatBoost loaded')

print('🎉 All models loaded successfully!')
"
```

---

### Bước 4: Chạy Bot Trên VPS

```bash
# Nếu test load models OK, chạy bot
python3 bot.py

# Hoặc chạy background
nohup python3 bot.py > bot.log 2>&1 &

# Hoặc dùng screen
screen -S farmaster
python3 bot.py
# Ctrl+A, D để detach
```

---

## 🔄 WORKFLOW TỰ ĐỘNG (Script)

### Cách 1: Dùng PowerShell Script (Windows - Dễ nhất)

```powershell
# 1. Mở file upload_models.ps1 và sửa cấu hình VPS
notepad upload_models.ps1

# Sửa dòng 6-7:
# $VPS_USER = "your-username"  → Thay bằng username VPS thật
# $VPS_HOST = "your-vps-ip"    → Thay bằng IP VPS thật

# 2. Chạy script
.\upload_models.ps1

# 3. Nhập "yes" để confirm upload
```

**Output mẫu:**
```
📤 UPLOAD MODELS TO VPS
======================================================================
🔍 Checking local models...
   ✅ lstm_model.pt              45.23 MB
   ✅ xgboost_model.json          2.15 MB
   ✅ lightgbm_model.txt          1.89 MB
   ✅ catboost_model.cbm          3.21 MB

✅ All 4 models found!

🔧 Checking VPS configuration...
   VPS User: farmaster
   VPS Host: 123.45.67.89
   VPS Path: /home/farmaster/farmaster/models
   SSH Port: 22

⚠️ READY TO UPLOAD
======================================================================
From: C:\LAINP\Augment\FarmAster\models
To:   farmaster@123.45.67.89:/home/farmaster/farmaster/models
Files: 4 models (~50 MB total)

❓ Continue? (yes/no): yes

📤 Uploading models to VPS...
======================================================================

📦 Uploading lstm_model.pt...
   ✅ lstm_model.pt uploaded successfully!

📦 Uploading xgboost_model.json...
   ✅ xgboost_model.json uploaded successfully!

📦 Uploading lightgbm_model.txt...
   ✅ lightgbm_model.txt uploaded successfully!

📦 Uploading catboost_model.cbm...
   ✅ catboost_model.cbm uploaded successfully!

======================================================================
📊 Upload Summary: 4/4 models uploaded

✅ UPLOAD COMPLETED SUCCESSFULLY!
======================================================================
🚀 Next steps on VPS:
   1. SSH to VPS: ssh farmaster@123.45.67.89
   2. Verify: ls -lh /home/farmaster/farmaster/models
   3. Run bot: python3 bot.py
======================================================================
```

### Cách 2: Dùng Python Script (Cross-platform)

```powershell
# 1. Mở file upload_models_to_vps.py và sửa cấu hình
notepad upload_models_to_vps.py

# Sửa dòng 12-14:
# VPS_USER = "your-username"  → Thay bằng username VPS thật
# VPS_HOST = "your-vps-ip"    → Thay bằng IP VPS thật
# VPS_PATH = "/home/farmaster/farmaster/models"

# 2. Chạy script
python upload_models_to_vps.py
```

---

## 🔐 SETUP SSH KEY (Khuyến Nghị)

Để không phải nhập password mỗi lần upload:

### Windows

```powershell
# 1. Tạo SSH key (nếu chưa có)
ssh-keygen -t rsa -b 4096

# 2. Copy public key lên VPS
type $env:USERPROFILE\.ssh\id_rsa.pub | ssh user@vps-ip "cat >> ~/.ssh/authorized_keys"

# 3. Test
ssh user@vps-ip
# Không cần password nữa!
```

### Linux/Mac

```bash
# 1. Tạo SSH key
ssh-keygen -t rsa -b 4096

# 2. Copy lên VPS
ssh-copy-id user@vps-ip

# 3. Test
ssh user@vps-ip
```

---

## 📊 SO SÁNH CÁC CÁCH

| Cách | Ưu Điểm | Nhược Điểm | Khuyến Nghị |
|------|---------|------------|-------------|
| **PowerShell Script** | ✅ Tự động<br>✅ Dễ dùng<br>✅ Có progress | ⚠️ Chỉ Windows | ⭐⭐⭐⭐⭐ |
| **Python Script** | ✅ Cross-platform<br>✅ Tự động verify | ⚠️ Cần Python | ⭐⭐⭐⭐ |
| **WinSCP GUI** | ✅ Trực quan<br>✅ Dễ dùng | ⚠️ Thủ công<br>⚠️ Cần cài app | ⭐⭐⭐⭐ |
| **SCP Manual** | ✅ Nhanh<br>✅ Không cần script | ⚠️ Phải gõ lệnh nhiều | ⭐⭐⭐ |
| **Git** | ✅ Version control | ❌ Chậm<br>❌ Không tối ưu | ⭐⭐ |

---

## ⚡ QUICK START (TL;DR)

```powershell
# 1. Train local
python scripts/auto_retrain.py --days 180

# 2. Sửa config trong upload_models.ps1
notepad upload_models.ps1

# 3. Upload
.\upload_models.ps1

# 4. SSH vào VPS và chạy bot
ssh user@vps-ip
cd /home/farmaster/farmaster
python3 bot.py
```

---

## 🐛 TROUBLESHOOTING

### Lỗi: "scp: command not found"

**Windows:**
```powershell
# Cài OpenSSH Client
Settings > Apps > Optional Features > Add "OpenSSH Client"

# Hoặc dùng WinSCP GUI
```

**Linux/Mac:**
```bash
# Ubuntu/Debian
sudo apt install openssh-client

# Mac
# Đã có sẵn
```

### Lỗi: "Permission denied"

```bash
# Kiểm tra SSH key
ssh user@vps-ip

# Nếu không được, setup lại SSH key
ssh-copy-id user@vps-ip
```

### Lỗi: "Connection refused"

```bash
# Kiểm tra VPS có bật SSH không
ssh -v user@vps-ip

# Kiểm tra firewall
# Đảm bảo port 22 mở
```

### Upload chậm

```bash
# Nén models trước khi upload
tar -czf models.tar.gz models/

# Upload file nén
scp models.tar.gz user@vps-ip:/home/farmaster/farmaster/

# SSH vào VPS và giải nén
ssh user@vps-ip
cd /home/farmaster/farmaster
tar -xzf models.tar.gz
rm models.tar.gz
```

---

## 💡 TIPS & BEST PRACTICES

### 1. Backup Models Cũ Trên VPS

```bash
# SSH vào VPS
ssh user@vps-ip

# Backup models cũ
cd /home/farmaster/farmaster
cp -r models models_backup_$(date +%Y%m%d)

# Hoặc
tar -czf models_backup_$(date +%Y%m%d).tar.gz models/
```

### 2. So Sánh Models Local vs VPS

```bash
# Local (Windows)
Get-FileHash models\lstm_model.pt -Algorithm MD5

# VPS
ssh user@vps-ip "md5sum /home/farmaster/farmaster/models/lstm_model.pt"

# Hash phải giống nhau
```

### 3. Upload Chỉ Models Thay Đổi

```powershell
# Chỉ upload LSTM nếu chỉ retrain LSTM
scp models/lstm_model.pt user@vps-ip:/home/farmaster/farmaster/models/
```

### 4. Tự Động Hóa Hoàn Toàn

Tạo file `train_and_deploy.ps1`:

```powershell
# Train
Write-Host "🧠 Training models..." -ForegroundColor Yellow
python scripts/auto_retrain.py --days 180

# Backtest
Write-Host "📊 Running backtest..." -ForegroundColor Yellow
python run_backtest_90days.py

# Confirm
$confirm = Read-Host "Deploy to VPS? (yes/no)"
if ($confirm -eq "yes") {
    # Upload
    Write-Host "📤 Uploading to VPS..." -ForegroundColor Yellow
    .\upload_models.ps1
}
```

---

## 📞 SUPPORT

Nếu gặp vấn đề:

1. **Kiểm tra SSH connection:**
   ```bash
   ssh user@vps-ip
   ```

2. **Kiểm tra models local:**
   ```bash
   ls -lh models/
   ```

3. **Test upload 1 file nhỏ:**
   ```bash
   echo "test" > test.txt
   scp test.txt user@vps-ip:/tmp/
   ```

4. **Xem log chi tiết:**
   ```bash
   scp -v models/lstm_model.pt user@vps-ip:/path/
   ```

---

**✅ Workflow này giúp bạn:**
- ⚡ Train nhanh hơn trên máy local
- 💰 Tiết kiệm CPU VPS
- 🔧 Dễ debug và monitor
- 📊 Test kỹ trước khi deploy

**Chúc bạn thành công! 🚀**

