"""
method aka action

string method => action on a string
syntax
string_value or variable.method_name()
"""

name = "Ben Blanc"
print(name.upper())

name = "john smith"

print(name.title())
name = "Ben Blanc"

print(name.swapcase())

name = name.swapcase()
print("B" in name)

print(name.startswith("A"))
print(name.endswith("c".upper()))