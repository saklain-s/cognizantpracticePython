"""
👉 Write a Python program to check whether the given string is a palindrome.
✅ Example 1:
Input: madam
Output: Palindrome
"""
#
# text = input()
# reversedStr = text[::-1]
# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")
#
# index = len(text) -1
# startIndex = 0
# x = True
# while index > startIndex:
#     if text[index] != text[startIndex]:
#         x = False
#         break
#     index -= 1
#     startIndex +=1
# if x:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
#
# text2 = input()
# index2 = len(text2) -1
# reversedString = ""
# while index2 >= 0:
#     reversedString += text2[index2]
#     index2-=1
# if reversedString == text2:
#     print("Palindrome")
# else:
#     print("No")
#
#




text3 = input()
newText = text3[::-1]
if text3 == newText:
    print("Palindrome")
else:
    print("NO")

start = 0
end = len(text3)-1

Y = True
while start <= end:
    if text3[start] != text3[end]:
        Y = False
        break
    start+=1
    end-=1

if Y :
    print("Palindrome")
else:
    print("No")

givenText = input()
length = len(givenText)-1
palindrome = ""
while length >=0:
    palindrome+=givenText[length]
    length-=1
print(givenText)
if givenText == palindrome:
    print("palindrome")
else:
    print("Get the fuck out")