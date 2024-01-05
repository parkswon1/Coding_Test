import sys
from collections import deque

def bfs():
    while(que):
        node = que.popleft()
        if visited[node] == 0:
            visited[node] = 1
            for n in nodes[node]:
                que.append(n)

def cantrip():
    for t in trip:
        if visited[t-1] == 0:
            print('NO')
            return
    print('YES')


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
nodes = [[] for n in range(N)]
for m in range(N):
    line = list(map(int,sys.stdin.readline().split()))
    for n in range(N):
        if line[n] == 1:
            nodes[m].append(n)


visited = [0]*N
trip = set((map(int,sys.stdin.readline().split())))
que = deque([trip.pop()-1])
bfs()
cantrip()