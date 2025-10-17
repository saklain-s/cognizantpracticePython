# 🧮 Problem 34: Find the maximum product of two numbers in an array
# --------------------------------------------------
# Problem Statement:
# Given an array of integers, find two numbers whose product is maximum
# and return that maximum product value.
#
# Example:
# Input:  [2, 3, -2, 4, -1]
# Output: 12
#
# Explanation:
# The maximum product is obtained from 4 × 3 = 12.
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: Try every possible pair and track the maximum product.
# - Optimized: Sort the array and consider products of the two largest
#   and the two smallest numbers (since two negatives can yield a positive).

def brute(nums):
    max_prod = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            prod = nums[i] * nums[j]
            max_prod = max(max_prod,prod)
            prod = 0

    return max_prod

def optimized(nums):
    nums.sort()
    return max(nums[0] * nums[1], nums[-1] * nums[-2])

nums = list(map(int,input().split()))
print(brute(nums))
print(optimized(nums))