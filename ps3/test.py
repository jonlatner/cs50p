# https://cs50.harvard.edu/python/2022/psets/3/outdated/

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

dictionary = {}
i = 0
for month in months:
    i = i + 1
    dictionary[month] = dictionary.get(month, 0) + i

while True:
    # date = month, day, year
    date = input("Date: ")
    date = date.strip()
#    date = "19/8/1636"
#    date = "10/40/1734"
#    date = "10/19/1636"
    try:
        # split date by /
        month, day, year = date.split("/")
        if (month > 12 or day > 31):
            break
    except:
        try:
            # split date by space
            m, d, y = date.split(" ")
            day = int(d.replace(",","").strip())
            month = m.replace(",","").strip()
            year = int(y)
            if (m > 12 or day > 31):
                break
            # Find dictionary matching value in list
            if month in dictionary:
                month = int(dictionary[month])
        except:
            pass
    else:
        break

if day < 10:
    day = f"{day:02}"        
if month < 10:
    month = f"{month:02}"

# date = year, month, day
print(f"{year}-{month}-{day}")

"""
"""