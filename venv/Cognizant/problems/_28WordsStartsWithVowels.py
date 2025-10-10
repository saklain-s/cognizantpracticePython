"""
Title: Count Words Starting with Vowels

Problem Statement:
You are given a string S consisting of multiple words separated by spaces.
Your task is to count how many words in the string start with a vowel
(a, e, i, o, u – case insensitive).

Input Specification:
- input1: A string S containing words separated by spaces.

Output Specification:
- Return an integer representing the number of words that start with a vowel.

Example 1:
Input:
S = "apple orange banana umbrella egg mango"
Output:
4

Explanation:
The words starting with vowels are: "apple", "orange", "umbrella", "egg".
So the result is 4.
"""

S = input().strip()
words = S.split()
cnt = 0

vowels = set("aieouAEIOU")

for word in words:
    if word[0] in vowels:
        cnt+=1

print(cnt)