import sys
from collections import deque

def BFS():
    while(que):
        n, count, k = que.popleft()
        for mn in (n + 1, n - 1, 2 * n):
            mcount = count + 1
            mk = k + mcount
            check = count % 2
            if 500001 > mn > -1 and 500001 > k > -1 and visited[mn][check] != mn:
                visited[mn][check] = 1
                if visited[mk][check] != 0:
                    print(mcount)
                    return
                que.append([mn,mcount,mk])

    print(-1)
    return

sys.setrecursionlimit(10**7)
N, K = map(int,sys.stdin.readline().split())
visited = [[0,0] for i in range(500001)]
visited[N][0] = 1
que = deque([[N,0,K]])
if N == K:
    print(0)
else:
    BFS()