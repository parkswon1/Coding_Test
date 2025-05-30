def solution(N, number):
    dp = [set() for _ in range(9)]
    
    if N == number:
        return 1
    
    dp[1].add(N)
    for i in range(2,9):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
        dp[i].add(int(str(N) * i))
        
        if number in dp[i]:
            return i
    
    return -1