#!/usr/bin/env python3
user_input = input("Please endter an IPv4 address:")

##the line below creates a single string that is passed to print()
# print("You told me the IPv4 address is:" + user_input)

##print() can be given a series of objects seperated by a comma
print("You told me the IPv4 address is:", user_input)

user_input_vendor = input("Please enter the vendor name associated with the device:")
print("You told me the vendor name is:" + user_input_vendor)


