#!/usr/bin/env python3
# ============================================
# 🔴 CLOSE ALL POSITIONS
# Emergency close tất cả positions
# ============================================

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config
from trading.asterdex_client import AsterDEXClient
from utils.logger import logger

def main():
    """Close all positions"""
    Config.validate()
    
    client = AsterDEXClient()
    
    logger.info("=" * 60)
    logger.info("🔴 CLOSING ALL POSITIONS")
    logger.info("=" * 60)
    
    # Confirm
    response = input("\n⚠️  Are you sure? (yes/no): ")
    
    if response.lower() != 'yes':
        logger.info("❌ Cancelled")
        return
    
    # Close all
    closed_count = 0
    
    for symbol in Config.SYMBOLS:
        pos = client.get_position(symbol)
        
        if pos:
            logger.info(f"\n📊 Closing {symbol}...")
            logger.info(f"   {pos['side']} {pos['amount']} @ ${pos['mark_price']:.2f}")
            logger.info(f"   PnL: {pos['pnl_pct']*100:.2f}%")
            
            if client.close_position(symbol):
                logger.info(f"   ✅ Closed!")
                closed_count += 1
            else:
                logger.error(f"   ❌ Failed to close!")
    
    logger.info(f"\n✅ Closed {closed_count} positions")
    logger.info("=" * 60)

if __name__ == '__main__':
    main()

