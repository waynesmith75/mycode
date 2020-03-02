
#!/usr/bin/env python3

# create a list containing three items
my_list = ["192.18.0.5", 5060, "UP"]

# display the first item in the list
print("The first item in the list (IP): " + my_list[0] )

# display the second item in the list
print("The second item in the list is (port): " + str(my_list[1]) )

# Display the last item in the list
print("The last item in the list (state): " + my_list[2] )

new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

#Display the new sentence
#split into multi-line for readability
print("When I " + new_list[5] + " into IP addresses " + new_list[3])
print("or " + new_list[4] + "I am unable to ping ports")
print(str(new_list[0]) + ", " + new_list[1] + ", or " + str(new_list[2]))


