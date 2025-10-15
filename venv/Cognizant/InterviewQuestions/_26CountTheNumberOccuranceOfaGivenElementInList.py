# 🧮 Problem 26: Count the number of occurrences of a given element in an array
# --------------------------------------------------
# Problem Statement:
# Given an array of integers and a target element, count how many times the target element appears in the array.
#
# Example:
# Input:  arr = [1, 2, 3, 2, 2, 4], target = 2
# Output: 3
#
# Expected:
# - Implement your own logic to count occurrences.
# - Consider both brute-force (loop) and optimized approaches (using collections.Counter or dictionary).

def brute(nums,target):
    cnt = 0
    for num in nums:
        if num == target:
            cnt+=1
    return cnt

def optimized(nums,target):

    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0)+1

    return freq[target]

nums = list(map(int,input().split()))
print(brute(nums,2))
print(optimized(nums,2))