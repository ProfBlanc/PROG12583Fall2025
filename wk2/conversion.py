
"""
each data type in python has a method that can convert a value to a target data type


str()       any data type to string
int()       string to int
float()     string to float
bool()      any to boolean

what is boolean? a data type that represents yes or no, on or off, positive or negative
                True or False


"""

value_1 = "1"
value_2 = int(value_1)
value_3 = float(value_1)
value_4 = bool(value_1)  # if the value is empty => False. Any other value => True

value_5 = float(value_2)
value_6 = int(value_5)  # to convert float to int, float values must be whole number (#.0)

print(value_1, value_2, value_3, value_4)