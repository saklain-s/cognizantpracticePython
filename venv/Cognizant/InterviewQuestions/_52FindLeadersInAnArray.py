# 🧮 Problem 53: Find Leaders in an Array
# --------------------------------------------------
# Problem Statement:
# Given an array of integers, print all the "leaders" in the array.
# An element is a leader if it is strictly greater than all the elements to its right.
#
# Example:
# Input: [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]
# (Explanation: 17 > all to its right, 5 > 2, and 2 is last → all are leaders)
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: for each element, check all elements to its right.
# - Optimized: traverse the array from right to left while tracking the current maximum.
# - Handle edge cases:
#   → Empty array should return an empty list.
#   → Single-element array should return that element as a leader.


def brute(arr):
    leaders = []
    n = len(arr)
    for i in range(n):
        is_leader = True
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                is_leader = False
                break
        if is_leader:
            leaders.append(arr[i])
    return leaders


def optimized(arr):
    if not arr:
        return []
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            leaders.append(arr[i])
    return leaders[::-1]


arr = list(map(int, input().split()))
print("Brute Force:", brute(arr))
print("Optimized:", optimized(arr))
