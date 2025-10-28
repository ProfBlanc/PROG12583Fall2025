for i in range(2):
    data = input("Enter name, birth year and favourite colour all separated by a comma: ")
    data = data.split(",")
    if len(data) != 3:
        print("Error!")
    else:
        for d in data:
            print(d)