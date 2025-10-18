# 🧮 Problem 60: Find the Intersection of Two Strings (Common Characters)
# --------------------------------------------------
# Problem Statement:
# Given two strings s1 and s2, find all the characters that are common between them.
# The result should not include duplicates.
#
# Example:
# Input:
# s1 = "aabcc"
# s2 = "adcaa"
# Output: ['a', 'c']
#
# Explanation:
# Common characters between "aabcc" and "adcaa" are 'a' and 'c'.
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: use nested loops to compare every character of s1 with s2.
# - Optimized: use sets and intersection operation.
# - Handle edge cases:
#   → Empty strings should return an empty list.
#   → Case sensitivity should be preserved (treat 'A' and 'a' as different characters).

def brute(s1, s2):
    common = []
    for ch in s1:
        if ch in s2 and ch not in common:
            common.append(ch)
    return common

def optimized(s1, s2):
    return list(set(s1) & set(s2))

s1 = input("Enter first string: ").strip()
s2 = input("Enter second string: ").strip()

print("Brute Force:", brute(s1, s2))
print("Optimized:", optimized(s1, s2))
