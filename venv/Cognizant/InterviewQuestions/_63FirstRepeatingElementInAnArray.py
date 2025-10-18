# 🧮 Problem 63: Find the First Repeating Element in an Array
# --------------------------------------------------
# Problem Statement:
# Given an array of integers, find the first element that repeats (appears more than once).
#
# Example:
# Input: [10, 5, 3, 4, 3, 5, 6]
# Output: 5
# (Explanation: 5 is the first element that repeats)
#
# Input: [1, 2, 3, 4]
# Output: -1
# (Explanation: No element repeats)
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: check each element with every other element for repetition.
# - Optimized: use a set or dictionary to track seen elements.
# - Handle edge cases:
#   → Empty array should return -1.

def brute(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return nums[i]
    return -1

def optimized(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

nums = list(map(int, input("Enter numbers: ").split()))
print("Brute Force:", brute(nums))
print("Optimized:", optimized(nums))
