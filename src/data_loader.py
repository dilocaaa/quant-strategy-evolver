import os
import pandas as pd

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
PROCESSED_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
os.makedirs(PROCESSED_DIR, exist_ok=True)

def clean_data(filename):
    raw_path = os.path.join(RAW_DIR, filename)
    processed_path = os.path.join(PROCESSED_DIR, filename)

    try:
        df = pd.read_csv(raw_path, parse_dates=["Date"])
    except Exception as e:
        print(f"⚠️ Error leyendo {filename}: {e}")
        return

    df.set_index("Date", inplace=True)
    df = df.sort_index()
    df = df.dropna()

    df.to_csv(processed_path)
    print(f"✅ {filename} limpio y guardado en {processed_path}")

def clean_all():
    files = [f for f in os.listdir(RAW_DIR) if f.endswith(".csv")]
    if not files:
        print("⚠️ No hay archivos CSV en data/raw.")
        return
    
    for file in files:
        clean_data(file)

if __name__ == "__main__":
    clean_all()

