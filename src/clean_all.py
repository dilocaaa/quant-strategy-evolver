from data_loader import clean_data
import os

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')

# Lista automática de archivos CSV en raw
files = [f for f in os.listdir(RAW_DIR) if f.endswith('.csv')]

for file in files:
    clean_data(file)
