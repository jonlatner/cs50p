# https://cs50.harvard.edu/python/2022/psets/2/twttr/
# implement a program that prompts the user for a str of text and 
# then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
# whether inputted in uppercase or lowercase.

def main():
    word = input("Input: ")
    output = shorten(word)
    print(output, end = "")

def shorten(word):
    new_word = ""
    for s in word:
        if s.lower() not in ["a", "e", "i", "o", "u"]:
            new_word = new_word + s
    return new_word


if __name__ == "__main__":
    main()

