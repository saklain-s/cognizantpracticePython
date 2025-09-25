s = input()
n = len(s)
max_dist = 0

for i in range(n):
    for j in range(i+1, n):
        if s[i] != s[j]:
            max_dist = max(max_dist, j - i)

print(max_dist)
