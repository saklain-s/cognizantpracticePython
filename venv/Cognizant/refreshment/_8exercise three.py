"""
✅ Mini-Exercises (Step 3):

Print all prime numbers between 1 and 50.

Write a program that prints the factorial of a given number using a loop.

Use a list comprehension to generate a list of all even numbers from 1 to 20.

"""
import math
from math import factorial

for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

x = int(input())

factorial =1
for i in range(1,x+1):
    factorial *=i
print(factorial)

nums = []
for i in range(1,21):
    if i %2 == 0:
        nums.append(i)
print(nums)

print(math.factorial(5))