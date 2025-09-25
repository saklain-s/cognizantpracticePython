"""
Problem: Smallest Positive Unique Loan Waiver

Jack is a loan manager and has an interesting scheme to waive off one of the loans
of a customer. He placed all the customers' loan amounts in an integer array L of size N.
The conditions to waive off a loan amount are:

1. Only **one** customer's loan amount will be waived off.
2. The customer must have a **minimum positive** loan amount.
3. If two customers have the same loan amount, it is **not unique**, so it will not be picked.

Your task:
- Find and return the **smallest positive unique loan amount** that will be waived off.

---

Input Specification:
input1 : An integer N representing the size of the array.
input2 : An integer array L of size N representing the loan amounts.

Output Specification:
- Return an integer representing the smallest positive unique loan amount.

---

Example 1:
Input  :
N = 3
L = [-1, 1, 3, 2, 3, 4, 3, 4, 5]

Output :
1

Explanation:
- The positive numbers are: 1, 2, 3, 4, 5
- Unique positive numbers are: 1, 2, 5 (because 3 and 4 appear multiple times)
- The smallest among them is 1.
"""

N = int(input())
L = list(map(int,input().split()))

freq={}
for num in L:
    if num > 0:
        freq[num] = freq.get(num,0)+1

unique = [num for num in freq if freq[num] == 1]

if unique:
    print(min(unique))
else:
    print(-1)

