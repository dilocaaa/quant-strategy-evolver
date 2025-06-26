import os
import pandas as pd

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')

def check_columns(filename):
    raw_path = os.path.join(RAW_DIR, filename)
    df = pd.read_csv(raw_path)
    print(f"Columnas en {filename}: {df.columns.tolist()}")

if __name__ == "__main__":
    # Cambia el nombre por uno de tus archivos CSV
    check_columns("sp500.csv")
