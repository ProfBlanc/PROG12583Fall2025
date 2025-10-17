grades = list()

grades.append(
    {
        "course": "python",
        "grade": 90
    }
)
grades.append(
    
    {
        "course": "english",
        "grade": 80
    }
)
grades.append(
    {
        "course": "french",
        "grade": 70
    }
)

grade_total = 0

for grade in grades:
    print(grade)
    grade_total += grade["grade"]

print(grade_total)