"""
picnic game where user must enter unique value to attend picnic

"""

picnic = list()

while True:
    item = input("Enter a unique item to bring to the picnic: ")

    if item in picnic:
        print("Eh! The item of", item, "is already in the picnic. You lose!")
        break

    picnic.append(item)
    print("\n" * 30)