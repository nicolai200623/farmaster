# ============================================
# 📊 DATA FETCHER - Coingecko & AsterDEX
# ============================================

import requests
import pandas as pd
import time
from datetime import datetime, timedelta
from utils.logger import logger

class DataFetcher:
    """Lấy dữ liệu lịch sử từ Coingecko và realtime từ AsterDEX"""
    
    COINGECKO_API = "https://api.coingecko.com/api/v3"
    
    # Mapping symbol -> coingecko id
    COIN_MAP = {
        'BTCUSDT': 'bitcoin',
        'ETHUSDT': 'ethereum',
        'BNBUSDT': 'binancecoin',
        'SOLUSDT': 'solana',
        'ADAUSDT': 'cardano',
        'DOTUSDT': 'polkadot',
        'AVAXUSDT': 'avalanche-2',
        'XRPUSDT': 'ripple',
        'LTCUSDT': 'litecoin',
        'MATICUSDT': 'matic-network',
        'LINKUSDT': 'chainlink',
        'UNIUSDT': 'uniswap',
        'ATOMUSDT': 'cosmos',
        'XLMUSDT': 'stellar',
        'VETUSDT': 'vechain',
        'FILUSDT': 'filecoin',
        'TRXUSDT': 'tron',
        'ETCUSDT': 'ethereum-classic',
        'EOSUSDT': 'eos',
        'AAVEUSDT': 'aave',
        'MKRUSDT': 'maker',
        'THETAUSDT': 'theta-token',
        'ALGOUSDT': 'algorand',
        'XTZUSDT': 'tezos',
        'ZECUSDT': 'zcash',
        # ASTERUSDT không có trên Coingecko, sẽ fallback sang bitcoin
    }
    
    @classmethod
    def fetch_historical_ohlcv(cls, symbol, days=365, max_retries=3):
        """
        Lấy dữ liệu OHLCV lịch sử từ AsterDEX/Binance API (unlimited data!)

        Args:
            symbol: Trading pair (e.g., 'BTCUSDT')
            days: Số ngày lịch sử
            max_retries: Số lần retry nếu bị rate limit

        Returns:
            DataFrame với columns: timestamp, open, high, low, close, volume
        """
        # Use AsterDEX/Binance API instead of Coingecko (no limits!)
        url = "https://fapi.asterdex.com/fapi/v1/klines"

        # Calculate start time
        end_time = int(time.time() * 1000)  # Current time in ms
        start_time = end_time - (days * 24 * 60 * 60 * 1000)  # days ago

        params = {
            'symbol': symbol,
            'interval': '1h',  # 1-hour candles (changed from 15m for quality signals)
            'startTime': start_time,
            'endTime': end_time,
            'limit': 1500  # Max per request
        }

        logger.info(f"Fetching {days} days data for {symbol}...")

        for attempt in range(max_retries):
            try:
                response = requests.get(url, params=params, timeout=30)
                response.raise_for_status()
                data = response.json()

                if not data:
                    logger.warning(f"No data returned for {symbol}")
                    return pd.DataFrame()

                # Parse Binance klines format
                # [timestamp, open, high, low, close, volume, close_time, ...]
                df = pd.DataFrame(data, columns=[
                    'timestamp', 'open', 'high', 'low', 'close', 'volume',
                    'close_time', 'quote_volume', 'trades', 'taker_buy_base',
                    'taker_buy_quote', 'ignore'
                ])

                # Convert types
                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
                df['open'] = df['open'].astype(float)
                df['high'] = df['high'].astype(float)
                df['low'] = df['low'].astype(float)
                df['close'] = df['close'].astype(float)
                df['volume'] = df['volume'].astype(float)

                # Keep only needed columns
                df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]

                logger.info(f"✅ Fetched {len(df)} candles for {symbol}")
                return df

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 429:  # Rate limit
                    wait_time = 10 * (attempt + 1)
                    logger.warning(f"⚠️ Rate limit hit, waiting {wait_time}s... (attempt {attempt+1}/{max_retries})")
                    time.sleep(wait_time)
                    continue
                else:
                    logger.error(f"AsterDEX API error: {e}")
                    return pd.DataFrame()
            except Exception as e:
                logger.error(f"Data fetch error: {e}")
                return pd.DataFrame()

        logger.error(f"❌ Failed to fetch {symbol} after {max_retries} retries")
        return pd.DataFrame()
    
    @classmethod
    def fetch_multiple_symbols(cls, symbols, days=365):
        """
        Lấy data cho nhiều symbols

        Returns:
            Dict {symbol: DataFrame}
        """
        result = {}
        for i, symbol in enumerate(symbols):
            df = cls.fetch_historical_ohlcv(symbol, days)
            if not df.empty:
                result[symbol] = df

            # Rate limit: Wait longer between requests
            # Coingecko free tier: ~10-30 calls/minute
            if i < len(symbols) - 1:  # Don't wait after last symbol
                wait_time = 3.0  # 3 seconds = max 20 calls/minute (safe)
                logger.info(f"⏳ Waiting {wait_time}s before next request...")
                time.sleep(wait_time)

        return result
    
    @classmethod
    def combine_dataframes(cls, data_dict):
        """
        Kết hợp nhiều DataFrames thành 1 cho training
        
        Args:
            data_dict: Dict {symbol: DataFrame}
            
        Returns:
            Combined DataFrame
        """
        dfs = []
        for symbol, df in data_dict.items():
            df_copy = df.copy()
            df_copy['symbol'] = symbol
            dfs.append(df_copy)
        
        if not dfs:
            return pd.DataFrame()
        
        combined = pd.concat(dfs, ignore_index=True)
        logger.info(f"✅ Combined {len(dfs)} symbols: {len(combined)} total rows")
        return combined

