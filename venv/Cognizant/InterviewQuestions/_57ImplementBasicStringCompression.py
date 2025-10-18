# 🧮 Problem 57: Implement Basic String Compression
# --------------------------------------------------
# Problem Statement:
# Given a string, implement basic string compression using the counts of repeated characters.
# For example, the string "aaabb" becomes "a3b2".
# If the compressed string is not smaller than the original, return the original string.
#
# Example:
# Input: "aaabbccccd"
# Output: "a3b2c4d1"
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: count each sequence of characters manually.
# - Optimized: use a list to build compressed parts efficiently.
# - Handle edge cases:
#   → Empty string should return "".
#   → No repeating characters → return original string.

def brute(s):
    if not s:
        return ""

    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1
    result += s[-1] + str(count)

    return result if len(result) < len(s) else s


def optimized(s):
    if not s:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(f"{s[i - 1]}{count}")
            count = 1
    compressed.append(f"{s[-1]}{count}")

    result = "".join(compressed)
    return result if len(result) < len(s) else s


s = input().strip()
print("Brute Force:", brute(s))
print("Optimized:", optimized(s))
