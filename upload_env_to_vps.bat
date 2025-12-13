@echo off
REM Upload .env to VPS
REM Usage: Thay VPS_USER, VPS_HOST, VPS_PATH truoc khi chay

SET VPS_USER=root
SET VPS_HOST=your_vps_ip
SET VPS_PATH=/root/FarmAster

echo ============================================
echo UPLOADING .env TO VPS
echo ============================================
echo.
echo VPS: %VPS_USER%@%VPS_HOST%
echo Path: %VPS_PATH%
echo.

REM Upload .env
scp .env %VPS_USER%@%VPS_HOST%:%VPS_PATH%/.env

echo.
echo ============================================
echo UPLOAD COMPLETE!
echo ============================================
echo.
echo Next steps:
echo 1. SSH to VPS: ssh %VPS_USER%@%VPS_HOST%
echo 2. Restart bot: cd %VPS_PATH% ^&^& pkill -f bot.py ^&^& nohup python bot.py ^> bot.log 2^>^&1 ^&
echo 3. Check log: tail -f %VPS_PATH%/bot.log
echo.
pause
