import requests

API_KEY = 'fca_live_wH1VpbqQoyMGE760kddTmLVGVNchRyZI0TvZ22Co'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base): 
    currencies = ",".join(CURRENCIES) # Because we should give it as CSV to the url 
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}" 
    try: 
        response = requests.get(url) # The response is going to contain a JSON (in python we will get a disctionary back 
        # with key value pairs with the data that the API returned )
        data = response.json() # Parsing the JSON format that we got from the API call to a dictionary 
        return data["data"]
    except Exception as e:
        print("Invalid Currency")
        return None 
    
if __name__ == '__main__':
    # We enter while as true 
    while True: 

        name = input("Please enter your first name: ")
        
        base = input("Please enter the base currency (q for quit) ").upper() # Invalid currency check in convert_currency

        if base.lower() == "q" :
            break

        amount = input("Please enter the amount you have: ") # The digit number that we enter is saved as a string "100"

        try: # This will convert the number from a string to a number and check for wrong datatype 
            amount = float(amount)
        except ValueError:
            break

        data = convert_currency(base)
        if not data:
            continue 
            
            # if the value returned from the function is false (none in this case) we will 
            # Continue for next while iteration (not the same as if data is None:)

        del data[base]

        print(f"Hello, {name}.\nYour conversion rate is:")
        for ticker, value in data.items():
            final = value * amount
            print(f"{ticker} is: {final}")



    