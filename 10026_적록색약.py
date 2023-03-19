def DFS_B_RG(Node):
    for mv in Move:
        y = mv[0] + Node[0]
        x = mv[1] + Node[1]
        if 0 <= x < N and 0 <= y < N:
            if Picture[y][x] == Check:
                Picture[y][x] = Number
                DFS_B_RG([y,x])
                
import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())

Picture = []
Move = [[1,0],[-1,0],[0,1],[0,-1]]
for n in range(N):
    Picture.append(list(sys.stdin.readline().rstrip()))
    
Healthy = 0
C_Weak = 0
for n in range(N):
    for m in range(N):
        if Picture[n][m] != 1 and Picture[n][m] != 0:
            Healthy += 1
            Check = Picture[n][m]
            if Check == 'B':
                Number = 1
            else:
                Number = 0
            Picture[n][m] = Number
            DFS_B_RG([n,m])
            
for n in range(N):
    for m in range(N):
        if Picture[n][m] != 2:
            C_Weak += 1
            Check = Picture[n][m]
            Number = 2
            Picture[n][m] = Number
            DFS_B_RG([n,m])
            
print(Healthy,C_Weak)