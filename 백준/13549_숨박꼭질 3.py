def dfs(nodes):
    global low
    new_nodes = []
    for n in nodes:
        if n[0] == K:
            low = min(low,n[1])
        next = n[0] * 2
        if 100001 > next > -1 and index[next] > n[1]:
            new_nodes.append([next,n[1]])
            index[next] = n[1]
        next = n[0] + 1
        if 100001 > next > -1 and index[next] > n[1] + 1:
            new_nodes.append([next, n[1]+1])
            index[next] = n[1]+1
        next = n[0] - 1
        if 100001 > next > -1 and index[next] > n[1] + 1:
            new_nodes.append([next, n[1]+1])
            index[next] = n[1]+1
    if len(new_nodes) == 0:
        return
    dfs(new_nodes)

import sys
sys.setrecursionlimit(10**7)

index = [float('inf')]*(100001)
low = float('inf')
N, K = map(int,sys.stdin.readline().split())
index[N] = float('inf')
if K < N:
    low = N - K
else:
    dfs([[N,0]])

print(low)