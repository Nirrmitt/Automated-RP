import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(df["Sales"].median())
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(1)
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Profit Margin"] = df["Profit"] / df["Sales"].replace(0, 1)
    df["Month"] = df["Order Date"].dt.month
    df["Year"] = df["Order Date"].dt.year
    print("✅ Data cleaned & features engineered")
    return df