# 🧮 Problem 62: Find the Missing Number in a Consecutive Sequence
# --------------------------------------------------
# Problem Statement:
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
# find the one number that is missing from the sequence.
#
# Example:
# Input: [3, 0, 1]
# Output: 2
#
# Input: [0, 1]
# Output: 2
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: check each number from 0 to n and see if it exists in the array.
# - Optimized: use the formula sum(0..n) - sum(array) or XOR approach.
# - Handle edge cases:
#   → Empty array should return 0.

def brute(nums):
    n = len(nums)
    for i in range(n+1):
        if i not in nums:
            return i
    return -1

def optimized(nums):
    n = len(nums)
    expected_sum = n*(n+1)//2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

nums = list(map(int, input("Enter numbers: ").split()))
print("Brute Force:", brute(nums))
print("Optimized:", optimized(nums))
