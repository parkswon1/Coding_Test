def solution(triangle):
    dp = [triangle[0]]

    for i in range(1, len(triangle)):
        temp = []
        temp.append(dp[i-1][0] + triangle[i][0]) 

        for j in range(1, len(triangle[i]) - 1):
            temp.append(max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])

        temp.append(dp[i-1][-1] + triangle[i][-1])
        dp.append(temp)

    return max(dp[-1])
