def game():
    global second, direction
    for n in range(N):
        print(board[n])
    print('')
    second += 1
    mx = snail[-1][1] + move[direction][1]
    my = snail[-1][0] + move[direction][0]
    if N > my > -1 and N > mx > -1 and board[my][mx] != 1:
        snail.append([my,mx])
        board[my][mx] = 1
        if board[my][mx] != 2:
            yx = snail.popleft()
            board[yx[0]][yx[1]] = 0
        if len(command) != 0 and command[0][0] == second:
            if command[0][1] == 'D':
                direction = (direction + 1)%4
            else:
                direction = (direction - 1)%4
            command.popleft()
        game()
    else:
        print(second)
        return

import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

snail = deque([[0,0]])
board = []
command = deque([])
for n in range(N):
    board.append([0]*N)

for k in range(K):
    y, x = map(int,input().split())
    board[y][x] = 2
board[0][0] = 1
L = int(input())

move = [[0,1],[1,0],[0,-1],[-1,0]]

for l in range(L):
    X, com = input().split()
    command.append([int(X),com])

second = 0
direction = 0
game()