from collections import Counter

text = input()
text = text.lower()
freq = {}

for ch in text:
    freq[ch] = freq.get(ch,0) + 1
print(freq)

str2 = Counter(text)
for ch,count in str2.items():
    print(ch,":",count)