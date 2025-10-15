# 🧮 Problem 23: Reverse words in a sentence
# --------------------------------------------------
# Problem Statement:
# Given a sentence (string), reverse the order of the words while keeping
# the words themselves intact.
#
# Example:
# Input:  "Hello world from Python"
# Output: "Python from world Hello"
#
# Notes / Expected:
# - Words are separated by one or more spaces.
# - Trim leading/trailing spaces in the result and reduce multiple spaces between words to a single space.
# - Implement at least two approaches:
#     1) Using built-in string methods (split/reverse/join).
#     2) In-place style (without using split()) — e.g., reverse the whole string then reverse each word (optional / interview-style).
#
# Bonus:
# - Handle punctuation as part of words (no special removal needed unless asked).
# - Preserve original casing.

def not_optimal(S):

    words = s.split()
    newStr = ""
    index = len(words) -1
    while index >= 0:
        newStr += words[index] + " "
        index-=1
    return newStr

def optimal(S):

    return " ".join(s.split()[::-1])

s = input().strip()
print(not_optimal(s))
print(optimal(s))
