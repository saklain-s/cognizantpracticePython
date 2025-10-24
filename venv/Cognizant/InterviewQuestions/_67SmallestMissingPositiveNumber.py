# 🧩 Problem: Find the Minimum Missing Positive Number
#
# Given an unsorted integer array `nums`, find the smallest positive integer
# (greater than 0) that does not appear in the array.
#
# Implement two versions:
# 1. brute(nums)  -> Simple approach using sorting or extra space.
# 2. optimal(nums) -> Efficient approach in O(n) time and O(1) space.
#
# Example 1:
# Input: nums = [1, 2, 0]
# Output: 3
# Explanation: The numbers 1 and 2 are present, so the smallest missing positive is 3.
#
# Example 2:
# Input: nums = [3, 4, -1, 1]
# Output: 2
# Explanation: The numbers 1 and 3 are present, so the smallest missing positive is 2.
#
# Example 3:
# Input: nums = [7, 8, 9, 11, 12]
# Output: 1
# Explanation: No positive numbers smaller than 7 are present.
#
# Constraints:
# 1 <= len(nums) <= 10^5
# -10^6 <= nums[i] <= 10^6
#
# Function signature:
# def first_missing_positive(nums: list[int]) -> int

def brute(nums):
    nums = sorted(set([x for x in nums if x > 0]))
    missing = 1
    for num in nums:
        if num == missing:
            missing+=1
        elif num > missing:
            break
    return missing

def optimal(nums):
    n = len(nums)
    i = 0
    while i < n:
        correct = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i],nums[correct] = nums[correct],nums[i]
        else:
            i+=1

    for i in range(n):
        if nums[i] != i +1:
            return i+1
    return n + 1

nums = list(map(int,input().split()))
print(brute(nums))
print(optimal(nums))