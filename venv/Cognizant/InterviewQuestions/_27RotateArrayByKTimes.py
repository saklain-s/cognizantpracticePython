# 🧮 Problem 27: Rotate an array by k positions
# --------------------------------------------------
# Problem Statement:
# Given an array and an integer k, rotate the array to the right by k steps.
#
# Example:
# Input:  arr = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]
#
# Expected:
# - Implement your own logic to rotate the array.
# - Consider both brute-force (one step at a time) and optimized approaches (using slicing or reversal).

def rotate(nums,k):
    n = len(nums)
    k = k % n
    reverse_fuc(nums,0,n-1)
    reverse_fuc(nums,0,k-1)
    reverse_fuc(nums,k,n-1)

    return nums
def reverse_fuc(nums,start,end):
    while start<end:
        nums[start],nums[end]=nums[end],nums[start]
        start+=1
        end-=1
def optimized(nums,k):

    n = len(nums)
    k = k % n

    return nums[-k:] + nums[:-k]


nums = list(map(int,input().split()))
target = int(input())
print(rotate(nums,target))
nums = list(map(int,input().split()))
target = int(input())
print(optimized(nums,target))
