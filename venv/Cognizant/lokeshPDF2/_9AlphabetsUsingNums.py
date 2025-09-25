"""
Problem: Count all valid numeric mappings
You are given a numeric string S containing digits from '1' to '9'.
Each number can be mapped to a letter in the alphabet as follows:
    1 -> A, 2 -> B, ..., 26 -> Z
Task:
Count **all valid single-digit and consecutive two-digit numbers** in S that can map to letters.
Rules:
- Single digits '1' to '9' are valid → count each.
- Two-digit numbers 10 to 26 are valid → count each.
- Consecutive numbers can overlap.
Example 1:
Input: "226"
Valid mappings:
- 2  -> B
- 2  -> B
- 6  -> F
- 22 -> V
- 26 -> Z
Output: 5
Explanation:
For "226", we can extract the following:
1. Single digits:
    - s[0] = '2' → B
    - s[1] = '2' → B
    - s[2] = '6' → F
2. Two-digit numbers:
    - s[0:2] = '22' → V
    - s[1:3] = '26' → Z
Total valid mappings = 5
"""

s = input().strip()
count = 0
n = len(s)

for i in range(n):
    # Single-digit check
    if '1' <= s[i] <= '9':
        count += 1
    # Two-digit check (consecutive)
    if i < n - 1:
        num = int(s[i:i+2])
        if 10 <= num <= 26:
            count += 1

print(count)
