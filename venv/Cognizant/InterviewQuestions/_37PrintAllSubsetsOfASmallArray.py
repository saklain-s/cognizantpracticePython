# 🧮 Problem 37: Print all subsets of a small array
# --------------------------------------------------
# Problem Statement:
# Given a small array of integers, print all possible subsets (the power set) of the array.
#
# Example:
# Input: [1, 2]
# Output: [], [1], [2], [1, 2]
#
# Expected:
# - Implement your own logic to generate all subsets.
# - Consider both iterative and recursive approaches.
# - Hint: For an array of size n, there are 2^n subsets.


def brute(nums):
    result = [[]]
    for num in nums:
        new_subsets = []
        for subset in result:
            new_subsets.append(subset+[num])
        result.extend(new_subsets)
    return result


nums = list(map(int,input().split()))
print(brute(nums))