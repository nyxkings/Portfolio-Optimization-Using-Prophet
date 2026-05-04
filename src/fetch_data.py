"""Fetching data from yfinance"""
import logging

import pandas as pd
import yfinance as yf

"""I will use US stock data because Nigerian data APIs have less historical depth than US """