# create a new function 
def api_function(): 
    # As Alpha Vantage standard API call frequency is only 5 calls per minute, a message would be printed when user runs the code too many times 
    # With a different message, the dictionary would change and the system would not be able to find the exact key for rate, incurring a key error
    # Hence, we used try run the code as follows:
    try: 
        import requests 
        # Alpha vantage API Key 
        api_key = "1H49MTNIA7TNIJLO"

        # Calling API from python 
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
        ####
        response = requests.get(url)
        ####
        data = response.json()
        # From the dictionary "data", extract the rate 
        rate=data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        # Convert the rate to a float 
        rate = float(rate)
        # Return the final message
        return f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{rate}\n"
    # When a key error appears, the function follows:
    except KeyError: 
        # A note would be returned 
        return f"{data['Note']}\n"

# Create a new function to extract rate only
def rate_function(): 
    # As Alpha Vantage standard API call frequency is only 5 calls per minute, a message would be printed when user runs the code too many times 
    # With a different message, the dictionary would change and the system would not be able to find the exact key for rate, incurring a key error
    # Hence, we used try run the code as follows:
    try: 
        import requests 
        # Alpha vantage API Key 
        api_key = "1H49MTNIA7TNIJLO"
        
        # Calling API from python 
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
        # use get method to access to access currency exchange data and assign it to response
        response = requests.get(url)
        # retrieve data as a dicitonary with .json() and assign it to data
        data = response.json()
         # From the dictionary "data", extract the rate 
        rate=data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        # Convert the rate to a float 
        rate = float(rate)
        # Return the rate 
        return rate
    # When a key error appears, the function follows:
    except KeyError: 
        # A note would be returned 
        return f"{data['Note']}\n"