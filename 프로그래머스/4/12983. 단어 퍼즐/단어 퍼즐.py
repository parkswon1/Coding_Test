def solution(strs, t):
    n = len(t)
    strSet = set(strs)
    sizes = set(len(s) for s in strs)
    
    dp = [float("inf")] * (n+1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        for size in sizes:
            if i - size >= 0 and t[i -size:i] in strSet:
                dp[i] = min(dp[i], dp[i - size] + 1)

    return dp[n] if dp[n] != float("inf") else - 1