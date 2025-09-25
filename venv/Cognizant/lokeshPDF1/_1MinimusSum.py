"""
Question 1: Minimum Sum
You are given two integer arrays A and B of length N.
In one operation, you can swap any two elements of A or any two elements of B any number of times (including zero).
Your task is to find and return the minimum possible value of
A[i]∗B[i]
after performing the operations any number of times.
Input
input1: An integer N representing the size of both arrays.
input2: Integer array A of size N.
input3: Integer array B of size N.
Output
An integer — the minimum possible sum of A[i] * B[i].
Example 1
Input:
N = 3
A = [4, 1, 6]
B = [3, 1, 2]
Output:
17
Explanation:
Rearrange A as [1, 4, 6] and B as [3, 2, 1].
Sum = 1*3 + 4*2 + 6*1 = 17.
"""

n = int(input())
arr1 = [int(input()) for _ in range(n)]
arr2 = [int(input()) for _ in range(n)]

arr1.sort()
arr2.sort(reverse=True)
total = 0
for i in range(n):
    total += arr1[i]*arr2[i]
print(total)