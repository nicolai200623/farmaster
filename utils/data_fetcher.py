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
    }
    
    @classmethod
    def fetch_historical_ohlcv(cls, symbol, days=365):
        """
        Lấy dữ liệu OHLCV lịch sử từ Coingecko
        
        Args:
            symbol: Trading pair (e.g., 'BTCUSDT')
            days: Số ngày lịch sử
            
        Returns:
            DataFrame với columns: timestamp, open, high, low, close, volume
        """
        coin_id = cls.COIN_MAP.get(symbol)
        if not coin_id:
            logger.warning(f"Symbol {symbol} không có trong COIN_MAP, dùng bitcoin")
            coin_id = 'bitcoin'
        
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
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Coingecko API error: {e}")
            return pd.DataFrame()
        except Exception as e:
            logger.error(f"Data fetch error: {e}")
            return pd.DataFrame()
    
    @classmethod
    def fetch_multiple_symbols(cls, symbols, days=365):
        """
        Lấy data cho nhiều symbols
        
        Returns:
            Dict {symbol: DataFrame}
        """
        result = {}
        for symbol in symbols:
            df = cls.fetch_historical_ohlcv(symbol, days)
            if not df.empty:
                result[symbol] = df
            time.sleep(1.5)  # Rate limit Coingecko: 50 calls/min
        
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

