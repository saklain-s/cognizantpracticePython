# 🧮 Problem 31: Move all zeros in an array to the end
# --------------------------------------------------
# Problem Statement:
# Given an array of integers, move all zeros to the end while maintaining
# the relative order of the non-zero elements.
#
# Example:
# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: Create a new array, first add non-zero elements, then zeros.
# - Optimized: Do it in-place using a two-pointer technique.


def brute(nums):

    newList = []
    index=0
    for num in nums:
        if num != 0:
            newList.append(num)
        else:
            index+=1

    for _ in range(index):
        newList.append(0)
    return newList

def optimized(nums):
    l = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[l],nums[i] = nums[i],nums[l]
            l+=1
    return nums

nums = list(map(int,input().split()))

print(optimized(nums))
print(brute(nums))