# 🛒 Automated Retail Analytics Reporter
> A Python-powered pipeline that turns raw retail data into polished, scheduled PDF reports, no manual Excel work required.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

##  Why I Built This
In retail and e-commerce, teams often waste hours every week pulling data, cleaning it in Excel, building charts, and emailing stakeholders. That’s slow, error-prone, and leaves analysts doing copy-paste work instead of uncovering insights.

I built this project to solve that exact pain point: **a fully automated, end-to-end reporting pipeline** that extracts data, calculates KPIs, generates a branded PDF, and delivers it to stakeholders, on a schedule, with zero manual intervention.

---

 📊 Business Impact
| Metric | Before | After |
|--------|--------|-------|
| ⏱️ Time spent per report | ~3–4 hours (manual) | ~5 seconds (fully automated) |
| 📉 Human error in KPIs | Frequent (formula drift, copy-paste mistakes) | 0% (code-enforced logic) |
| 📈 Reporting frequency | Weekly | Daily/Weekly (configurable) |
| 🔍 Decision latency | Days | Hours |

> 💡 *This isn’t just a script. It’s a production-ready analytics workflow designed to scale with real business needs.*

---

##  How It Works

📥 Raw CSV/DB → 🧹 Clean & Transform → 📊 KPI Engine → 📄 PDF/Chart Generator → 📧 Email/Slack → 👥 Stakeholders


1. **Extract**: Pulls data from local files or databases
2. **Transform**: Handles missing values, standardizes types, and engineers features (MoM, margins, dates)
3. **Analyze**: Calculates business KPIs (Revenue, AOV, Top Categories, Profitability)
4. **Visualize**: Generates clean, branded PDFs with embedded charts
5. **Deliver**: Emails reports automatically or triggers Slack/webhook alerts
6. **Schedule**: Runs on cron via GitHub Actions or local task scheduler

---

## 🛠️ Tech Stack
| Layer | Tools |
|-------|-------|
| **Language** | Python 3.10+ |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Plotly (optional) |
| **Report Generation** | FPDF2 |
| **Orchestration** | GitHub Actions (cron + manual triggers) |
| **Delivery** | SMTP + Gmail App Passwords |
| **Testing** | pytest |
| **Logging** | Loguru |
| **Config** | `python-dotenv` + YAML-ready structure |

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.10 or higher
- Git installed
- A Gmail account (for sending reports via App Password)

### 📦 Local Setup
 ```
# 1. Clone & navigate
git clone https://github.com/YOUR_USERNAME/automated-retail-reporter.git
cd automated-retail-reporter
```

# 2. Create & activate virtual environment
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```
# 3. Install dependencies
```pip install -r requirements.txt```

# 4. Configure credentials
```cp .env.example .env  # Or create .env manually```
# Add your Gmail App Password & recipient emails

▶️ Run the Pipeline

```python -m src.main```

You’ll see a PDF generated in data/output/ and an email delivered to your configured recipients.

⏱️ Automation & CI/CD
This repo uses GitHub Actions to run the pipeline automatically:

📅 Scheduled: Every Monday at 9 AM UTC (customizable)
🖱️ Manual: Click Run workflow in the Actions tab
🔐 Secure: All credentials stored in GitHub Secrets
🔑 Add Your Secrets

Go to your repo → Settings → Secrets and variables → Actions
Add these repository secrets:
EMAIL_USER: Your Gmail address
EMAIL_PASS: 16-character Gmail App Password
EMAIL_RECIPIENTS: Comma-separated email list

🧪 Testing & Quality
```
pytest tests/ -v
```


✅ Validates data cleaning logic

✅ Ensures KPI calculations return expected structures

✅ Catches missing columns or type mismatches early

🔄 Runs automatically on every push via CI

🔒 Security & Best Practices

🔐 No hardcoded credentials: Uses .env + GitHub Secrets

📦 Dependency pinning: requirements.txt locks versions for reproducibility

🛡️ Graceful error handling: Pipeline fails loudly with clear logs instead of silently breaking

📁 Data isolation: Raw/output data ignored via .gitignore

📜 Modular design: Each step is independently testable and swappable

## 📈 What’s Next
Connect to live SQL/BigQuery/Snowflake sources
Add Power BI REST API for dashboard refreshes
Implement data quality checks with Great Expectations
Dockerize for local/cloud deployment
Add Slack/Teams webhook notifications
Build a Streamlit frontend for on-demand report viewing

## 💡 Key Takeaways
This project taught me how to bridge the gap between analytics and engineering:
Writing code that runs reliably without human babysitting
Designing for maintainability, not just functionality
Thinking like a stakeholder: What do they actually need to make decisions?
Treating data pipelines like software: versioned, tested, documented, and monitored
## 🤝 Connect & Contribute
I’m always open to feedback, collaboration, or chat about analytics engineering, automation, or data storytelling.

📧 Email: nirrmit.rtickoo@gmail.com

🌐 Portfolio: [NRT](https://nirrmitt.github.io/NRT-Terminal)

💼 LinkedIn: [Nirrmit R. Tickoo](https://www.linkedin.com/in/n-r-t/)

🐙 GitHub: [ @nirrmitt](https://github.com/Nirrmitt)

🔧 Found a bug or have an idea? Open an issue or submit a PR. I review all contributions!

### 📜 License
MIT ©[Nirrmitt](https://nirrmitt.github.io/NRT-Terminal) Feel free to use, adapt, and build upon this for your own projects or learning journey.
