# ============================================
# 🚀 ASTERDEX PERP FARM BOT - MAIN
# Stage 3 - Full Production Bot
# ============================================

import os
import sys
# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import time
from datetime import datetime
import signal

from config import Config
from utils.logger import logger
from trading.asterdex_client import AsterDEXClient
from trading.signal_generator import SignalGenerator
from trading.risk_manager import RiskManager
from trading.position_tracker import PositionTracker
from ml.lstm_model import LSTMTrainer
from ml.ensemble import EnsemblePredictor
from ml.features import FeatureEngine

class AsterDEXBot:
    """Main trading bot"""

    def __init__(self):
        logger.info("=" * 60)
        logger.info("🚀 ASTERDEX PERP FARM BOT - INITIALIZING")
        logger.info("=" * 60)

        # Validate config
        Config.validate()

        # Initialize components
        self.client = AsterDEXClient()
        self.risk_manager = RiskManager()
        self.position_tracker = PositionTracker()

        # Load ML models
        if Config.USE_ENSEMBLE:
            logger.info("🎭 Loading Ensemble models...")
            self.predictor = EnsemblePredictor(
                models=Config.ENSEMBLE_MODELS,
                weights=Config.ENSEMBLE_WEIGHTS,
                input_size=len(FeatureEngine.FEATURE_COLUMNS)
            )

            if not self.predictor.load_models():
                logger.error("❌ Ensemble models chưa được train! Chạy ml/train_ensemble.py trước.")
                sys.exit(1)
        else:
            logger.info("🧠 Loading LSTM model...")
            self.predictor = LSTMTrainer(input_size=len(FeatureEngine.FEATURE_COLUMNS))

            if not self.predictor.load():
                logger.error("❌ LSTM model chưa được train! Chạy ml/train.py trước.")
                sys.exit(1)

        self.signal_generator = SignalGenerator(self.predictor)
        
        # State
        self.running = True
        self.loop_count = 0
        
        # Setup signal handlers
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        
        logger.info("✅ Bot initialized successfully!")
        logger.info(f"   Symbols: {Config.SYMBOLS}")
        logger.info(f"   Leverage: {Config.LEVERAGE}x")
        logger.info(f"   Position Size: {Config.SIZE_PCT*100}%")
        logger.info(f"   TP/SL: {Config.TP_PCT*100}% / {Config.SL_PCT*100}%")
        logger.info(f"   Position Timeout: {Config.POSITION_TIMEOUT_HOURS}h")
        logger.info("=" * 60)
    
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        logger.info("\n🛑 Shutdown signal received...")
        self.running = False
    
    def start(self):
        """Bắt đầu bot"""
        logger.info("🏁 BOT STARTED!", send_tg=True)
        
        # Get initial balance
        balance = self.client.get_account_balance()
        self.risk_manager.set_daily_start(balance)
        
        logger.info(f"💰 Starting balance: ${balance:.2f}", send_tg=True)
        
        # Main loop
        while self.running:
            try:
                self.loop_count += 1
                logger.info(f"\n{'='*60}")
                logger.info(f"🔄 LOOP #{self.loop_count} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                logger.info(f"{'='*60}")
                
                # Get current balance
                current_balance = self.client.get_account_balance()
                
                # Check if can trade
                can_trade, reason = self.risk_manager.should_trade(current_balance)
                
                if not can_trade:
                    logger.warning(f"⚠️ Cannot trade: {reason}", send_tg=True)
                    break
                
                # Process each symbol (with small delay to avoid rate limiting)
                for i, symbol in enumerate(Config.SYMBOLS):
                    self._process_symbol(symbol, current_balance)

                    # Small delay between symbols (except last one)
                    if i < len(Config.SYMBOLS) - 1:
                        time.sleep(0.5)  # 500ms delay

                # Cleanup stale position tracking (every 10 loops)
                if self.loop_count % 10 == 0:
                    active_symbols = [s for s in Config.SYMBOLS if self.client.get_position(s) is not None]
                    self.position_tracker.cleanup_stale_positions(active_symbols)

                # Daily reset check (00:00)
                if datetime.now().hour == 0 and datetime.now().minute < 1:
                    self._daily_reset()
                
                # Sleep
                logger.info(f"\n💤 Sleeping {Config.LOOP_SLEEP}s...")
                time.sleep(Config.LOOP_SLEEP)
                
            except KeyboardInterrupt:
                logger.info("\n⌨️ Keyboard interrupt...")
                break
            except Exception as e:
                logger.error(f"Loop error: {e}")
                time.sleep(60)
        
        # Shutdown
        self._shutdown()
    
    def _process_symbol(self, symbol, current_balance):
        """Xử lý 1 symbol"""
        logger.info(f"\n📊 Processing {symbol}...")
        
        try:
            # Check current position
            position = self.client.get_position(symbol)
            
            if position:
                # Get position age
                position_age_hours = self.position_tracker.get_position_age_hours(symbol)

                logger.info(f"   Current position: {position['side']} {position['amount']}")
                logger.info(f"   Entry: ${position['entry_price']:.2f} | Mark: ${position['mark_price']:.2f}")
                logger.info(f"   PnL: {position['pnl_pct']*100:.2f}% (${position['pnl_usdt']:.2f})")

                if position_age_hours is not None:
                    logger.info(f"   Age: {position_age_hours:.1f}h / {Config.POSITION_TIMEOUT_HOURS}h")

                # Check if should close (including timeout check)
                should_close, reason = self.signal_generator.should_close_position(
                    position,
                    position_age_hours=position_age_hours
                )

                if should_close:
                    logger.info(f"   🔴 Closing position: {reason}")

                    if self.client.close_position(symbol):
                        logger.trade(f"CLOSE {position['side']} {symbol} | {reason} | PnL: {position['pnl_pct']*100:.2f}%")

                        # Clear position tracking
                        self.position_tracker.clear_position(symbol)

                        # Record trade
                        self.risk_manager.record_trade(
                            symbol=symbol,
                            side=f"CLOSE_{position['side']}",
                            quantity=position['amount'],
                            price=position['mark_price'],
                            pnl_pct=position['pnl_pct']
                        )
            
            else:
                # No position - check for entry signal
                signal_result = self.signal_generator.generate_signal(self.client, symbol)

                # Handle both advanced (tuple) and legacy (str) return types
                if Config.USE_ADVANCED_ENTRY:
                    signal, confluence_score, reasons = signal_result
                else:
                    signal = signal_result
                    confluence_score = 0
                    reasons = []

                if signal != 'HOLD':
                    logger.info(f"   🟢 Entry signal: {signal}")
                    if Config.USE_ADVANCED_ENTRY:
                        logger.info(f"   📊 Confluence: {confluence_score}")
                        logger.info(f"   📝 Reasons: {', '.join(reasons[:3])}")

                    # Setup leverage and margin
                    self.client.set_leverage(symbol, Config.LEVERAGE)
                    self.client.set_margin_type(symbol, 'ISOLATED')

                    # Get price
                    price = self.client.get_ticker_price(symbol)

                    # Calculate position size
                    raw_quantity = self.risk_manager.calculate_position_size(
                        current_balance, price, Config.LEVERAGE
                    )

                    # Format quantity according to exchange rules
                    quantity = self.client.format_quantity(symbol, raw_quantity)

                    # Log calculation details
                    logger.info(f"💰 Position calculation for {symbol}:")
                    logger.info(f"   Balance: ${current_balance:.2f}")
                    logger.info(f"   Price: ${price:.2f}")

                    if Config.POSITION_SIZE_USDT is not None:
                        logger.info(f"   Capital (fixed): ${Config.POSITION_SIZE_USDT:.2f}")
                    else:
                        logger.info(f"   Capital ({Config.SIZE_PCT*100}%): ${current_balance * Config.SIZE_PCT:.2f}")

                    logger.info(f"   Leverage: {Config.LEVERAGE}x")
                    logger.info(f"   Raw quantity: {raw_quantity:.8f}")
                    logger.info(f"   Formatted quantity: {quantity:.8f}")

                    # Check minimum quantity
                    if quantity > 0:
                        # Determine side
                        side = 'BUY' if signal == 'LONG' else 'SELL'

                        # Create order
                        order = self.client.create_market_order(
                            symbol=symbol,
                            side=side,
                            quantity=quantity
                        )

                        if order:
                            # Log trade with confluence info if available
                            if Config.USE_ADVANCED_ENTRY:
                                logger.trade(f"OPEN {signal} {symbol} | Qty: {quantity} | Price: ${price:.2f} | Score: {confluence_score} | {reasons[0] if reasons else ''}")
                            else:
                                logger.trade(f"OPEN {signal} {symbol} | Qty: {quantity} | Price: ${price:.2f}")

                            # Track position opening time
                            self.position_tracker.track_position_open(symbol)

                            # Record trade
                            self.risk_manager.record_trade(
                                symbol=symbol,
                                side=signal,
                                quantity=quantity,
                                price=price
                            )
                    else:
                        # Quantity too small
                        logger.warning(f"⚠️ Quantity too small ({quantity}), skipping {symbol}")
                        logger.warning(f"   Minimum notional value may not be met")
                        logger.warning(f"   Try increasing balance or SIZE_PCT")
                else:
                    logger.info(f"   ⚪ No signal - HOLD")
        
        except Exception as e:
            logger.error(f"Error processing {symbol}: {e}")
    
    def _daily_reset(self):
        """Reset daily stats"""
        logger.info("\n🌅 DAILY RESET")
        
        # Send daily report
        stats_msg = self.risk_manager.get_stats_message()
        logger.info(stats_msg, send_tg=True)
        
        # Reset
        balance = self.client.get_account_balance()
        self.risk_manager.set_daily_start(balance)
    
    def _shutdown(self):
        """Shutdown bot"""
        logger.info("\n" + "=" * 60)
        logger.info("🛑 SHUTTING DOWN BOT")
        logger.info("=" * 60)
        
        # Close all positions (optional)
        # for symbol in Config.SYMBOLS:
        #     self.client.close_position(symbol)
        
        # Final stats
        stats_msg = self.risk_manager.get_stats_message()
        logger.info(stats_msg, send_tg=True)
        
        logger.info("👋 Bot stopped!", send_tg=True)

def main():
    """Main entry point"""
    # Create necessary directories
    os.makedirs('logs', exist_ok=True)
    os.makedirs('models', exist_ok=True)
    os.makedirs('data', exist_ok=True)

    # Start bot
    bot = AsterDEXBot()
    bot.start()

if __name__ == '__main__':
    main()

