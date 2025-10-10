def duplicates(nums):
    uniquq_nums = []
    for num in nums:
        if num not in uniquq_nums:
            uniquq_nums.append(num)
    return uniquq_nums

nums = list(map(int,input().split()))
temp = list(dict.fromkeys(nums))
print(duplicates(nums))
print(temp)