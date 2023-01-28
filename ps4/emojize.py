# https://cs50.harvard.edu/python/2022/psets/4/emojize/
import emoji

input = input("Input: ")

print("Output:", emoji.emojize(input, language='alias'))
