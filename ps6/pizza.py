# https://cs50.harvard.edu/python/2022/psets/6/lines/

import sys
import csv
from tabulate import tabulate

menu = []
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) == 2:
    f=sys.argv[1]
    try:
        if ".csv" in f:
            with open(f) as file:
                reader = csv.reader(file)
                for row in reader:
                    menu.append(row)
        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(menu[1:], headers=menu[0], tablefmt="grid"))


      
"""

"""

