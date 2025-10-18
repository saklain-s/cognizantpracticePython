# 🧮 Problem 64: Check if a Number is a Happy Number
# --------------------------------------------------
# Problem Statement:
# A happy number is defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits, and repeat the process until
# the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not
# include 1. Numbers for which this process ends in 1 are happy numbers.
#
# Example:
# Input: 19
# Output: True
# (Explanation: 19 → 1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1)
#
# Input: 20
# Output: False
# (Explanation: 20 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → ... cycle)
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: simulate the process using a set to detect loops.
# - Optimized: use Floyd’s cycle detection (fast and slow pointers).
# - Handle edge cases:
#   → n = 1 should return True
#   → n <= 0 should return False

def sum_of_squares(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total

def brute(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)
    return n == 1

def optimized(n):
    slow = n
    fast = n
    while True:
        slow = sum_of_squares(slow)
        fast = sum_of_squares(sum_of_squares(fast))
        if slow == fast:
            break
    return slow == 1

n = int(input("Enter number: "))
print("Brute Force:", brute(n))
print("Optimized:", optimized(n))
