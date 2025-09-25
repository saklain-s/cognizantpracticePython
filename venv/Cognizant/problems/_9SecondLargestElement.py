def second_largest_single_pass(nums):
    first = second = None
    for num in nums:
        if first is None or num > first:
            second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num
    if second is None:
        print("No second largest element")
    else:
        print(second)


nums = list(map(int, input("Enter integers separated by space: ").split()))
second_largest_single_pass(nums)

def second_largest(nums):
    unique_nums = set(nums) # removes duplicates
    if len(unique_nums) < 2:
        print("No second largest element")
        return
    sorted_nums = sorted(unique_nums, reverse=True)
    print(sorted_nums[1])

nums = list(map(int, input("Enter integers separated by space: ").split()))
second_largest(nums)
unique_nums = set(nums)
sortedList = sorted(unique_nums,reverse=True)
print(sortedList[1])