import requests
import plotly.graph_objects as go

# Retrieve price data for Armada's jitoSOL-USDC pool
armada_prices_response = requests.get('https://armadafi.so/clmm')
try:
    armada_prices_response.raise_for_status()  # Raise exception for HTTP errors
    armada_prices_data = armada_prices_response.json()
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Oops! Something went wrong:", err)
except ValueError:
    print("Response content is not in valid JSON format:", armada_prices_response.text)

# The rest of your code for data processing and plotting...
