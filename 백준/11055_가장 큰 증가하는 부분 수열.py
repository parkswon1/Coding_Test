import sys
N = int(sys.stdin.readline())

dp = [0] * N
numbers = list(map(int, sys.stdin.readline().split()))
dp[0] = numbers[0]

output = dp[0]
for i in range(1,N):
    temp = 0
    for j in range(i-1,-1,-1):
        if numbers[j] < numbers[i]:
            temp = max(dp[j], temp)
    dp[i] = numbers[i] + temp
    output = max(dp[i], output)
print(output)