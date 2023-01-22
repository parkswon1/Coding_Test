N = int(input())

if N % 2 != 0:
    print(0)
else:
    N = N//2
    dp = [0]*(N+1)
    dp[1] = 3
    for i in range(2,N+1):
        dp[i] += dp[i-1]*3
        for j in range(i-2,0,-1):
            dp[i] += dp[j]*2
        dp[i] += 2
        
    print(dp[N])