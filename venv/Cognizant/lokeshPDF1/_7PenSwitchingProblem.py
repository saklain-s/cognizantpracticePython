n = int(input())
arr = list(map(int,input().split()))
switches=0
prev_odd = None
for num in arr:
    is_odd = num % 2 ==1
    if prev_odd is not None:
        if not is_odd and prev_odd:
            switches+=1
    prev_odd = is_odd
print(switches)
