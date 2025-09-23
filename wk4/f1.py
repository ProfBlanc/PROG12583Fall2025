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
if temp > 0:
    print(temp, "is a hot temperature")
elif temp < 0:
    print(f"{temp} is a cold temperature") #f-string
else:
    print(str(temp) + " is a neutural temperature")




