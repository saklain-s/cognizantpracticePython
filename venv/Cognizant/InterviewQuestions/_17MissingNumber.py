# 🧮 Problem 16: Find the missing number in an array of 1 to n
# --------------------------------------------------
# Problem Statement:
# Given an array containing n-1 integers from 1 to n (no duplicates),
# find the missing number.
#
# Example:
# Input: [1, 2, 4, 5, 6]
# Output: 3
#
# Explanation:
# The array should contain numbers 1 through 6. Number 3 is missing.
#
# Expected:
# - Implement your own logic to find the missing number.
# - Hint: Use the formula sum(1..n) = n*(n+1)/2 for an optimal solution.


def missin_number(nums):
    given_sum = sum(nums)
    n = len(nums)+1
    actual_sum = n * (n + 1) // 2
    return actual_sum - given_sum

def missin_xor(nums):
    xor = 0
    n = len(nums)
    for i in range(1,n+2):
        xor ^= i
    for num in nums:
        xor ^= num
    return xor




nums = list(map(int,input().split()))
print(missin_number(nums))
print(missin_xor(nums))