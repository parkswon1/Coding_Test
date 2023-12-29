def dfs(y,x,count):
    global output, check
    moveMix = int(board[y][x])
    output = max(output, count)
    for m in move:
        my = y + (moveMix * m[0])
        mx = x + (moveMix * m[1])
        if N > my > -1 and M > mx > -1 and board[my][mx] != 'H' and count > dp[my][mx]:
            if visited[my][mx] != 1:
                visited[my][mx] = 1
                dp[my][mx] = count
                dfs(my, mx, count + 1)
                visited[my][mx] = 0
            else:
                check = 1
                return

import sys
sys.setrecursionlimit(10**7)

move = [[1,0],[-1,0],[0,-1],[0,1]]
N, M = map(int,sys.stdin.readline().split())
board = []
visited = []
dp = []
for n in range(N):
    visited.append([0] * M)
    dp.append([0] * M)
    board.append(list(sys.stdin.readline().rstrip()))

visited[0][0] = 1
output = 0
check = 0
dfs(0,0,1)

if check == 0:
    print(output)
else:
    print(-1)