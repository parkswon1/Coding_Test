import sys
sys.setrecursionlimit(10**6)

def cal(dp,count):
    if count == n:
        print(sum(dp)%9901)
        return
    output = [0,0,0]
    output[0] = sum(dp)
    output[1] = dp[0] + dp[2]
    output[2] = dp[0] + dp[1]
    cal(output,count+1)
        
n = int(input())
cal([1,1,1],1)