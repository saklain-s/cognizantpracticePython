"""
Problem: Dopamine Level Game

You start with dopamine level = 0.
You are given:
- N : number of elements in an array A
- L : lower bound of range
- R : upper bound of range

Rules:
• For each element in A:
    - If it lies within [L, R] (inclusive), dopamine level increases by 1.
    - If it lies outside [L, R], dopamine level decreases by 1.

Task:
Return two integers separated by a space:
    <maximum dopamine level> <minimum dopamine level>
where:
    - maximum = final dopamine level after all changes
    - minimum = lowest level reached (i.e. total negative drops)

Example:
Input:
4
1
3
4 3 2 1

Output:
2 -1

Explanation:
• 4 -> outside range -> -1
• 3 -> inside range  -> +1
• 2 -> inside range  -> +1
• 1 -> inside range  -> +1

Net change = -1 + 3 = 2
Maximum level = 2
Minimum level = -1
"""
# Input
n = int(input())
l = int(input())
r = int(input())
arr = list(map(int, input().split()))

maxLevel = 0
minLevel = 0

for num in arr:
    if num < l or num > r:      # outside range
        minLevel -= 1
    else:                       # inside range
        maxLevel += 1

print(f"{maxLevel} {minLevel}")
