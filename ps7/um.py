# https://cs50.harvard.edu/python/2022/psets/7/um/

import re

def main():
    print(count(input("Text: ")))

def count(s):
    count = len(re.findall(r"\bum\b", s, re.IGNORECASE))
    return count

if __name__ == "__main__":
    main()