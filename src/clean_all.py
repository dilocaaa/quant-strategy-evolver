from data_loader import clean_data
import os
# LISTA DE ARCHIVOS A LIMPIAR
files = [
  "TSLA.csv",
  "MSFT.csv",
  "AAPL.csv",
  "NVDA.csv",
  "QQQ.csv",
  "VTI.csv",
  "SPY.csv",
  "AMZN.csv",
  "^DJI.csv",
  "^GSPC.csv",
  "^NDX.csv",
]

for file in files:
clean_data(file)
