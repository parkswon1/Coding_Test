def DFS(n,m):
    for mv in MV:
        y = n + mv[0]
        x = m + mv[1]
        if 0 <= x < M and 0 <= y < N:
            if Field[y][x] == 1:
                Field[y][x] = 0
                DFS(y,x)
import sys
sys.setrecursionlimit(10**7)

T = int(sys.stdin.readline())
for t in range(T):
    M, N, K = list(map(int,sys.stdin.readline().split()))
    
    Field = []
    
    for n in range(N):
        Field.append([0]*M)    
    
    for i in range(K):
        X,Y = list(map(int,sys.stdin.readline().split()))
        Field[Y][X] = 1
        
    Output = 0
    MV = [[1,0],[-1,0],[0,-1],[0,1]]
    
    for n in range(N):
        for m in range(M):
            if Field[n][m] == 1:
                Output += 1
                DFS(n,m)
                
    print(Output)