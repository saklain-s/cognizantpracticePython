nums = list(map(int,input().split()))
unique = list(set(nums))
unique.sort(reverse=True)
print(unique[1])