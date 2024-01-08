import sys
from collections import deque

def melt(air):
    global time
    time += 1
    nextAir = deque([])
    while(air):
        y,x = air.popleft()
        for mv in move:
            my = y + mv[0]
            mx = x + mv[1]
            if 0 <= my < N and 0 <= mx < M:
                if board[my][mx] == 1:
                    board[my][mx] = time
                    nextAir.append([my,mx])
                elif board[my][mx] == 0:
                    board[my][mx] = -1
                    air.append([my,mx])
    if len(nextAir) != 0:
        melt(nextAir)
    else:
        print(time - 2)
        output = 0
        for n in range(N):
            for m in range(M):
                if board[n][m] == time - 1:
                    output += 1
        print(output)

N, M = map(int, sys.stdin.readline().split())

board = []
air = deque([[0,0]])
time = 1
move = [[0,1],[1,0],[-1,0],[0,-1]]
for n in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

board[0][0] = -1
melt(air)