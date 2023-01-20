N,K = list(map(int,input().split()))

coins = []

for i in range(N):
    coins.append(int(input()))
    
dp = [99999]*(K+1)
dp[0] = 0
for i in range(1,K+1):
    for coin in coins:
        if coin <= i:
            if dp[i] > 1 + dp[i - coin]:
                dp[i] = 1 + dp[i - coin]

if dp[K] == 99999:
    print(-1)
else:
    print(dp[K])