import sys
N = int(sys.stdin.readline())
P = [0] + list(map(int,sys.stdin.readline().split()))
dp = [0]*(N+1)
for j in range(1,N+1):
    for i in range(1,j+1):
        if dp[j] < dp[j - i] + P[i]:
            dp[j] = dp[j - i] + P[i]
            
print(dp[N])