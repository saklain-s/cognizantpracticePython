nums = list(map(int, input().split()))
nums = sorted(nums,reverse=True)

second = None
maximum = nums[0]
for x in nums[1:]:
    if x != maximum:
        second = x
        break

if second is None:
    print("NA")
else:
    print(second)