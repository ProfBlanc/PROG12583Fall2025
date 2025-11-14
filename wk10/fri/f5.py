from common_vars_between_tasks1_and_2 import root_path


def main():
    lines = list()

    lines.append("Hello World\n")
    lines.append("I love python\n")
    lines.append("End of paragraph\n")

    filename = "paragraph1.txt"

    with open(root_path + filename, "w") as file:
        #file.writelines(lines)
        for line in lines:
            file.write(line)

if __name__ == "__main__":
    main()