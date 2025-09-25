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








def fibonaci(n):
    if n <=1:
        return n
    else:
        return fibonaci(n-1) + fibonaci(n-2)
x = int(input())
f,s = 0,1
for i in range(x):
    print(f,end=" ")
    f,s = s,f+s
print()
for i in range(x):
    print(fibonaci(i),end=" ")