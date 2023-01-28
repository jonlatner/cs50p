#https://cs50.harvard.edu/python/2022/psets/4/professor/

import random

def main():

    level = get_level()

    correct = 0
    incorrect = 0

    while correct < 10:

        x,y = generate_integer(level)
        answer = x + y
        z = int(input(f"{x} + {y} = "))

        if z == answer:
            correct = correct + 1

        while z != answer:
            incorrect = incorrect + 1
            print("EEE")
            z = int(input(f"{x} + {y} = "))
            if incorrect == 2:
                print(answer)
                break

    print("Score: ",correct)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                break
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    if level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    if level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

if __name__ == "__main__":
    main()

"""

"""