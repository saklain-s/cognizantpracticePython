# 🧮 Problem 43: Find the longest substring without repeating characters
# --------------------------------------------------
# Problem Statement:
# Given a string, find the length of the longest substring that contains no repeating characters.
#
# Example:
# Input: "abcabcbb"
# Output: 3
# (Explanation: The longest substring without repeating characters is "abc")
#
# Expected:
# - Implement both brute-force and optimized approaches.
# - Brute-force: check all possible substrings and track the maximum length.
# - Optimized: use the sliding window technique with a set or dictionary to track characters efficiently.

def brute(S):
    n = len(S)
    max_len = 0
    for i in range(n):
        seen = set()
        current_len = 0
        for j in range(i,n):
            if S[j] in seen:
                break
            seen.add(S[j])
            current_len+=1
        max_len = max(max_len,current_len)
    return max_len

def optimized(s):
    if len(s) == 0:
        return 0
    l=r=0
    maxSum=0
    n = len(s)
    hash_map = [-1] * 256
    while r < n:
        ch = s[r]
        if hash_map[ord(ch)] != -1:
            l = max(l, hash_map[ord(ch)]+1)
        hash_map[ord(ch)] = r
        currentSum = r - l + 1
        maxSum = max(currentSum,maxSum)
        r+=1
    return maxSum
S = input().strip()
print(brute(S))
print(optimized(S))


