# 🧮 Problem 39: Find the Sum of Digits of a Number
# --------------------------------------------------
# Problem Statement:
# Given an integer n (which may be negative), find the sum of all its digits.
#
# Example:
# Input: 1234
# Output: 10
# (Explanation: 1 + 2 + 3 + 4 = 10)
#
# Input: -521
# Output: 8
# (Explanation: 5 + 2 + 1 = 8)
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: extract digits using % 10 and // 10.
# - Optimized: convert to string and sum each digit.
# - Handle negative numbers using abs(n).
# - Edge case: if n = 0 → sum should be 0.

def brute(n):
    total = 0
    n = abs(n)
    while n > 0:
        rem = n % 10
        total+=rem
        n//=10
    return total

def optimized(n):
    return sum(int(digit) for digit in str(n))
n = int(input())
print(brute(n))
print(optimized(n))
