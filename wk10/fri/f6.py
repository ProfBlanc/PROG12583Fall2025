from f4 import filename_odd_numbers, root_path

def main():
    with open(root_path + filename_odd_numbers, "r") as file:
        # contents = file.read()
        # print(contents)
        ########################
        # while(True):
        #     line = file.readline()
        #     if len(line) == 0:
        #         break
        #     print("Line Content =", line.strip())
        ########################
        contents_line_by_line = file.readlines()
        print(contents_line_by_line)
        for line in contents_line_by_line:
            print(line.strip())

if __name__ == "__main__":
    main()