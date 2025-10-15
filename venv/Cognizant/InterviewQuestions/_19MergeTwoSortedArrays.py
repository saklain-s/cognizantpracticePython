# 🧮 Problem 18: Merge two sorted arrays
# --------------------------------------------------
# Problem Statement:
# Given two sorted arrays, merge them into a single sorted array.
#
# Example:
# Input: arr1 = [1, 3, 5], arr2 = [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]
#
# Expected:
# - Implement the merging logic manually (do not use Python's sort()).
# - Maintain the sorted order while merging.
# - Hint: Use two pointers, one for each array.
def merge_sorted_list(nums1,nums2):
    i = 0
    j = 0
    newList = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            newList.append(nums1[i])
            i+=1
        else:
            newList.append(nums2[j])
            j+=1

    while i < len(nums1):
        newList.append(nums1[i])
        i+=1

    while j < len(nums2):
        newList.append(nums2[j])
        j+=1

    return newList

nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))

print(merge_sorted_list(nums1,nums2))

