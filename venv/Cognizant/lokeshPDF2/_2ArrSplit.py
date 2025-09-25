"""
Problem Restatement
You are given:
An integer array A of length N.
Alice can split the array into two non-empty parts at index i.
You need to count how many fair splits are possible.
Step 1: Understand the Split
For an array A = [10, 10, 3, 7, 6]:
Possible split indices are i = 0, 1, 2, 3 (since both parts must be non-empty).
Splits:
i = 0 → [10] and [10, 3, 7, 6]
Sum1 = 10, Sum2 = 26 → |10 - 26| = 16 (even ✅)
i = 1 → [10, 10] and [3, 7, 6]
Sum1 = 20, Sum2 = 16 → |20 - 16| = 4 (even ✅)
i = 2 → [10, 10, 3] and [7, 6]
Sum1 = 23, Sum2 = 13 → |23 - 13| = 10 (even ✅)
i = 3 → [10, 10, 3, 7] and [6]
Sum1 = 30, Sum2 = 6 → |30 - 6| = 24 (even ✅)
All four splits are fair, so the output is 4.
"""
n = int(input())
arr = list(map(int,input().split()))
arrSum = sum(arr)
prefix_sum = 0
fait_slipts = 0
for i in range(n-1):
    prefix_sum += arr[i]
    if ((2*prefix_sum) - arrSum) % 2 == 0:
        fait_slipts +=1
print(fait_slipts)


