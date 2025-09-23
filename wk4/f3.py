"""
ask user for their age
ask user for the number of tickets they want to buy
calculate the price
"""
age = int(input("Enter your age: "))
quantity = int(input("How many tickets? "))

base_price = int("20")
category = "adult"
if age <= 13:
    base_price /= 2  # base_price = base_price / 2
    category = "child"
elif age > 65 and age < 80 and 1 < -1 and "hi" != "bye":
    base_price /= 4
    category = "senior"
total = base_price * quantity
print(f"As a {category}, purchasing {quantity} tickets, costs {total}")
    


    
