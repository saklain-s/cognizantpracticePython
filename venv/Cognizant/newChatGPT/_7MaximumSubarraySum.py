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


n = int(input())
nums = list(map(int,input().split()))
max_sum=nums[0]
for i in range(len(nums)):
    total = 0
    for j in range(i,n):
        total+=nums[j]
        max_sum = max(max_sum,total)
print(max_sum)

# Kadane's Algorith

x = int(input())
nums2 = list(map(int,input().split()))

max_sum2 = nums2[0]
current_sum = nums2[0]
for i in range(1,x):
    current_sum = max(nums2[i], current_sum+nums2[i])
    max_sum2 = max(current_sum,max_sum2)
print(max_sum2)