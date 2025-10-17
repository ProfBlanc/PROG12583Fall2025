"""
    List 
    Tuple
        a series of values
        any data type
        diff: Tuple cannot be changed -> immutable
    
        ordered
            how? by index   0, 1, 2
    
    Set
        unordered: you cannot access by index
        python re-orders values as it pleases
        sets store unique, immutable values 

        why use Sets? 
            store unique values
            set operations
                distinct/unique
                differences (in 1 set not in another set)
                disjoint (not in both sets)

    Dictionary
"""

s1 = set()  # an empty set

s1.add(123)
s1.add("hello")
s1.add(123)

print(s1)

"""
List        =>          []

Tuple       =>          ()

Set         =>          {}


"""

first, second = s1
t1 = tuple(s1)  # converts a set to a tuple
l1 = list(s1) # converts a set to a list
s2 = set(l1)

one, two = t1  # unpacking

f1, f2 = l1

print(first, second)

for value in s1:
    print(value)