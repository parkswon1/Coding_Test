def solution(strs, t):
    n = len(t)
    INF = 10**9
    dp = [INF] * (n + 1)
    dp[0] = 0

    strs_set = set(strs)
    max_len = max(len(s) for s in strs)

    for i in range(1, n + 1):
        for l in range(1, max_len + 1):
            if i - l >= 0 and t[i-l:i] in strs_set:
                dp[i] = min(dp[i], dp[i-l] + 1)

    return -1 if dp[n] == INF else dp[n]