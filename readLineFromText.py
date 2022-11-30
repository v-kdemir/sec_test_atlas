import git
from git import Repo

# To initiate new Git repo in the mentioned directory
repo = Repo.init("home/kdemir/Documents/py/readLineFromText.py")

import pdb; pdb.set_trace();
# Define the name of the file to read from
filename = "xss_payload"

#open file to write
f = open("test.txt", "a+")

# Open the file for reading
filehandle = open(filename, 'r')
while True:
    # read a single line
    line = filehandle.readline()
    if not line:
        break
    print(f.read())
    f.write("test")
    print(f.read())
    repo.git.add('--all')  
    repo.git.commit('-m', 'test' )
    origin = repo.remote(name='main')
    origin.push()
f.close()

# Close the pointer to that file
filehandle.close()
