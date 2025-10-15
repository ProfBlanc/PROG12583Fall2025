
times = 3

for time in range(times):

    pwd = input(f"Enter password {time + 1} of {times}: ")

    num_characters = len(pwd)

    for asterik in range(num_characters):
        print("*", end='')
    print()