def BFS():
    global output
    for n in range(1,N+1):
        if visit[n] == 0:
            output += 1
            que = deque([])
            visit[n] = 1
            que.append(n)
            while(que):
                nowNode = que.popleft()
                nextNodes = nodes[nowNode]
                for next in nextNodes:
                    if visit[next] == 0:
                        visit[next] = 1
                        que.append(next)

import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
nodes = [[]for n in range(N + 1)]
visit = [0] * (N + 1)
for m in range(M):
    u,v = map(int,sys.stdin.readline().split())
    nodes[u].append(v)
    nodes[v].append(u)

output = 0
BFS()
print(output)