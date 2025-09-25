def brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []

def optimized(nums, target):
    freq = {}  # num -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in freq:
            return [freq[complement], i]
        freq[num] = i
    return []

nums = [2,7,11,15]
target = 9
print(brute_force(nums,9))
print(optimized(nums,9))
