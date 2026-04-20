# src/visualize/report_builder.py
import os
import matplotlib
matplotlib.use("Agg")  # Required for headless servers like GitHub Actions
import matplotlib.pyplot as plt
from fpdf import FPDF
from pathlib import Path

def generate_pdf_report(kpis: dict, df: object, output_path: str = "data/output/retail_report.pdf"):
    """Generates a branded PDF report with KPIs and a category sales chart."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    # 1. Create & save chart
    plt.figure(figsize=(8, 4))
    # Handle potential missing 'Category' column gracefully
    if "Category" in df.columns:
        df.groupby("Category")["Sales"].sum().plot(kind="bar", color="#2563EB")
        plt.title("Revenue by Category", fontsize=14, fontweight="bold")
    else:
        plt.text(0.5, 0.5, "Category data not available", ha="center", va="center", fontsize=14)
    
    plt.tight_layout()
    chart_path = "data/output/chart.png"
    plt.savefig(chart_path, dpi=150)
    plt.close()
    
    # 2. Build PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=16)
    pdf.cell(200, 10, txt="Automated Retail Analytics Report", ln=True, align="C")
    pdf.ln(8)
    
    for k, v in kpis.items():
        pdf.set_font("Helvetica", size=12)
        pdf.cell(0, 8, txt=f"{k}: {v}", ln=True)
    
    pdf.ln(5)
    if Path(chart_path).exists():
        pdf.image(chart_path, x=10, y=80, w=190)
    
    pdf.output(output_path)
    print(f"✅ Report saved: {output_path}")
    return output_path