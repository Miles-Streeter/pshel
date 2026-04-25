import os
import sys

# TODO: make list of already existing linux commands
existing_cmds = os.listdir("/bin/")

# remade cd command
def dir_nav(area):

    if area == '..':
        try:
            os.chdir('..')    
        except:
            print(f"{area} Not Found")
    else:
        try:
            os.chdir(area)
        except:
            print(f"Unable to move to {area} directory")



# TODO: make loop to take input
while True:

    line = input("#> ")
    line_tokens = line.split(" ")

    if line_tokens[0] in existing_cmds:
        os.system(line)
    elif line_tokens[0] == 'cd':
        dir_nav(line_tokens[1])
    
    

