"""

Ask the user for a season: winter, fall, spring, summer
Ask the user for a month: jan, feb, etc

Determine if the season and month combo exists

season: winter
month: sept
    False

"""
season = input("Enter the season: ").lower()
month = input("Enter the month: ").lower()[:3]

print(season, month)

if season[0] == "w":
    if month.startswith("d") or month.startswith("ja") or month.startswith("f"):
        print(f"{month.title()} is a valid month for the season {season.title()}")
    else:
        print(f"Sorry, but the month of {month} is not in the Winter season")
        
elif season[0]  == "f" and month == "sep" or month == "oct" or month[0] == "n" or month.startswith("d"):
    print("Valid fall month")
elif season[:2] == "sp":
    pass
else:
    pass