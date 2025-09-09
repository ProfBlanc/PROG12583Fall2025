# intro.py
# similuating two peoeple having a converation
# YOU will be person1
# The user will be person2
# person1 will introduce themself by greeting and asking for 
# person2's name

"""
person2 will answer the question
person1 will say that it was nice to meet person2
person2 will ask the age of person1
person2 will state that person1 was X years old 10 years ago
"""
person1 = "Ben"
person2 = "computer"
"""
person1, person2 = "Ben", "cpu"

print("Hi, my name is", person1)  #print arguments
print("Hi, my name is " + person1)  # concatenation




print("Hi", 1, 2.2, person1, person2)

#print("Hi" + 3.3)
print(1 + 3.3)

# string formatting
print(f"Hi, my name is {person1}. I am { 5 * 6} years old")

print("Hi, my name is", person1, ". I am", 6*5, "years old")

print("Hi, my name is " + person1 + ". I am " + str(6 * 5) +\
" years old")
"""

print("Hi, my name is", person1)
person2 = input("What is your name? ")
print(f"Nice to meet you, {person2}")
#person1_age = input("How old are you, " + person1 + "? ")
#person1_age = int(person1_age)
person1_age = int(input("How old are you, " + person1 + "? "))

half_person1_age = person1_age / 2  # ERROR!
value_as_float = float(person1_age)
print(f"Nice. Guess what, {person1}. Ten years ago, you were "\
f"{person1_age - 10} years old" )

