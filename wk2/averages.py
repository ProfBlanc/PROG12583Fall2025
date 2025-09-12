"""
Ask the user for 3 numbers NOT using loops
Calculate the average of these three numbers
"""

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

lowest = min(n1, n2, n3)  # find the lowest value
highest = max(n2, n1, n3)

avg = (n1 + n2 + n3) / 3  # right?

avg = round(avg, 1)

print(avg)
print("Lowest =", lowest, "Highest=", highest)