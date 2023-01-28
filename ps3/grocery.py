list = []
while True:
    try:
        item = input("")
        list.append(item.upper())
    except EOFError:
        print()
        break

list.sort()
dictionary = {}
for item in list:
    dictionary[item] = dictionary.get(item, 0) + 1

for d in dictionary:
    print(dictionary[d], d)
