string = input("Enter a string: ")

for char in string:
    if char in "'.,;:?!":
        print("that string contains punctuation")
        break 
else:
    print("that string does not contain punctuation")