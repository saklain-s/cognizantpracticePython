def is_palindrome(s)->bool:
    temp = s[::-1]
    return temp == s


def palidromeornot(s)->bool:
    newStr = ""
    index = len(s)-1
    while index >= 0:
        newStr+=s[index]
        index-=1
    return s == newStr

text = input().strip()
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")

if palidromeornot(text):
    print("Palindrome")
else:
    print("Not a Palindrome")