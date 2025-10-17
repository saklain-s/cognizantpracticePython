def brute(S):
    cnt=0
    in_word = False

    for ch in S:
        if ch != ' ' and not in_word:
            cnt+=1
            in_word = True
        elif ch == ' ':
            in_word = False
    return cnt

def optimized(S):
    words = S.split()
    return len(words)

S = input().strip()
print(brute(S))
print(optimized(S))