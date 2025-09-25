str1 = input()
cnt = 0
for ch in str1:
    if ch == 'a' or ch == 'e' or ch =='i' or ch== 'o' or ch =='u' or ch =='A' or ch == 'E' or ch== 'I' or ch =='O' or ch =='U':
        cnt+=1
print(cnt)

cnt2=0
str2 = input()
for ch in str2:
    if ch in "aeiouAEIOU":
        cnt2+=1
print(cnt2)
