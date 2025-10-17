# 🧮 Problem 46: Check if a String Has Balanced Parentheses
# --------------------------------------------------
# Problem Statement:
# Given a string containing only parentheses characters — '(', ')', '{', '}', '[' and ']' —
# determine if the parentheses are balanced.
#
# A string is said to have balanced parentheses if every opening bracket
# has a corresponding closing bracket in the correct order.
#
# Example:
# Input:  ()[]{}
# Output: True
#
# Input:  (]
# Output: False
#
# Input:  ([{}])
# Output: True
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: Repeatedly remove pairs of (), [], and {} until none remain.
# - Optimized: Use a stack — push opening brackets, and pop when a matching closing bracket is found.
# - Handle edge cases:
#   → Empty string should return True.
#   → String with only closing brackets should return False.
#   → String with odd length can never be balanced.

def brute(s):
    prev = None
    while s != prev:
        prev = s
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""

def optimized(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0


s = input().strip()
print(brute(s))
print(optimized(s))
