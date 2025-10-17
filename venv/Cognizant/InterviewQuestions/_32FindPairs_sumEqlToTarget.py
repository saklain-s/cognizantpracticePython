# 🧮 Problem 33: Find pairs in an array whose sum equals a given number
# --------------------------------------------------
# Problem Statement:
# Given an array of integers and a target sum, find all unique pairs of elements whose sum equals the target.
#
# Example:
# Input: arr = [1, 2, 3, 4, 5], target = 5
# Output: [(1, 4), (2, 3)]
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: Check every pair of elements.
# - Optimized: Use a set or dictionary to find complements efficiently.
import numpy as np

def brute_force(nums,target):
    newList=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                newList.append((nums[i],nums[j]))
    return newList

def optimized(nums,target):
    freq={}
    pairs=[]
    for num in nums:
        complement = target - num
        if complement in freq:
            pairs.append((complement,num))
        freq[num] = freq.get(num,0)+1

    return pairs


nums = list(map(int,input().split()))
tar = int(input())
print(brute_force(nums,tar))
print(optimized(nums,tar))