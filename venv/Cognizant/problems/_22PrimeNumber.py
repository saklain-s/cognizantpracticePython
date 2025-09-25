import math
x = int(input())
if x < 2:
    print("Not Prime")
else:
    prime = True
    for i in range(2,int(math.sqrt(x))+1): # range(2, int(x**0.5)+1) optimized sol
        if x % i == 0:
            prime = False
            break
    if prime:
        print("Prime")
    else:
        print("Not Prime")