from common_vars_between_tasks1_and_2 import *

def main():

    fn = open(root_path + filename_first_name, "r").read()
    ln = open(root_path + filename_last_name).read()
    age = open(root_path + filename_age).read()

    print(f"First name = {fn}, Last name = {ln}, Age = {age}")

if __name__ == "__main__":
    main()