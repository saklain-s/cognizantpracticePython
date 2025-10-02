from collections import Counter
nums = list(map(int, input().split()))

counter = Counter(nums)
print(counter)