import os

# To initiate new Git repo in the mentioned directory
os.chdir('/home/kdemir/Documents/Github/sec_test_atlas')
print("Current working directory: {0}".format(os.getcwd()))

#import pdb; pdb.set_trace();
# Define the name of the file to read from
filename = "ldap_payload"
pyfile="test.py"

# Open the file for reading
filehandle = open(filename, 'r+')
while True:
    # read a single line
    line = filehandle.readline()
    if not line:
        break
    print( line)
    with open(pyfile, "a+") as f:
        f.write("a")
    os.system('git add test.py')
    os.system('git commit -m' + '"' + line +'/'+ '"')
    os.system('git push')
    f.close()

# Close the pointer to that
filefilehandle.close()
