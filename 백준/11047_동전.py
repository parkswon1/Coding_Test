import sys
N, K= list(map(int,sys.stdin.readline().split()))

coins = []
for i in range(N):
    coins.append(int(sys.stdin.readline()))

count = 0
for i in range(-1,-(N+1),-1):
    count += K//coins[i]
    K = K%coins[i]
    if K == 0:
        break
    
print(count)