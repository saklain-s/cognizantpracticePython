"""
Given an integer array nums, find the subarray with the largest sum,
and return its sum.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
ie 4,-1,2,1
Output: 6
"""
def largest_sum(nums):
    sums= 0
    max_sum = float('-inf')
    for num in nums:
        sums+=num
        max_sum=max(max_sum,sums)
        if sums < 0:
            sums = 0
    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(largest_sum(nums))