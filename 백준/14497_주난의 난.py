import sys
from collections import deque

def bfs(nodes):
    global count
    count += 1
    nextNode = deque([])
    while(nodes):
        y, x = nodes.popleft()
        for mv in move:
            my = y + mv[0]
            mx = x + mv[1]
            if N > my > -1 and M > mx > -1:
                if board[my][mx] == '0':
                    board[my][mx] = '2'
                    nodes.append([my, mx])
                elif board[my][mx] == '1':
                    board[my][mx] = '2'
                    nextNode.append([my, mx])
                elif board[my][mx] == '#':
                    print(count)
                    return
    if len(nextNode) > 0:
        bfs(nextNode)


sys.setrecursionlimit(10**7)
N, M = map(int, sys.stdin.readline().split())
y1, x1, y2, x2 = map(int, sys.stdin.readline().split())

board = []
move = [[1,0],[-1,0],[0,-1],[0,1]]
for n in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

que = deque([[y1-1, x1-1]])
count = 0
bfs(que)