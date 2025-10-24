# 🧮 Problem 30: Check if an array is sorted
# --------------------------------------------------
# Problem Statement:
# Given an array of integers, determine if the array is sorted in non-decreasing order.
#
# Example:
# Input: [1, 2, 2, 3, 4]
# Output: True
#
# Input: [3, 1, 2, 4]
# Output: False
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: Compare each element with every other element.
# - Optimized: Compare each element with its next neighbor.

def brute(nums):
    copt = sorted(nums)
    return copt == nums

def brute_without_fun(nums):
    Y = True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return Y

nums = list(map(int,input().split()))
print(brute(nums))
print(brute_without_fun(nums))