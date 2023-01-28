# https://cs50.harvard.edu/python/2022/psets/4/adieu/

"""
list = ["one", "two", "three", "four", "five"]
list = ["one", "two"]
list = ["one"]
"""
list = []
while True:
    try:
        name = input("Name: ")
        list.append(name)
    except EOFError:
        print()
        break

print("Adieu, adieu, to ", end = "")
max = len(list)
count = 1
for item in list:
    if count <= max-2 and max > 2:
        print(item, end = ", ")
    if count == max-1 and max > 2:
        print(item, end = ", and ")
    if count == max-1 and max == 2:
        print(item, end = " and ")
    if max == 1:
        print(item)
        break
    if count == max:
        print(item)
    count = count + 1

