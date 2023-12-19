def BFS(nodes):
    global output, moveCount
    new_nodes = []
    for n in nodes:
        for m in move:
            mz = n[0] + m[0]
            my = n[1] + m[1]
            mx = n[2] + m[2]
            if K+1 > mz > -1 and H > my > -1 and W > mx > -1:
                if my == H-1 and mx == W-1:
                    output = min(output,moveCount)
                    return
                elif travelBoard[mz][my][mx] == 0:
                    travelBoard[mz][my][mx] = moveCount
                    new_nodes.append([mz,my,mx])
    moveCount += 1

    if len(new_nodes) != 0:
        BFS(new_nodes)

import sys
sys.setrecursionlimit(10**7)
K = int(sys.stdin.readline())
W,H = map(int,sys.stdin.readline().split())

travelBoard = []
move = [[0,1,0],[0,-1,0],[0,0,1],[0,0,-1],[1,2,1],[1,2,-1],[1,-2,1],[1,-2,-1],[1,1,2],[1,1,-2],[1,-1,2],[1,-1,-2]]

for k in range(K+1):
    board = []
    for h in range(H):
        board.append([0]*W)
    travelBoard.append(board)

for h in range(H):
    line = list(map(int,sys.stdin.readline().split()))
    for w in range(W):
        if line[w] == 1:
            for k in range(K+1):
                travelBoard[k][h][w] = 1
moveCount = 1
output = float('inf')
travelBoard[0][0][0] = 1
if W == 1 and H == 1:
    print(0)
else:
    BFS([[0, 0, 0]])
    if output != float('inf'):
        print(output)
    else:
        print(-1)