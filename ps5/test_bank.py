# https://cs50.harvard.edu/python/2022/psets/5/test_bank/

import pytest
from bank import value

def main():
    test_value()

def test_value():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("whatsup") == 100

if __name__ == "__main__":
    main()
