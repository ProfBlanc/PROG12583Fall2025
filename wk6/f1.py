"""
In python, there are two major loops
    FOR loop
        fixed amount of iteration (cycles)
        also iterate values of a collection (list, tuple, etc)

    WHILE loop
        iterations based on condition


"""

nums = list(range(1, 5))  # [1, 2, 3, 4]
# range(start,end,step)
# range(end): 0 -> end-1
#range(1, 11, 2) -> [1, 3, 5, 7, 9]

user_nums = list()
max_times = 5
for i in range(max_times):
    # print(i)
    user_nums.append(int(input(f"Enter number {i + 1} of {max_times}: ")))

print(user_nums)

"""
using a loop, ask the user for the name of 5 friends. Add the names to a list
outside the loop, print the 5 names that the user inputted.
"""