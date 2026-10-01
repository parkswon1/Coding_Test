def solution(triangle):
    answer = 0
    dp = [triangle[0]]
    for y in range(1, len(triangle)):
        dp.append(triangle[y][:])
        dp[y][0] = dp[y-1][0] + triangle[y][0]
        dp[y][-1] = dp[y-1][-1] + triangle[y][-1]
        for x in range(1, len(dp[y]) - 1):
            dp[y][x] = max(dp[y-1][x]+ triangle[y][x], + dp[y-1][x -1] + triangle[y][x])
    return max(dp[-1])