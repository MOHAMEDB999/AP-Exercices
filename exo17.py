nums = []
shoesizes = []

nums.append(1)
nums.append(2)
nums.append(3)
nums.append(4)
nums.append(5)

for size in [8, 9, 10, 11, 12]:
    shoesizes.append(size)

nums.append(3)
nums.append(4)

nums = list(set(nums))  

combined_list = nums + shoesizes

print("Numbers List:", nums)
print("Shoe Sizes List:", shoesizes)
print("Combined List:", combined_list)
