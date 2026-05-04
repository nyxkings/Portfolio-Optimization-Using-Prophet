"""Database operations for saving results to Supabase"""

import yfinance as yf


import yfinance as yf
import pandas as pd

# Download some test data
data = yf.download("AAPL", period="5d")
print("\n✓ Successfully downloaded Apple stock data:")
print(data.head())
