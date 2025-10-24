from collections import Counter
from statistics import mode



def most_repeating(nums):
    max_count = 0
    number = -1
    for i in range(len(nums)):
        cnt = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                cnt+=1
        if cnt > max_count:
            max_count = cnt
            number = nums[i]
    return number

def most_freq(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1

    return max(freq,key=freq.get)

def most_freq_count(nums):
    counter = Counter(nums)
    most_frequent = counter.most_common(1)[0][0]
    return most_frequent

def modei(nums):
    return  mode(nums)

nums = list(map(int,input().split()))
most_rep = max(nums,key=nums.count)
print(most_repeating(nums))
print(most_freq(nums))
print(most_freq_count(nums))
print(modei(nums))
