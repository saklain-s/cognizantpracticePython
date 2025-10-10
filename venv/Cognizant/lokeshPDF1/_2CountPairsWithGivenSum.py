"""
Question 2: Count Pairs with Given Sum
Problem
Given an array of integers and a target integer k, count how many distinct pairs (i, j) exist (with i < j) such that:
arr[i]+arr[j]=k
Input
First line: integer n — number of elements in the array.
Second line: n space-separated integers — the array elements.
Third line: integer k — the target sum.
Output
A single integer — the number of pairs whose sum equals k.
Example 1
Input:
5
1 5 7 -1 5
6
Output:
3
Explanation: The valid pairs are
(1,5) [first 5], (7,-1), and (1,5) [second 5].
"""

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

counter = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j] == target:
            counter+=1


count=0
freq={}
for num in arr:
    seen = target-num
    if seen in freq:
        count+=1
    freq[num] = freq.get(num,0)+1
print(counter)
print(count)