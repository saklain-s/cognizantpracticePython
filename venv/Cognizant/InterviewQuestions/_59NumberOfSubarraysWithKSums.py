# 🧮 Problem 59: Count the Number of Subarrays with Sum = K
# --------------------------------------------------
# Problem Statement:
# Given an array of integers and an integer k, find the total number of continuous subarrays
# whose sum equals to k.
#
# Example:
# Input: nums = [1, 1, 1], k = 2
# Output: 2
# (Explanation: Subarrays [1,1] (first two) and [1,1] (last two) both sum to 2)
#
# Input: nums = [1, 2, 3], k = 3
# Output: 2
# (Explanation: Subarrays [1,2] and [3] both sum to 3)
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: use two nested loops to check all subarray sums.
# - Optimized: use prefix sum and hashmap to track previous sums efficiently.
# - Handle edge cases:
#   → Empty array should return 0.
#   → Negative numbers should also be handled correctly.
from sys import prefix


def brute(nums, k):
    count = 0
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i,len(nums)):
            curr_sum+= nums[j]
            if curr_sum == k:
                count+=1

    return count

def optimized(nums,k):
    count = 0
    curr_sum = 0
    prefix_sums = {0:1}
    for num in nums:
        curr_sum += num
        if curr_sum - k in prefix_sums:
            count+=1
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum,0)+1

    return count

nums = list(map(int,input().split()))
k = int(input())
print(brute(nums,k))
print(optimized(nums,k))
