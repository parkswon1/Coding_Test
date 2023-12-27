import sys

T = int(sys.stdin.readline())
dp = ['188888888888889'] * 94
dp = [0,0,'1','7','4','2','0','8'] + dp
dp[13] = '68'

for i in range(8,101):
    for j in range(2,i-1):
        dpnow = dp[i-j] + dp[j]
        if dpnow[0] != '0':
            dp[i] = str(min(int(dpnow),int(dp[i])))

for r in range(T):
    N = int(sys.stdin.readline())
    big = []
    n = N
    if n >= 3:
        if n%2 != 0:
            n = n - 3
            big.append('7')
            for _ in range(n//2):
                big.append('1')
        else:
            for _ in range(n//2):
                big.append('1')
    else:
        big = ['1']
    if N == 6:
        print(6,''.join(big))
    else:
        print(dp[N],''.join(big))