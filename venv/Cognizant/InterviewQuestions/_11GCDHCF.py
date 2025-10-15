# 🧮 Problem 11: Find the GCD (HCF) of two numbers
# --------------------------------------------------
# Problem Statement:
# Given two integers a and b, find their Greatest Common Divisor (GCD),
# also known as the Highest Common Factor (HCF).
#
# The GCD of two numbers is the largest positive integer that divides both numbers exactly (without remainder).
#
# Example:
# Input: a = 36, b = 60
# Output: 12
#
# Explanation:
# 36 = 2 × 2 × 3 × 3
# 60 = 2 × 2 × 3 × 5
# Common factors = 2 × 2 × 3 = 12
#
# Expected:
# - Implement your own logic to find GCD
# - (Optional) verify result using math.gcd()

import math

def gcd(a, b):
    # Handle edge cases
    if a == 0:
        return b
    if b == 0:
        return a

    gcd_val = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd_val = i
    return gcd_val

def gcdOptimal(a,b):

    while b != 0:
        a,b = b, a % b
    return a

# Example input
a, b = map(int, input("Enter two numbers: ").split())

# Print both results
print(gcd(a, b))
print( gcdOptimal(a, b))


