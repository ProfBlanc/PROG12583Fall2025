student = dict()

student["student_id"] = 12345
student['name'] = 'Scholar Student'
student['age'] = 20
student['grade'] = [
    {
        "course": "python",
        "grade": 80
    },
    {
        "course": "english",
        "grade": 85
    },
]
print(student['student_id'])
print(student['grade'][0]['course'])
print(student['grade'][1])  # {"course": "english", "grade": 85}

#print(student)
#student['grade'] = "hello"
#print(student)
student['grade'].append("I love python")
print(student)
# update the python grade to 90
student['grade'][0]['grade'] = 90
print(student)
