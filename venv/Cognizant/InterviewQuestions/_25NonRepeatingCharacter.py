# 🧮 Problem 25: Find the first non-repeating character in a string
# --------------------------------------------------
# Problem Statement:
# Given a string, find the first character that does not repeat anywhere in the string.
#
# Example:
# Input:  "swiss"
# Output: "w"
#
# Input:  "aabbcc"
# Output: None  # or an indication that no unique character exists
#
# Expected:
# - Implement your own logic to find the first non-repeating character.
# - Consider using dictionaries or arrays to count character frequencies.
# - Aim for an optimal solution with a single pass for counting and another for identifying the first unique character.

def function(S):

    for ch in range(len(S)):
        if S.count(S[ch]) == 1:
            return S[ch]

    return None

def optimized(S):

    freq = {}
    for ch in S:
        freq[ch] = freq.get(ch,0)+1

    for ch in S:
        if freq[ch] == 1:
            return ch

    return None

S = input().strip()
print(function(S))
print(optimized(S))