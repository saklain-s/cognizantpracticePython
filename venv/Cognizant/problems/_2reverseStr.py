"""
Question 2 – Reverse a String
Write a Python program to reverse a string entered by the user.
👉 Example
Input:
Saklain
Output:
nialkaS
"""

name = input().strip()
reversedStr = name[::-1]
print(reversedStr)

newStr = ""
index = len(name)-1
while index >= 0:
    newStr += name[index]
    index-=1

print(newStr)

newStr2 = "".join(reversed(name))
print(newStr2)