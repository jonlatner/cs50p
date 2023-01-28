# https://cs50.harvard.edu/python/2022/psets/7/response/

from validator_collection import validators, checkers, errors

email = "test@domain.edu"

if checkers.is_email(email) == True:
    print("Valid")
else:
    print("Invalid")
