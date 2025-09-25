books = list(map(int, input().split()))
rem_time = int(input())
size = int(input())

books.sort()
count, total = 0, 0

for book in books:
    if total + book <= rem_time:
        total += book
        count += 1

print(count)
