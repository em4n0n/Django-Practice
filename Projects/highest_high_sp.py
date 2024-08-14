# Import the necessary modules.
import pandas as pd

# Load the historical data for the S&P 500.
data = pd.read_csv('SP500.csv')

# Select the last 30 days of data.
last_30_days = data.tail(30)

# Find the highest price in the last 30 days.
highest_price = last_30_days['close'].max()

# Print the highest price.
print(f"The highest price in the last 30 days was: {highest_price:.2f}")
