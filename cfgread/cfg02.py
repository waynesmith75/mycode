#!usr/bin/env python3

######## EXPLORE READ ########
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    configlist = configfile.readlines()



print(configlist)



