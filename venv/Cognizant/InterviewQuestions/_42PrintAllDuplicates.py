# 🧮 Problem 42: Print all duplicates in an array
# --------------------------------------------------
# Problem Statement:
# Given an array of integers, print all elements that appear more than once.
#
# Example:
# Input: [1, 2, 3, 2, 4, 1, 5]
# Output: [1, 2]
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: use nested loops to find duplicates.
# - Optimized: use a dictionary or set to track duplicates efficiently.

def brute(nums):
    newList = []
    for i in  range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                newList.append(nums[i])
    return newList

def optimized(nums):
    newList=[]
    freq={}
    for num in nums:
        if num in freq:
            newList.append(num)
        freq[num]=freq.get(num,0)+1
    return newList
def optimized2(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

nums = list(map(int,input().split()))
print(brute(nums))
print(optimized(nums))
print(optimized2(nums))
