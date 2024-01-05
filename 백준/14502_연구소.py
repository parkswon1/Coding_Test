import copy
import sys
from collections import deque
import copy
def search(count):
    if count == 3:
        bfs()
        return

    else:
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    board[i][j] = 1
                    search(count + 1)
                    board[i][j] = 0
def bfs():
    global output
    que = deque([])
    visited = copy.deepcopy(board)
    for n in range(N):
        for m in range(M):
            if visited[n][m] == 2:
                que.append([n,m])
    while que:
        y,x = que.popleft()
        for mv in move:
            my = y + mv[0]
            mx = x + mv[1]
            if 0 <= my < N and 0 <= mx < M:
                if visited[my][mx] == 0:
                    visited[my][mx] = 2
                    que.append([my,mx])
    count = 0
    for n in range(N):
        for m in range(M):
            if visited[n][m] == 0:
                count += 1
    output = max(count,output)

N, M = map(int,sys.stdin.readline().split())
board = []

zeroCount = 0
virus = []
move = [[1,0],[0,1],[-1,0],[0,-1]]
output = 0
for n in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
search(0)

print(output)