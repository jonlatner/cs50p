# https://cs50.harvard.edu/python/2022/psets/4/game/

import random

while True:
    try:
        level = int(input("Level: "))
        number = random.randint(1, level)
        print(number)
        if level == 1:
            guess = int(input("Guess: "))
            if guess == 1:
                print("Thats right!")
                break
        if level > 0:
                guess = int(input("Guess: "))
                while True:
                    try:
                        guess != number
                        if guess > number:
                            print("Too large!")
                        if guess < number:
                            print("Too small!")
                        if guess == number:
                            print("Just right!")
                            break
                        guess = int(input("Guess: "))
                    except ValueError:
                        pass
    except ValueError:
        pass
    else:
        break

