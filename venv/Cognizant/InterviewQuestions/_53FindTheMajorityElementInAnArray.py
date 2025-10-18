# 🧮 Problem 54: Find the Majority Element in an Array
# --------------------------------------------------
# Problem Statement:
# Given an array of integers, find the element that appears more than ⌊n/2⌋ times.
# If no such element exists, return -1.
#
# Example:
# Input: [3, 3, 4, 2, 3, 3, 5]
# Output: 3
#
# Explanation:
# - The element 3 appears 4 times out of 7 (> 7/2), so it's the majority element.
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: count occurrences of each element using nested loops.
# - Optimized: use Boyer-Moore Voting Algorithm (O(n) time, O(1) space).
# - Handle edge cases:
#   → Empty array → return -1.
#   → If no majority element → return -1.


def brute(arr):
    n = len(arr)
    if n == 0:
        return -1
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == arr[i]:
                count += 1
        if count > n // 2:
            return arr[i]
    return -1


def optimized(arr):
    if not arr:
        return -1

    # Phase 1: Find potential candidate using Boyer-Moore
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Phase 2: Verify candidate
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return -1


arr = list(map(int, input().split()))
print("Brute Force:", brute(arr))
print("Optimized:", optimized(arr))
