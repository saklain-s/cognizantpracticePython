x = int(input())
sumof = 0
temp = x
while(x > 0):
    rem = x % 10
    sumof = (sumof * 10) +rem
    x//=10
if sumof == temp:
    print("Palindrome")
else:
    print("Not a Palindrome")

#Or this method
n = input()
if(int(n)<0):
    print("Invalid Input")
elif(n==n[::-1]):
    print("Palindrome")
else:
    print("Not palindrome")