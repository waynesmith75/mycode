#!/usr/bin/env python3

switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}
print(switch["hostname"])
print(switch["ip"])

# request fake key
#print(switch["lynx"])

# request fake key with .get() method
print("First test - .get()")
print(switch.get("lynx"))

print("Second test - .get()")
print(switch.get("lynx", "THE KEY IS IN THE OTHER CASTLE"))

print("Third test - .get()")
print(switch.get("version"))


print("Fourth test - .keys()")
print(switch.keys())

print("Fifth test - .values()")
print(switch.values())

print("Sixth test - .pop()")
switch.pop("version")  # removes this key (and value) pair
print(switch.keys()) # notice the value of version is gone
print(switch.values()) # notice the value 1.2

print("Seventh test - ADD a new value")
switch["adminlogin"] = "kar108"
print(switch.keys())
print(switch.values())

print("Eight test - ADD a new value")
switch["password"] = "qwerty"
print(switch.keys())
print(switch.values())

        
