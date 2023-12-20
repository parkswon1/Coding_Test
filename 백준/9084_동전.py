import sys

for t in range(int(sys.stdin.readline())):
    dp = [0]*10001
    N = int(sys.stdin.readline())
    number = list(map(int,sys.stdin.readline().split()))
    dp[0] = 1
    for n in number:
        for i in range(1,10001):
            if i - n >= 0:
                dp[i] += dp[i-n]
    print(dp[int(sys.stdin.readline())])