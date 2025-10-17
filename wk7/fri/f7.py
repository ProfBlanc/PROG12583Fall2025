"""
dictionary
    a data type that stores key-value pairs

set, list, tuple only stores values
["ben", "blanc"]

"""

person = dict()
person["firstname"] = "Ben"
person["lastname"] = "Blanc"

person1 = {
    "firstname": "Ben",
    "lastname": "Blanc"
}

person["middlename"] = "ProfBlanc"
person1["middlename"] = "ProfBlanc"

print(person, person1)
print(person["firstname"])

