def DFS(N,M):
    global Count
    for mv in Move:
        y = N + mv[0]
        x = M + mv[1]
        if 0 <= x < m and 0 <= y < n:
            if paper[y][x] == 1:
                paper[y][x] = 0
                Count += 1
                DFS(y,x)
                
import sys
sys.setrecursionlimit(10**6)
n, m = list(map(int,sys.stdin.readline().split()))

paper = []
Output = []
Move = [[1,0],[-1,0],[0,-1],[0,1]]

for N in range(n):
    paper.append(list(map(int,sys.stdin.readline().rstrip().split())))

for N in range(n):
    for M in range(m):
        if paper[N][M] == 1:
            Count = 1
            paper[N][M] = 0
            DFS(N,M)
            Output.append(Count)

if len(Output) == 0:
    print(0)
    print(0)

else:      
    print(len(Output))
    print(max(Output))