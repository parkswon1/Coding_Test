def solution(m, n, puddles):
    answer = 0
    dp = []
    for y in range(n):
        dp.append([0] * m)
    
    p = set()
    for x, y in puddles:
        p.add((y -1,x -1))
    
    dp[0][0] = 1
    for x in range(1, m):
        if (0, x) in p:
            continue
        dp[0][x] = dp[0][x - 1]
    
    for y in range(1, n):
        if (y, 0) not in p:
            dp[y][0] = dp[y-1][0]
            
        for x in range(1, m):
            if (y, x) in p:
                continue
            dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % 1000000007
    
    
    return dp[-1][-1]