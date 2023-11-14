T = int(input())

for test_case in range(1,T+1):
    board = []
    check = 1
    for _ in range(9):
        line = list(map(int,input().split()))
        for i in range(1,10):
            if i not in line:
                check = 0
        board.append(line)
    check_line = [1,2,3,4,5,6,7,8,9]
    for x in range(9):
        line = [0]*9
        for y in range(9):
            line[board[y][x]-1] = board[y][x]
        if line != check_line:
            check = 0

    for m in range(0,7,3):
        for n in range(0,7,3):
            line = [0] * 9
            for y in range(m,m+3):
                for x in range(n,n+3):
                    line[board[y][x]-1] = board[y][x]
            if line != check_line:
                check = 0
    print(f'#{test_case}', check)