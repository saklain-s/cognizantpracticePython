# 🧮 Problem 22: Find all prime numbers up to n
# --------------------------------------------------
# Problem Statement:
# Given a positive integer n, print all prime numbers less than or equal to n.
#
# A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
#
# Example:
# Input: 10
# Output: [2, 3, 5, 7]
#
# Expected:
# - Implement two versions:
#     1️⃣ Basic approach – check each number one by one using a loop.
#     2️⃣ Optimized approach – use the Sieve of Eratosthenes algorithm.
#
# 💡 Hint for the Sieve:
# - Create a boolean array `is_prime[n+1]` initialized to True.
# - Mark all multiples of each prime as False.
# - Collect all numbers still marked True.
import math


def brute(n):
    primes = []
    for x in range(2,n+1):
        is_prime = True
        for i in range(2,x):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return primes


def optimized(n):
    primes = []
    for x in range(2,n+1):
        is_prime = True
        for i in range(2,int(math.sqrt(x))+1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)

    return primes

def sieve_of_eratoshenes(n):
    if n < 2:
        return []
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = True

    for i in range(2, int(n ** 0.5)+1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2,n+1) if is_prime[i]]

    return primes

n = int(input())
print(brute(n))
print(optimized(n))
print(sieve_of_eratoshenes(n))