import os
from dotenv import load_dotenv
from loguru import logger
from src.extract.loader import load_retail_data
from src.transform.cleaner import clean_data
from src.analyze.kpi_engine import calculate_kpis
from src.visualize.report_builder import generate_pdf_report
from src.notify.email_sender import send_report_email

load_dotenv()

def run_pipeline():
    logger.info("🚀 Starting Retail Reporting Pipeline")
    try:
        df = load_retail_data()
        df_clean = clean_data(df)
        kpis = calculate_kpis(df_clean)
        report_path = generate_pdf_report(kpis, df_clean)
        send_report_email(report_path, os.getenv("EMAIL_RECIPIENTS"))
        logger.success("✅ Pipeline completed successfully")
    except Exception as e:
        logger.error(f"❌ Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    run_pipeline()