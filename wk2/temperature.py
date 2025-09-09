# temperature.py
# ask the user for a temperature
# determine if the temperature is hot, cold or neutral

answer = input("Enter a temperature: ")

temperature = int(answer) # convert answer into an integer

if temperature == 0:
    print("Neutral temperature")
elif temperature > 0: 
    print("Hot temperature")
else: 
    print("Cold temperature")

print("""Hi
Second Line
Third Line
""")

print("Hi " \
"Second Line" \
"Third Line")

print("My friend said, 'You are a cool prof!' - end")
print('My friend said, "You are a cool prof!" - end')

#name = 100

first_name = "Ben"  # snake case
firstName = "Ben"  # camelCase 
