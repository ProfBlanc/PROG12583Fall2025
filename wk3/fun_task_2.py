"""
Ask the user for a num
Determine if all character are numerical
convert number to int
print(number squared)

"""

answer = input("Enter a number: " )
print(answer.isdigit()) # isnumeric/al()
answer = int(answer)
print(answer ** 2)