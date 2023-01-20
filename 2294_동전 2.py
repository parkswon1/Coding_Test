import sys
N,K = list(map(int,sys.stdin.readline().split()))

coins = []

for i in range(N):
    coins.append(int(sys.stdin.readline()))
    
dp = [99999]*(K+1)
dp[0] = 0
for i in range(1,K+1):
    for coin in coins:
        if coin <= i and dp[i % coin] != 99999:
            if dp[i] > (i // coin) + dp[i % coin]:
                dp[i] = (i // coin) + dp[i % coin]

if dp[K] == 99999:
    print(-1)
else:
    print(dp[K])