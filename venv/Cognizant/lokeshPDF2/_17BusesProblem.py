"""
Problem: Sum of Tall Buildings

You are given an integer array representing building heights and an integer D. 
A building at index i is considered "tall" if it is strictly taller than the buildings 
at indices i-D and i+D (if these indices exist).

Your task is to compute the sum of the heights of all "tall" buildings.

Input Specification:
input1 : An integer N, representing the number of buildings.
input2 : An integer array of size N, representing the heights of the buildings.
input3 : An integer D, representing the distance to check neighbors.

Output Specification:
Return an integer representing the sum of the heights of all "tall" buildings.

Example 1:
Input:
6
1 3 2 1 5 4
2

Output:
12

Explanation:
Buildings at indices 1 (height 3), 4 (height 5), and 5 (height 4) are "tall". 
Sum = 3 + 5 + 4 = 12

Example 2:
Input:
2
2 1
1

Output:
2

Explanation:
Only the first building is "tall". Sum = 2
"""

def findTotal(buildings, D):
    total = 0
    N = len(buildings)

    for i in range(N):
        left_index = i - D
        right_index = i + D

        left_ok = left_index < 0 or buildings[i] > buildings[left_index]
        right_ok = right_index >= N or buildings[i] > buildings[right_index]

        if left_ok and right_ok:
            total += buildings[i]

    return total
# Python solution
N = int(input())
buildings = list(map(int, input().split()))
D = int(input())

total = 0
for i in range(N):
    left_index = i - D
    right_index = i + D

    left_ok = left_index < 0 or buildings[i] > buildings[left_index]
    right_ok = right_index >= N or buildings[i] > buildings[right_index]

    if left_ok and right_ok:
        total += buildings[i]

print(total)
print(findTotal(buildings,D))
