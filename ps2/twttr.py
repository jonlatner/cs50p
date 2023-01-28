# https://cs50.harvard.edu/python/2022/psets/2/twttr/
# implement a program that prompts the user for a str of text and 
# then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
# whether inputted in uppercase or lowercase.

string = input("Input: ")
print("Output: ", end = "")

for s in string:
    if s.lower() in ["a", "e", "i", "o", "u"]:
        print("", end = "", sep = "")
    else:
        print(s, end = "", sep = "")

print()

