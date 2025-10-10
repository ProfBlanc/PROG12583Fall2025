"""
Task 2 but using while loop
"""

"""
Create an app that 
    -stores the list of values of user-inputted provincial codes (ON, QC, AB, BC, etc)
Ask the user to enter the province codes for 5 provinces
Only add the provincial code IF the code is at least two digits and is unique
"""

prov_codes = list()
num_times = 5
#for i in range(1, num_times + 1):
while len(prov_codes) < num_times:
    answer = input(f"Enter province code {len(prov_codes) + 1} of {num_times}: ").upper()

    if len(answer) >= 2 and answer not in prov_codes:
        prov_codes.append(answer)

print(prov_codes)