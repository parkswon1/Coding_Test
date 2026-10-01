def dp(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    dp[1] = max(arr[1], dp[0])
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-2] + arr[i], dp[i-1])

    return dp[-1]

def solution(money):


    answer = 0
    answer = max(dp(money[:-1]), dp(money[1:]))
    
    return answer