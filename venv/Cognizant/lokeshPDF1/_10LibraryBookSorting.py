n = int(input())
text = input()
counter=0
correct = ''.join(sorted(text))
for i in range(n):
    if text[i] != correct[i]:
        counter+=1

print(counter)