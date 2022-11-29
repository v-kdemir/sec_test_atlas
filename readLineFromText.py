import git

# Define the name of the file to read from
filename = "xss_payload"
# Open the file for reading
filehandle = open(filename, 'r')
while True:
    # read a single line
    line = filehandle.readline()
    if not line:
        break
    print(line)
    repo.git.add('--all')  
    repo.git.commit('-m', line , author='kdemir@valven.com')
    origin = repo.remote(name='sec_test_atlas.git')
    origin.push()

# Close the pointer to that file
filehandle.close()
