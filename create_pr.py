import os

os.chdir('/home/kdemir/Documents/py')
print("Current working directory: {0}".format(os.getcwd()))

filename = "sql_injection_payload"
pyfile = "test.py"

filehandle = open(filename, 'r+')
while True:
    lines = filehandle.readlines()
    count=1000
    if not lines:
        break
#    import pdb; pdb.set_trace();
    for i in range(1,1000,1):
        count+=1
        os.system('git branch ' + str(count))
        os.system('git push')
        os.system('git pull')

