"""
Ask the user to enter 3 odd numbers
If user adds 0 or an even number, reject the input and ask them to try again
When user has finished entering 3 odd numbers, output the min, max and average value of these numbers
-list
-loop
-if

"""
odd_numbers = list()
target_unique_values = 3

while len(odd_numbers) < target_unique_values:
    answer = input(f"Enter odd number {len(odd_numbers) + 1} of {target_unique_values}: ")
    num = int(answer)
    if num != 0 and num % 2 == 1 and num not in odd_numbers:
        odd_numbers.append(num)
        print("Number", num, "was added our our list")
    else:
        print("Sorry! Try again")

print("-" * 10)
print("Here are the numbers inputted")
for num in odd_numbers:
    print(num, end="\t")
print()
print("Max num =", max(odd_numbers), "Min num =", min(odd_numbers), "Avg = ", 
      round(sum(odd_numbers)/len(odd_numbers), 1))