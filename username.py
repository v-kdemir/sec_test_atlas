import os

# To initiate new Git repo in the mentioned directory
os.chdir('/home/kdemir/Documents/Github/sec_test_atlas')

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
    os.system('git checkout main')
    os.system('git add test.py')
    os.system('git config  user.name ' +  '"'+  line + '"'  )
    os.system('git config  user.email ' +  '"'+  line + '"'  )
    os.system('git commit -m "comm" --author ' + '\"'+line + '\"' +" " + '\"'+  line + '\"')
    os.system('git push')
    
# Close the pointer to that file
filehandle.close()
