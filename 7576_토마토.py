def BFS(Tomatos):
    global day
    NewTomatos = []
    for Tomato in Tomatos:
        for mv in Move:
            y = Tomato[0] + mv[0]
            x = Tomato[1] + mv[1]
            if 0 <= y < N and 0 <= x < M:
                if Box[y][x] == 0:
                    Box[y][x] = 1
                    NewTomatos.append([y,x])
    if len(NewTomatos) == 0:
        for n in range(N):
            for m in range(M):
                if Box[n][m] == 0:
                    print(-1)
                    return
        print(day)
        return
    day += 1
    BFS(NewTomatos)

import sys
sys.setrecursionlimit(10**9)

M, N = list(map(int,sys.stdin.readline().split()))

Box = []
Tomatos = []
Move = [[0,1],[0,-1],[1,0],[-1,0]]
for n in range(N):
    Line = list(map(int,sys.stdin.readline().split()))
    for l in range(len(Line)):
        if Line[l] == 1:
            Tomatos.append([n,l])
    Box.append(Line)

day = 0
BFS(Tomatos)