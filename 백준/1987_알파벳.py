def DFS():
    global output
    while(visited):
        y, x, visit, count = visited.pop()
        output = max(count,output)
        for m in move:
            my = y + m[0]
            mx = x + m[1]
            if R > my > -1 and C > mx > -1:
                if board[my][mx] not in visit:
                    visited.add((my, mx, visit + board[my][mx], count + 1))
    return

import sys
sys.setrecursionlimit(10**7)
R, C = map(int,sys.stdin.readline().split())

board = []
move = [[0,1],[0,-1],[-1,0],[1,0]]
for r in range(R):
    board.append(list(sys.stdin.readline().rstrip()))

output = 0
visited = set()
visited.add((0,0,board[0][0],1))
DFS()

print(output)