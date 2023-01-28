# https://cs50.harvard.edu/python/2022/psets/1/extensions/

# get user input
# if gif or png or jpg or jpeg, print "image/type"
x = input("File name: ").lower()

# remove spaces and make it lower
if ".gif" in x:
    print("image/gif")
elif ".png" in x:
    print("image/png")
elif ".jpg" in x:
    print("image/jpeg")
elif ".jpeg" in x:
    print("image/jpeg")
# if pdf or zip, print "application/type"
elif ".zip" in x:
    print("application/zip")
elif ".pdf" in x:
    print("application/pdf")
# if txt, print "text/plain"
elif ".txt" in x:
    print("text/plain")
# otherwise, print "application/octet-stream"
else:
    print("application/octet-stream")

