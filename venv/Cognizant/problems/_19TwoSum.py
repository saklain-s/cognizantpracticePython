def twoSum(nums, t):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j] == t:
                return [i,j]

def twoSumDict(nums,t):
    seen = {}
    for i, num in enumerate(nums):
        complement = t - num
        if complement in seen:
            return [seen[complement],i]
        seen[num]=i
    return [-1,-1]


nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))
print(twoSumDict(nums,target))
