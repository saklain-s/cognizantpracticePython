from collections import Counter
# 🧮 Problem 29: Find the intersection of two arrays
# --------------------------------------------------
# Problem Statement:
# Given two arrays, find the elements that are present in both arrays.
#
# Example:
# Input: nums1 = [1, 2, 2, 3], nums2 = [2, 2, 4]
# Output: [2, 2]  # include duplicates if they appear in both arrays
#
# Expected:
# - Implement your own logic to find the intersection.
# - Consider both brute-force (nested loops) and optimized approaches (using dictionaries or sets).



def brute(nums1,nums2):
    newList = []
    for num in nums1:
        if num in nums2:
            newList.append(num)

    return newList

def optimized(nums1,nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    newList = []
    for num in set1:
        if num in set2:
            newList.append(num)

    return newList
    # or return list(set1 & set2)
def optimized_two(nums1,nums2): # duplicate aware i
    c1 = Counter(nums1)
    c2 = Counter(nums2)

    result = []
    for num in c1:
        if num in c2:
            result.extend([num] * min(c1[num], c2[num]))
    return result

nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
print(brute(nums1,nums2)) # wrong output for ns1 2 2 2 3 ns2 2 3
print(optimized(nums1,nums2)) # wrong output for ns1 2 2 2 3 ns2 2 3
print(optimized_two(nums1,nums2))