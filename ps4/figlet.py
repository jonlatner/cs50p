from pyfiglet import Figlet
import sys

if len(sys.argv) < 2:
    sys.exit("Invalid usage")
if sys.argv[1] != "-f":
    sys.exit("Invalid usage")
else:
    result = input("Input: ")
    figlet = Figlet()
    figlet.setFont(font=sys.argv[2])
    print("Output: \n", figlet.renderText(result), sep = "")

"""
"""