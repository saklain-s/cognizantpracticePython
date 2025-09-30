"""
ip hello world this is python
op 3

"""

S = input().strip()
words = S.split()
cnt = 0
for word in words:
    lenght = len(word)
    if lenght %2 == 0:
        cnt+=1
print(cnt)