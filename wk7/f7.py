num = 0

# while not num % 2 == 1
while num % 2 == 0:
    num = int(input("Enter an odd number: "))

    if num % 2 == 0:
        print("Sorry, but that number wasn't odd")

print("Congrats, the number", num, "is an odd number")