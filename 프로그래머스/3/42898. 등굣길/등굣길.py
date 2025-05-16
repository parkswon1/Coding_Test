def solution(M, N, puddle):
    board = [[0] * M for _ in range(N)]
    puddles = {(p[1] - 1, p[0] - 1) for p in puddle}

    for m in range(M):
        if (0, m) in puddles:
            break
        board[0][m] = 1

    for n in range(N):
        if (n, 0) in puddles:
            break
        board[n][0] = 1

    for y in range(1, N):
        for x in range(1, M):
            if (y, x) in puddles:
                board[y][x] = 0
            else:
                board[y][x] = (board[y - 1][x] + board[y][x - 1]) % 1000000007

    return board[N - 1][M - 1]