# https://cs50.harvard.edu/python/2022/psets/6/shirt/

import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) == 3:
    before_file=sys.argv[1].lower()
    after_file=sys.argv[2].lower()
    try:
        if before_file.split(".")[1] == after_file.split(".")[1] and ((".png" in before_file and ".png" in after_file) or (".jpg" in before_file and ".jpg" in after_file) or (".jpeg" in before_file and ".jpeg" in after_file)):

            shirt = Image.open("shirt.png")
            before_pic = Image.open(before_file)

            before_pic = ImageOps.fit(before_pic, size = shirt.size)
            before_pic.paste(shirt, shirt)

            before_pic.save(after_file)

        else:
            sys.exit("Input and output have different extensions")
    except FileNotFoundError:
        sys.exit("File does not exist")


"""

"""