import sys

N, K = map(int,sys.stdin.readline().split())
dp = [[0] * (K+1)]
WV = []
for n in range(N):
    WV.append(list(map(int,sys.stdin.readline().split())))

WV.sort()

for i in range(N):
    w = WV[i][0]
    v = WV[i][1]
    dpk = [0]*(K+1)
    for k in range(1,K+1):
        if k - w >= 0:
            dpk[k] = v +dp[i][k-w]
        dpk[k] = max(dp[i][k],dpk[k])
    dp.append(dpk)

print(dp[-1][-1])