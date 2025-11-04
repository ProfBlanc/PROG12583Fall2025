import common_functions

result = common_functions.add(1.1, [])
print(result)

avg = common_functions.average([1,2,3,4,5])
print(avg)

ex1 = common_functions.mode(['a', 'b', 'c'])
print(ex1)  # ['a','b','c']

ex2 = common_functions.mode([1,2,3,4,5,4,3,2,1,1,2,2,2,2,2,2,])
print(ex2)