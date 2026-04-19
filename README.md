# 🛒 Automated Retail Analytics Reporter
> End-to-end Python pipeline that extracts, cleans, analyzes, generates PDF reports, and emails stakeholders on schedule.

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![CI](https://github.com/YOUR_USERNAME/automated-retail-reporter/actions/workflows/run-report.yml/badge.svg)](https://github.com/YOUR_USERNAME/automated-retail-reporter/actions)

## 🎯 Business Impact
⏱️ **Saved 4+ hrs/week** by replacing manual Excel reporting  
📈 **Enabled daily KPI tracking** for inventory & pricing decisions  
✅ **100% reproducible** metrics with automated validation

## 🏗️ Architecture
`CSV → Clean/Transform → KPI Engine → PDF/Chart → Email → Stakeholders`

## 🛠️ Tech Stack
Python, Pandas, Matplotlib, FPDF, GitHub Actions, SMTP, pytest

## 🚀 Local Setup
```powershell
git clone https://github.com/YOUR_USERNAME/automated-retail-reporter.git
cd automated-retail-reporter
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
# Fill .env with Gmail App Password & run:
python -m src.main