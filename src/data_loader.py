import os
import pandas as pd

# Define rutas
RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
PROCESSED_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')

# Asegurarse de que la carpeta processed existe
os.makedirs(PROCESSED_DIR, exist_ok=True)

def clean_data(filename):
    """
    Carga un CSV de raw/, limpia los datos y lo guarda en processed/
    """
    raw_path = os.path.join(RAW_DIR, filename)
    processed_path = os.path.join(PROCESSED_DIR, filename)

    # Carga el CSV
    df = pd.read_csv(raw_path, parse_dates=["Date"])
    df.set_index("Date", inplace=True)

    # Limpieza básica
    df = df.dropna()  # Elimina filas con nulos

    # Ordena por fecha por si acaso
    df = df.sort_index()

    # Guarda en processed
    df.to_csv(processed_path)
    print(f"✅ {filename} limpio y guardado en {processed_path}")

