
def lengthOfLongestSubstring(s) -> int:

    if len(s) == 0:
        return 0

    l=r=0
    maxSum=0
    n = len(s)
    hash_map = [-1] * 256
    while(r < n):
        ch = s[r]
        if hash_map[ord(ch)] != -1:
            l = max(l, hash_map[ord(ch)]+1)
        hash_map[ord(ch)] = r
        currentSum = r - l + 1
        maxSum = max(currentSum,maxSum)
        r+=1

    return maxSum



text = input().strip()

print(lengthOfLongestSubstring(text))