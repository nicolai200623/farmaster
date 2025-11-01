# ============================================
# 🛡️ RISK MANAGER
# Quản lý rủi ro và position sizing
# ============================================

from config import Config
from utils.logger import logger

class RiskManager:
    """Quản lý rủi ro trading"""
    
    def __init__(self):
        self.daily_start_balance = 0
        self.daily_trades = 0
        self.daily_volume = 0
        self.daily_pnl = 0
        self.total_trades = 0
        self.winning_trades = 0
        self.losing_trades = 0
    
    def set_daily_start(self, balance):
        """Set balance đầu ngày"""
        self.daily_start_balance = balance
        self.daily_trades = 0
        self.daily_volume = 0
        self.daily_pnl = 0
        logger.info(f"📊 Daily start balance: ${balance:.2f}")
    
    def check_daily_loss_limit(self, current_balance):
        """
        Kiểm tra daily loss limit
        
        Returns:
            tuple: (exceeded: bool, pnl_pct: float)
        """
        if self.daily_start_balance == 0:
            return False, 0
        
        pnl_pct = (current_balance - self.daily_start_balance) / self.daily_start_balance
        
        if pnl_pct < -Config.DAILY_LOSS_LIMIT:
            logger.error(f"🛑 DAILY LOSS LIMIT EXCEEDED: {pnl_pct*100:.2f}%")
            return True, pnl_pct
        
        return False, pnl_pct
    
    def calculate_position_size(self, balance, price, leverage=None):
        """
        Tính position size
        
        Args:
            balance: USDT balance
            price: Giá hiện tại
            leverage: Đòn bẩy
            
        Returns:
            float: Quantity to trade
        """
        leverage = leverage or Config.LEVERAGE
        
        # Capital cho trade này
        capital = balance * Config.SIZE_PCT
        
        # Quantity = capital / price (đã tính leverage)
        quantity = (capital * leverage) / price
        
        return quantity
    
    def round_quantity(self, quantity, symbol):
        """
        Làm tròn quantity theo quy định của exchange
        
        Args:
            quantity: Raw quantity
            symbol: Trading pair
            
        Returns:
            float: Rounded quantity
        """
        # Binance/AsterDEX thường yêu cầu 3 chữ số thập phân cho BTC/ETH
        if 'BTC' in symbol:
            return round(quantity, 3)
        elif 'ETH' in symbol:
            return round(quantity, 2)
        else:
            return round(quantity, 1)
    
    def record_trade(self, symbol, side, quantity, price, pnl_pct=None):
        """Ghi nhận trade"""
        self.daily_trades += 1
        self.total_trades += 1
        
        # Volume
        volume = quantity * price * Config.LEVERAGE
        self.daily_volume += volume
        
        # PnL tracking
        if pnl_pct is not None:
            if pnl_pct > 0:
                self.winning_trades += 1
            else:
                self.losing_trades += 1
        
        logger.info(f"📝 Trade recorded: {side} {quantity} {symbol} @ ${price:.2f}")
        logger.info(f"   Daily trades: {self.daily_trades} | Volume: ${self.daily_volume/1000:.1f}k")
    
    def get_daily_stats(self):
        """Lấy stats trong ngày"""
        win_rate = 0
        if self.total_trades > 0:
            win_rate = self.winning_trades / self.total_trades * 100
        
        return {
            'trades': self.daily_trades,
            'volume': self.daily_volume,
            'pnl': self.daily_pnl,
            'total_trades': self.total_trades,
            'win_rate': win_rate,
            'winning_trades': self.winning_trades,
            'losing_trades': self.losing_trades
        }
    
    def get_stats_message(self):
        """Tạo message stats"""
        stats = self.get_daily_stats()
        
        msg = f"""
📊 <b>DAILY STATS</b>
━━━━━━━━━━━━━━━━
Trades: {stats['trades']}
Volume: ${stats['volume']/1e6:.2f}M
PnL: {stats['pnl']:.2f}%

<b>Overall</b>
Total Trades: {stats['total_trades']}
Win Rate: {stats['win_rate']:.1f}%
W/L: {stats['winning_trades']}/{stats['losing_trades']}
        """.strip()
        
        return msg
    
    def should_trade(self, current_balance):
        """
        Kiểm tra có nên trade không
        
        Returns:
            tuple: (can_trade: bool, reason: str)
        """
        # Check daily loss limit
        exceeded, pnl_pct = self.check_daily_loss_limit(current_balance)
        if exceeded:
            return False, f"Daily loss limit exceeded ({pnl_pct*100:.2f}%)"
        
        # Check minimum balance
        if current_balance < 10:
            return False, "Balance too low (<$10)"
        
        return True, ""

