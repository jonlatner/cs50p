# https://cs50.harvard.edu/python/2022/psets/1/meal/

# breakfast between 7:00 and 8:00
# lunch between 12:00 and 13:00
# dinner between 18:00 and 19:00.

def main():
    # Get time from the user
    answer = input("What time is it? ")

    # Call the convert function
    time = convert(answer)

    if 7 <= time <= 8:
        print("Breakfast time")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")
    else:
        print("")

def convert(time):
    if ":" in time:
        # get the hour and minute
        hours, minutes = time.split(":")

        # convert time into a float number
        new_minutes = float(minutes) / 60

        # Return the result to the main function
        return float(hours) + new_minutes

    elif "." in time:

        # Return the result to the main function
        return float(time)

    else:
        print("Invalid operator")

if __name__ == "__main__":
    main()

