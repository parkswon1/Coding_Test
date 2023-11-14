def bfs(before):
    after = []

    for node in before:
        y = node[0]
        x = node[1]
        for yx in mv:
            mx = x + yx[1]
            my = y + yx[0]
            if N > mx > -1 and N > my > -1:
                if score[my][mx] > score[y][x] + board[my][mx]:
                    score[my][mx] = score[y][x] + board[my][mx]
                    after.append([my,mx])

    if len(after) == 0:
        return
    else:
        bfs(after)

T = int(input())

mv = [[1,0],[-1,0],[0,1],[0,-1]]
for i in range(1,T+1):
    N = int(input())
    board = []
    score = []
    for n in range(N):
        score.append([999999]*N)
        board.append([int(i) for i in input()])

    score[0][0] = 0
    bfs([[0,0]])

    print(f'#{i}', score[N-1][N-1])
    