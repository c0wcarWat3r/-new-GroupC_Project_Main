# create a new function 
def api_function(): 
    import requests 
    # Alpha vantage API Key 
    api_key = "1H49MTNIA7TNIJLO"

    # Calling API from python 
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
    # Use .get() method to access currency data and assign it to 'response'
    response = requests.get(url)
    # Retrieve data as a dictionary with .json() and assign it to 'data'
    data = response.json()
    # From the dictionary "data", extract the rate 
    rate=data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    # Convert the rate to a float 
    rate = float(rate)
    # Return the final message
    return f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{rate}\n"

# Create a new function to extract rate only
def rate_function(): 
    import requests 
    # Alpha vantage API Key 
    api_key = "1H49MTNIA7TNIJLO"
    
    # Calling API from python 
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
    # Use get method to access to access currency exchange data and assign it to response
    response = requests.get(url)
    # Retrieve data as a dicitonary with .json() and assign it to data
    data = response.json()
    # From the dictionary "data", extract the rate 
    rate=data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    # Convert the rate to a float 
    rate = float(rate)
    # Return the rate 
    return rate