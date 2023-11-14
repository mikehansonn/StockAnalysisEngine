import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Define the ticker symbols for the stocks
ticker_symbols = ["META", "AAPL", "AMZN", "NVDA", "AMD", "GOOG", "LMT", "TSLA"]

# Set the date range for the last week
end_date = datetime.now()
start_date = end_date - timedelta(days=3)
print(start_date)

# Create a figure with subplots for each stock
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(14, 14))
fig.suptitle("Minute-by-Minute", fontsize=16)

# Fetch and plot data for each stock
for i, ticker_symbol in enumerate(ticker_symbols):
    row = i // 2
    col = i % 2

    # Fetch minute-by-minute historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date, interval="2m")
    for stock in stock_data['Close']:
        print(stock)
    # Plot the closing prices for the stock
    axes[row, col].plot(stock_data.index, stock_data['Close'], label=f"{ticker_symbol} Price", color='blue')
    axes[row, col].set_title(f"{ticker_symbol}")
    axes[row, col].legend()
    axes[row, col].grid(True)

# Adjust subplot spacing and display the graphs
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()
