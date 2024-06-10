import sys

def dfs(index, visited):
    global answer
    if index == cctvCount:
        answer = min(totalCount - len(visited), answer)
        return

    y, x, type = CCTV[index]
    for move in moves[type]:
        newVisited = set([])
        for moveIndex in move:
            dy = y
            dx = x
            my = moveY[moveIndex]
            mx = moveX[moveIndex]
            while(1):
                dy += my
                dx += mx
                if 0 <= dy < N and 0 <= dx < M and board[dy][dx] != 6:
                    newVisited.add((dy, dx))
                else:
                    break

        dfs(index+1, visited.union(newVisited))


N, M = map(int, sys.stdin.readline().split())
totalCount = N*M

board = []
CCTV = []
moveX = [-1, 0, 1, 0]
moveY = [0, 1, 0, -1]

moves = [[],
         [(0,), (1,), (2,), (3,)],
         [(0, 2), (1, 3)],
         [(0, 1), (1, 2), (2, 3), (3, 0)],
         [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
         [(0, 1, 2, 3)]]

visited = set([])
for n in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for m in range(M):
        if line[m] != 0:
            if line[m] != 6:
                CCTV.append([n, m, line[m]])
            visited.add((n,m))
    board.append(line)

answer = float('inf')
cctvCount = len(CCTV)

dfs(0, visited)
print(answer)