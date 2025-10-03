
text = input().strip()
text2 = input().strip()

temp1 = sorted(text)
temp2 = sorted(text2)
print(temp1==temp2)

freq1={}
for ch in text:
    freq1[ch] = freq1.get(ch,0)+1

freq2={}
for ch in text2:
    freq2[ch] = freq2.get(ch,0)+1

print(freq2==freq1)

from collections import Counter

cnt1 = Counter(text2)
cnt2 = Counter(text)

print(cnt1==cnt2)