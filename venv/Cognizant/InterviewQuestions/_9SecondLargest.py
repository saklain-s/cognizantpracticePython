import heapq


def second_largest(nums):
    First, Second = None,None

    for num in nums:
        if First is None or num > First:
            Second = First
            First = num
        elif num != First and (Second is None or num > Second):
            Second = num
    return Second

def usingHeap(nums,k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap,num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
nums = list(map(int,input().split()))
print(second_largest(nums))
print(usingHeap(nums,2))

