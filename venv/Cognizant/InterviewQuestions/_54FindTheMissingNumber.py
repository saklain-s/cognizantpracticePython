# 🧮 Problem 55: Find the Missing Number
# --------------------------------------------------
# Problem Statement:
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
# find the one number that is missing from the array.
#
# Example:
# Input: [3, 0, 1]
# Output: 2
#
# Explanation:
# The array contains numbers 0, 1, 3 — missing number is 2.
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: check each number from 0 to n if it's missing.
# - Optimized: use the sum formula or XOR method.
# - Handle edge cases:
#   → Empty array → return 0 (since 0 is missing).
#   → Array with all elements → return -1 (no missing number).

def brute(nums):
    n = len(nums)
    for i in range(n+1):
        if i not in nums:
            return i
    return -1

def optimized(nums):
    n = len(nums)
    total_sum = n * (n+1)//2
    return total_sum - sum(nums)

arr = list(map(int,input().split()))
print(brute(arr))
print(optimized(arr))