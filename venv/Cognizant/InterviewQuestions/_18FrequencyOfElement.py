nums = list(map(int,input().split()))

freq = {}
for num in nums:
    freq[num] = freq.get(num,0)+1

print(freq)