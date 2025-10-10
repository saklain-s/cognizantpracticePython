def kth_largest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]
def kth_largest2(nums,k):
    nums.sort()
    index = len(nums)
    return nums[index-k]
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest(nums,k))
print(kth_largest2(nums,k))