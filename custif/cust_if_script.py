#!/usr/bin/env python3

message = "Your internet service is "

connection = float( input("What is your internet service speed in Mbps?"))


if connection=="":
    print("You didn't provide any input.")




if  connection >= 500:
    message = message + "awesome!"
elif connection >= 250:
    message = message + "steller."
elif connection >= 100:
    message = message + "not bad."
elif connection >= 25:
    message = message + "barely considered broadband."
else:
    message = message + "not sufficient. Find another provider."
print(message)


