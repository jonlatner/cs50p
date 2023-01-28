# https://cs50.harvard.edu/python/2022/psets/3/taqueria/

# initializing Dictionary
items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

# encapsulating list and dictionary keys in list
total = 0
while True:
    try:
        i = input("Item: ").strip().title()
        if i not in items:
            pass
        if i in items:
            cost = items[i]
            total = total + cost
    except EOFError:
        print()
        break
    else:
        print(f"Total: ${total:.2f}")
        
