n = int(input())
total = 0

for i in range(1, n + 1):
    chocolates = i

    left = n if i == 1 else i - 1
    right = 1 if i == n else i + 1

    if i % 5 != 0 and (left % 5 == 0 or right % 5 == 0):
        chocolates += 2

    total += chocolates

print(total % (10**9 + 7))
