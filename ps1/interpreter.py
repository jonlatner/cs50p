# https://cs50.harvard.edu/python/2022/psets/1/interpreter/

# get user input
x = input("Expression: ").split(" ")
x0 = int(x[0])
x1 = int(x[2])
y = x[1]

if y == "+":
  z = (x0 + x1)
  print(f"{z:.1f}")

elif y == "-":
  z = (x0 - x1)
  print(f"{z:.1f}")

elif y == "*":
  z = (x0 * x1)
  print(f"{z:.1f}")

elif y == "/":
  z = (x0 / x1)
  print(f"{z:.1f}")
else:
  print("Invalid operator")
