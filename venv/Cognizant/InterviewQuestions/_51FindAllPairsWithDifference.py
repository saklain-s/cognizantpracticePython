# 🧮 Problem 52: Find all pairs with a given difference in an array
# --------------------------------------------------
# Problem Statement:
# Given an array of integers and an integer k, find all unique pairs (a, b) such that a - b = k.
#
# Example:
# Input: nums = [1, 5, 2, 2, 2, 5, 3], k = 3
# Output: [(5, 2), (3, 0), ...]  # all pairs where the difference is 3
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: use nested loops to check every possible pair.
# - Optimized: use a set or dictionary to check for complements efficiently.
# - Handle edge cases:
#   → Empty array should return an empty list.
#   → Multiple occurrences of the same element should be counted according to unique pairs.

def brute(nums, k):
    pairs = []
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if i != j and nums[i] - nums[j] == k:
                pair = (nums[i], nums[j])
                if pair not in pairs:  # to avoid duplicates
                    pairs.append(pair)
    return pairs

def optimized(nums, k):
    seen = set(nums)
    pairs = set()
    for num in nums:
        if (num - k) in seen:
            pairs.add((num, num - k))
    return list(pairs)

nums = list(map(int,input().split()))
target = int(input())
print(brute(nums,target))
print(optimized(nums,target))

