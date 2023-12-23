import sys
N = int(sys.stdin.readline())
P = [0] + list(map(int,sys.stdin.readline().split()))

dp = [float('inf')] * (N+1)

for n in range(1,N+1):
    dp[n] = P[n]
    for p in range(1,N+1):
        dp[n] = min(dp[n], dp[n-p]+P[p])

print(dp[-1])