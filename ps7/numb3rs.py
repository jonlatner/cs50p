# https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

import re


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if "." in ip:
        length = ip.split(".")
        if len(length) == 4:
            num1, num2, num3, num4 = ip.split(".")
            if (0<=int(num1)<=255 and 0<=int(num2)<=255 and 0<=int(num4)<=255 and 0<=int(num4)<=255): 
                return True
            else:
                return False
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()

"""
"""