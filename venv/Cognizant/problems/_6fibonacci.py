#
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# n= int(input())
# f,s = 0,1
# for i in range(n):
#     print(f,end=" ")
#     f,s = s, f+s
# print()
# for i in range(n):
#     print(fibonacci(i),end=" ")
#
#
#

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
x = int(input())
f,s = 0,1
for i in  range(x):
    print(f,end=" ")
    f,s = s,f+s

print()
for i in range(x):
    print(fibonacci(i),end=" ")