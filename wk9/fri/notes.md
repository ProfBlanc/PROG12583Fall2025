A function is a request to order something
Used to package/box/wrap-up a series of steps

A variable stores 1 data type
A data type can store 1 or many values.
    - one if primitive (int, str, float, bool)
    - many if collection/iterable type (list, tuple, set, diction)

A function aka method stores a series of statements
These statements help in produce a result

To describe anything, you need to answer the 5 W's 

Who         program/programmer via the user is making the request
Where       at the line that the function is DECLARED (has keyword def)
What        what the function accomplished
When        at the line that the function is CALLED
How         the statements that the function execute => producing the result


We are going to focus on the HOW. Why? 

HOW is a process.
process is similar to a sentance

NOUN + VERB

Noun: something that holds a value aka a variable
Verb: an action => a calculation

Many noun and many verbs

My friend and I are walking

nouns = ['friend', 'I']
verb = walking(person)

for p in nouns:
    walking(p)


___________________________________________________________

Take the example of ordering a shirt

This is a process

Setup
    -  What you need to process the order request
        - size, color, payment, type, shipping_details,
Quality Assessments
    - ensure what receive that you expect


_____________________________________________________________
Create a function that adds all odd_digits of a number 
that is at least 5 digits long

    func(12345)    => 9
    func(123)   => None b/c does not pass of QA
    func(24680) => 0 b/c no odd numbers
    func(11223344) => 8


Stepup
    - one number value (int)
Quality Check
    - ensure the number passed is at least 5 digits
    1: convert number to str
    2: take the len of the str
    3: make sure str len (of num) is at least 5
Process
    - values
        - param (dt: int)
        - converted param value (dt: str)
    -calculate the sum of odd digits
        - create a var to store the sum of odd digits
        - loop the converted param value
            - reconvert the str value to int value
            - compared the reconverted int value represent the digit to determine if its value is odd or even
                - if odd
                    - add its value to the sum of odd digits
                - if even
                    - ignore

I want to write a function that accepts a string text
Return a dictionary that stores: the number of spaces, commas, questionmarks AND a list of all the words of the text

    func("Hi, is my name python?") -> {"num_commas": 1, "num_spaces": 4, "num_questionmarks": 1, "words": ["Hi", "is", "my", "name", "python]}

Outline the steps that you need to write this functions


- store punctuations to count in list variable
- initialize dictionary with keys
	num_...x 3, words
- ensure param is string
- count all punctions in string text
	store int value in dict key that starts with num_
- store all words in words key of dict
	-split text by space
-iterate all words and determine if word ends in punctuation
	- if yes, remove punctuation
- return dictionary 