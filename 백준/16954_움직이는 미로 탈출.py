def BFS(nodes,wall):
    newNodes = []
    newWall = []
    for n in nodes:
        if board[n[0]][n[1]] == '.':
            for mv in move:
                my = mv[0] + n[0]
                mx = mv[1] + n[1]
                if 8 > my > -1 and 8 > mx > -1:
                    if board[my][mx] == '.':
                        if my == 0 and mx == 7:
                            print(1)
                            return
                        newNodes.append([my,mx])
    for w in wall:
        my = w[0] + 1
        board[w[0]][w[1]] -= 1
        if board[w[0]][w[1]] == 0:
            board[w[0]][w[1]] = '.'
        if 8 > my > -1:
            if board[my][w[1]] == '.':
                board[my][w[1]] = 1
            else:
                board[my][w[1]] += 1
            newWall.append([my,w[1]])

    if len(newNodes) == 0:
        print(0)
    else:
        BFS(newNodes,newWall)

import sys
sys.setrecursionlimit(10**7)

board = []
wall = []
nodes = [[7,0]]
for i in range(8):
    line = list(sys.stdin.readline().rstrip())
    for j in range(8):
        if line[j] == '#':
            line[j] = 1
            wall.append([i,j])
    board.append(line)

move = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1],[0,0]]
BFS(nodes,wall)