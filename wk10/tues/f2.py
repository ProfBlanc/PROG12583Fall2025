def greet(intro="Hello", name="Friend"):
    return intro + " " + name


print(greet())
print(greet(intro="Hi", name="There"))
print(greet(name="Ben", intro="Salutations"))

"""
Create a function named add()
    adds two numbers together
        use 1 as default value for first number
        use 2 as default value for second number
Create a function named divide
    divides two numbers together
        user 10 as default value for first number
        use 1 as default value for second number
        evaluated 2nd number, if 0, change value to 1
"""

def add(n1=1, n2=2):
    return n1 + n2

def divide(n1=10, n2=1):
    n2 = 1 if n2 == 0 else n2
    return n1 / n2

print(add())
print(add(10))
print(add(n2=5))

print(divide(n2=2, n1=10))
print(divide(100))
print(divide(10, 0))
