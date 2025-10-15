# break = stop the loop
# continue = skip the rest of the loop

"""
continually ask user for a number until they input an odd number
"""

#number = 0

while True:
    num = int(input("Enter an odd number: "))
    if num % 2 == 1:
        print("Congrats, you entered an odd number")
        break
    else:
        print("You did not enter an odd number. Pleae try again!")
