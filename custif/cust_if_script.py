#!/usr/bin/env python3

message = "Your internet service is "

connection = input("What is your internet service speed in Mbps?")


if connection=="":
    print("You didn't provide any input.")
    exit()

if float(connection) == float:
    connection = int(round(connection))

connection_int = int(connection)


if  connection_int >= 500:
    message = message + "awesome!"
elif connection_int >= 250:
    message = message + "steller."
elif connection_int >= 100:
    message = message + "not bad."
elif connection_int >= 25:
    message = message + "barely considered broadband."
else:
    message = message + "not sufficient. Find another provider."
print(message)


