def add_and_get_stats(*nums):
    """
    This function adds all the numbers together
    It also returns the min, max and average number 
    """
    return sum(nums), min(nums), max(nums), sum(nums)/len(nums)

result = add_and_get_stats(1, 10, -10, 20, 15, -5)

a, b, c , d = result

print(result)
print(a,b,c,d)
