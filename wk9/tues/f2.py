def get_number(text):
    num = 0
    answer = input(f"{text}: ")    
    if answer.isdigit():
        num = int(answer)    
    return num

def get_text_input(text):
    prompt_ending = ": "
    if prompt_ending not in text:
        text += prompt_ending
    answer = input(text)
    if len(answer) < 3:
        answer = "abc"
    return answer


def get_text_with_restrictions_on_vowels(text, min_num_vowels):
    answer = input(text + ": ")

    count_vowels = 0
    # count_vowels += answer.lower().count("a")
    # count_vowels += answer.lower().count("u")
    # count_vowels += answer.lower().count("o")
    # count_vowels += answer.lower().count("e")
    # count_vowels += answer.lower().count("i")
    for letter in "aeiou":
        count_vowels += answer.lower().count(letter)

    if count_vowels < min_num_vowels:
        answer = ""
    return answer
"""
ask the user for the the number of t-shirts they name
ask the user for their name
ask the user for the favourite year 
ask the user for their favourite country
ask the user for their python grade 
"""
def main():
    num_shirts = get_number("Enter number of t-shirts")
    name = get_text_input("Enter name: ")
    fav_year = get_number("Enter fav year")
    fav_country = get_text_input("Enter fav country")
    py_grade = get_number("Enter python grade")

    print(num_shirts, name, fav_year, fav_country, py_grade, sep="\n")
    


if __name__ == "__main__":
    main()