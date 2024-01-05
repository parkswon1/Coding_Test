import sys
from collections import deque

def fising(shark):
    global output
    new_shark = deque([])
    king += 1
    nice(king)
    while(shark):
        y,x = shark.popleft()
        s,d,z = board[y][x]
        if d != 0:
            board[y][x] = [0,0,0]
            my = (move[d][0] * s)
            if R <= my:
                my = 2(R - 1) - my
                d = 2
            elif my < 0:
                my = abs(my)




            mx = (move[d][1] * s)






def nice(x):
    global output
    for r in range(R):
        if board[r][x] != 0:
            output += board[r][x][2]
            board[r][x] = [0,0,0]
            return

move = [[],[-1,0],[1,0],[0,1],[0,-1]]
R, C, M = map(int, sys.stdin.readline().split())
board = [[0,0,0] * C for _ in range(R)]
shark = deque([])
king = -1
for i in range(R):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    board[r][c] = [s,d,z]
    shark.append([r,c])

output = 0
fising()