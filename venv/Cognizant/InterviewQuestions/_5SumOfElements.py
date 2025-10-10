def sumOfElements(nums):

    total = 0
    for num in nums:
        total+=num
    return total

nums = list(map(int,input().split()))
print(sumOfElements(nums))