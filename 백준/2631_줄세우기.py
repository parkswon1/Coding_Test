import sys
N = int(sys.stdin.readline())

dp = [0] * N
numbers = []
for n in range(N):
    numbers.append(int(sys.stdin.readline()))

dp[0] = 1
output = dp[0]
for i in range(1,N):
    temp = 0
    for j in range(i-1,-1,-1):
        if numbers[j] < numbers[i]:
            temp = max(dp[j], temp)
    dp[i] = 1 + temp
    output = max(dp[i], output)
print(N - output)