import pandas as pd

# -----------------------
# LOAD DATA
# -----------------------
df = pd.read_csv("data/pa_account.csv")

# -----------------------
# CLEAN DATA
# -----------------------
df["pnl"] = pd.to_numeric(df["pnl"], errors="coerce")
df = df.dropna(subset=["pnl"])

df["boughtTimestamp"] = pd.to_datetime(df["boughtTimestamp"], errors="coerce")
df = df.dropna(subset=["boughtTimestamp"])

df = df.sort_values("boughtTimestamp")

df["date"] = df["boughtTimestamp"].dt.date

# -----------------------
# BASIC METRICS
# -----------------------
pnl = df["pnl"]

total_trades = len(df)
total_profit = pnl.sum()

wins = pnl[pnl > 0]
losses = pnl[pnl < 0]

win_rate = (len(wins) / total_trades) * 100 if total_trades > 0 else 0

avg_win = wins.mean() if len(wins) > 0 else 0
avg_loss = losses.mean() if len(losses) > 0 else 0

profit_factor = (
    wins.sum() / abs(losses.sum())
    if losses.sum() != 0 else 0
)

# -----------------------
# EQUITY CURVE
# -----------------------
df["equity"] = df["pnl"].cumsum()

# -----------------------
# DAILY PnL
# -----------------------
daily_pnl = df.groupby("date")["pnl"].sum()

# -----------------------
# OUTPUT
# -----------------------
print("\n=== TRADING SUMMARY ===")
print("Total Trades:", total_trades)
print("Total Profit:", round(total_profit, 2))
print("Win Rate:", round(win_rate, 2), "%")
print("Avg Win:", round(avg_win, 2))
print("Avg Loss:", round(avg_loss, 2))
print("Profit Factor:", round(profit_factor, 2))

print("\n=== BIGGEST TRADES ===")
print("Big Win:", pnl.max())
print("Big Loss:", pnl.min())

print("\n=== EQUITY (LAST 10 TRADES) ===")
print(df["equity"].tail(10))

print("\n=== DAILY PnL (LAST 5 DAYS) ===")
print(daily_pnl.tail(5))