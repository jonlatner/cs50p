#!/usr/bin/env python3
import sys
code = sys.argv[1]
try:
    code_int = int(code)
except ValueError:
    print("Unable to parse code as an integer")
    sys.exit(1)

print("Parsed code as {}".format(code_int))