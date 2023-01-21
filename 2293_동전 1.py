import sys
n, k = list(map(int,sys.stdin.readline().split()))

coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline()))

dp = [[0 for _ in range(n)] for _ in range(k + 1)]
dp[0][0] = 1

for i in range(k+1):
    for coin in range(n):
        if i - coins[coin] >= 0:
            dp[i][coin] = sum(dp[i-coins[coin]][0:coin+1])

print(sum(dp[k]))