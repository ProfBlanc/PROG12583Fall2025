values = 0
text = list()

while values == len(text):
    answer = input("Enter any value: ").lower()
    if not answer == "stop":
        text.append(answer)

    values += 1


print("Here are the values entered")

for v in text:
    print(v)

