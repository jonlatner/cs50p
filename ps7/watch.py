# https://cs50.harvard.edu/python/2022/psets/7/watch/

import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if "src" and "youtube" in s:
        x = re.search(r'(?=src)src=\"(?P<src>[^\"]+)', s)
        x = x.group("src")
        x = x.replace("embed/","")
        x = x.replace("youtube.com", "youtu.be")
        x = x.replace("http://","https://")
        x = x.replace("www.","")
        return x
    else:
        return None

if __name__ == "__main__":
    main()