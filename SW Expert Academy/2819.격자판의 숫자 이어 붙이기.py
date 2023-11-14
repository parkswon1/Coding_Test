def search(y,x,numbers):
    if len(numbers) == 7:
        output.add(''.join(map(str,numbers)))
        return
    for m in mv:
        mx = m[1] + x
        my = m[0] + y
        if 4 > mx > -1 and 4 > my > -1:
            search(my,mx,numbers + [board[my][mx]])

mv = [[1,0],[-1,0],[0,1],[0,-1]]
T = int(input())
for test_case in range(1,T+1):
    output = set()
    board = []
    for i in range(4):
        line = list(map(int,input().split()))
        board.append(line)

    for i in range(4):
        for j in range(4):
            numbers = [board[i][j]]
            search(i,j,numbers)
    print(f'#{test_case}', len(output))