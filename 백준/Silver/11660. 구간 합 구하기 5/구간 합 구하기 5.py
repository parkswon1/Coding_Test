import sys

N, M = map(int, sys.stdin.readline().split())

temp = []

for n in range(N):
    temp.append(list(map(int, sys.stdin.readline().split())))

board = [[0 for i in range(N + 1)] for j in range(N + 1)]

for y in range(1, N + 1):
    for x in range(1, N + 1):
        board[y][x] = temp[y - 1][x - 1] + board[y - 1][x] + board[y][x - 1] - board[y - 1][x - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    res = (
            board[x2][y2]
            - board[x1 - 1][y2]
            - board[x2][y1 - 1]
            + board[x1 - 1][y1 - 1]
    )
    print(res)