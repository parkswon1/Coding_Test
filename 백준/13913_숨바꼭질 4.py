from collections import deque

def bfs(start):
    global count
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current == K:
            print(count[K])
            dfs(K)
            print(*output)
            return

        next_nodes = []
        n_next = current * 2
        if n_next <= 100000 and visit[n_next] == -1 and n_next != 0:
            next_nodes.append(n_next)
            visit[n_next] = current
            count[n_next] = count[current] + 1
            queue.append(n_next)
        n_next = current - 1
        if 0 <= n_next <= 100000 and visit[n_next] == -1:
            next_nodes.append(n_next)
            visit[n_next] = current
            count[n_next] = count[current] + 1
            queue.append(n_next)
        n_next = current + 1
        if n_next <= 100000 and visit[n_next] == -1:
            next_nodes.append(n_next)
            visit[n_next] = current
            count[n_next] = count[current] + 1
            queue.append(n_next)

def dfs(K):
    output.appendleft(K)
    while K != N:
        K = visit[K]
        output.appendleft(K)

import sys
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())

visit = [-1]*100001
count = [0]*100001
visit[N] = N
count[N] = 0
output = deque([])
bfs(N)