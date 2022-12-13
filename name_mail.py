import os

# To initiate new Git repo in the mentioned directory
os.chdir('/home/kdemir/Documents/Github/sec_test_atlas')
print("Current working directory: {0}".format(os.getcwd()))

#import pdb; pdb.set_trace();
# Define the name of the file to read from
filename = "ldap_payload"
pyfile="testt.py"

# Open the file for reading
filehandle = open(filename, 'r+')
while True:
    # read a single line
    line = filehandle.readline()
    if not line:
        break
    print( line)
    os.system('git checkout main')
    os.system('git config  user.name ' +  '"'+  line + '"'  )
    os.system('git config  user.name ' )
    os.system('git config  user.email ' +  '"'+  line + '"'  )
    os.system('git config  user.email ')
    os.system('git add test.py')
    os.system('git commit -m "comm"')
    os.system('git push')

# Close the pointer to that file
filehandle.close()

