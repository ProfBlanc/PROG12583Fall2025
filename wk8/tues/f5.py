user1 = {}
user2 = {}
users = [user1, user2]
keys = "birth_year,fav_colour".split(",")
number_of_times_to_ask_user = 2
for user in users:
    for i in range(number_of_times_to_ask_user):
        name = input("Enter a name: ")
        birth_year = int(input("Enter a birth year: "))
        fav_colour = input("Enter a favourite colour: ")
        user[name] = {keys[0]: birth_year, keys[1]: fav_colour}
    print("End of 1 user info")
    print("*" * 10)

print(user1, user2, sep='\n')

fav_colours = set()
for user in users:
    for data in user.values():
        fav_colours.add(data[keys[1]])

print("Fav Colors", "=", fav_colours)