def brute(s: str) -> str:

    maxStr = ""
    curr = ""
    for ch in s:
        if ch != " ":
            curr += ch
        else:
            if len(curr) > len(maxStr):
                maxStr = curr
            curr = ""
    return maxStr


def optimal(s: str) -> str:
    words = s.split()
    cnt1 = 0
    longest = ""
    for word in words:
        cnt = len(word)
        if cnt > cnt1:
            longest = word
            cnt1 = cnt
    return longest

def optimizedOneLine(s):
    return max(s.split(), key=len)

s = input().strip()
print(brute(s))
print(optimal(s))
print(optimizedOneLine(s))
