import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd  # Import pandas library

# Create a Ticker object for the stock
meta = yf.Ticker("META")

# Get stock statistics
meta_statistics = meta.history(period="1d", interval="5m")

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Print the entire DataFrame
print(meta_statistics)

x = list(range(len(meta_statistics['Open'])))  # Simplify the x creation

plt.plot(x, meta_statistics['Close'])

plt.xlabel('Days')
plt.ylabel('Closing Price')

plt.title('Meta YTD Graph')
plt.show()
