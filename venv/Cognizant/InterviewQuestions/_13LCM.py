# 🧮 Problem 12: Find the LCM (Least Common Multiple) of two numbers
# --------------------------------------------------
# Problem Statement:
# Given two integers a and b, find their Least Common Multiple (LCM).
#
# The LCM of two numbers is the smallest positive integer that is divisible by both a and b.
#
# Example:
# Input: a = 12, b = 15
# Output: 60
#
# Explanation:
# Multiples of 12 → 12, 24, 36, 48, 60, ...
# Multiples of 15 → 15, 30, 45, 60, 75, ...
# The smallest common multiple is 60.
#
# Expected:
# - Implement your own logic to find LCM.
# - (Optional) Verify the result using the formula:
#       LCM(a, b) = abs(a * b) // GCD(a, b)




def getGCD(a,b):
    while b!=0:
        a,b = b, a % b
    return a

def lcm(a,b):
    return abs(a * b ) // getGCD(a,b)

x = int(input())
y = int(input())
print(lcm(x,y))