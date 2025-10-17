from multiprocessing.reduction import duplicate


def brute(nums)->str:
    correct = 1
    extra = 0
    missing = -1
    for i in range(len(nums)):
        if nums[i] != correct:
            missing = correct
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                extra=nums[i]
        correct+=1
    return f"Missing = {missing}, Duplicate = {extra}"

def optimized(nums):
    n = len(nums)

    # Expected sums for 1..n
    sum_n = n * (n + 1) // 2
    sum_squares_n = n * (n + 1) * (2 * n + 1) // 6

    # Actual sums from the array
    sum_nums = sum(nums)
    sum_squares_nums = sum(x * x for x in nums)

    # Differences between actual and expected
    sum_diff = sum_nums - sum_n          # duplicate - missing
    square_diff = sum_squares_nums - sum_squares_n  # duplicate^2 - missing^2

    # duplicate + missing
    sum_duplicate_plus_missing = square_diff // sum_diff

    # Solve for duplicate and missing
    duplicate = (sum_diff + sum_duplicate_plus_missing) // 2
    missing = sum_duplicate_plus_missing - duplicate

    return f"Missing = {missing}, Duplicate = {duplicate}"

def xor_solution(nums):
    n = len(nums)
    xor_all = 0

    # XOR of all numbers from 1 to n
    for i in range(1, n+1):
        xor_all ^= i

    # XOR of all numbers in the array
    for num in nums:
        xor_all ^= num

    # xor_all = missing ^ duplicate
    rightmost_set_bit = xor_all & -xor_all  # isolate any set bit

    x = 0  # will hold one of missing/duplicate
    y = 0  # will hold the other

    # Divide numbers into two groups based on rightmost_set_bit
    for i in range(1, n+1):
        if i & rightmost_set_bit:
            x ^= i
        else:
            y ^= i

    for num in nums:
        if num & rightmost_set_bit:
            x ^= num
        else:
            y ^= num

    # Determine which is missing and which is duplicate
    if x in nums:
        duplicate, missing = x, y
    else:
        duplicate, missing = y, x

    return f"Missing = {missing}, Duplicate = {duplicate}"


nums = list(map(int,input().split()))
print(brute(nums))
print(optimized(nums))
print(xor_solution(nums))

