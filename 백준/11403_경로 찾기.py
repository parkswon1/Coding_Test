def DFS(nd):
    check = 0
    for i in node[nd]:
        if visited[i] == 0:
            check = 1
            visited[i] = 1
            DFS(i)
    if check == 0:
        return

import sys
sys.setrecursionlimit(10**7)
N = int(sys.stdin.readline())
node = [[]for i in range(N)]
for n in range(N):
    line = list(map(int,sys.stdin.readline().split()))
    for m in range(N):
        if line[m] == 1:
            node[n].append(m)
for n in range(N):
    visited = [0] * N
    DFS(n)
    print(*visited)