import sys

dp = [0]*10001
number = [1,2,3]
dp[0] = 1
for n in number:
    for i in range(1,10001):
        if i - n >= 0:
            dp[i] += dp[i-n]

T = int(sys.stdin.readline())
for t in range(T):
    print(dp[int(sys.stdin.readline())])