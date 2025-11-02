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
        Lấy dữ liệu OHLCV lịch sử từ Coingecko

        Args:
            symbol: Trading pair (e.g., 'BTCUSDT')
            days: Số ngày lịch sử
            max_retries: Số lần retry nếu bị rate limit

        Returns:
            DataFrame với columns: timestamp, open, high, low, close, volume
        """
        coin_id = cls.COIN_MAP.get(symbol)
        if not coin_id:
            logger.warning(f"Symbol {symbol} không có trong COIN_MAP, dùng bitcoin")
            coin_id = 'bitcoin'

        for attempt in range(max_retries):
            try:
                url = f"{cls.COINGECKO_API}/coins/{coin_id}/ohlc"
                params = {
                    'vs_currency': 'usd',
                    'days': days
                }

                logger.info(f"Fetching {days} days data for {symbol} ({coin_id})...")
                response = requests.get(url, params=params, timeout=30)
                response.raise_for_status()

                data = response.json()

                # Parse data
                df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close'])
                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

                # Coingecko không có volume trong OHLC, estimate từ price
                df['volume'] = (df['high'] - df['low']) * 1000000  # Dummy volume

                logger.info(f"✅ Fetched {len(df)} candles for {symbol}")
                return df

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 429:  # Rate limit
                    wait_time = 10 * (attempt + 1)  # Exponential backoff: 10s, 20s, 30s
                    logger.warning(f"⚠️ Rate limit hit, waiting {wait_time}s... (attempt {attempt+1}/{max_retries})")
                    time.sleep(wait_time)
                    continue
                else:
                    logger.error(f"Coingecko API error: {e}")
                    return pd.DataFrame()
            except requests.exceptions.RequestException as e:
                logger.error(f"Coingecko API error: {e}")
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

