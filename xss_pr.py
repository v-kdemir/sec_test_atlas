#!/uisr/bin/env python
import git
import os
import requests

# To initiate new Git repo in the mentioned directory
os.chdir('/home/kdemir/Documents/py')
print("Current working directory: {0}".format(os.getcwd()))

#import pdb; pdb.set_trace();
# Define the name of the file to read from
filename = "xss_payload"
pyfile="test.py"
url="https://api.github.com/repos/v-kdemir/sec_test_atlas/pulls"

# Open the file for reading
filehandle = open(filename, 'r+')
while True:
    # read a single line
    line = filehandle.readline()
    if not line:
        break
    print( line)
    os.system('git pull')
    with open(pyfile, "a+") as f:
        f.write("a")
    #import pdb; pdb.set_trace()
    os.system('git add test.py')
    os.system('git commit -m' + 'commit')
    os.system('git push')
    os.system('git fetch --all')
    os.system('curl \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer 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" \
  https://api.github.com/repos/v-kdemir/sec_test_atlas/pulls" \
  d {\"title\":' + '\"' + line + '\"' + ',\"body\":' + '\"' + line + '\"' + ',\"head\":"main",\"base\":"test"}')
    payload={}
    headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer <YOUR-TOKEN>'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text + "pr_list")
    f.close()
# Close the pointer to that file
filehandle.close()
