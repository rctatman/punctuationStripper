__author__ = 'rctatman'

# this simple program removes all the punctuation except for . and ' from every .txt file in the directory it's run in

import re, glob, os

os.chdir("./")
print("The following files had their puncutation removed:")
for file in glob.glob("*.txt"):
    print(file)
    with open(file, 'r+') as f:
        s = f.read()
        s = re.sub('[^0-9a-zA-Z\s\.]+','',s)
        f.truncate(0)
        f.write(s)
