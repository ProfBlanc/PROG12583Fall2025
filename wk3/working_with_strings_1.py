"""
a string is a collection of characters
collection = series
"""

name = "Ben Blanc"
"""
string      B   e   n       B   l   a   n   c

index       0   1   2   3   4   5   6   7   8
position
location
            -9  -8  -7  -6  -5  -4  -3  -2  -1

"""
print(len(name))
print(name[1-1])
# print out 'l' in name
print(name[-4], name[5])
# print "Ben" from string "Ben Blanc"
print(name[0:3])
print(name[-9:-6])
# string slicing
# [starting_index:exclusive_ending_index:step]
# default values
# starting_index: 0
# ending index: len(string)
# step : 1
print(name[0:7:2]) # BnBa

print("B" in name)
print(" " in name)
print("d" in name) 


print(  chr(66) )

print(ord("Z"))