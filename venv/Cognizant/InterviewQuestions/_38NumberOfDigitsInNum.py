# 🧮 Problem: Count number of digits in a number
# --------------------------------------------------
# Problem Statement:
# Given an integer n (could be negative), count the number of digits it contains.
#
# Example:
# Input:  12345
# Output: 5
#
# Input:  -987
# Output: 3
#
# Expected:
# - Implement both brute-force (loop dividing by 10) and optimized approaches.
# - Brute-force: repeatedly divide the absolute value by 10 and count iterations.
# - Optimized: you can use string conversion: len(str(abs(n))) or math.log10 for positive numbers.
# - Handle edge cases like n = 0 correctly (should return 1).


def brute(n):
    if n == 0:
        return 1
    n = abs(n)
    # or without abs if n < 0: n = -n
    digits = 0
    while n > 0:
        n//=10
        digits+=1
    return digits
def optimized(n):
    return len(str(abs(n)))
import math
def optimized_math(n):
    if n == 0:
        return 1
    return int(math.log10(abs(n))) + 1

n = int(input())

print(brute(n))
print(optimized(n))