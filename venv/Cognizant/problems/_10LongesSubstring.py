
def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0:
        return 0
    l = 0
    r = 0
    maxSum = 0
    n = len(s)
    hash_map = [-1] * 256
    while(r < n):
        ch = s[r]
        if hash_map[ord(ch)] != 1:
            l = max(l, hash_map[ord(ch)]+1)
        hash_map[ord(ch)] = r
        currSum = r - l +1
        maxSum = max(maxSum,currSum)
        r+=1
    return maxSum

