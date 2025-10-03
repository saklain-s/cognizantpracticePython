# Problem: Merge Two Sorted Arrays
#
# Given two sorted arrays, merge them into a single sorted array.
#
# Input:
#   - First line: integer n (size of first array)
#   - Second line: n integers (sorted in non-decreasing order)
#   - Third line: integer m (size of second array)
#   - Fourth line: m integers (sorted in non-decreasing order)
#
# Output:
#   - A single line with the merged sorted array
#
# Example 1:
# Input:
# 4
# 1 3 5 7
# 3
# 2 4 6
# Output:
# 1 2 3 4 5 6 7
#
# Example 2:
# Input:
# 3
# 10 20 30
# 4
# 5 15 25 35
# Output:
# 5 10 15 20 25 30 35
#
# Constraints:
#   - 1 <= n, m <= 10^5
#   - Arrays are already sorted

n = int(input())
nums1 = list(map(int,input().split()))

m = int(input())
nums2 = list(map(int,input().split()))

i,j = 0,0

merged = []

while i < n and j < m:
    if nums1[i] < nums2[j]:
        merged.append(nums1[i])
        i+=1
    else:
        merged.append(nums2[j])
        j+=1

while i < n:
    merged.append(nums1[i])
    i+=1
while j < m:
    merged.append(nums2[j])
    j+=1

print(*merged)

print(sorted(nums1+nums2))