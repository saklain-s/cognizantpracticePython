import math

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

x = int(input())
fact=1
for i in range(1,x+1):
    fact*=i
print(fact)
print(math.factorial(x))
print(factorial(x))
