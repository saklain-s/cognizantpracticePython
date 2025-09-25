try:
    nums = [1,2,3]
    print(nums[5])
    print(nums[1]/0)
except (IndexError, ZeroDivisionError) as e:
    print("Error occurred:",e)