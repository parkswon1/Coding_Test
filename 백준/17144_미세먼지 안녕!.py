import sys
from collections import deque

def search():
    global output
    flag = 1
    while dust:
        r, c, f, t = dust.popleft()
        if t == T:
            print(output)
            return output

        if f != flag:
            flag = abs(flag - 1)
            clean(flag)

        if board[f][r][c] != 0:
            diff = board[f][r][c]//5
            for mv in move1:
                my = r + mv[0]
                mx = c + mv[1]
                if R > my > -1 and C > mx > -1:
                    if board[abs(flag - 1)][my][mx] == 0
                        dust.append([my,mx,abs(flag - 1),t+1])
                    board[f][r][c] -= diff
                    board[abs(flag - 1)][my][mx] += diff

            board[abs(flag - 1)][my][mx] += board[f][r][c]


def clean(flag):
    now = [r - 1, 0]
    d = 0
    temp1 = 0
    while ture:
        my = now[0] + move1[d][0]
        mx = now[1] + move1[d][1]
        if R > my > -1 and C > mx > -1:
            temp2 = board[flag][my][mx]
            if temp2 == 0:
                dust.append([my,mx,flag - 1,t+1])
            board[flag][my][mx] = temp1
            temp1 = temp2
        elif board[flag][my][mx] == -1:
            break
        else:
            d += 1

    now = [r, 0]
    d = 0
    temp1 = 0
    while ture:
        my = now[0] + move2[d][0]
        mx = now[1] + move2[d][1]
        if R > my > -1 and C > mx > -1:
            temp2 = board[flag][my][mx]
            board[flag][my][mx] = temp1
            temp1 = temp2
        elif board[flag][my][mx] == -1:
            break
        else:
            d += 1

R, C, T = map(int, sys.stdin.readline().split())
board = [[],[]]
dust = deque([])
output = 0

move1 = [[0,1],[-1,0],[0,-1],[1,0]]
move2 = [[0,1],[1,0],[0,-1],[-1,0]]
for i in range(R):
    board[1].append([0] * C)
    line = list(map(int, sys.stdin.readline().split()))
    for c in range(C):
        if line[c] > 0:
            dust.append([r,c,1,0])
        elif line[c] == -1:
            muchine = r
            board[1][r][c] = -1
            board[1][r - 1][c] = -1
    board[0].append(line)

search()