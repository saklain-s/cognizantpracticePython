"""
Title: Count the Most Frequent Character(s)

Problem Statement:
Given a string S, determine which character(s) appear most frequently.
- Ignore spaces while counting.
- If multiple characters have the same highest frequency, print all of them
  in alphabetical order separated by a space.

Input Specification:
- A single line string S (may contain letters, digits, punctuation, and spaces).

Output Specification:
- Print the character(s) that appear most frequently (ignoring spaces),
  separated by a single space.

Example 1:
Input:
hello world
Output:
l

Example 2:
Input:
aab bcc
Output:
a b c
"""

S = input().strip()
S = S.replace(" ","")

freq={}
for ch in S:
    freq[ch] = freq.get(ch,0)+1

maximim = max(freq.values())

result = [ch for ch in freq if freq[ch] == maximim]

print(" ".join(sorted(result)))