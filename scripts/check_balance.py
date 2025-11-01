#!/usr/bin/env python3
# ============================================
# 💰 CHECK BALANCE
# Kiểm tra balance và positions
# ============================================

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config
from trading.asterdex_client import AsterDEXClient
from utils.logger import logger

def main():
    """Check balance và positions"""
    Config.validate()
    
    client = AsterDEXClient()
    
    logger.info("=" * 60)
    logger.info("💰 ACCOUNT STATUS")
    logger.info("=" * 60)
    
    # Balance
    balance = client.get_account_balance()
    logger.info(f"\n💵 USDT Balance: ${balance:.2f}")
    
    # Positions
    logger.info(f"\n📊 POSITIONS:")
    has_position = False
    
    for symbol in Config.SYMBOLS:
        pos = client.get_position(symbol)
        
        if pos:
            has_position = True
            logger.info(f"\n{symbol}:")
            logger.info(f"  Side: {pos['side']}")
            logger.info(f"  Amount: {pos['amount']}")
            logger.info(f"  Entry: ${pos['entry_price']:.2f}")
            logger.info(f"  Mark: ${pos['mark_price']:.2f}")
            logger.info(f"  PnL: {pos['pnl_pct']*100:.2f}% (${pos['pnl_usdt']:.2f})")
    
    if not has_position:
        logger.info("  No open positions")
    
    logger.info("\n" + "=" * 60)

if __name__ == '__main__':
    main()

