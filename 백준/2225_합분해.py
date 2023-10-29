import sys
N, K = list(map(int,sys.stdin.readline().split()))

dp = []
dp.append([1]*(N+1))
for j  in range(K-1):
    dp.append([1] + [0 for i in range(N)])

for i in range(1,K):
    for j in range(1,N+1):
        for m in range(j+1):
            dp[i][j] += dp[i-1][m]
            
print(dp[-1][-1]%1000000000)