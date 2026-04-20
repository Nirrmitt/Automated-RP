# src/transform/cleaner.py
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    # 1. Clean Sales
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(df["Sales"].median())
    
    # 2. Clean Quantity (defensive: handles missing columns gracefully)
    if "Quantity" in df.columns:
        df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(1)
    else:
        df["Quantity"] = 1  # Fallback for datasets without quantity
        
    # 3. Clean Dates & Metrics
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Profit Margin"] = df["Profit"] / df["Sales"].replace(0, 1)
    df["Month"] = df["Order Date"].dt.month
    df["Year"] = df["Order Date"].dt.year
    
    print("✅ Data cleaned & features engineered")
    return df