# import math
#
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * factorial(n-1)
# n = int(input())
# fact =1
# for i in range(1,n+1):
#     fact *= i
# print(fact)
# print(math.factorial(n))
# print(factorial(n))
#
#
from math import factorial
def factoria(n):
    if n <=1:
        return 1
    return n * factoria(n-1)
x = int(input())
fact = 1
for i in range(1,x+1):
    fact*=i
print(fact)
print(factoria(x))
print(factorial(x))

