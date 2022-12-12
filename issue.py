import os

# To initiate new Git repo in the mentioned directory
os.chdir('/home/kdemir/Documents/py')

filename = "sql_injection_payload"
pyfile = "test.py"

# Open the file for reading
filehandle = open(filename, 'r+')
while True:
    # read a single line
    line = filehandle.readline()
    if not line:
        break
    print(line)
    os.system('gh issue create --title ' + '"' + line +'"' + ' --body '+ '"'+  line + '"'  )
    os.system('git push')
    os.system('git fetch')
# Close the pointer to that file
filehandle.close()

