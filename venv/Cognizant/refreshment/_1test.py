'''

Write a program that takes your name and age as input, then prints:
"Hello Saklain, you are 23 years old."

Write a program to input 2 numbers and print their sum, difference, product, and quotient.

Write a program that checks if a number is even or odd.
'''

name = input()
age = int(input())
print(f"Hello {name} your are {age} years old.")

x = int(input())
y = int(input())

print(x+y)
print(x-y)
print(x*y)
print(x//y)
print(x/y)


z = int(input())

if z & 1 == 1:
    print("Odd")
else:
    print("Even")