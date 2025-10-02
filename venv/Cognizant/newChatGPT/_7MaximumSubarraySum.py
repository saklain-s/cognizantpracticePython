# Problem: Maximum Subarray Sum
#
# Given an array of integers, find the contiguous subarray that has the largest sum.
#
# Input:
#   - First line: integer n (size of array)
#   - Second line: n integers (array elements)
#
# Output:
#   - Print the maximum subarray sum
#
# Example 1:
# Input:
# 5
# -2 -3 4 -1 -2 1 5 -3
# Output:
# 7
# Explanation:
# The subarray [4, -1, -2, 1, 5] has the largest sum = 7
#
# Example 2:
# Input:
# 4
# 1 2 3 4
# Output:
# 10
# Explanation:
# The subarray [1, 2, 3, 4] has the largest sum = 10
#
# Constraints:
#   - Array size up to 10^5
#   - Elements can be negative or positive


target = int(input())
nums = list(map(int,input().split()))
total = 0

for i in range(len(nums)):
    for j in range(i,(len(nums))):
        if total < target:
            total+= nums[j]
print(total)