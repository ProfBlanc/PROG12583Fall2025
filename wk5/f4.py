empty1 = []
empty2 = list()

# either or, creates an empty list

values = [1, "1", True, 1.0]
# list actions = list methods
# find
print("1" in values)  # True
print(1 in values)  # True
print('o' in "John")  # True

# remove
values.remove(1)
print(values)
to_remove = 2
if to_remove in values:
    values.remove(to_remove)

# locate the index (position of value)
print(values.index("1"))  # 0. WARNING: may return error if not found

values.append(2)  # add at the end
values.append("2")
values.insert(1, "overridding index 1 value")
print(values)

# editing/overriding a value at a specified index
values[1] = "new value"

# copying list values
#second_list = values[0:len(values)]  # copy the VALUES of the list
second_list = values[:]  # copy the VALUES of the list
print(second_list)
values.append(100)
print(second_list)
values.remove("1")
print(second_list)

third = values + second_list
print(third)
print("*" * 10)
fourth = third[:3] * 2  # 2 items: item1, item2, item3, item1, item2, item3
print(fourth)

# Be back at 9:15
