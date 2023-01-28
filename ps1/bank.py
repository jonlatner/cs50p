# Compares multiple strings

answer = input("Do you agree? ").strip().lower().replace(",", "").split()[0]

if answer == "hello":
    print("$0")
elif answer.startswith("h"):
    print("$20")
else:
    print("$100")
