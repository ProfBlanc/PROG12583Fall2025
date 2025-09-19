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

if season[0] == "w" and month == "dec":
    print("Yes, december is in the winter season")
if season == "winter" and month[0:2] == "ja":
    print("Yes, january is in the winter season")
