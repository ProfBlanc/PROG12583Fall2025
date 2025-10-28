"""
    course grades

        python      80
        english     90
        network     70

"""

course_grades = {
    "python": 80,
    "english": 90,
    "network": 70
}

print(course_grades['python'])  # 80

# get all of the keys
keys = course_grades.keys()   # ViewObject
print(type(keys))

# get all of the values of the dictionary
values = course_grades.values()
print(keys, values)

keys = list(keys)  
keys = set(keys)
keys = tuple(keys)

avg = sum(values) / len(values) 
print(avg)