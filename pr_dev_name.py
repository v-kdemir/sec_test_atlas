import git
import os

os.chdir('/home/kdemir/Documents/Github/sec_test_atlas')
print("Current working directory: {0}".format(os.getcwd()))

filename = "command_injection_payload"
pyfile = "test.py"

filehandle = open(filename, 'r+')
while True:
    lines = filehandle.readlines()
    count=1100
    if not lines:
        break
#    import pdb; pdb.set_trace();
    for line in lines:
        count+=1
#        os.system('git auth login --with-token < token.txt')
        os.system('git fetch --all')
        os.system('git checkout ' + str(count))
        os.system('git pull')
        with open(pyfile, "a+") as f:
            f.write("a")
        os.system('git add test.py')
        os.system('git config  --global --replace-all  user.name ' +  '"'+  line + '"'  )
        os.system('git config --global --replace-all  user.email ' +  '"'+  line + '"'  )
        print('it config user.name')
        print('it config user.email')
        os.system('git commit -m "diff user"')
        os.system('git push --set-upstream origin ' + str(count))
        print('gh pr create -B main -H  ' + str(count) + ' --title diff --body body ')
        os.system('gh pr create -B main -H  ' + str(count) + ' --title diff --body body' )
f.close()
filehandle.close()
