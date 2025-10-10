
n = int(input())
if n <=0:
    print("-1")
f,s = 0,1

for i in range(n):
    print(f,end=" ")
    f,s= s,f+s
