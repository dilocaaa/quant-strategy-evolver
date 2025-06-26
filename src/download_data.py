import yfinance as yf
import pandas as pd
import os

# Crear carpetas necesarias si no existen
RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
os.makedirs(RAW_DIR, exist_ok=True)

# ----- Configuración -----
tickers = [
    "SPY",      # S&P 500 ETF
    "QQQ",      # Nasdaq 100 ETF
    "VTI",      # Total US Market
    "AAPL",     # Apple
    "MSFT",     # Microsoft
    "TSLA",     # Tesla
    "BTC-USD"   # Bitcoin en USD
]

start_date = "2019-01-01"
end_date = "2024-06-01"
interval = "1d"  # Puede ser "1d", "1h", "5m", etc.

# ----- Descarga de datos -----
for ticker in tickers:
    print(f"Descargando datos de {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

    if not data.empty:
        filename = os.path.join(RAW_DIR, f"{ticker}.csv")
        data.to_csv(filename)
        print(f"✅ Datos de {ticker} guardados en {filename}")
    else:
        print(f"⚠️ No se pudieron descargar datos de {ticker}. Revisa el ticker o configuración.")
