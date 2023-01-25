def bfs(tomatos):
    global count
    if len(tomatos) == 0:
        check = 0
        for y in range(N):
            for x in range(M):
                if visit[y][x] == 0:
                    check = 1
                    break
        if check == 0:
            print(count+H)
        else:
            print(-1)
        return
    nexttomatos = []
    for tomato in tomatos:
        for r in ripen:
            y = tomato[0] + r[0]
            x = tomato[1] + r[1]
            if 0 <= y < N and 0 <= x < M:
                if visit[y][x] == 0:
                   nexttomatos.append([y,x])
                   visit[y][x] = 1
    bfs(nexttomatos)
    

M,N,H = list(map(int,input().split()))

visit = []
tomatos = []
ripen = [[1,0],[-1,0],[0,1],[0,-1]]
for y in range(N):
    visit.append([0]*M)
    line = list(map(int,input().split()))
    for x in range(M):
        if line[x] == 1:
            tomatos.append([y,x])
            visit[y][x] = 1
        elif line[x] == -1:
            visit[y][x] = 1

count = 0
bfs(tomatos)