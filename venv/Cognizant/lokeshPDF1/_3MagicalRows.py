"""
2️⃣ Magical Library Problem
Description:
Given a 2D array where each row represents a series of books, a row is considered magical if the sum of the odd values of the books is even. Your task is to return the number of magical rows.
Input Specification:
input1: Number of rows in the 2D array
input2: Number of columns
input3: 2D integer array A
Output Specification:
Return an integer value representing the number of magical rows.
Example 1:
Input1: 3
Input2: 3
Input3: [[1,2,3], [4,5,6], [7,8,9]]
Output: 2
Explanation:
Row 1: [1,2,3], odd numbers = [1,3], sum = 4 (even)
Row 2: [4,5,6], odd numbers = [5], sum = 5 (odd)
Row 3: [7,8,9], odd numbers = [7,9], sum = 16 (even)
Hence, 2 magical rows.
Example 2:
Input1: 3
Input2: 2
Input3: [[2,4],[0,0],[11,11]]
Output: 1
Explanation:
Only last row [11,11] has odd sum = 22 (even). So 1 magical row.
"""
r = int(input())
c = int(input())
arr = [list(map(int,input().split())) for _ in range(r)]

cnt = 0
for i in range(r):
    sumOf = 0
    for j in range(c):
        if arr[i][j] %2 !=0:
            sumOf+=arr[i][j]
    if sumOf%2==0:
        cnt+=1
print(cnt)
