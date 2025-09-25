def solution(money):
    answer = 0
    
    def dp(arr):
        dp = [0] * len(arr)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            dp[i] = max(arr[i] + dp[i-2], dp[i-1])
        return dp[-1]        
        
    return max(dp(money[:-1]), dp(money[1:]))