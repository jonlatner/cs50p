# https://cs50.harvard.edu/python/2022/psets/8/seasons/

import pytest
import sys
from seasons import convert

def main():
    test_convert()

def test_convert():
    assert convert("12661920") == "Twelve million, six hundred and sixty-one thousand, nine hundred and twenty minutes"

if __name__ == "__main__":
    main()

