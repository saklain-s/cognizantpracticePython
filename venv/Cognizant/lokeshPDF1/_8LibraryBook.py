import math
def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
x = int(input())
arr = list(map(int, input().split()))
total = 0
for i in range(1,n+1):
    if isPrime(i):
        total += min(x,arr[i-1])
print(total)

