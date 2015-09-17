__author__ = 'rctatman'

# this simple program removes all the punctuation except for . and ' from every .txt file in the directory it's run in

import re, glob, os

os.chdir("./")
for file in glob.glob("*.txt"):
    print(file)
    with open(file, 'r+') as f:
        s = f.read()
        s = re.sub('[^0-9a-zA-Z\s.\']+','',s)
        f.write(s)
