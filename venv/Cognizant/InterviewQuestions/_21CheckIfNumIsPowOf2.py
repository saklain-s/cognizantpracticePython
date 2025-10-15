def brute_force(n):
    if n <= 0:
        return False

    while n > 1:
        if n % 2 != 0:
            return False

        n = n // 2

    return True

def optimized(n):

    return (n > 0) and ((n&(n-1)) == 0)



n = int(input())
print(brute_force(n))
print(optimized(n))