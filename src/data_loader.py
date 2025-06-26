import yfinance as yf
import pandas as pd
import os

# Crear carpeta 'data' si no existe
if not os.path.exists("data"):
    os.makedirs("data")

# ----- Configuración -----
ticker = "BTC-USD"  # Cambia aquí el ticker por el que quieras analizar
start_date = "2019-01-01"
end_date = "2024-06-01"
interval = "1d"  # Puede ser "1d", "1h", "5m", etc.

# ----- Descarga de datos -----
print(f"Descargando datos de {ticker}...")
data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

if not data.empty:
    print("Primeras filas de los datos:")
    print(data.head())

    # Guardar en CSV dentro de la carpeta data
    filename = f"data/{ticker}.csv"
    data.to_csv(filename)
    print(f"Datos guardados en {filename}")
else:
    print("No se pudieron descargar datos. Revisa el ticker o la configuración.")

