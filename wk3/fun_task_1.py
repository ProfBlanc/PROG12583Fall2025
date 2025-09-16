"""
Ask the user for their name
Transform their name into a proper title

Determine if all characters of the name are alphabetical
Determine if there is a space in their name
Find the position/index of the space in their name

"""
name = input("Enter your name: ")
name = name.title()
is_alphabetical = name.isalpha()
has_space = " " in name
position_of_space = name.index(" ")

print(name, is_alphabetical, has_space, position_of_space)
