import sys
N = int(sys.stdin.readline())

dp = [0] * N
numbers = list(map(int, sys.stdin.readline().split()))
dp[0] = 1
dpList = [[numbers[0]]]
output = 0
for i in range(1,N):
    temp = i
    for j in range(i-1,-1,-1):
        if numbers[j] < numbers[i]:
            if dp[j] > dp[temp]:
                temp = j
    dp[i] = 1 + dp[temp]
    if temp != i:
        dpList.append(dpList[temp] + [numbers[i]])
    else:
        dpList.append([numbers[i]])
    if dp[i] > dp[output]:
        output = i
print(dp[output])
print(*dpList[output])