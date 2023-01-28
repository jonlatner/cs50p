# https://cs50.harvard.edu/python/2022/psets/7/working/

import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    try:
        p1, p2 = s.split(" to ")

        if " AM" in p1:
            am = p1

        if " AM" in p2:
            am = p2

        if " PM" in p1:
            pm = p1

        if " PM" in p2:
            pm = p2

        am = am.replace("AM","").strip()
        if ":" in am:
            h, m = am.split(":")

        else:
            h = am
            m = "00"

        if int(h)>12 or int(m)>59:
            raise ValueError

        if int(h)>9:
            pass

        if int(h)<10:
            h = int(h)
            h = f"{h:02}"
        
        if int(h)==12:
            h = f"{00:02}"
            
        if int(h)>12 or int(m)>60:
            raise ValueError

        am = str(f"{h}:{m}")

        pm = pm.replace("PM","").strip()

        if ":" in pm:
            h, m = pm.split(":")

            if int(m)>60:
                raise ValueError

            if int(h)<12:
                h = int(h) + 12

        else:
            h = pm
            if int(h)<12:
                h = int(h) + 12
            if int(h)==12:
                h = 12
        

        pm = str(f"{h}:{m}")

        if "AM" in p1:
            first = am
            second = pm
        else:
            first = pm
            second = am

        return f"{first} to {second}"

    except (ValueError,UnboundLocalError):
        raise ValueError

if __name__ == "__main__":
    main()
