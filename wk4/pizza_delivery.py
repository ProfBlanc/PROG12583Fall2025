"""
Allow the user to order a pizza
Choose between sizes: S, M, L pizza
input the toppings separated by a comma
input how far away they live from the pizza store
generate a bill
    base price for pizza: 5
        add 1 dollar for medium & 2 dollars for L pizza
    1-topping: free, 2 dollars per addition topping
    Charge 25 cents per KM. We will not travel more than 25K

    Outline the charges => total + tax (13%) => Grand Total
"""

print("Welcome to our Pizza Delivery Restaurant/App")
print("You will enter the size of the pizza, the amount of toppings,", end=" ")
print("the distance between this restaurant and your home, and we will", end=" ")
print("calculate the bill")

print("\n" * 2)  # \t => a tab aka 4 spaces    \ = escape sequence. What are you escaping: output the literal value iso programming
#print("\\", "He said, \"Hi There!\" to the stranger")

#available_sizes = tuple("SML") => ("S", "M", "L")
available_sizes = ("(S)mall", "(M)edium", "(L)arge")  # tuple => a collection of values that are IMMUTABLE (unchangeable)
available_toppings = "Cheese,Chicken,Green Peppers,Peperoni".split(",")  # transforms string into a list. why? just for practice

display_available_sizes = ", ".join(available_sizes)
display_available_toppings = ", ".join(available_toppings)

chosen_size = input(f"Enter your pizza size from one of these {len(available_sizes)} options: {display_available_sizes}: ")
chosen_toppings = input(f"Enter your toppings, separated by a comma(,).\nPossible options are {display_available_toppings}:")
distance_from_restaurant = input("Enter your distance in KM from our restaurant: ")

#list() is similar to int() or float() or str() for bool() => converts string to a list data type
#list data type is a collection of values, where each value is stored an a position (index)
#list("SML")  => ["S", "M", "L"]
# validate
chosen_size = chosen_size.upper()
if chosen_size[0] not in list("SML"):
    exit("Error! Invalid Pizza Size chosen")

summary_of_chosen_toppings = chosen_toppings.split(",")  # create a list of chosen toppings
number_of_chosen_toppings = len(summary_of_chosen_toppings)

if number_of_chosen_toppings > len(available_toppings):
    exit(f"You entered {number_of_chosen_toppings} toppings, however, the max amount of toppings is {len(available_toppings)}!")

if not distance_from_restaurant.isdigit():
    exit("Invalid distance entered")

distance_from_restaurant = int(distance_from_restaurant)

if distance_from_restaurant <= 0 or distance_from_restaurant > 25:
    exit(f"Sorry, but our drivers cannot delivery to your home because {distance_from_restaurant} km is too far")

base_price = 5
price_per_topping = 2
price_per_km = 1/4

total_price = base_price


if chosen_size[0].upper() == "M":
    size_price = 1
elif chosen_size[0].upper() == "L":
    size_price += 2
else:
    size_price = 0

total_price += size_price

toppings_price = number_of_chosen_toppings * price_per_topping
total_price += toppings_price

distance_price = round(distance_from_restaurant * price_per_km, 2)

total_price += distance_price

just_size = 24

print("Description".ljust(just_size), "Value".ljust(just_size), "Price".rjust(just_size))

#print("Hello".ljust(just_size), "World".rjust(just_size))

print("Pizza Size".ljust(just_size), chosen_size.ljust(just_size), f"${size_price}".rjust(just_size))

print("Pizza Toppings".ljust(just_size), chosen_toppings[:24].ljust(just_size), f"${toppings_price}".rjust(just_size))

print("Distance".ljust(just_size), f"{distance_from_restaurant} KM".ljust(just_size), f"${distance_price}".rjust(just_size))
print("Grand Total ".ljust(just_size), "".ljust(just_size), f"${total_price}".rjust(just_size))