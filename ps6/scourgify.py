# https://cs50.harvard.edu/python/2022/psets/6/scourgify/

import sys
import csv
from tabulate import tabulate

students = []
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) == 3:
    before_file=sys.argv[1]
    after_file=sys.argv[2]
    try:
        if ".csv" in before_file and ".csv" in after_file:
            with open(before_file) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    names = row["name"].split(",")
                    first = names[1].strip()
                    last = names[0].strip()
                    house = row["house"]
                    students.append({'first': first, 'last': last, "house": house})
        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")

    # header names, first/last/house
    keys = students[0].keys()
    with open(after_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, keys)
        writer.writeheader()
        writer.writerows(students)


