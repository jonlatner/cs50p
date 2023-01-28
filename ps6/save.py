# Reads a CSV file using csv.DictReader

import csv

students = []

with open("before.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        names = row["name"].split(",")
        first = names[1]
        last = names[0]
        house = row["house"]
        students.append({'first': first, 'last': last, "house": house})

with open("after.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writerow({"first": first, "last": last, "house": house})

"""
"""
