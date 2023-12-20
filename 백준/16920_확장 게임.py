def BFS(players):
    check = 0
    for i in range(P):
        if len(players[i]) != 0:
            checkS = players[i][0][2]
        while(players[i]):
            p = players[i].popleft()
            if p[2] == checkS + S[i]:
                players[i].append(p)
                break
            for mv in move:
                my = p[0] + mv[0]
                mx = p[1] + mv[1]
                if N > my > -1 and M > mx > -1 and board[my][mx] == '.':
                    check = 1
                    count[i] += 1
                    board[my][mx] = i
                    players[i].append([my, mx, p[2] + 1])
    if check == 1:
        BFS(players)

import sys
from collections import deque
sys.setrecursionlimit(10**7)

N, M, P = map(int,sys.stdin.readline().split())
S = list(map(int,sys.stdin.readline().split()))
board = []
player = [deque([]) for p in range(P)]
count = [0] * (P)
for n in range(N):
    line = list(sys.stdin.readline().rstrip())
    for m in range(M):
        if line[m] != '#' and line[m] != '.':
            count[int(line[m])-1] += 1
            player[int(line[m])-1].append([n,m,1])
    board.append(line)

move = [[1,0],[-1,0],[0,1],[0,-1]]

BFS(player)

print(*count)