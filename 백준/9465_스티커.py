import sys
T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    stiker = []
    dp = []
    for _ in range(2):
        dp.append([0]*N)
        stiker.append(list(map(int,sys.stdin.readline().split())))
    dp[0][0] = stiker[0][0]
    dp[1][0] = stiker[1][0]

    for n in range(1,N):
        dp[0][n] = max(dp[1][n - 1] + stiker[0][n], dp[0][n - 1])
        dp[1][n] = max(dp[0][n - 1] + stiker[1][n], dp[1][n - 1])

    print(max(dp[0][N - 1], dp[1][N - 1]))