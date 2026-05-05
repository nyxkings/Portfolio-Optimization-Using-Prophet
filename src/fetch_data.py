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
    )
    
    """
        Initialize the data fetcher.
        
        Args:
            start_date: Start date for data (YYYY-MM-DD)
            end_date: End date for data (YYYY-MM-DD)
            use_cache: Whether to cache downloaded data
            cache_dir: Directory to store cached data
        """