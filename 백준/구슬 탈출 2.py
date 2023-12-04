def game(board,m,B,R):
    for i in range(4):
        if i != m:



import sys

N, M = map(int,sys.stdin.readline().split())

board = []
move = [[1,0][-1,0][0,1][0,-1]]

for n in range(N):
    line = list(sys.stdin.readline().rstrip())
    for l in range(M):
        if line[l] == 'B':
            B = [n][l]
        elif line[l] == 'R':
            R = [n][l]
        elif line[l] == 'O':
            O = [n][l]
    board.append(line)

game(board,4,B,R)