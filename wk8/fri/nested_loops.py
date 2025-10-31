"""
Ask the user to enter a number

Input: 5

1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25

"""

num = int(input("Enter a number: "))

for row in range(1, num + 1):
    for column in range(1, num + 1):
        pass
        # What do put here?
        if row > 1 and row == column:
            print("X" * len(str(row * column)) , end='\t')
        else:
            print(row * column, end='\t')
    print() # move to next line

# How would I replace square numbers with the X for all numbers gt 2