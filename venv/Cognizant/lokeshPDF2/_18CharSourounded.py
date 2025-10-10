"""
Problem: Count Digit Substrings Surrounded by Letters

You are given a string S containing lowercase letters (a-z) and digits (0-9).
A digit substring is a sequence of one or more consecutive digits.
You need to count how many digit substrings are surrounded by letters on both sides.

Input Specification:
input1 : A single string S consisting of lowercase English letters (a-z) and digits (0-9)

Output Specification:
Return an integer representing the count of digit substrings that are surrounded on both sides by lowercase letters.

Example 1:
Input: "a123d"
Output: 1
Explanation: "123" is a digit substring surrounded by 'a' and 'd'.

Example 2:
Input: "x9y2z33a"
Output: 3
Explanation:
- "9" is surrounded by 'x' and 'y'
- "2" is surrounded by 'y' and 'z'
- "33" is surrounded by 'z' and 'a'
 index: 0 1 2 3 4 5 6 7
 char : x 9 y 2 z 3 3 a
 n = 8
"""

s = input().strip()
count = 0
i = 0
n = len(s)

while i < n:
    if s[i].isdigit():
        start = i
        while i < n and s[i].isdigit():
            i+=1
        end =i -1
        if start > 0 and end < n -1 and s[start-1].isalpha() and s[end+1].isalpha():
            count+=1
    else:
        i+=1
print(count)

