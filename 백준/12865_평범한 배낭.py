import sys
N, K = map(int,sys.stdin.readline().split())
product = []
dp = [0] * (K + 1)
for n in range(N):
    product.append(list(map(int,sys.stdin.readline().split())))

max_score = 0
for k in range(1,K+1):
    for p in product:
        W = k - p[0]
        if W >= 0:
            plus = p[1] + dp[W]
            dp[k] = max(dp[k-1], plus, dp[k])

print(dp[-1])