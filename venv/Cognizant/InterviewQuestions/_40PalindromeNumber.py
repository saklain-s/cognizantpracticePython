# 🧮 Problem 40: Check if a Number is a Palindrome
# --------------------------------------------------
# Problem Statement:
# Given an integer n (which may be negative), check if it reads the same backward as forward.
#
# Example:
# Input: 121
# Output: True
# (Explanation: Reversed number is also 121)
#
# Input: -121
# Output: False
# (Explanation: Negative sign makes it not a palindrome)
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: reverse the digits manually using % and //.
# - Optimized: convert to string and compare with its reverse.
# - Edge cases:
#   → Negative numbers are not palindromes.
#   → Single-digit numbers (0–9) are palindromes.

def brute(n):
    if n < 0:
        return False

    temp = n
    revered_num = 0
    while n >0:
        rem = n % 10
        revered_num = revered_num * 10  + rem
        n//= 10
    return revered_num == temp

def optimized(n):
    n=str(n)
    return n[::-1] == n
def optimized2(n):
    temp=str(n)
    revers_str = reversed(temp)
    revedd_temp = "".join(revers_str)
    return  temp == revedd_temp

n = int(input())
print(brute(n))
print(optimized(n))
print(optimized2(n))

