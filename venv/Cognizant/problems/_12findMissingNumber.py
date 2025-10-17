def missing(nums):
    n = len(nums)+1
    actual_sum = n * (n-1) // 2
    given_sum = sum(nums)
    return actual_sum - given_sum

def missingXor(nums):
    n = len(nums)
    xor = 0
    for i in range(1,n):
        xor^=i
    for num in nums:
        xor^=num
    return xor

nums = list(map(int,input().split()))
print(missing(nums))
print(missingXor(nums))
