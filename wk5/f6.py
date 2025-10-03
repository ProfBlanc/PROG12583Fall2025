# tuple <=> list
# both: collections/series of values, indexes
# difference: tuple: immutable (cannot alter), list is mutable

name = "Ben"
print(name[0])  # 'B'
#name[0] = "H"  # error: string is immutable

values1 = tuple("Ben")
values2 = list("Ben")

if "e" in values1:
    values1.index("e")

print(values1[1])

values3 = values1 + tuple("Blanc")

values4 = values1 * 3 # ("B", "e", "n","B", "e", "n","B", "e", "n")
print(values1)
print(values2)