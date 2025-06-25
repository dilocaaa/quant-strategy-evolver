import yfinance as yf
import pandas as pd

def download_data(ticker, start, end, interval="1d"):
    data = yf.download(ticker, start=start, end=end, interval=interval)
    return data
