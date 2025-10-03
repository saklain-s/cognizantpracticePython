"""
👉 Write a Python program to check whether the given string is a palindrome.
✅ Example 1:
Input: madam
Output: Palindrome
"""

text = input().strip()

reversedStr1 = text[::-1]

print(text==reversedStr1)

start = 0
end = len(text)-1
Y = True
while start <= end:
    if text[start] != text[end]:
        Y = False
        break
    start+=1
    end-=1
if Y:
    print("Palindrome")

reversedStr2 = ""
index = len(text)-1
while index >= 0:
    reversedStr2+=text[index]
    index-=1

print(reversedStr2==text)