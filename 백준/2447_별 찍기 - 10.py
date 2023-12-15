def mark(N,y,x):
    M = N//3
    for k in range(M+y,M+M+y):
        for l in range(M+x,M+M+x):
            board[k][l] = ' '

    if M != 1:
        for i in range(3):
            for j in range(3):
                mark(M,y+i*M,x+j*M)

N = int(input())

board = []

for _ in range(N):
    board.append(['*']*N)

mark(N,0,0)

for n in range(N):
    print(''.join(board[n]))