# text = 'bsfsf'
#
# for i in range(len(text)):
#     print(text[i])
text = input().strip()
words = text.split()
cnt=0
cnt2=0
for word in words:
    newStr=""
    lenthg = len(word)-1
    while lenthg >=0:
        newStr+=word[lenthg]
        lenthg-=1
    if newStr == word:
        cnt+=1
print(cnt)

for word in words:
    if word == word[::-1]:
        cnt2+=1
print(cnt2)

count = 0
current_word = ""
for ch in text:
    if ch != " ":
        current_word+=ch
    else:
        if current_word == current_word[::-1]:
            count+=1
        current_word=""

if current_word == current_word[::-1] and current_word != "":
    count+=1

print(count)