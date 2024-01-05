import sys

def search(y,x,n,count):
    global output
    if y == H:
        if x == n:
            if x == N - 1:
                output = min(count)
            else:
                search(0,n+1,n+1,count)

    elif board[y][x] == 0:
        for mx in (1,-1):
            if N-1 > x + mx > -1:
                board[y][x-mx] = 1
                board[y][x] = -1
                search(y, x + mx, n, count + 1)
                board[y][x] = 0
        search(y + 1, x, n, count)
    else:
        search(y,x + board[y][x],n, count)
    return


sys.setrecursionlimit(10**7)
N, M, H = map(int,sys.stdin.readline().split())
board = [[0 for n in range(N)] for h in range(H)]

for m in range(M):
    a, b = map(int,sys.stdin.readline().split())
    board[a-1][b-1] = 1
    board[a-1][b] = -1

output = float('inf')
search(0,0,0,0)

print(output)