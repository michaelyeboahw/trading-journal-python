# Trading Journal & Analytics Platform (Python + Pandas)

## Overview
This project is a Python-based trading journal that analyzes real trading data exported from Tradovate. It processes raw trade history and generates performance metrics to help evaluate trading behavior, profitability, and risk exposure.

The goal is to turn raw broker data into actionable insights using data analysis tools.

---

## Key Features

- Loads and processes Tradovate CSV trade exports
- Cleans and validates trading data using pandas
- Calculates core performance metrics:
  - Total profit/loss
  - Win rate
  - Average win and average loss
  - Profit factor
- Builds equity curve over time
- Groups and analyzes daily performance
- Identifies best and worst trades

---

## Tech Stack

- Python
- Pandas

---

## Project Structure

TradingJournal/
│
├── data/
│   └── pa_account.csv        (NOT uploaded to GitHub)
│
├── src/
│   └── analysis.py
│
├── requirements.txt
└── README.md

---

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run the analysis
python src/analysis.py

---

## Example Output

=== TRADING SUMMARY ===
Total Trades: 243
Total Profit: 5421.50
Win Rate: 58.40%
Profit Factor: 1.67

Big Win: 320.00
Big Loss: -180.00

---

## What I Learned From This Project

- Data cleaning and preprocessing with pandas
- Working with real-world financial datasets
- Handling missing and inconsistent data formats
- Time series analysis using timestamps
- Calculating performance and risk metrics
- Structuring a Python analytics project

---

## Future Improvements

- Add interactive dashboard using Streamlit
- Add trade tagging (breakout, reversal, trend)
- Visual charts (equity curve, drawdown)
- Automated PDF performance reports
- Multi-account support

---

## Note

This project uses personal trading data exported from Tradovate and is intended for educational and performance analysis purposes.