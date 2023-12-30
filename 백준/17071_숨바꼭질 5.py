import sys
from collections import deque

def BFS():
    while(que):
        n, count = que.popleft()
        for mn in (n + 1, n - 1, 2 * n):
            mcount = count + 1
            check = count % 2
            if 500001 > mn > -1 and visited[mn][check] != mn:
                visited[mn][check] = mcount
                que.append([mn,mcount])


N, K = map(int,sys.stdin.readline().split())
visited = [[0,0] for i in range(500001)]
visited[N][0] = 1
que = deque([[N,0]])
if N == K:
    print(0)
else:
    BFS()