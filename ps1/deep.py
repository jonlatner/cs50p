# Compares multiple strings

answer = input("Do you agree? ").strip().lower().title().replace("-"," ")
if answer == "42" or answer == "Forty Two" or answer == "forty-two":
    print("Yes")
else:
    print("No")
