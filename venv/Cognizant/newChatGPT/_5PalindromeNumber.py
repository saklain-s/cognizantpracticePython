# Problem: Palindrome Checker
#
# Determine if a given number is a palindrome. A palindrome is a number that reads
# the same forwards and backwards (e.g., 121, 454).
#
# Input:
#   - A single integer number
#
# Output:
#   - Print "Palindrome" if the number is a palindrome
#   - Print "Not Palindrome" if the number is not a palindrome
#   - Print "Invalid Input" if the number is negative
#
# Example 1:
# Input: 121
# Output: Palindrome
#
# Example 2:
# Input: -121
# Output: Invalid Input
#
# Example 3:
# Input: 123
# Output: Not Palindrome
x = int(input())

original = x
reversed_num = 0

while x > 0:
    rem = x % 10
    reversed_num = reversed_num * 10 + rem
    x = x // 10

print(reversed_num == original)
