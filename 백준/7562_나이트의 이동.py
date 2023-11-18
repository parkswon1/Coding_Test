from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
dx=[-2,-2,-1,-1,1,1,2,2]
dy=[1,-1,2,-2,2,-2,1,-1]
def bfs(x,y,a,b):
    queue = deque()
    temp = deque()
    queue.append((x,y))
    cnt =0
    while True:
        for i in range(len(queue)):
            x,y= queue.popleft()
            for i in range(8):
                if x == a and y == b:
                    return cnt
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or nx>=m or ny<0 or ny>=m:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    temp.append((nx,ny))

        cnt+=1
        queue = temp

for _ in range(n):
    m = int(stdin.readline().rstrip())
    graph = [] #visited로 사용//
    for i in range(m):
        graph.append([])
        for j in range(m):
            graph[i].append(0)
    a,b = map(int,stdin.readline().rstrip().split()) #//현재 나이트
    x,y = map(int,stdin.readline().rstrip().split()) #//목표
    print(bfs(x,y,a,b))
