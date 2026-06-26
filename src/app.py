import streamlit as st
import pandas as pd

st.title("📊 Trading Journal Dashboard")

# -----------------------------
# FILE UPLOAD
# -----------------------------
uploaded_file = st.file_uploader("Upload your Tradovate CSV", type="csv")

# ONLY RUN IF FILE EXISTS
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # -----------------------------
    # CLEAN DATA
    # -----------------------------
    df["pnl"] = pd.to_numeric(df["pnl"], errors="coerce")
    df = df.dropna(subset=["pnl"])

    df["boughtTimestamp"] = pd.to_datetime(df["boughtTimestamp"], errors="coerce")
    df = df.dropna(subset=["boughtTimestamp"])

    df = df.sort_values("boughtTimestamp")

    df["date"] = df["boughtTimestamp"].dt.date
    df["equity"] = df["pnl"].cumsum()

    pnl = df["pnl"]

    # -----------------------------
    # METRICS
    # -----------------------------
    total_trades = len(df)
    total_profit = pnl.sum()
    win_rate = (pnl > 0).mean() * 100

    wins = pnl[pnl > 0]
    losses = pnl[pnl < 0]

    profit_factor = wins.sum() / abs(losses.sum()) if losses.sum() != 0 else 0

    # -----------------------------
    # UI OUTPUT
    # -----------------------------
    st.subheader("📊 Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Trades", total_trades)
    col2.metric("Total Profit", round(total_profit, 2))
    col3.metric("Win Rate", f"{round(win_rate, 2)}%")
    col4.metric("Profit Factor", round(profit_factor, 2))

    st.divider()

    st.subheader("📈 Equity Curve")
    st.line_chart(df.set_index("boughtTimestamp")["equity"])

    st.subheader("📅 Daily PnL")

    daily_pnl = df.groupby("date")["pnl"].sum()
    st.bar_chart(daily_pnl)

    st.subheader("📄 Trades")
    st.dataframe(df)

else:
    st.info("Upload a CSV file to begin analysis.")