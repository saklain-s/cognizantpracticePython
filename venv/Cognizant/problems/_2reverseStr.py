"""
Question 2 – Reverse a String
Write a Python program to reverse a string entered by the user.
👉 Example
Input:
Saklain
Output:
nialkaS
"""

name = input()
print(name[::-1])

index = len(name) - 1
reversedStr = ""
while index >=0:
    reversedStr += name[index]
    index -= 1
print(reversedStr)


text = len(name)-1
reversedString = ""
while text>=0:
    reversedString += name[text]
    text-=1
print(reversedString)

if name == reversedString:
    print("yes")


text2 = input()
print(text2[::-1])
new_text = ""
size = len(text2)-1
while size >=0:
    new_text+=text2[size]
    size-=1
print(new_text)