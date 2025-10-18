# Problem: Find the kth largest element in an unsorted list without sorting the entire list.
# For example:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
# Implement a function `kth_largest(nums: List[int], k: int) -> int` that returns the kth largest element.
# Try to do it without sorting the whole array.
import heapq


def kth_largest2(nums,k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap,num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

nums = list(map(int,input().split()))
k = int(input())
print(kth_largest2(nums,k))