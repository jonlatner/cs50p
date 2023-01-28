# https://cs50.harvard.edu/python/2022/psets/3/fuel/

def main():
    while True:
        fraction = input("Fraction: ").strip().title()
        try:
            percentage = convert(fraction)
            if (0 < percentage <= 100):
                print(gauge(percentage))
                break
            else:
                pass
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    x, y = fraction.split("/")
    percentage = int(x)/int(y)*100
    return percentage

def gauge(percentage):
    if percentage >= 99:
        output = "F"
    if percentage <= 1:
        output = "E"
    if 1 < percentage < 99:
        output = f"{percentage:.0f}%"
    return output


if __name__ == "__main__":
    main()

"""

"""