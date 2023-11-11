ds = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def isField(i, j):
    return 0 <= i < N and 0 <= j < N

def bfs(i, j):
    queue = [(i, j)]
    while queue:
        temp = queue[:]
        queue = []
        while temp:
            si, sj = temp.pop()
            for di, dj in ds:
                ni = si + di
                nj = sj + dj
                if isField(ni, nj) and (not visited[ni][nj] or shortcut[ni][nj] > shortcut[si][sj] + g[ni][nj]):
                    shortcut[ni][nj] = shortcut[si][sj] + g[ni][nj]
                    queue.append((ni, nj))
                    visited[ni][nj] = 1

for i in range(int(input())):
    N = int(input())
    shortcut = [[90001] * N for _ in range(N)]
    shortcut[0][0] = 0
    visited = [[0] * N for _ in range(N)]
    g = [[int(i) for i in list(input())] for _ in range(N)]
    time_sum = 0
    bfs(0, 0)
    print('#{} {}'.format(i+1, shortcut[N-1][N-1]))