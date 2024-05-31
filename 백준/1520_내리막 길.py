import sys
sys.setrecursionlimit(100000)
M,N = map(int,sys.stdin.readline().split())
miro = []
DP = []
for i in range(M):
    miro.append(list(map(int,sys.stdin.readline().split())))

DP = [[-1] * N for _ in range(M)]

def dfs(y, x):

    if (y, x) == (M-1, N-1):
        return 1

    if DP[y][x]==-1:
        DP[y][x]=0

        move = [(0,1),(0,-1),(1,0),(-1,0)]

        for dy, dx in move:
            my = y + dy
            mx = x + dx

            if 0 <= my < M and 0 <= mx < N and miro[my][mx] < miro[y][x]:
                DP[y][x] += dfs(my, mx)

    return DP[y][x]

print(dfs(0,0))