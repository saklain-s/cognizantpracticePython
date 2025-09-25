"""
Problem: Largest Absolute Difference of Fruit Frequencies

You are given a string S where each character represents a type of fruit.
Your task is to:

1. Count the frequency of each fruit (character) in the string.
2. From these frequencies:
   - Find the **maximum frequency** among the fruits whose frequency is **odd**.
   - Find the **minimum frequency** among the fruits whose frequency is **even**.
3. Return the absolute difference between these two numbers.

Notes:
- It is guaranteed that there is at least one fruit with an odd frequency
  and at least one fruit with an even frequency.

Input Specification:
input1 : A string S representing different types of fruits.

Output Specification:
Return an integer representing the absolute difference between:
   (maximum odd frequency) and (minimum even frequency).

Example 1:
Input  : aartfu
Output : 1

Explanation:
Frequencies:
    a -> 2
    r -> 1
    t -> 1
    f -> 1
    u -> 1

Odd frequencies: 1, 1, 1, 1   → maximum = 1
Even frequencies: 2          → minimum = 2

Absolute difference = |1 - 2| = 1
"""
import math
fruits = input().strip()


freq = {}
for ch in fruits:
    freq[ch] = freq.get(ch, 0) + 1

max_odd = 0
min_even = float('inf')  # start with a very large number

for ch in freq:
    if freq[ch] % 2 == 1:
        max_odd = max(max_odd, freq[ch])
    else:  # even frequency
        min_even = min(min_even, freq[ch])

print(abs(max_odd - min_even))
