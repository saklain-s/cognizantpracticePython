import math
x = int(input())
if x < 2:
    print("Not a prime")
else:
    Y = True
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            Y = False
            break
    if Y:
        print("Prime")
    else:
        print("No ")