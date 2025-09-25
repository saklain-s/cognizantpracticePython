import math

nums = [1, 2, 3, 5, 6, 7]

print(nums)
nums[0]=2
nums.remove(3)
print(nums)
print(nums[::-1])

list = [10, 20, 30, 40, 50]
list.sort()

print(list[-2])

for i in list:
    print(i)

for i in range(len(list)):
    print(list[i])

#numbers = [10, 20, 30]
#for i in numbers:         # i takes values 10, 20, 30 (not indices)
 #   numbers[i] = numbers[i] * 2  # tries to access numbers[10], numbers[20]... (IndexError)


numbers = [10, 20, 30]
for i in range(len(numbers)):  # i = 0, 1, 2
    numbers[i] = numbers[i] * 2





n = int(input())
arr = [int(input()) for _ in range(n)]
print(arr)