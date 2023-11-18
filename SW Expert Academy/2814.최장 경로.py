def DFS(n,count,visit):
    global score
    score = max(count,score)
    for node in nodes[n]:
        if visit[node] != 1:
            visit[node] = 1
            DFS(node,count+1,visit)
            visit[node] = 0

T = int(input())

for test_case in range(1,T+1):
    score = 0
    N, M = map(int,input().split())
    nodes = [[] for n in range(N+1)]
    visit = [0] * (N+1)
    if M != 0:
        for m in range(M):
            x, y = map(int,input().split())
            nodes[x].append(y)
            nodes[y].append(x)
        for n in range(1,N+1):
            visit[n] = 1
            DFS(n,0,[0]*(N+1))
            visit[n] = 0
    print(f'#{test_case}',score)