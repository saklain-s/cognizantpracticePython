"""
Title: Reverse Words in a String

Problem Statement:
You are given a string S consisting of words separated by spaces.
Your task is to reverse the order of the words without reversing the characters inside each word.

Input Specification:
- input1: A string S containing one or more words separated by spaces.

Output Specification:
- Return a string with the words in reversed order.

Example 1:
Input:  "I love programming"
Output: "programming love I"

Example 2:
Input:  "hello world"
Output: "world hello"
"""


S = input().strip()

words = S.split()
newStr = ""

for ch in range(len(S),-1,-1):
    newStr+=S[ch]
print(newStr)