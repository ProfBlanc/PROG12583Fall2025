# version 1
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))
# version 2
nums = list()
for i in range(3):
    nums.append(int(input("Enter number")))

# version3
def get_user_input():
    num = int(input("Enter a number: "))
    return num



nums2 = list()

for i in range(3):
    num2.append(get_user_input())
