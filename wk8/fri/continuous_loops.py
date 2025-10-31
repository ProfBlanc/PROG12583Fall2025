num_list = []
for i in range(1000000000):
    num = input("Enter a non-negative number: " )
    if num.isdigit():
        num = int(num)
        if num < 0:
            print("Error! You did not input a non-negative number")
            break
    else:
        print("Invalid number inputted")
        break
    
    num_list.append(num)

print("*" * 100)
keep_running = True
nums_list_2 = list()
while keep_running:
    num = input("Enter a non-negative number: ")
    if num.isdigit() and int(num) >= 0:
        nums_list_2.append(int(num))
    else:
        print(num, "is invalid")
        keep_running = False

print(num_list, nums_list_2, sep='\n')