"""
In python, you can convert one data type to a target data types

"""

num = int("100")
temp = float("15.5")

print(type(num))  # class<int> => int
print(type(temp)) # class<float> => float

letters = list("john smith")

"""
0   1   2   3   4   5   6   7   8   9
j   o   h   n       s   m   i   t   h

"""
print(letters[3])

#digits = list(12345)  # error!
digits1 = list(str(12345))  # ["1", "2", "3", "4", "5"]
digits1_2 = list("12345")  # above & this line are the same. except above line first converts int value to str, then list converts str to invidual digits
digits2 = list(range(1, 6))
print(digits1)
print(digits2)

twos_from_2_to_20 = list(range(2, 21, 2))  
print(twos_from_2_to_20)

countdown = list(range(10, -1, -1))
print(countdown)
