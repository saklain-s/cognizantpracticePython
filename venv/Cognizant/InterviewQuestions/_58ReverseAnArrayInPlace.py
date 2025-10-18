# 🧮 Problem 58: Reverse an Array In Place
# --------------------------------------------------
# Problem Statement:
# Given an array, reverse it **in place** (without using extra space for another array).
#
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: create a new reversed array manually.
# - Optimized: reverse the array in place using two-pointer technique.
# - Handle edge cases:
#   → Empty array should remain empty.
#   → Single-element array should remain unchanged.

def brute(nums):
    new_arr = []
    for i in  range(len(nums)-1,-1,-1):
        new_arr.append(nums[i])
    return new_arr

def optimized(nums):
    left, right = 0, len(nums)-1
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
        right-=1

    return nums

nums = list(map(int,input().split()))
print(brute(nums))
print(optimized(nums))
