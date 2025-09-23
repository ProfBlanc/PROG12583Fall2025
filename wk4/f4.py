"""
ask the user for a word
determine if the word is valid
    valid =
            1 letter only: needs to be a vowel
            2+ letters: 1 letter needs to be a vowel            
"""
word = input("Enter a word: ").upper()

word_length = len(word)
#print(word_length)
if word_length == 0:
    print("No input given")
elif word_length == 1 and word[0] == "A" or word[-1] == "I":
    print(word, "is a valid 1-letter word")
#elif word_length == 2 and word[-2] in "a,e,i,o,u,y".split(",")
elif word_length == 2 and word[-2] in list("aeiouy"):
    print(word, "is a valid 2-letter word")
else:
    print("To be continued")


"""
        0   1   2   3   4   5
        a   e   i   o   u   y

"""

