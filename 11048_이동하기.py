import sys
sys.setrecursionlimit(10**6)

def dfs(node,count):
    count += miro[node[0]][node[1]]
    if node == [N-1,M-1]:
        output.append(count)
        return
    for yx in move:
        y = node[0] + yx[0]
        x = node[1] + yx[1]
        if 0 <= x < M and 0 <= y < N:
            dfs([y,x],count)

N, M = list(map(int,sys.stdin.readline().split()))
miro = []
for i in range(N):
    miro.append(list(map(int,sys.stdin.readline().split())))

output = []
move = [[0,1],[1,0],[1,1]]
dfs([0,0],0)

print(max(output))