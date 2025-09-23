"""
Ask the user for a temperature
Determine if the temperature is hot, cold or netural
"""
# ask user for temp
# convert temp to a number
# determine whether number is hot, cold or neutural
temp = float(input("Enter a temperature: "))

"""
if <boolean expression>:
    statements
"""
output = " is a "
if temp > 0:
    output += "hot"
elif temp < 0:
    output += "cold"
else:
    output += "neutral" # output = output + "neutural"

output += " temperature"
print(f"{temp}{output}")

