# Problem: Buzz Number Checker
#
# Check if a number is a Buzz number. A Buzz number is a number that:
#   - Ends with 7 OR
#   - Is divisible by 7
#
# Input:
#   - A single integer number
#
# Output:
#   - Print "Buzz Number" if the number is a Buzz number
#   - Print "Not Buzz Number" if it is not
#
# Example 1:
# Input: 14
# Output: Buzz Number
#
# Example 2:
# Input: 27
# Output: Buzz Number
#
# Example 3:
# Input: 13
# Output: Not Buzz Number
num = int(input())

if num % 10 == 7 or num % 7 == 0:
    print("Buzz Number")
else:
    print("Not Buzz Number")
