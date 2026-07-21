def solution(m, n, puddles):
    answer = 0
    puddlset =set()
    for p in puddles:
        puddlset.add((p[1] - 1,p[0] - 1))
    dp = [[0] * (m) for _ in range(n)]
    for x in range(m):
        if (0, x) in puddlset:
            break
        dp[0][x] = 1
    for y in range(n):
        if (y, 0) in puddlset:
            break
        dp[y][0] = 1
    for y in range(1, n):
        for x in range(1, m):
            dp[y][x] = dp[y][x - 1] + dp[y - 1][x]
            if (y, x) in puddlset:
                dp[y][x] = 0
    
    
    print(dp)
    print(puddlset)
    
    return dp[n - 1][m - 1] % 1000000007