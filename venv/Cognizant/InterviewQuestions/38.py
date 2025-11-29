def bubble(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums
def method2(nums):
    return " ".join(sorted(nums))
nums = [-1,5,4,3,2,1,-2]
print(bubble(nums))
print(method2(nums))