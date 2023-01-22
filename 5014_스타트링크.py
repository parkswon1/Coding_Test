import sys
sys.setrecursionlimit(10**7)

def bfs(S):
    global count
    nextS = []
    for s in S:
        if s == G:
            print(count)
            return
        u = s + U
        if u <= F:
            if visit[u] == 0:
                visit[u] = 1
                nextS.append(u)
        d = s - D
        if d > 0:
            if visit[d] == 0:
                visit[d] = 1
                nextS.append(d)
    count += 1
    if len(nextS) == 0:
        print("use the stairs")
    else:
        bfs(nextS)
        
F, S, G, U, D = list(map(int,sys.stdin.readline().rstrip().split()))

visit = [0]*(F+1)
visit[S] = 1
count = 0
bfs([S])