"""
You are given an array of integers containing N elements. Your task is to find and return
an integer value representing the total number of subarrays of size 3 such that the sum
of the first element and the third element is equal to the second element.

Note: A continuous part of an array is a subarray.

Input Specification:

input1 : An integer array of size N.
input2 : An integer value N, representing the size of array.

Output Specification:
Return an integer value representing the total number of subarrays of size 3 such
that the sum of the first element and the third element is equal to the second
element

Example 1:
input1 : (1,2,1,3,5,2,4,2)
input2 : 8
Outout : 3
"""
arr = list(map(int,input().split()))
n = int(input())
cnt=0
for i in range(n-2):
    if arr[i]+arr[i+2] == arr[i+1]:
       cnt+=1
print(cnt)