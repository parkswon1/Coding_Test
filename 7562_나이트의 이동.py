def BFS(Knights):
    global Output
    New_Knights = []
    Output += 1
    
    for KT in Knights:
        for mv in Move:
            y = KT[0] + mv[0]
            x = KT[1] + mv[1]
            if 0 <= x < I and 0 <= y < I:
                if [y,x] == Goal:
                    print(Output)
                    return
                elif Board[y][x] == 0:
                    New_Knights.append([y,x])
                    Board[y][x] = 1
    
    BFS(New_Knights)

import sys
sys.setrecursionlimit(10**7)

T = int(input())

Move = [[1,2],[-1,2],[1,2],[1,-2],[2,1],[-2,1],[2,1],[2,-1]]
for t in range(T):
    I = int(sys.stdin.readline())
    Board = []
    
    for i in range(I):
        Board.append([0]*I)
    
    Knight = list(map(int,sys.stdin.readline().split()))
    Board[Knight[0]][Knight[1]] = 1
    Goal = list(map(int,sys.stdin.readline().split()))
    Output = 0
    
    if Knight == Goal:
        print(Output)
    else:
        BFS([Knight])