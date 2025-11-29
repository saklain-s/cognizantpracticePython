# 🧮 Problem 14: Sort an array using Bubble Sort
# --------------------------------------------------
# Problem Statement:
# Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm.
#
# Bubble Sort repeatedly steps through the array, compares adjacent elements,
# and swaps them if they are in the wrong order.
#
# Example:
# Input: [5, 2, 9, 1, 5, 6]
# Output: [1, 2, 5, 5, 6, 9]
#
# Expected:
# - Implement the sorting logic manually (do not use Python's sort()).
# - Optimize by stopping early if no swaps occur in a full pass.
def bubble(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

nums = list(map(int,input().split()))
n = len(nums)
for i in range(n):
    swapped = False

    for j in range(0,n-i-1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            swapped= True
    if not swapped:
        break
print(nums)
print(bubble(nums))