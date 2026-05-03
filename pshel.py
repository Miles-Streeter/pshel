import os
import sys

# Grabs list of existing commands on open
# TODO: Maybe make this write to a settings file so it doesn't have to check each time the shell opens
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

    curdir = os.getcwd()
    line = input(curdir + "#> ")
    line_tokens = line.split(" ")

    if line_tokens[0] in existing_cmds:
        os.system(line)
    elif line_tokens[0] == 'cd':
        dir_nav(line_tokens[1])
    elif line_tokens[0] == 'exit':
        quit()

