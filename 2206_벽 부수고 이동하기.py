import sys
sys.setrecursionlimit(10**7)

def bfs(node,count):
    nextnode =[]
    for yxz in node:
        for mv in move:
            y = yxz[0] + mv[0]
            x = yxz[1] + mv[1]
            if y == N-1 and x == M-1:
                print(count)
                return
            if 0 <= y < N and 0 <= x < M:
                if visit[y][x] == 0:
                  if wall[y][x] == '0':
                      visit[y][x] = 1
                      nextnode.append([y,x,yxz[2]])
                  elif wall[y][x] == '1' and yxz[2] == 0:
                      visit[y][x] = 1
                      nextnode.append([y,x,1])
    if len(nextnode) == 0:
        print(-1)
        return
    else:
        bfs(nextnode,count+1)

N, M = list(map(int,sys.stdin.readline().rstrip().split()))

wall = []
visit = []
move = [[0,1],[0,-1],[1,0],[-1,0]]
for i in range(N):
    wall.append(list(input()))
    visit.append([0]*M)
visit[0][0]=1
node = [[0,0,0]]
if N == 1 and M == 1:
    print(1)
else:
    bfs(node,2)