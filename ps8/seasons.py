# https://cs50.harvard.edu/python/2022/psets/8/seasons/

from datetime import date
import inflect
p = inflect.engine()
import sys

def main():
    # YYYY-MM-DD format
    string = input("Date of Birth: ")
    valid_string = validate(string)
    days = count_days(valid_string)
    days_text = convert(days)
    print(days_text)

def validate(string):
    try:
        result = date.fromisoformat(string)
        return result
    except ValueError:
        sys.exit("Invalid date")

def count_days(days):
    today = date.today()
    difference = today - days
    # days * hours * minutes
    difference = difference.days * 24 * 60
    return difference

def convert(text):
    text = p.number_to_words(text, andword="")
    return text.capitalize() + " minutes"

if __name__ == "__main__":
    main()
