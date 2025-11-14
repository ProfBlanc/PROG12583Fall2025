from common_vars_between_tasks1_and_2 import root_path
import random

filename_odd_numbers = "odd.txt"
filename_even_numbers = "even.txt"

file_odd = open(root_path + filename_odd_numbers, "a")
file_even = open(root_path + filename_even_numbers, "a")


def main():
    numbers = list()

    for i in range(10):
        numbers.append(random.randint(1, 100))

    for num in numbers:
        if num % 2 == 0:
            file_even.write(str(num) + "\n")
        else:
            file_odd.write(str(num) + "\n")

if __name__ == "__main__":
    main()