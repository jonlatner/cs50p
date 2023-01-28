# https://cs50.harvard.edu/python/2022/psets/3/fuel/

while True:
    try:
        frac = input("Fraction: ").strip().title()
        x, y = frac.split("/")
        z = int(x)/int(y)
        if z > 1:
            break
        if z >= .99:
            print("F")
            break
        if z <= .01:
            print("E")
            break
    except (ValueError, ZeroDivisionError):
        pass
    else:
        z = z * 100
        print(f"{z:.0f}%")
        break

