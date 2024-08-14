# Import the necessary modules.
import requests

# Set the base URL for the Binance REST API.
base_url = 'https://api.binance.com/api/v3/depth'

# Set the parameters for the API request.
# In this case, we are requesting the current orderbook for the BTC/USDT market on Binance.
params = {
  'symbol': 'BTCUSDT',
  'limit': 10,
}

# Send the API request and store the response.
response = requests.get(base_url, params=params)

# Check the status code of the response to ensure that the request was successful.
if response.status_code == 200:
  # If the request was successful, parse the JSON data from the response.
  data = response.json()

  # Print the bids and asks from the orderbook.
  print('Bids:')
  for bid in data['bids']:
    print(f"  Price: {bid[0]}, Quantity: {bid[1]}")
  print('Asks:')
  for ask in data['asks']:
    print(f"  Price: {ask[0]}, Quantity: {ask[1]}")
else:
  # If the request was not successful, print an error message.
  print('Error: Could not retrieve orderbook data.')

# In this implementation, we import the requests module and use it to send an API request to the Binance REST API. 
# We set the parameters for the request to request the current orderbook for the BTC/USDT market on Binance. 
# We then check the status code of the response to ensure that the request was successful, and if it was, we parse the JSON data from the response and print the bids and asks from the orderbook.