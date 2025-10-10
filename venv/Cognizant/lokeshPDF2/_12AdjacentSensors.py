"""
Problem:
For each sensor, count how many of its two adjacent sensors in a circular
arrangement have a strictly greater signal strength.

Input:
- An integer N (number of sensors)
- A list of N integers A (signal strengths)

Output:
- A list of N integers: counts of greater adjacent sensors for each sensor.

Example:
Input:
5
10 15 12 9 14
Output:
[2, 0, 1, 2, 0]
"""
def adjacent_sensors(A, N):
    result = []
    for i in range(N):
        cnt = 0
        left = A[(i-1)%N]
        right =A[(i+1)%N]
        if left > A[i]:
            cnt+=1
        if right > A[i]:
            cnt+=1
        result.append(cnt)
    return result

N = int(input().strip())
A = list(map(int, input().split()))

print(adjacent_sensors(A, N))
