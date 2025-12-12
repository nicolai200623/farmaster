# ============================================
# 🔌 BINANCE CLIENT
# Official Binance Futures client
# ============================================

from binance.client import Client
from binance.exceptions import BinanceAPIException
import time
from config import Config
from utils.logger import logger
from trading.base_exchange import BaseExchangeClient


class BinanceClient(BaseExchangeClient):
    """
    Binance Futures Client
    Kết nối trực tiếp tới Binance Futures API
    """

    # Binance Futures URLs
    MAINNET_URL = 'https://fapi.binance.com'
    TESTNET_URL = 'https://testnet.binancefuture.com'

    def __init__(self, api_key=None, api_secret=None, testnet=None):
        # Get credentials (sử dụng BINANCE_ prefix)
        api_key = api_key or Config.BINANCE_API_KEY
        api_secret = api_secret or Config.BINANCE_API_SECRET
        testnet = testnet if testnet is not None else Config.BINANCE_TESTNET_MODE

        # Initialize base class
        super().__init__(api_key, api_secret, testnet)

        # Set exchange name
        self.exchange_name = "Binance"

        # Initialize Binance client
        self.client = Client(self.api_key, self.api_secret)

        # Set correct URL
        base_url = self.TESTNET_URL if self.testnet else self.MAINNET_URL
        if self.testnet:
            self.client.FUTURES_URL = base_url

        # Log connection info
        mode = "TESTNET" if self.testnet else "MAINNET"
        logger.info(f"🔌 Binance Client initialized ({mode})")
        logger.info(f"   URL: {base_url}")

    def get_account_balance(self):
        """Lấy balance USDT"""
        try:
            balances = self.client.futures_account_balance()
            usdt_balance = next((b for b in balances if b['asset'] == 'USDT'), None)

            if usdt_balance:
                return float(usdt_balance['balance'])
            return 0.0

        except BinanceAPIException as e:
            logger.error(f"[{self.exchange_name}] Get balance error: {e}")
            return 0.0

    def get_position(self, symbol):
        """
        Lấy thông tin position

        Returns:
            dict hoặc None: {
                'side': 'LONG' | 'SHORT',
                'amount': float,
                'entry_price': float,
                'mark_price': float,
                'pnl_pct': float,
                'pnl_usdt': float
            }
        """
        try:
            positions = self.client.futures_position_information(symbol=symbol)

            for pos in positions:
                amt = float(pos['positionAmt'])

                if amt != 0:
                    entry_price = float(pos['entryPrice'])
                    mark_price = float(pos['markPrice'])
                    unrealized_pnl = float(pos['unRealizedProfit'])

                    # Get leverage for this symbol
                    leverage = int(pos.get('leverage', Config.BINANCE_LEVERAGE))

                    # Calculate PnL % (WITH LEVERAGE for actual PnL)
                    if amt > 0:  # LONG
                        price_change_pct = (mark_price - entry_price) / entry_price
                        side = 'LONG'
                    else:  # SHORT
                        price_change_pct = (entry_price - mark_price) / entry_price
                        side = 'SHORT'

                    # PnL% = Price Change% * Leverage
                    pnl_pct = price_change_pct * leverage

                    return {
                        'side': side,
                        'amount': abs(amt),
                        'entry_price': entry_price,
                        'mark_price': mark_price,
                        'pnl_pct': pnl_pct,  # Includes leverage effect
                        'pnl_usdt': unrealized_pnl
                    }

            return None

        except BinanceAPIException as e:
            logger.error(f"[{self.exchange_name}] Get position error: {e}")
            return None

    def get_klines(self, symbol, interval='1m', limit=100):
        """Lấy candlestick data"""
        try:
            klines = self.client.futures_klines(
                symbol=symbol,
                interval=interval,
                limit=limit
            )
            return klines
        except BinanceAPIException as e:
            logger.error(f"[{self.exchange_name}] Get klines error: {e}")
            return []

    def get_orderbook(self, symbol, limit=10):
        """Lấy order book"""
        try:
            orderbook = self.client.futures_order_book(symbol=symbol, limit=limit)
            return orderbook
        except BinanceAPIException as e:
            # Symbol unavailable (skip silently)
            if e.code == -1121 or e.code == -4108:
                logger.warning(f"[{self.exchange_name}] Symbol {symbol} temporarily unavailable, skipping...")
            else:
                logger.error(f"[{self.exchange_name}] Get orderbook error: {e}")
            return {'bids': [], 'asks': []}

    def get_ticker_price(self, symbol):
        """Lấy giá hiện tại"""
        try:
            ticker = self.client.futures_symbol_ticker(symbol=symbol)
            return float(ticker['price'])
        except BinanceAPIException as e:
            logger.error(f"[{self.exchange_name}] Get ticker error: {e}")
            return 0.0

    def set_leverage(self, symbol, leverage):
        """Set leverage"""
        try:
            self.client.futures_change_leverage(symbol=symbol, leverage=leverage)
            logger.info(f"✅ [{self.exchange_name}] Set leverage {leverage}x for {symbol}")
            return True
        except BinanceAPIException as e:
            logger.error(f"[{self.exchange_name}] Set leverage error: {e}")
            return False

    def set_margin_type(self, symbol, margin_type='ISOLATED'):
        """Set margin type"""
        try:
            self.client.futures_change_margin_type(symbol=symbol, marginType=margin_type)
            logger.info(f"✅ [{self.exchange_name}] Set margin type {margin_type} for {symbol}")
            return True
        except BinanceAPIException as e:
            # Ignore nếu đã set rồi
            if 'No need to change margin type' in str(e):
                return True
            logger.warning(f"[{self.exchange_name}] Set margin type warning: {e}")
            return False

    def _get_symbol_info(self, symbol):
        """Get symbol info with caching"""
        if symbol not in self._symbol_info_cache:
            try:
                exchange_info = self.client.futures_exchange_info()
                for s in exchange_info['symbols']:
                    if s['symbol'] == symbol:
                        self._symbol_info_cache[symbol] = s
                        break
            except Exception as e:
                logger.error(f"[{self.exchange_name}] Error getting symbol info: {e}")
                return None
        return self._symbol_info_cache.get(symbol)

    def format_quantity(self, symbol, quantity):
        """Format quantity according to symbol's LOT_SIZE filter"""
        try:
            symbol_info = self._get_symbol_info(symbol)
            if not symbol_info:
                # Default to 3 decimals if can't get info
                return round(quantity, 3)

            # Get LOT_SIZE filter
            lot_size_filter = next(
                (f for f in symbol_info['filters'] if f['filterType'] == 'LOT_SIZE'),
                None
            )

            if lot_size_filter:
                step_size = float(lot_size_filter['stepSize'])

                # Calculate precision from step_size
                # e.g., 0.001 -> 3 decimals, 0.01 -> 2 decimals, 1.0 -> 0 decimals
                precision = 0
                if step_size < 1:
                    precision = len(str(step_size).rstrip('0').split('.')[-1])

                # Round to step_size
                formatted = round(quantity / step_size) * step_size
                # Round to precision
                formatted = round(formatted, precision)

                return formatted
            else:
                # Fallback to quantityPrecision
                qty_precision = symbol_info.get('quantityPrecision', 3)
                return round(quantity, qty_precision)

        except Exception as e:
            logger.error(f"[{self.exchange_name}] Error formatting quantity: {e}")
            return round(quantity, 3)  # Safe default

    def create_market_order(self, symbol, side, quantity, reduce_only=False):
        """
        Tạo market order

        Args:
            symbol: Trading pair
            side: 'BUY' hoặc 'SELL'
            quantity: Số lượng (will be formatted to correct precision)
            reduce_only: True nếu đóng position
        """
        try:
            # Format quantity to correct precision
            formatted_qty = self.format_quantity(symbol, quantity)

            logger.info(f"📝 [{self.exchange_name}] Order: {side} {symbol}")
            logger.info(f"   Raw qty: {quantity:.8f} -> Formatted: {formatted_qty}")

            params = {
                'symbol': symbol,
                'side': side,
                'type': 'MARKET',
                'quantity': formatted_qty
            }

            if reduce_only:
                params['reduceOnly'] = True

            order = self.client.futures_create_order(**params)

            logger.info(f"✅ [{self.exchange_name}] Order created: {side} {formatted_qty} {symbol}")
            return order

        except BinanceAPIException as e:
            logger.error(f"[{self.exchange_name}] Create order error: {e}")
            logger.error(f"   Symbol: {symbol}, Side: {side}, Qty: {quantity}")
            return None

    def close_position(self, symbol):
        """Đóng toàn bộ position"""
        pos = self.get_position(symbol)

        if not pos:
            logger.info(f"[{self.exchange_name}] No position to close for {symbol}")
            return True

        # Determine close side
        close_side = 'SELL' if pos['side'] == 'LONG' else 'BUY'

        # Close order
        order = self.create_market_order(
            symbol=symbol,
            side=close_side,
            quantity=pos['amount'],
            reduce_only=True
        )

        return order is not None
