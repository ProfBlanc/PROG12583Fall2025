"""
Ask 2 users which countries they have been to
    (Use loops, you decide how many times to ask user for country)
Compare the country list of two users, 
    determine 
        common countries visited
        contries that both users haven't visited (1 user visited, the other did not)
"""
answers = list()
for i in range(2):
    answers.append([])
print(answers)

for user in answers:
    # user => a list
    while True:
        ans = input(f"Enter a country that you have visited press enter with blank response to end: ")
        if len(ans) > 0:
            user.append(ans)
            continue
        break
    print("Moving on to next user")

print(answers)

common_countries = set(answers[0]).intersection(set(answers[1]))
countries_not_visited_by_both = set(answers[0]).symmetric_difference(set(answers[1]))

print("Common", common_countries)
print("Not by both", countries_not_visited_by_both)