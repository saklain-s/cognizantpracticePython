"""
Problem:
You are given a string `text` that you want to type on a standard keyboard layout:
"abcdefghijklmnopqrstuvwxyz".

The keyboard is arranged in alphabetical order with:
    - index of 'a' = 0,
    - index of 'b' = 1,
    - ...
    - index of 'z' = 25.

The total distance is the sum of the absolute differences between the indices of
consecutive characters in `text` (you type each character sequentially).

Input:
- A string `text` containing only lowercase letters ('a'–'z').

Output:
- An integer representing the total distance required to type the given text.

Example:
Input : "cba"
Output: 2
Explanation:
Indices: c→2, b→1, a→0
Distance = |2-1| + |1-0| = 1 + 1 = 2
"""
text = input().strip()

total_distance = 0
for i in range(1, len(text)):
    total_distance += abs(ord(text[i]) - ord(text[i-1]))

print(total_distance)
