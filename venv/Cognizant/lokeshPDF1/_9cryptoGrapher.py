
text = input().strip()
newStr=""

for ch in text:
    if ch == 'a':
        newStr+='Z'
    elif ch == 'A':
        newStr+='z'
    else:
        newStr+=chr(ord(ch)-1)

print(newStr)