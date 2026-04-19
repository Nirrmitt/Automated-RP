# tests/test_pipeline.py
import pandas as pd
from src.transform.cleaner import clean_data
from src.analyze.kpi_engine import calculate_kpis

def test_cleaner_handles_missing():
    df = pd.DataFrame({
        "Sales": [100, None, 300],
        "Profit": [10, 20, 30],
        "Quantity": [2, None, 5],  # ✅ ADDED
        "Order Date": ["2024-01-01", "2024-01-02", "2024-01-03"],
        "Category": ["A", "B", "C"]
    })
    df_clean = clean_data(df)
    assert df_clean["Sales"].isnull().sum() == 0
    assert df_clean["Quantity"].isnull().sum() == 0  # ✅ Added validation

def test_kpi_returns_dict():
    df = pd.DataFrame({
        "Sales": [100, 200],
        "Profit": [10, 20],
        "Quantity": [1, 2],  # ✅ ADDED FOR CONSISTENCY
        "Order Date": ["2024-01-01", "2024-01-02"],
        "Category": ["A", "B"]
    })
    kpis = calculate_kpis(df)
    assert isinstance(kpis, dict)
    assert "Total Revenue" in kpis