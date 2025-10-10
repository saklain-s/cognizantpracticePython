nums = list(map(int, input().split()))
unique_nums = sorted(set(nums),reverse=True)
print(unique_nums[1])
nums = sorted(nums,reverse=True)

second = None
maximum = nums[0]
for num in nums:
    if num != maximum:
        second = num
        break


if second is None:
    print("NA")
else:
    print(second)