# https://cs50.harvard.edu/python/2022/psets/2/twttr/
# implement a program that prompts the user for a str of text and 
# then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
# whether inputted in uppercase or lowercase.

def main():
    answer = input("Do you agree? ").strip().lower().replace(",", "").split()[0]
    greeting = value(answer)
    print("$", greeting, sep = "")

def value(answer):
    amount = 0
    if answer == "hello":
        amount = amount + 0
    elif answer.startswith("h"):
        amount = amount + 20
    else:
        amount = amount + 100
    return amount

if __name__ == "__main__":
    main()


