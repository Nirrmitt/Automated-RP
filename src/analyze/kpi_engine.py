import pandas as pd

def calculate_kpis(df: pd.DataFrame) -> dict:
    return {
        "Total Revenue": f"${df['Sales'].sum():,.2f}",
        "Total Profit": f"${df['Profit'].sum():,.2f}",
        "Avg Order Value": f"${df['Sales'].mean():,.2f}",
        "Top Category": df.groupby("Category")["Sales"].sum().idxmax(),
        "Total Orders": len(df)
    }