"""
picnic game where user must enter unique value to attend picnic

"""

picnic = ["water"]

print("The picnic game is starting. The first item in the picnic is " + picnic[0])

gameOver = False

while not gameOver:

    # ask the user enter all previously existing items in the picnic
    prev_existing = picnic[:]
    num_prev_existing = len(prev_existing)
    while len(prev_existing) > 0 and not gameOver:
        answer = input(f"Enter previous item ({len(prev_existing)} remaining)")

        if answer in prev_existing:
            print("Yes", answer, "is in the picnic")
            prev_existing.remove(answer)
        else:
            print("Sorry, but your memory has failed you")
            gameOver = True

    if len(prev_existing) != 0:
        continue

    item = input("Enter a unique item to bring to the picnic: ")

    if item in picnic:
        print("Eh! The item of", item, "is already in the picnic. You lose!")
        gameOver = True
        continue

    picnic.append(item)
    print("\n" * 30)