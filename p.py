import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("pa_account.csv")

# -----------------------------
# CLEAN DATA
# -----------------------------
df["pnl"] = pd.to_numeric(df["pnl"], errors="coerce")
df = df.dropna(subset=["pnl"])

# Convert timestamps
df["boughtTimestamp"] = pd.to_datetime(df["boughtTimestamp"], errors="coerce")
df["soldTimestamp"] = pd.to_datetime(df["soldTimestamp"], errors="coerce")

# Remove bad timestamp rows (optional safety)
df = df.dropna(subset=["boughtTimestamp"])

# Sort by time (VERY IMPORTANT for equity curve)
df = df.sort_values("boughtTimestamp")

# Create usable date column
df["date"] = df["boughtTimestamp"].dt.date

# -----------------------------
# BASIC STATS
# -----------------------------
pnl = df["pnl"]

total_trades = len(df)
total_profit = pnl.sum()

wins = pnl[pnl > 0]
losses = pnl[pnl < 0]

win_rate = (len(wins) / total_trades * 100) if total_trades > 0 else 0

avg_win = wins.mean() if len(wins) > 0 else 0
avg_loss = losses.mean() if len(losses) > 0 else 0

profit_factor = (
    wins.sum() / abs(losses.sum())
    if len(losses) > 0 and losses.sum() != 0
    else 0
)

# -----------------------------
# EQUITY CURVE
# -----------------------------
df["equity"] = df["pnl"].cumsum()

# -----------------------------
# DAILY PnL
# -----------------------------
daily_pnl = df.groupby("date")["pnl"].sum()

# -----------------------------
# RESULTS OUTPUT
# -----------------------------
print("\n=== Trading Journal Summary ===")
print("Total Trades:", total_trades)
print("Total Profit:", round(total_profit, 2))
print("Win Rate:", round(win_rate, 2), "%")
print("Average Win:", round(avg_win, 2))
print("Average Loss:", round(avg_loss, 2))
print("Profit Factor:", round(profit_factor, 2))

print("\n=== Best / Worst Trades ===")
print("Biggest Win:", pnl.max())
print("Biggest Loss:", pnl.min())

print("\n=== Equity Curve (Last 10 Trades) ===")
print(df["equity"].tail(10))

print("\n=== Daily PnL (Last 10 Days) ===")
print(daily_pnl.tail(10))