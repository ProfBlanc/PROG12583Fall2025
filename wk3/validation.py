"""
Ask the user to input their name
ensure name contains 1 space char
ensure that the first character of each name is capitalized
"""

answer = input("Enter your first and last name, separated by a space: ")

print("You entered the value of", answer)


"""
and    =>   combine, join, add additional boolean expression
            all boolean expressions must be true


            1 + 3 + 5 + 7

"""


if " " in answer and answer.count(" ") >= 1 and answer.istitle():
    print("Congratulation, you correctly followed the instructions")
else:
    print("Nope! Sorry! Try again")