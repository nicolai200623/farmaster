# ============================================
# 📝 LOGGING & TELEGRAM NOTIFICATION
# ============================================

import logging
import sys
from datetime import datetime
from telegram import Bot
from telegram.error import TelegramError
from config import Config

class Logger:
    """Logger với Telegram integration"""

    def __init__(self):
        # Setup file logging with UTF-8 encoding for Windows
        file_handler = logging.FileHandler(
            f'logs/bot_{datetime.now().strftime("%Y%m%d")}.log',
            encoding='utf-8'
        )

        # Setup console handler with UTF-8 encoding
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setStream(open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1))

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            handlers=[file_handler, console_handler]
        )
        self.logger = logging.getLogger(__name__)
        
        # Telegram bot
        self.tg_bot = None
        if Config.TELEGRAM_TOKEN and Config.TELEGRAM_CHAT_ID:
            try:
                self.tg_bot = Bot(token=Config.TELEGRAM_TOKEN)
                self.logger.info("✅ Telegram bot initialized")
            except Exception as e:
                self.logger.warning(f"⚠️ Telegram bot init failed: {e}")
    
    def info(self, msg, send_tg=False):
        """Log info message"""
        self.logger.info(msg)
        if send_tg:
            self._send_telegram(msg)
    
    def warning(self, msg, send_tg=True):
        """Log warning"""
        self.logger.warning(msg)
        if send_tg:
            self._send_telegram(f"⚠️ {msg}")
    
    def error(self, msg, send_tg=True):
        """Log error"""
        self.logger.error(msg)
        if send_tg:
            self._send_telegram(f"❌ {msg}")
    
    def trade(self, msg):
        """Log trade với Telegram"""
        self.logger.info(f"💰 TRADE: {msg}")
        self._send_telegram(f"💰 {msg}")
    
    def _send_telegram(self, msg):
        """Gửi message qua Telegram"""
        if not self.tg_bot:
            return
        
        try:
            self.tg_bot.send_message(
                chat_id=Config.TELEGRAM_CHAT_ID,
                text=msg,
                parse_mode='HTML'
            )
        except TelegramError as e:
            self.logger.error(f"Telegram send failed: {e}")

# Global logger instance
logger = Logger()

