def right(x,y,count):
    global output
    mx = x + 1
    if mx < N and board[y][mx] == 1:
        right(mx,y,count+1)
    elif count == K:
        output += 1
        return


def down(x,y,count):
    global output
    my = y + 1
    if my < N and board[my][x] == 1:
        down(x, my, count + 1)
    elif count == K:
        output += 1
        return

T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    board = []
    output = 0
    for n in range(N):
        line = list(map(int,input().split()))
        board.append(line)

    for y in range(N):
        for x in range(N):
            if (x == 0 and board[y][x] == 1) or (board[y][x - 1] == 0 and board[y][x] == 1):
                right(x,y,1)
            if (y == 0 and board[y][x] == 1) or (board[y - 1][x] == 0 and board[y][x] == 1):
                down(x,y,1)

    print(f'#{test_case}',output)