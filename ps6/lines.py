# https://cs50.harvard.edu/python/2022/psets/6/lines/

import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) == 2:
    f=sys.argv[1]
    try:
        if ".py" in f:
            count = 0
            with open(f) as file:
                for line in file:
                    line = line.strip()
                    if (len(line)>0 and not line.startswith('#')):
                        count += 1
            print(count)
        else:
            sys.exit("Not a Python file")
    except FileNotFoundError:
        sys.exit("File does not exist")

      
"""

"""