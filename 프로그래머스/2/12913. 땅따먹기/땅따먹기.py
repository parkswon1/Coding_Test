def solution(land):
    answer = 0
    dp = land[0][:]
    for i in range(1, len(land)):
        nextdp = [0] * len(land[0])
        for j in range(len(nextdp)):
            for k in range(len(nextdp)):
                if j == k:
                    continue
                
                nextdp[j] = max(nextdp[j], dp[k] + land[i][j])
        
        dp = nextdp[:]
    return max(dp)