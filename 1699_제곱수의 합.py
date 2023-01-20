N = int(input())

dp = [0]*(N+1)
dp[1] = 1
dp[2] = 2

for i in range(1,N+1):
    dp[i] = i
    for j in range(1,i):
        if j**2 > i:
            break
        if dp[i] > dp[i-j**2] + 1 :
            dp[i] = dp[i-j**2] + 1

print(dp[i])