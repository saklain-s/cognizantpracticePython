
S = input().strip()

newStr=""

lenth = len(S)-1

while lenth >= 0:
    newStr+= S[lenth]
    lenth-=1

if newStr == S:
    print("Palindrome")
else:
    print("Not Palindrome")
newStr2=""

for i in range(len(S)-1,-1,-1):
    newStr2+= S[i]
print(newStr2 == S)