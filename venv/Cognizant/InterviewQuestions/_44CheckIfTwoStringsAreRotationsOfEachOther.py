# 🧮 Problem 44: Check if two strings are rotations of each other
# --------------------------------------------------
# Problem Statement:
# Given two strings s1 and s2, check if s2 is a rotation of s1.
#
# Example:
# Input: s1 = "abcd", s2 = "cdab"
# Output: True
# (Explanation: "cdab" is "abcd" rotated by 2 positions)
#
# Input: s1 = "abcd", s2 = "acbd"
# Output: False
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: generate all rotations of s1 and check if any equals s2.
# - Optimized: check if s2 is a substring of s1 + s1 and lengths are equal.

def brute(s1,s2):
    n = len(s1)
    if n != len(s2) or n == 0:
        return False
    for i in range(n):
        rotated_s1 = s1[i:] + s1[:i]
        if rotated_s1 == s2:
            return True
    return False

def optimized(s1,s2):
    if len(s1) != len(s2):
        return False

    temp = s1 + s1
    return s2 in temp

s = input().strip()
s2 = input().strip()
print(brute(s,s2))
print(optimized(s,s2))