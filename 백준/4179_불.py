def bfs(J,F):
    global count
    count += 1
    newJ = []
    newF = []
    for j in J:
        if board[j[0]][j[1]] != 'F':
            for m in move:
                my = m[0] + j[0]
                mx = m[1] + j[1]
                if R > my > -1 and C > mx > -1:
                    if board[my][mx] == '.':
                        newJ.append([my,mx])
                        board[my][mx] = 'J'
                else:
                    print(count)
                    return
    for f in F:
        for m in move:
            my = m[0] + f[0]
            mx = m[1] + f[1]
            if R > my > -1 and C > mx > -1:
                if board[my][mx] != '#' and board[my][mx] != 'F':
                    newF.append([my,mx])
                    board[my][mx] = 'F'

    if len(newJ) == 0:
        print('IMPOSSIBLE')
    else:
        bfs(newJ,newF)

import sys

R, C = map(int,sys.stdin.readline().split())

fire = []
board = []
move = [[1,0],[-1,0],[0,1],[0,-1]]
count = 0
for r in range(R):
    line = list(sys.stdin.readline().rstrip())
    for c in range(C):
        if line[c] == 'J':
            ji = [[r,c]]
        if line[c] == 'F':
            fire.append([r,c])
    board.append(line)

bfs(ji,fire)