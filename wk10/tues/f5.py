def student(name, student_number, **hobbies):
    print("name =", name)
    print("student_number=", student_number)

    for k, v in hobbies.items():
        print(k, "=", v)


student(name="Honor Roll Student", student_number=12345, 
        collecting="cards", watching="tv series")
