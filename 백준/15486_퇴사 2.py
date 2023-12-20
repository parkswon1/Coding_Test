from sys import stdin

N = int(stdin.readline())
dp = [0]*(N+1)
for i in range(1, N+1):
    t, p = map(int, stdin.readline().split())
    dp[i] = max(dp[i-1], dp[i])
    if i+t<=N+1:
        dp[i+t-1] = max(dp[i-1]+p, dp[i+t-1])

print(dp[-1])