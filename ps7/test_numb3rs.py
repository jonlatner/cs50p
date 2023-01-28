# https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

import pytest
from numb3rs import validate

def main():
    test_validate()

def test_value():
    assert validate("1.1.1.1") == True
    assert validate("1") == False
    assert validate("275.3.6.28") == False
    assert validate("cat") == False
    assert validate("75.456.76.65") == False

if __name__ == "__main__":
    main()
