#!/usr/bin/env python3

message = "Your internet service is " # The movie is about to begin, we recommed "

# wrap connection in a Float() to accept decimals as numbers
connection = float(input("What is your connection speed in Mbps?"))

#if input value was higher or equal to 25
if connection >= 500:
    message = message + "awesome!"
elif connection >= 250:
    message = message + "steller."
elif connection >= 100:
    message = message + "not bad."
elif connection >= 25:
    message = message + "barely considered broadband."
else:
    message = message + "not sufficient. We recommend finding a new provider."
print(message)


