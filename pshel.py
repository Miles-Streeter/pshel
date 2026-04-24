import os
import sys

# TODO: make list of already existing linux commands
existing_cmds = os.listdir("/bin/")

# TODO: make some functions
def dir_nav(area):

    if area == '..':
        try:
            os.chdir('..')    
        except:
            print(f"{area} Not Found")

# TODO: make a function that creates some environment variables


# TODO: make loop to take input
while True:

    line = input("#> ")
    line_tokens = line.split(" ")

    if line_tokens[0] in existing_cmds:
        os.system(line)
    
    

