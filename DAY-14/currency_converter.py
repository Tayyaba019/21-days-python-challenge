# from dotenv import load_dotenv
# import os
# from requests import get 
# from pprint import PrettyPrinter

# load_dotenv()  # Load variables from the .env file into the environment

# BASE_URL = "https://v6.exchangerate-api.com/v6/"
# API_KEY = os.getenv("API_KEY")  # Safely access the API key from environment variables

# printer = PrettyPrinter()

# def get_currencies():
#     # Get all currency conversion rates based on USD
#     endpoint = f"{API_KEY}/latest/USD"
#     url = BASE_URL + endpoint
#     data = get(url).json()['conversion_rates']

#     data = list(data.items())  # Convert dict to list of tuples
#     data.sort()  # Sort the currency codes alphabetically
#     return data

# def print_currencies(currencies):
#     # Print all currencies with their rates
#     for currency ,rate in currencies: 
#         print(f"{currency},{rate}")

# def excahnge_rate(currency1, currency2):
#     # Fetch the exchange rate between two currencies
#     url = f'{BASE_URL}/{API_KEY}/pair/{currency1}/{currency2}'
#     data = get(url).json()

#     if len(data) == 0: 
#         print("Invalid currencies")
#         return 
#     rate = data['conversion_rate']
#     print(f"{currency1}->{currency2} = {rate}")
#     return rate  

# def convert(currency1, currency2, amount): 
#     # Convert given amount from currency1 to currency2
#     rate = excahnge_rate(currency1,currency2)
#     if rate is None: 
#         return 
#     try: 
#         amount = float(amount)
#     except: 
#         print("Invalid amount.")
#         return
#     converted_amount = amount * rate
#     print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
#     return converted_amount

# def main():
#     currencies = get_currencies()

#     print("Welcome to the currency converter!")
#     print("List-list the different currencies")
#     print("Converter-convert from one currency to another")
#     print("Rate-get the exchange rate of two currencies")
#     print()

#     while True: 
#         command = input('Enter a command (q to quit): ').lower()
#         if command == 'q': 
#             break 
#         elif command == 'list': 
#             return print_currencies(currencies)
#         elif command == 'convert': 
#             currency1 = input('Enter the base currency: ').upper()
#             amount = input(f'Enter the amount in {currency1}: ')
#             currency2 = input("Enter a currency to convert to: ").upper()
#             convert(currency1,currency2,amount)
#         elif command == 'rate': 
#             currency1 = input('Enter the base currency: ').upper()
#             currency2 = input("Enter a currency to convert to: ").upper()
#             excahnge_rate(currency1,currency2)
#         else: 
#             print('Unrecognized Command!')

# main() 
import requests

try:
    response = requests.get("https://www.google.com", timeout=5)
    if response.status_code == 200:
        print("Internet access OK. No firewall blocking basic requests.")
    else:
        print(f"Unexpected response code: {response.status_code}")
except Exception as e:
    print(f"Request failed: {e}")