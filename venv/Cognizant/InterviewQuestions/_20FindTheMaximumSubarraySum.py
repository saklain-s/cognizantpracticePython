# 🧩 Problem Statement:
# Given an integer array 'nums', find the contiguous subarray (containing at least one number)
# which has the largest sum and return that sum.
#
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.
#
# This is the famous "Maximum Subarray Problem" (Kadane’s Algorithm).

def brute_force(nums):

    maximum = nums[0]
    for i in range(len(nums)):
        total = 0
        for j in range(i,len(nums)):
            total+=nums[j]
            maximum = max(maximum,total)
    return maximum

def optimized_solution(nums2):
    max_sum2 = nums2[0]
    current_sum = nums2[0]
    for i in range(1,len(nums2)):
        current_sum = max(nums2[i],current_sum+nums2[i])
        max_sum2 = max(current_sum,max_sum2)
    return max_sum2

nums = list(map(int,input().split()))
print(brute_force(nums))
print(optimized_solution(nums))