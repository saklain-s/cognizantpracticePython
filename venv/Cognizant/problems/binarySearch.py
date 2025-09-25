def binary(arr,target):
    start = 0
    end = len(arr) -1
    while(start<=end):
        mid = start+(end-start) // 2
        if target > arr[mid] :
            start = mid + 1
        elif target < arr[mid] :
            end = mid - 1
        else:
            return mid
    return -1


ar = [1,2,3,4,5,5,6]
print(binary(ar,3))

