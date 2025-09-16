"""
ask the user for two numbers
output the remainder of quotient of two numbers
n1 / n2, has a remainder of result
% = modulus => the remainder of division statement
"""

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

result = round(n1 % n2, 2)

print(f"{n1} / {n2} has a remainder of", result )