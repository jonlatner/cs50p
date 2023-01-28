# https://cs50.harvard.edu/python/2022/psets/7/watch/

import re
import sys

string = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
string = '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
x = re.search(r'(?=src)src=\"(?P<src>[^\"]+)', string).group(1)
x = x.replace("embed/","")
print(string)
print(x)
