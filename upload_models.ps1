# ============================================
# 📤 UPLOAD MODELS TO VPS (PowerShell)
# ============================================

# CẤU HÌNH VPS - SỬA PHẦN NÀY
$VPS_USER = "your-username"  # Thay bằng username VPS
$VPS_HOST = "your-vps-ip"    # Thay bằng IP VPS
$VPS_PATH = "/home/farmaster/farmaster/models"
$VPS_PORT = 22

# ============================================
# SCRIPT - KHÔNG CẦN SỬA
# ============================================

Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 69) -ForegroundColor Cyan
Write-Host "📤 UPLOAD MODELS TO VPS" -ForegroundColor Yellow
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 69) -ForegroundColor Cyan
Write-Host ""

# Check models exist
Write-Host "🔍 Checking local models..." -ForegroundColor Cyan
$models = @(
    "lstm_model.pt",
    "scaler.pkl",
    "xgboost_model.json",
    "xgboost_scaler.pkl",
    "lightgbm_model.txt",
    "lightgbm_scaler.pkl",
    "catboost_model.cbm",
    "catboost_scaler.pkl"
)

$allExist = $true
foreach ($model in $models) {
    $path = "models\$model"
    if (Test-Path $path) {
        $size = (Get-Item $path).Length / 1MB
        Write-Host "   ✅ $($model.PadRight(25)) $("{0:N2}" -f $size) MB" -ForegroundColor Green
    } else {
        Write-Host "   ❌ $model not found" -ForegroundColor Red
        $allExist = $false
    }
}

if (-not $allExist) {
    Write-Host ""
    Write-Host "❌ Please train models first:" -ForegroundColor Red
    Write-Host "   python scripts/auto_retrain.py --days 180" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "✅ All $($models.Count) models found!" -ForegroundColor Green

# Check VPS config
Write-Host ""
Write-Host "🔧 Checking VPS configuration..." -ForegroundColor Cyan

if ($VPS_USER -eq "your-username" -or $VPS_HOST -eq "your-vps-ip") {
    Write-Host "❌ Please configure VPS settings in this script:" -ForegroundColor Red
    Write-Host "   1. Open: upload_models.ps1" -ForegroundColor Yellow
    Write-Host "   2. Edit lines 6-7:" -ForegroundColor Yellow
    Write-Host "      `$VPS_USER = '$VPS_USER'  # Your VPS username" -ForegroundColor Yellow
    Write-Host "      `$VPS_HOST = '$VPS_HOST'  # Your VPS IP" -ForegroundColor Yellow
    exit 1
}

Write-Host "   VPS User: $VPS_USER" -ForegroundColor White
Write-Host "   VPS Host: $VPS_HOST" -ForegroundColor White
Write-Host "   VPS Path: $VPS_PATH" -ForegroundColor White
Write-Host "   SSH Port: $VPS_PORT" -ForegroundColor White

# Check SCP available
Write-Host ""
Write-Host "🔌 Checking SCP availability..." -ForegroundColor Cyan

try {
    $scpCheck = Get-Command scp -ErrorAction Stop
    Write-Host "   ✅ SCP found: $($scpCheck.Source)" -ForegroundColor Green
} catch {
    Write-Host "   ❌ SCP not found!" -ForegroundColor Red
    Write-Host ""
    Write-Host "💡 Please install OpenSSH Client:" -ForegroundColor Yellow
    Write-Host "   Settings > Apps > Optional Features > Add OpenSSH Client" -ForegroundColor Yellow
    Write-Host "   Or download: https://github.com/PowerShell/Win32-OpenSSH/releases" -ForegroundColor Yellow
    exit 1
}

# Confirm upload
Write-Host ""
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 69) -ForegroundColor Cyan
Write-Host "⚠️ READY TO UPLOAD" -ForegroundColor Yellow
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 69) -ForegroundColor Cyan
Write-Host "From: $(Get-Location)\models" -ForegroundColor White
Write-Host "To:   ${VPS_USER}@${VPS_HOST}:${VPS_PATH}" -ForegroundColor White
Write-Host "Files: $($models.Count) files (models + scalers)" -ForegroundColor White
Write-Host ""

$confirm = Read-Host "❓ Continue? (yes/no)"

if ($confirm -ne "yes" -and $confirm -ne "y") {
    Write-Host "❌ Upload cancelled" -ForegroundColor Red
    exit 0
}

# Upload models
Write-Host ""
Write-Host "📤 Uploading models to VPS..." -ForegroundColor Cyan
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 69) -ForegroundColor Cyan

$successCount = 0

foreach ($model in $models) {
    Write-Host ""
    Write-Host "📦 Uploading $model..." -ForegroundColor Yellow
    
    $localPath = "models\$model"
    $remotePath = "${VPS_USER}@${VPS_HOST}:${VPS_PATH}/$model"
    
    try {
        $result = scp -P $VPS_PORT $localPath $remotePath 2>&1
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "   ✅ $model uploaded successfully!" -ForegroundColor Green
            $successCount++
        } else {
            Write-Host "   ❌ Failed to upload $model" -ForegroundColor Red
            Write-Host "   Error: $result" -ForegroundColor Red
        }
    } catch {
        Write-Host "   ❌ Error: $_" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 69) -ForegroundColor Cyan
Write-Host "📊 Upload Summary: $successCount/$($models.Count) models uploaded" -ForegroundColor Yellow

if ($successCount -eq $models.Count) {
    Write-Host ""
    Write-Host "=" -NoNewline -ForegroundColor Green
    Write-Host ("=" * 69) -ForegroundColor Green
    Write-Host "✅ UPLOAD COMPLETED SUCCESSFULLY!" -ForegroundColor Green
    Write-Host "=" -NoNewline -ForegroundColor Green
    Write-Host ("=" * 69) -ForegroundColor Green
    Write-Host ""
    Write-Host "🚀 Next steps on VPS:" -ForegroundColor Yellow
    Write-Host "   1. SSH to VPS: ssh ${VPS_USER}@${VPS_HOST}" -ForegroundColor White
    Write-Host "   2. Verify: ls -lh $VPS_PATH" -ForegroundColor White
    Write-Host "   3. Run bot: python3 bot.py" -ForegroundColor White
    Write-Host "=" -NoNewline -ForegroundColor Green
    Write-Host ("=" * 69) -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "❌ Upload incomplete!" -ForegroundColor Red
    Write-Host "   Please check errors above and try again" -ForegroundColor Yellow
    exit 1
}

