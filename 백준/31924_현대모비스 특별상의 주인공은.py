import sys

N = int(sys.stdin.readline())

board = []
for n in range(N):
    board.append(sys.stdin.readline().rstrip())

move = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]

answer = 0
for y in range(N):
    for x in range(N):
        if board[y][x] == 'M':
            for mv in move:
                str = 'M'
                my = y + mv[0]
                mx = x + mv[1]
                while(0 <= my < N and 0 <= mx < N):
                    str += board[my][mx]
                    if len(str) == 5:
                        break
                    my = my + mv[0]
                    mx = mx + mv[1]

                if str == 'MOBIS':
                    answer += 1

print(answer)