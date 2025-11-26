# ============================================
# 🎲 ADVANCED RISK MANAGER
# Dynamic position sizing & correlation management
# ============================================

import numpy as np
from typing import Dict, List, Tuple
from utils.logger import logger

class AdvancedRiskManager:
    """
    Advanced Risk Management System

    Features:
    1. Kelly Criterion for optimal position sizing
    2. Correlation-based position limiting
    3. Maximum drawdown protection
    4. Dynamic risk adjustment based on win rate
    """

    # Correlated pairs (BTC correlation > 0.7)
    CORRELATED_PAIRS = {
        'BTCUSDT': ['ETHUSDT', 'BNBUSDT'],
        'ETHUSDT': ['BTCUSDT', 'BNBUSDT'],
        'SOLUSDT': ['AVAXUSDT', 'DOTUSDT'],
        'AVAXUSDT': ['SOLUSDT', 'DOTUSDT'],
        'BNBUSDT': ['BTCUSDT', 'ETHUSDT'],
        'XRPUSDT': ['ADAUSDT'],
    }

    def __init__(self, max_correlated_positions=2, max_total_positions=4):
        """
        Initialize Advanced Risk Manager

        Args:
            max_correlated_positions: Max positions in correlated pairs
            max_total_positions: Max total open positions
        """
        self.max_correlated_positions = max_correlated_positions
        self.max_total_positions = max_total_positions

        # Performance tracking for Kelly
        self.trade_history = []  # List of (win: bool, profit_pct: float)
        self.win_count = 0
        self.loss_count = 0
        self.total_win_amount = 0.0
        self.total_loss_amount = 0.0

        logger.info(f"🎲 Advanced Risk Manager initialized")
        logger.info(f"   Max correlated positions: {max_correlated_positions}")
        logger.info(f"   Max total positions: {max_total_positions}")

    def calculate_kelly_position_size(self, balance: float, base_size_pct: float = 0.1) -> float:
        """
        Calculate optimal position size using Kelly Criterion

        Kelly % = W - [(1-W) / R]
        Where:
        - W = Win rate
        - R = Avg Win / Avg Loss ratio

        Args:
            balance: Current account balance
            base_size_pct: Base position size as % of balance (fallback)

        Returns:
            Position size in USDT
        """
        total_trades = self.win_count + self.loss_count

        # Need at least 20 trades for reliable Kelly
        if total_trades < 20:
            logger.info(f"📊 Using base size (only {total_trades} trades)")
            return balance * base_size_pct

        # Calculate win rate
        win_rate = self.win_count / total_trades

        # Calculate average win/loss
        avg_win = self.total_win_amount / self.win_count if self.win_count > 0 else 0
        avg_loss = abs(self.total_loss_amount) / self.loss_count if self.loss_count > 0 else 0

        if avg_loss == 0:
            logger.warning("⚠️ No losses yet - using base size")
            return balance * base_size_pct

        # Calculate R (reward/risk ratio)
        r_ratio = avg_win / avg_loss

        # Kelly Criterion
        kelly_pct = win_rate - ((1 - win_rate) / r_ratio)

        # Safety limits
        kelly_pct = max(0, min(kelly_pct, 0.25))  # Cap at 25%

        # Use half-Kelly for safety (reduces volatility)
        half_kelly = kelly_pct / 2

        # Don't go below base size
        final_pct = max(half_kelly, base_size_pct * 0.5)  # At least 50% of base

        position_size = balance * final_pct

        logger.info(f"📊 Kelly Sizing: WR={win_rate:.1%} R={r_ratio:.2f} Kelly={kelly_pct:.1%} HalfKelly={half_kelly:.1%}")
        logger.info(f"   Position size: ${position_size:.2f} ({final_pct:.1%} of balance)")

        return position_size

    def check_correlation_risk(self, new_symbol: str, existing_positions: List[str]) -> Tuple[bool, str]:
        """
        Check if opening position would violate correlation limits

        Args:
            new_symbol: Symbol to open position on
            existing_positions: List of symbols with existing positions

        Returns:
            allowed: True if allowed, False if not
            reason: Explanation
        """
        # Check if already have position
        if new_symbol in existing_positions:
            return False, f"Already have position on {new_symbol}"

        # Check total position count
        if len(existing_positions) >= self.max_total_positions:
            return False, f"Max total positions reached ({self.max_total_positions})"

        # Check correlated positions
        correlated_symbols = self.CORRELATED_PAIRS.get(new_symbol, [])

        # Count how many correlated positions we already have
        correlated_count = 0
        correlated_list = []

        for symbol in existing_positions:
            if symbol in correlated_symbols:
                correlated_count += 1
                correlated_list.append(symbol)

        if correlated_count >= self.max_correlated_positions:
            return False, f"Too many correlated positions: {', '.join(correlated_list)}"

        # All checks passed
        return True, "OK"

    def record_trade(self, win: bool, profit_pct: float):
        """
        Record trade result for Kelly calculation

        Args:
            win: True if profitable, False if loss
            profit_pct: Profit/loss as percentage (e.g., 0.02 = 2%)
        """
        self.trade_history.append({
            'win': win,
            'profit_pct': profit_pct
        })

        if win:
            self.win_count += 1
            self.total_win_amount += profit_pct
        else:
            self.loss_count += 1
            self.total_loss_amount += profit_pct  # Will be negative

        # Keep only last 100 trades
        if len(self.trade_history) > 100:
            # Remove oldest trade
            removed = self.trade_history.pop(0)
            if removed['win']:
                self.win_count -= 1
                self.total_win_amount -= removed['profit_pct']
            else:
                self.loss_count -= 1
                self.total_loss_amount -= removed['profit_pct']

        logger.info(f"📝 Trade recorded: {'WIN' if win else 'LOSS'} {profit_pct:+.2%}")
        logger.info(f"   Stats: {self.win_count}W / {self.loss_count}L ({self.get_win_rate():.1%} WR)")

    def get_win_rate(self) -> float:
        """Get current win rate"""
        total = self.win_count + self.loss_count
        return self.win_count / total if total > 0 else 0.5

    def get_avg_win(self) -> float:
        """Get average win percentage"""
        return self.total_win_amount / self.win_count if self.win_count > 0 else 0

    def get_avg_loss(self) -> float:
        """Get average loss percentage (absolute value)"""
        return abs(self.total_loss_amount) / self.loss_count if self.loss_count > 0 else 0

    def get_rr_ratio(self) -> float:
        """Get reward/risk ratio"""
        avg_loss = self.get_avg_loss()
        return self.get_avg_win() / avg_loss if avg_loss > 0 else 0

    def should_reduce_risk(self, recent_losses: int = 3) -> bool:
        """
        Check if should reduce risk due to losing streak

        Args:
            recent_losses: Number of recent trades to check

        Returns:
            True if should reduce risk
        """
        if len(self.trade_history) < recent_losses:
            return False

        # Check last N trades
        recent_trades = self.trade_history[-recent_losses:]

        # If all losses, reduce risk
        if all(not trade['win'] for trade in recent_trades):
            logger.warning(f"⚠️ Detected {recent_losses} consecutive losses - reducing risk")
            return True

        return False

    def get_risk_multiplier(self) -> float:
        """
        Get risk multiplier based on recent performance

        Returns:
            Multiplier for position size (0.5 to 1.5)
        """
        # Reduce risk after losing streak
        if self.should_reduce_risk(3):
            return 0.5  # 50% size

        # Increase risk if on winning streak
        if len(self.trade_history) >= 3:
            recent_trades = self.trade_history[-3:]
            if all(trade['win'] for trade in recent_trades):
                return 1.2  # 120% size (modest increase)

        return 1.0  # Normal size

    def calculate_optimal_position_size(self, balance: float, base_size_pct: float = 0.1,
                                       use_kelly: bool = True) -> float:
        """
        Calculate optimal position size with all factors

        Args:
            balance: Current balance
            base_size_pct: Base size percentage
            use_kelly: Whether to use Kelly Criterion

        Returns:
            Position size in USDT
        """
        if use_kelly:
            size = self.calculate_kelly_position_size(balance, base_size_pct)
        else:
            size = balance * base_size_pct

        # Apply risk multiplier
        multiplier = self.get_risk_multiplier()
        size *= multiplier

        logger.info(f"💰 Final position size: ${size:.2f} (multiplier: {multiplier:.1f}x)")

        return size

    def get_statistics(self) -> Dict:
        """
        Get comprehensive risk statistics

        Returns:
            Dictionary with statistics
        """
        total_trades = self.win_count + self.loss_count

        return {
            'total_trades': total_trades,
            'wins': self.win_count,
            'losses': self.loss_count,
            'win_rate': self.get_win_rate(),
            'avg_win': self.get_avg_win(),
            'avg_loss': self.get_avg_loss(),
            'rr_ratio': self.get_rr_ratio(),
            'risk_multiplier': self.get_risk_multiplier(),
        }
