"""
🧠 Problem Statement:
Given an array of integers, find the second largest element
without using any built-in sorting functions like `sorted()` or `.sort()`.

📥 Input:
nums = [10, 5, 8, 20, 2, 18]

📤 Output:
18

🧾 Explanation:
The largest element is 20.
The second largest element is 18.

⚙️ Constraints:
- You must not sort the array.
- The array has at least two distinct elements.
- You can only use a single pass (O(n)) or at most two passes.
"""
def brute(nums):
    n = len(nums)
    first = float('-inf')
    second = float('-inf')

    for i in range(n):
        for j in range(n):
            if nums[i] < nums[j] and nums[j] > first:
                first = nums[j]

    for i in range(n):
        if nums[i] < first and nums[i] > second:
            second = nums[i]

    return second


def optimal(nums):
    first,second = None,None
    for num in nums:
        if first is None or num > first:
            second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num
    return second

nums = list(map(int,input().split()))
print(brute(nums))
print(optimal(nums))