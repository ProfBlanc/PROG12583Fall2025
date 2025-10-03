"""
Ask the user to guess a vowel in a randomly generated name
Tell the user if the vowel is found in the name
If found, tell user the position of vowel
"""
import random

names = "Ben,John,Mary,Tiffany,Bob,Ashley,Frank,Jennifer,Lisa".split(",")
print(names)

selected_name = random.choice(names)
print(selected_name)
print(f"The randomly selected name has {len(selected_name)} letters")
vowel = input("Guess a vowel in the name: ")[0].strip().lower()

allowable_vowels = tuple("aeiou")  # ('a', 'e', 'i', 'o', 'u')
if vowel not in allowable_vowels:
    exit(f"Sorry but {vowel} is not a vowel")

if vowel in selected_name.lower():
    print(vowel, "was found", selected_name.count(vowel), " time(s) in our name")
    print("Can you guess the name with the following hint")
    print(selected_name.replace(vowel, "_"))
    guess = input().lower()
    if guess == selected_name.lower():
        print("Congrats! You correctly guessed the name")
    else:
        print("Sorry, but that isn't the correct name")
else:
    print("The vowel", vowel, "is not in the name.")
    print("The name was", selected_name)