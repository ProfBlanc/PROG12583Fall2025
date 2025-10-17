"""
Ask the user to enter 3 distinct values
Determine if the user entered 3 distinct values

"""
print("You will enter 3 distinct values")

num_times = 3
values = set()
for i in range(num_times):
    val = int(input(f"Enter value {i + 1} of {num_times}: "))
    values.add(val)

if len(values) == num_times:
    print("Congrats! You entered 3 distinct values")
else:
    print(f"Sorry, but you only entered {len(values)} distinct values")