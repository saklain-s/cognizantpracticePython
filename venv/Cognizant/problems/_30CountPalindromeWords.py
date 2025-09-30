"""
Title: Count Palindrome Words in a String

Problem Statement:
You are given a string S containing multiple words separated by spaces.
A word is called a palindrome if it reads the same forward and backward (e.g., "level", "madam").
Your task is to count how many words in the given string are palindromes.

Input Specification:
- input1 : A string S containing multiple words.

Output Specification:
- Return an integer value representing the count of palindrome words.

Example 1:
Input: "madam anna went to school"
Output: 2

Explanation:
"madam" and "anna" are palindromes.
"""


S = input().strip()

words = S.split()

cnt = 0

for word in words:
    if word == word[::-1]:
        cnt+=1

print(cnt)

