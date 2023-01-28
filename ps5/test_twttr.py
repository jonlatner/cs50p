# https://cs50.harvard.edu/python/2022/psets/5/test_twttr/

import pytest
from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("TwIttEr") == "Twttr"
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"

if __name__ == "__main__":
    main()
