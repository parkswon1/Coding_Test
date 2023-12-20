def BFS(nodes):
    global output
    newNodes = []
    for ns in nodes:
        for light in switch[ns[0]][ns[1]]:
            if visit[light[0]][light[1]] == 2:
                visit[light[0]][light[1]] =1
                output += 1
                for mv in move:
                    my = light[0] + mv[0]
                    mx = light[1] + mv[1]
                    if N > my > -1 and N > mx > -1:
                        if visit[my][mx] == 0:
                            newNodes.append([my,mx])
                            break
    for ns in nodes:
        for mv in move:
            my = ns[0] + mv[0]
            mx = ns[1] + mv[1]
            if N > my > -1 and N > mx > -1:
                if visit[my][mx] == 1:
                    newNodes.append([my,mx])
                    visit[my][mx] = 0

    if len(newNodes) != 0:
        BFS(newNodes)

import sys
sys.setrecursionlimit(10**7)
N, M = map(int,sys.stdin.readline().split())
switch = [[[] for _ in range(N)] for __ in range(N)]
visit = [[2 for _ in range(N)] for __ in range(N)]
visit[0][0] = 0

move = [[1,0],[-1,0],[0,1],[0,-1]]
for m in range(M):
    x,y,a,b = map(int,sys.stdin.readline().split())
    switch[y-1][x-1].append([b-1,a-1])

output = 1
BFS([[0,0]])

print(output)