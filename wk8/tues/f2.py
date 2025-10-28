people = dict()

names = list()
heights = list()

for i in range(3):
    name = input(f"Enter name of person {i + 1}: ")
    height = int(input(f"Enter the height of {name}: "))

    names.append(name)
    heights.append(height)

    people[name] = height


people1 = {

    names[0]: heights[0],
    names[1]: heights[1],
    names[2]: heights[2]
}
peoples2 = dict.fromkeys(names)  # 
peoples2[names[0]] = heights[0]
peoples2[names[1]] = heights[1]
peoples2[names[2]] = heights[2]

print(people, people1, peoples2, sep='\n')

values = people.values()
avg_height = sum( values    )  / len(values)

shortest_value = min(values)
tallest_value = max(values)
print(shortest_value, tallest_value)

