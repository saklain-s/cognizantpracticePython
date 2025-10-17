# 🧮 Problem 41: Find the most frequent element in an array
# --------------------------------------------------
# Problem Statement:
# Given an array of integers, find the element that appears the most number of times.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3
# (Explanation: 3 appears 3 times, more than any other element)
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: count frequency of each element using nested loops.
# - Optimized: use a dictionary or collections.Counter to track frequencies efficiently.

def brute(nums):
    max_count = 0
    number = -1
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                count+=1
            if count > max_count:
                max_count = count
                number = nums[i]
    return number

def optimized(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0)+1

    return max(freq,key=freq.get)

def optimized2(nums):
    return max(nums,key=nums.count)
from statistics import mode

def optimized3(nums):
    return mode(nums)

nums = list(map(int,input().split()))
print(brute(nums))
print(optimized(nums))
print(optimized2(nums))
print(optimized(nums))
