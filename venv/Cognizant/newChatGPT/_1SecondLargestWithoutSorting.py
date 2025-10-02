nums = list(map(int,input().split()))

largest = float('-inf')
secondLargest = float('-inf')

for num in nums:
    if num > largest:
        secondLargest = largest
        largest = num
    elif num > secondLargest and num != largest:
        secondLargest = num

print(secondLargest)