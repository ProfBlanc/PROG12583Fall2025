from common_vars_between_tasks1_and_2 import *


def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")

    file1 = open(root_path + filename_first_name, "w")
    file1.write(first_name)

    open(root_path + filename_last_name, "w").write(last_name)

    with open(root_path + filename_age, "w") as file3:
        file3.write(age)

if __name__ == "__main__":
    main()