def BFS(Tomatos):
    global day
    NewTomatos = []
    for Tomato in Tomatos:
        for mv in Move:
            x = mv[2] + Tomato[2]
            y = mv[1] + Tomato[1]
            z = mv[0] + Tomato[0]
            if 0 <= x < M and 0 <= y < N and 0 <= z < H :
                if Boxs[z][y][x] == 0:
                    Boxs[z][y][x] = 1
                    NewTomatos.append([z,y,x])    
    if len(NewTomatos) == 0:
        for h in range(H):
            for n in range(N):
                for m in range(M):
                    if Boxs[h][n][m] == 0:
                       print(-1)
                       return
        print(day)
        return
    day += 1
    BFS(NewTomatos)
    

import sys
sys.setrecursionlimit(10**9)

M,N,H = list(map(int,sys.stdin.readline().split()))

Move = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]
Boxs = []
Tomatos = []
for h in range(H):
    Box = []
    for n in range(N):
        Line = list(map(int,sys.stdin.readline().split()))
        for m in range(M):
            if Line[m] == 1:
                Tomatos.append([h,n,m])
        Box.append(Line)
    Boxs.append(Box)

day = 0
BFS(Tomatos)