x = int(input())
sumf = 0
temp = x
while x > 0:
    rem = x % 10
    sumf = sumf * 10 + rem
    x//=10

if sumf == temp:
    print("Palindrome")
else:
    print("Not a Palindrome")

#Or this method
n = input()
if (int(n)<0):
    print("Invalid")
elif n== n[::-1]:
    print("Yes")
else:
    print("No")