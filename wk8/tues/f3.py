people = {}

people['ben'] = 100
people['john'] = 110
people['mary'] = 120

print(people)

for p in people:
    print(p)

print("*" * 10)

for key in people.keys():
    print(key)

print("*" * 10)

for value in people.values():
    print(value)

print("*" * 10)

for data in people.items():
    print(data)

print("*" * 10)


for key, value in people.items():
    print(key, "=", value)

print("*" * 10)

shortest = min(people.values())
tallest = max(people.values())

shortest_person = ""
tallest_person = ""

for key, value in people.items():
    if value == shortest:
        shortest_person = key
    if value == tallest:
        tallest_person = key

print("The shortest person is", shortest_person)
print("The tallest person is", tallest_person)