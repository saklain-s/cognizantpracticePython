import math


def factiorialOf(n):
    if n <= 1:
        return 1
    return n * factiorialOf(n-1)

n = int(input())
fact = 1

for i in range(1,n+1):
    fact*=i
print(fact)
print(math.factorial(n))
print(factiorialOf(n))