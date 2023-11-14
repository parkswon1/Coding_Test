def search(board,count):
    global score
    if count == N+1:
        return
    count += 1
    for n in range(N):
        if board[n] == 0 and board[abs(count - (n+1))%N] == board[board[abs(count - (n+1))%N]] and board[(count + n+1)%N] == board[board[(count + n+1)%N]]:
            board[n] = count
            print(board)
            if 0 not in board:
                score += 1
            else:
                search(board,count)
            board[n] = 0

T = int(input())

for test_case in range(1,T+1):
    score = 0
    N = int(input())
    board = [0]*N
    search(board,0)

    print(f'#{test_case}',score)