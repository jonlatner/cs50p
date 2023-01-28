# implement a program that prompts the user for a vanity plate
# output Valid if meets all of the requirements or Invalid if it does not. 
# Assume that any letters in the user’s input will be uppercase. 
# Structure your program per the below, where 
#   is_valid returns True if s meets all requirements and False if it does not. 
# Assume that s will be a str. 
# You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # maximum of 6 characters and a minimum of 2 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # All vanity plates must start with at least two letters.
    if s[0].isalpha()==False or s[1].isalpha()==False:
        return False
    
    # Numbers only in middle, not at the end
    for i in range(len(s)-1):
        if s[i].isdecimal()==True and s[i+1].isalpha()==True:
            return False

    # First numeric cannot be 0
    i = 0
    while i < len(s):
        if s[i].isalpha()==False:
            if s[i] == "0":
                return False
            else:
                break
        i = i+1

    # No punctuation
    for c in s:
        if c in "'.,;:?!":
            return False

    return True

main()
