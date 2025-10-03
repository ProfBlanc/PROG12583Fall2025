"""
Ask the user for 3 inputs

Determine if input is 
    int,
    float,
    string

if input is int or float => typecast it (trasnform it to target data type)
Add input to a list of items
Bonus: only add if value is unique


"""

item1 = input("Enter first item: ")
item2 = input("Enter second item: ")
item3 = input("Enter third item: ")

user_inputs = list()
user_inputs.append(item1)
user_inputs.append(item2)
user_inputs.append(item3)

# if it has a decimal, it's a float

# if all chars are 0 to 9


values = []

for item in user_inputs:
    print("evaluating item", item)
    single_value = None  # official absence of a value

    if "." in item and item.count(".") == 1:
        single_value = float(item)
    elif item.isdigit() or ("-" in item and item.index("-") == 0 and item[1:].isdigit()):
        single_value = int(item)
    else:
        single_value = str(item)  # redundant 

    if single_value not in values:
        values.append(single_value)


print(values)