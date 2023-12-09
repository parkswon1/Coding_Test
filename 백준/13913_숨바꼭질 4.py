def bfs(node):
    global count
    next_node = []
    for n in node:
        if n == K:
            print(count)
            print(*visit[n])
            return
        arr = visit[n]
        n_next = n * 2
        if n_next <= 100000 and visit[n_next] == []:
            next_node.append(n_next)
            for a in arr:
                visit[n_next].append(a)
            visit[n_next].append(n_next)
        n_next = n - 1
        if n_next <= 100000 and visit[n_next] == []:
            next_node.append(n_next)
            for a in arr:
                visit[n_next].append(a)
            visit[n_next].append(n_next)
        n_next = n + 1
        if n_next <= 100000 and visit[n_next] == []:
            next_node.append(n_next)
            for a in arr:
                visit[n_next].append(a)
            visit[n_next].append(n_next)
    count += 1
    bfs(next_node)

import sys
sys.setrecursionlimit(10**7)

N, K = map(int,sys.stdin.readline().split())

if K < N:
    print(N-K)
    print(*[i for i in range(N,K-1,-1)])
else:
    visit = [[] for _ in range(100001)]
    visit[N].append(N)
    count = 0
    bfs([N])