# 🧮 Problem 24: Remove all vowels from a string
# --------------------------------------------------
# Problem Statement:
# Given a string, remove all vowels ('a', 'e', 'i', 'o', 'u') — both lowercase and uppercase.
#
# Example:
# Input:  "Beautiful Day"
# Output: "Btfl Dy"
#
# Expected:
# - Implement your own logic to remove all vowels from the string.
# - Try solving it using both brute-force and optimized approaches (e.g., using sets or list comprehension).
def brute(S):
    vowels = set("aieouAEIOU")
    newStr=""
    for ch in S:
        if ch not in vowels:
            newStr+=ch
    return newStr


def optimized(S):
    vowels = "aieouAEIOU"
    strr = [ch for ch in S if ch not in vowels]
    return "".join(strr)


S = input().strip()
print(brute(S))
print(optimized(S))