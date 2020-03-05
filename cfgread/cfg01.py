#!usr/bin/env python3

######## EXPLORE READ ########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## disply file to the screen - .read
print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ########
## recreate file object to explore ne method
configfile = open("vlanconfig.cfg", "r")

## make list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

## Iterate through configlist
for x in configlist:
    print(x)

## Always close your file
configfile.close()

