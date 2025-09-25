"""
Problem: Logical Operation – Bitwise OR

Explanation:
Given two integers A and B, find the integer value of their logical OR operation.
Here "logical OR" refers to the bitwise OR between the binary representations of A and B.

Rules:
• Bitwise OR compares each bit of A and B.
• A bit in the result is 1 if either of the bits in A or B is 1; otherwise it's 0.

Example:
Input :
5
9

Step :
5 in binary  → 0101
9 in binary  → 1001
-------------------
Bitwise OR  → 1101  (which is 13 in decimal)

Output :
13
"""


x = int(input())
y = int(input())
print(x|y)