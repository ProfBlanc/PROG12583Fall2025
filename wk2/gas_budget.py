"""
Version 1
Ask the user to the price of gas
Ask the user how much money they want to spend on gas
Output the amount of litres

Version 2
Ask the user the price of gas
Ask the user how large is their gas tank
Output how much money it will cost to fill up their gas tank

"""

# ask user for the price of gas
gas_price = float(input("What is the price of gas? "))

# ask user how much money they plan on spening on gas
budget_price = float(input("How much money do you plan on spending on gas? "))

# calculate amount of litres
litres = round(budget_price / gas_price, 2)

# output the output the liters
print(f"With a gas price of {gas_price} and a budget of {budget_price}, you can put {litres} litres of gas in your car")