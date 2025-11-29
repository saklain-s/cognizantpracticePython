# 🧮 Problem 61: Check if a Number is an Armstrong Number
# --------------------------------------------------
# Problem Statement:
# Given an integer n, check if it is an Armstrong number.
# An Armstrong number of order k is a number such that the sum of its digits
# each raised to the power k is equal to the number itself.
#
# Example:
# Input: 153
# Output: True
# (Explanation: 1^3 + 5^3 + 3^3 = 153)
#
# Input: 123
# Output: False
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: extract digits and compute sum manually using loops.
# - Optimized: convert number to string and use list comprehension with sum().
# - Handle edge cases:
#   → Negative numbers are not considered Armstrong numbers.

def brute(n):
    if n < 0:
        return False
    temp = n
    k = len(str(n))
    total = 0
    while temp > 0:
        rem = temp % 10
        total+= rem ** k
        temp //= 10
    return total == n

def optimized(n):
    if n < 0:
        return False
    k = len(str(n))
    return n == sum(int(d)**k for d in str(n))

n = int(input("Enter a number: "))
print("Brute Force:", brute(n))
print("Optimized:", optimized(n))
