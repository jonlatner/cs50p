# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import sys
import requests

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    if float(sys.argv[1]):
        pass
except ValueError:
    sys.exit("Command-line argument is not a number")
    
response = requests.get(
    "https://api.coindesk.com/v1/bpi/currentprice.json"
    )

rate=float(sys.argv[1])

data = response.json()

amount = data["bpi"]["USD"]["rate"]
amount = float(amount.replace(",",""))*rate

print(f"${amount:,.4f}")