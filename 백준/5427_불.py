def bfs(J,F):
    global count
    count += 1
    newJ = []
    newF = []
    for f in F:
        for m in move:
            my = m[0] + f[0]
            mx = m[1] + f[1]
            if R > my > -1 and C > mx > -1:
                if board[my][mx] != '#' and board[my][mx] != '*':
                    newF.append([my,mx])
                    board[my][mx] = '*'
    for j in J:
        for m in move:
            my = m[0] + j[0]
            mx = m[1] + j[1]
            if R > my > -1 and C > mx > -1:
                if board[my][mx] == '.':
                    newJ.append([my,mx])
                    board[my][mx] = '@'
            else:
                print(count)
                return

    if len(newJ) == 0:
        print('IMPOSSIBLE')
    else:
        bfs(newJ,newF)

import sys
sys.setrecursionlimit(10**7)

test_case = int(sys.stdin.readline())
for t in range(test_case):
    C, R = map(int,sys.stdin.readline().split())

    fire = []
    board = []
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    count = 0
    for r in range(R):
        line = list(sys.stdin.readline().rstrip())
        for c in range(C):
            if line[c] == '@':
                ji = [[r,c]]
            if line[c] == '*':
                fire.append([r,c])
        board.append(line)

    bfs(ji,fire)