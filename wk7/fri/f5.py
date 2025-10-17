s1 = set(range(1, 5))  # s1 = {1,2,3,4}
s2 = set(range(3,7))   # s2 = {3,4,5,6}

s3 = s1.union(s2)  

s4 = s1.difference(s2)
s5 = s2.difference(s1)

s6 = s1.intersection(s2)

s7 = s1.symmetric_difference(s2)

#s1.difference_update(s2)

print(s3)
print(s4)
print(s5)
print(s6)
print(s7)