nums = dict()

for i in range(1, 6):
    nums[f"n{i}"] = i * 10

print(nums)

# iterate the values of the dictionary

for keys in nums:
    print(keys, nums[keys])