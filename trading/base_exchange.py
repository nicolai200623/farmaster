# ============================================
# 🔌 BASE EXCHANGE CLIENT
# Abstract interface cho tất cả exchanges
# ============================================

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from utils.logger import logger


class BaseExchangeClient(ABC):
    """
    Base class cho tất cả exchange clients.
    Định nghĩa interface chung cho AsterDEX, Binance, và exchanges khác.
    """

    def __init__(self, api_key: str, api_secret: str, testnet: bool = False):
        """
        Initialize exchange client

        Args:
            api_key: API key
            api_secret: API secret
            testnet: Sử dụng testnet hay mainnet
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet
        self._symbol_info_cache = {}

        # Subclass sẽ implement client initialization
        self.client = None
        self.exchange_name = "BaseExchange"

    @abstractmethod
    def get_account_balance(self) -> float:
        """
        Lấy balance USDT trong futures account

        Returns:
            float: Số dư USDT
        """
        pass

    @abstractmethod
    def get_position(self, symbol: str) -> Optional[Dict[str, Any]]:
        """
        Lấy thông tin position hiện tại

        Args:
            symbol: Trading pair (e.g., 'BTCUSDT')

        Returns:
            dict hoặc None: {
                'side': 'LONG' | 'SHORT',
                'amount': float,
                'entry_price': float,
                'mark_price': float,
                'pnl_pct': float,  # PnL% (đã tính leverage)
                'pnl_usdt': float
            }
        """
        pass

    @abstractmethod
    def get_klines(self, symbol: str, interval: str = '1m', limit: int = 100) -> List[List]:
        """
        Lấy candlestick data

        Args:
            symbol: Trading pair
            interval: Timeframe ('1m', '5m', '1h', '4h', '1d', etc.)
            limit: Số lượng candles

        Returns:
            List of klines (OHLCV format)
        """
        pass

    @abstractmethod
    def get_orderbook(self, symbol: str, limit: int = 10) -> Dict[str, List]:
        """
        Lấy order book

        Args:
            symbol: Trading pair
            limit: Độ sâu order book

        Returns:
            dict: {'bids': [[price, qty], ...], 'asks': [[price, qty], ...]}
        """
        pass

    @abstractmethod
    def get_ticker_price(self, symbol: str) -> float:
        """
        Lấy giá hiện tại

        Args:
            symbol: Trading pair

        Returns:
            float: Current price
        """
        pass

    @abstractmethod
    def set_leverage(self, symbol: str, leverage: int) -> bool:
        """
        Đặt đòn bẩy cho symbol

        Args:
            symbol: Trading pair
            leverage: Đòn bẩy (1-125x)

        Returns:
            bool: True nếu thành công
        """
        pass

    @abstractmethod
    def set_margin_type(self, symbol: str, margin_type: str = 'ISOLATED') -> bool:
        """
        Đặt loại margin (ISOLATED hoặc CROSSED)

        Args:
            symbol: Trading pair
            margin_type: 'ISOLATED' hoặc 'CROSSED'

        Returns:
            bool: True nếu thành công
        """
        pass

    @abstractmethod
    def format_quantity(self, symbol: str, quantity: float) -> float:
        """
        Format quantity theo quy định của exchange (precision, step size)

        Args:
            symbol: Trading pair
            quantity: Số lượng chưa format

        Returns:
            float: Số lượng đã được format đúng
        """
        pass

    @abstractmethod
    def create_market_order(self, symbol: str, side: str, quantity: float,
                          reduce_only: bool = False) -> Optional[Dict]:
        """
        Tạo market order

        Args:
            symbol: Trading pair
            side: 'BUY' hoặc 'SELL'
            quantity: Số lượng
            reduce_only: True nếu đóng position

        Returns:
            dict hoặc None: Order info nếu thành công
        """
        pass

    @abstractmethod
    def close_position(self, symbol: str) -> bool:
        """
        Đóng toàn bộ position

        Args:
            symbol: Trading pair

        Returns:
            bool: True nếu thành công
        """
        pass

    @abstractmethod
    def _get_symbol_info(self, symbol: str) -> Optional[Dict]:
        """
        Lấy thông tin symbol từ exchange (precision, filters, etc.)
        Nên implement caching để tránh API calls không cần thiết

        Args:
            symbol: Trading pair

        Returns:
            dict hoặc None: Symbol info
        """
        pass

    def get_exchange_name(self) -> str:
        """Trả về tên exchange"""
        return self.exchange_name

    def is_testnet(self) -> bool:
        """Kiểm tra có đang dùng testnet không"""
        return self.testnet

    def log_connection_info(self):
        """Log thông tin kết nối (để subclass override)"""
        mode = "TESTNET" if self.testnet else "MAINNET"
        logger.info(f"🔌 {self.exchange_name} Client initialized ({mode})")
