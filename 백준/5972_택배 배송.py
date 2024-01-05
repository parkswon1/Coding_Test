import sys
from collections import deque

def search():
    while(que):
        x = que.popleft()
        for g in G[x]:
            if visited[g[0]] > visited[x] + g[1]:
                visited[g[0]] = visited[x] + g[1]
                que.append(g[0])

N, M = map(int, sys.stdin.readline().split())

visited = [float('inf')] * (N + 1)
G = [[] for _ in range(N + 1)]

visited[1] = 0
for m in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    G[A].append([B,C])
    G[B].append([A,C])
que = deque([1])
search()

print(visited[N])