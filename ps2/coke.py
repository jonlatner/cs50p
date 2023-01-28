# https://cs50.harvard.edu/python/2022/psets/2/coke/

due = 50
while due > 0:
    print("Amount Due:", due)
    insert = int(input("Insert Coin: "))
    if insert in [5, 10, 25]:
        due = due - insert

if due <= 0:
    print("Change owed:", abs(due), end = "")

print()
