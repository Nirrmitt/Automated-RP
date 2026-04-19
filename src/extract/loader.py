import pandas as pd
from pathlib import Path

def load_retail_data(file_path: str = "data/raw/sample_retail.csv") -> pd.DataFrame:
    if not Path(file_path).exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")
    df = pd.read_csv(file_path)
    print(f"✅ Loaded {len(df)} records from {file_path}")
    return df