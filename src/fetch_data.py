"""Fetching data from yfinance"""

import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import pandas as pd
import yfinance as yf
from pathlib import Path

"""I will use US stock data because Nigerian data APIs have less historical depth than US """

logger = logging.getLogger(__name__)

DEFAULT_START_DATE = (datetime.now() - timedelta(days=365*2)).strftime("%Y-%m-%d")
DEFAULT_END_DATE = datetime.now().strftime("%Y-%m-%d")

class DataFetcher:
    """Fetches stock data"""
    def __init__(
        self,
        start_date: str = DEFAULT_START_DATE,
        end_date: str = DEFAULT_END_DATE,
        use_cache: bool = True,
        cache_dir: str = "data/cache"
    ):
        
    
        """
        Initialize the data fetcher.
        
        Args:
            start_date: Start date for data (YYYY-MM-DD)
            end_date: End date for data (YYYY-MM-DD)
            use_cache: Whether to cache downloaded data
            cache_dir: Directory to store cached data
        """
        self.start_date = start_date
        self.end_date = end_date
        self.use_cache = use_cache
        self.cache_dir = Path(cache_dir)
        
        if use_cache:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            logger.info(f"Cache enabled at {self.cache_dir}")
    def _process_ticker_dataframe(
        self, 
        df: pd.DataFrame, 
        price_column: str = "Adj Close",
        add_returns: bool = True,
        add_log_returns: bool = False,
        add_volume: bool = False
    ) -> pd.DataFrame:
        """
        Process raw ticker DataFrame with enhanced features.
        
        Args:
            df: Raw DataFrame from yfinance
            price_column: Which price column to use ('Close' or 'Adj Close')
            add_returns: Add simple returns column
            add_log_returns: Add log returns column
            add_volume: Include volume data
            
        Returns:
            Processed DataFrame with selected columns
        """
        if df.empty:
            return pd.DataFrame()
    
    # CHANGED: Intelligent price column selection - try Adj Close first
        if price_column not in df.columns:
            if "Adj Close" in df.columns:
                price_column = "Adj Close"
                logger.warning(f"'{price_column}' not found, using 'Adj Close' instead")
            elif "Close" in df.columns:
                price_column = "Close"
                logger.warning(f"Using 'Close' instead of 'Adj Close' - returns may be inaccurate after splits/dividends")
            else:
                price_column = df.columns[0]
                logger.warning(f"No standard price column found, using '{price_column}'")
    
    result_df = pd.DataFrame(index=df.index)
    result_df["Price"] = df[price_column]
    
    