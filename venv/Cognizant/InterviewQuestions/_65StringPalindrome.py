# Problem: Check if a given string is a palindrome.
# A palindrome is a string that reads the same forwards and backwards.
# For example:
# "radar" -> True
# "hello" -> False
# "A man a plan a canal Panama" -> True (ignore spaces and case)
# Implement a function `is_palindrome(s: str) -> bool` that returns True if the string is a palindrome, else False.


def brute(s):
    return s==s[::-1]

def optimized(s):
    start = 0
    end = len(s)-1
    while start < end:
        if s[start] != s[end]:
            return False
        start+=1
        end-=1
    return True
def other(s):
    newStr = ""
    for ch in range(len(s)-1,-1,-1):
        newStr+=s[ch]
    return newStr==s
def other2(s):
    st = ''.join(reversed(s))
    return s == st


s = input().strip()
print(brute(s))
print(optimized(s))
print(other(s))
print(other2(s))