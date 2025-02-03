def solution(M, N, puddle):
    board = [[0] * M for _ in range(N)]
    puddles = {(p[1] - 1, p[0] - 1) for p in puddle}  # 리스트 대신 튜플을 set에 저장

    # 첫 번째 행 초기화 (물웅덩이를 만나면 이후로 0)
    for m in range(M):
        if (0, m) in puddles:
            break
        board[0][m] = 1

    # 첫 번째 열 초기화 (물웅덩이를 만나면 이후로 0)
    for n in range(N):
        if (n, 0) in puddles:
            break
        board[n][0] = 1

    # DP 채우기
    for y in range(1, N):
        for x in range(1, M):
            if (y, x) in puddles:
                board[y][x] = 0
            else:
                board[y][x] = (board[y - 1][x] + board[y][x - 1]) % 1000000007

    return board[N - 1][M - 1]
