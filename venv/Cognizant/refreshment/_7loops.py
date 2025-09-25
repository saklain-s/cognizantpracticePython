for i in range(1,10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)


squares = [i*i for i in range(5)]
print(squares)


squares1 = []
for i in range(1,5):
    squares1.append(i*i)
print(squares1)

for ch in "python":
    print(ch,end="")