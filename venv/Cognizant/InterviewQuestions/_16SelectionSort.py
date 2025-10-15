# 🧮 Problem 15: Sort an array using Selection Sort
# --------------------------------------------------
# Problem Statement:
# Given an array of integers, sort the array in ascending order using the Selection Sort algorithm.
#
# Selection Sort works by repeatedly finding the minimum element from the unsorted portion of the array
# and swapping it with the first unsorted element.
#
# Example:
# Input: [64, 25, 12, 22, 11]
# Output: [11, 12, 22, 25, 64]
#
# Expected:
# - Implement the sorting logic manually (do not use Python's sort()).
# - Swap only once per pass: place the smallest unsorted element in its correct position.


nums = list(map(int,input().split()))
n = len(nums)

# Selection Sort Implementation
nums = list(map(int, input("Enter numbers: ").split()))
n = len(nums)

for i in range(n):
    # Assume the minimum is the first unsorted element
    min_idx = i
    for j in range(i+1, n):
        if nums[j] < nums[min_idx]:
            min_idx = j
    nums[i], nums[min_idx] = nums[min_idx], nums[i]

print("Sorted array:", nums)
