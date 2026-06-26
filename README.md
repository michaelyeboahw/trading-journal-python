# Trading Journal & Analytics Platform (Python + Streamlit)

## Overview
This project is an interactive trading journal that analyzes real trading data exported from Tradovate. It processes raw trade history and generates performance metrics, visual analytics, and interactive dashboards to evaluate trading performance and risk.

The project demonstrates data cleaning, financial analysis, and web app development using Python.

---

## Live Demo

👉 https://trading-journal-python.streamlit.app

Upload your own Tradovate CSV file to generate real-time trading analytics.

---

## Key Features

- Upload and analyze Tradovate CSV files
- Cleans and processes raw trading data using pandas
- Calculates key performance metrics:
  - Total profit/loss
  - Win rate
  - Profit factor
  - Average win and loss
- Interactive equity curve visualization
- Daily PnL analysis
- Full trade data table view
- Web-based dashboard (Streamlit)

---

## Tech Stack

- Python
- Pandas
- Streamlit

---

## Project Structure

TradingJournal/
│
├── src/
│   └── app.py              # Streamlit dashboard application
│
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

---

## How to Run Locally

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run Streamlit app
python -m streamlit run src/app.py

---

## Example Features in Dashboard

- Equity curve (performance over time)
- Daily profit/loss tracking
- Win rate and profit factor metrics
- Interactive trade table
- CSV upload functionality

---

## What I Learned From This Project

- Data cleaning and preprocessing using pandas
- Handling real-world financial datasets
- Time series analysis using timestamps
- Building interactive dashboards with Streamlit
- Turning scripts into deployable web applications

---

## Future Improvements

- Add drawdown and risk metrics (prop firm style analysis)
- Trade tagging (breakout, reversal, trend classification)
- Sharpe ratio and volatility metrics
- Multi-account support
- Automated PDF performance reports

---

## Note

This project uses personal trading data exported from Tradovate and is intended for educational and analytical purposes only.