name = "John Smith"

for letter in name:
    print(letter, end='\t')

print("*" * 10)



for index in range(len(name)):
    letter = name[index]
    print(f"Index {index} has letter {letter}")