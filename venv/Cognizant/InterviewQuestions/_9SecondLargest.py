def second_largest(nums):
    First, Second = None,None

    for num in nums:
        if First is None or num > First:
            Second = First
            First = num
        elif num != First and (Second is None or num > Second):
            Second = num
    return Second
nums = list(map(int,input().split()))
unique = set(nums)
sorted_list = sorted(unique,reverse=True)
if len(sorted_list) < 2:
    print(None)
else:
    print(sorted_list[1])

