import sys
N = int(sys.stdin.readline())

dp1 = [0] * N
dp2 = [0] * N
numbers = list(map(int, sys.stdin.readline().split()))
dp1[0] = 1
dp2[-1] = 1

for i in range(1,N):
    temp = 0
    for j in range(i-1,-1,-1):
        if numbers[j] < numbers[i]:
            temp = max(dp1[j], temp)
    dp1[i] = 1 + temp

output = 0
for i in range(N-1,-1,-1):
    temp = 0
    for j in range(i+1,N):
        if numbers[j] < numbers[i]:
            temp = max(dp2[j], temp)
    dp2[i] = 1 + temp
    output = max(dp1[i] + dp2[i] - 1, output)

print(output)