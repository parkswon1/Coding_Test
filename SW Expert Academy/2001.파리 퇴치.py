T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    board = []
    score = 0
    for n in range(N):
        board.append(list(map(int,input().split())))

    for y in range(N+1-M):
        for x in range(N+1-M):
            count = 0
            for i in range(y,y+M):
                for j in range(x,x+M):
                    count += board[i][j]
            if count > score:
                score = count
    print(f'#{test_case}',score)