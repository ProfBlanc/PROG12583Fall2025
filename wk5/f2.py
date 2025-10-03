values = [True, 1.234, 2, "Hello", [1,2,3.3, False] ]

print(len(values))  # number of values in list
print(round(len(values)/2))  # 2
print(values[round(len(values)/2)])

print(values[-1][2])  # 3.3