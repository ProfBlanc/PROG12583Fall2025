"""
using a loop, ask the user for the name of 5 friends. Add the names to a list
outside the loop, print the 5 names that the user inputted.
"""

num_times = 5
friends_list = list()

for i in range(num_times):
    the_friend = input(f"Enter friend {i + 1} of {num_times}: ")
    friends_list.append(the_friend)

print(friends_list)

"""
Create an app that 
    -stores the list of values of user-inputted provincial codes (ON, QC, AB, BC, etc)
Ask the user to enter the province codes for 5 provinces
Only add the provincial code IF the code is at least two digits and is unique
"""
