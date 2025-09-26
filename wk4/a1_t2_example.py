value1 = "123"
value2 = 456

#op = input("Enter an operator: ")

if type(value1) == str:
    print("value1 is a string")

if isinstance(value2, int):
    print("value2 is an int")

value3 = 1234
if isinstance(value3, (int,float)):
    print("value3 is either the int or float data type")