#!/usr/bin/env python3

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test True
if ipchk:
    print("Looks like an IP address was set: " + ipchk)
else: # if data is not provided
    print("You did not provide input.")

