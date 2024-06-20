import sys

N, K = map(int, sys.stdin.readline().split())

board = []
pieceOnBoard = []
pieces = []

for n in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    pieceOnBoard.append([[] for i in range(N)])

for k in range(K):
    y, x, v = map(int, sys.stdin.readline().split())
    pieceOnBoard[y - 1][x - 1].append(k + 1)
    pieces.append([y - 1, x - 1, v - 1])

answer = -1
move = [(0,1),(0,-1),(-1,0),(1,0)]
def changV(v):
    if v == 0:
        return 1
    elif v == 1:
        return 0
    elif v == 2:
        return 3
    else:
        return 2


# 0흰색, 1 빨간색, 2 파란색
flag = 0
while(1):
    answer += 1
    if flag == 1:
        print(answer)
        break
    elif answer > 1000:
        print(-1)
        break

    for k in range(K):
        y, x, v = pieces[k]
        number = k + 1

        my = y + move[v][0]
        mx = x + move[v][1]
        index = pieceOnBoard[y][x].index(number)
        if index == 0:
            if 0 > my or my >= N or 0 > mx or mx >= N or board[my][mx] == 2:
                v = changV(v)
                my = y + move[v][0]
                mx = x + move[v][1]
                pieces[k][2] = v

            if 0 <= my < N and 0 <= mx < N and board[my][mx] != 2:
                if board[my][mx] == 0:
                    pieceOnBoard[my][mx] += pieceOnBoard[y][x][index:]
                    for _ in range(len(pieceOnBoard[y][x]) - index):
                        popedPiece = pieceOnBoard[y][x].pop()
                        pieces[popedPiece - 1][0] = my
                        pieces[popedPiece - 1][1] = mx

                elif board[my][mx] == 1:
                    for _ in range(len(pieceOnBoard[y][x]) - index):
                        popedPiece = pieceOnBoard[y][x].pop()
                        pieceOnBoard[my][mx].append(popedPiece)
                        pieces[popedPiece - 1][0] = my
                        pieces[popedPiece - 1][1] = mx

                if len(pieceOnBoard[my][mx]) >= 4:
                    flag = 1
                    break