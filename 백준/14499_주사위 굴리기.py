def xspin(d):
    if d == 1:
        bottom = xdice.pop()
        xdice.appendleft(ydice.pop())
    else:
        bottom = xdice.popleft()
        xdice.append(ydice.pop())

    ydice.append(bottom)
    ydice[1] = xdice[1]

def yspin(d):
    if d == 1:
        ydice.appendleft(ydice.pop())
    else:
        ydice.append(ydice.popleft())

    xdice[1] = ydice[1]

import sys
from collections import deque

N,M,x,y,K = map(int,sys.stdin.readline().split())
ydice = deque([0,0,0,0])
xdice = deque([0,0,0])
board = []
for n in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

command = list(map(int,sys.stdin.readline().split()))
move = [[0,1],[0,-1],[-1,0],[1,0]]
for c in command:
    c -= 1
    mx = x + move[c][1]
    my = y + move[c][0]
    if N > my > -1 and M > mx > -1:
        x = mx
        y = my
        if c == 0:
            xspin(1)
        elif c == 1:
            xspin(-1)
        elif c == 2:
            yspin(-1)
        else:
            yspin(1)
        if board[y][x] != 0:
            ydice[-1] = board[y][x]
            board[y][x] = 0
        else:
            board[y][x] = ydice[-1]
        print(ydice[1])