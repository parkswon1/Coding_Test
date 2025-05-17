def solution(k, money):
    answer = 0
    
    dp = [0]*(k+1)
    dp[0] = 1  

    for coin in money:
        for i in range(coin, k+1):
            dp[i] += dp[i - coin]

        
    
    return (dp[k])