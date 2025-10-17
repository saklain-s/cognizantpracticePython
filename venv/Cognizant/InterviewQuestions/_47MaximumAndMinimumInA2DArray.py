# 🧮 Problem 48: Find the Maximum and Minimum in a 2D Array
# --------------------------------------------------
# Problem Statement:
# Given a 2D array (matrix) of integers, find the maximum and minimum elements in it.
#
# Example:
# Input:
# [
#   [3, 5, 9],
#   [1, 6, 4],
#   [8, 2, 7]
# ]
# Output:
# Max = 9, Min = 1
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: iterate through all elements using nested loops.
# - Optimized: flatten the matrix and use built-in functions max() and min().
# - Handle edge cases:
#   → Empty matrix should return None for both max and min.
#   → Single row or single column matrices should also be handled.
def brute(nums):
    mini  = float('inf')
    maxi = float('-inf')
    for row in nums:
        for element in row:
            if element < mini:
                mini = element
            if element > maxi:
                maxi = element
    return mini,maxi

def optimized(nums):
    if not nums or not nums[0]:
        return None, None

    flat = [x for row in nums for x in row]

    return min(flat),max(flat)
r = int(input())
nums = [list(map(int,input().split()))for _ in range(r)]
print(brute(nums))
print(optimized(nums))