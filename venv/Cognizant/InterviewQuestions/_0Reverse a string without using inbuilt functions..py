text = input().strip()

index = len(text)-1

newStr=""
while index >= 0:
    newStr+= text[index]
    index-=1

print(newStr)