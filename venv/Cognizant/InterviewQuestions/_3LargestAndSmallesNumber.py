def largest_smallest(list):
    smallest=float('inf')
    largest=float('-inf')
    for num in list:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    return smallest, largest


nums = list(map(int,input().split()))
print(largest_smallest(nums))