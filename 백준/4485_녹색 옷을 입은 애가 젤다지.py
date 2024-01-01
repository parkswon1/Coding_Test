from collections import deque
import sys

move = [[0,1],[0,-1],[1,0],[-1,0]]
for i in range(1,99999999999):
    N = int(sys.stdin.readline())
    if N == 0:
        break

    board = []
    visited = []
    for n in range(N):
        visited.append([float('inf')] * N)
        board.append(list(map(int,sys.stdin.readline().split())))

    nodes = deque([[0,0]])
    visited[0][0] = board[0][0]
    while(nodes):
        y,x = nodes.popleft()
        for m in move:
            my = y + m[0]
            mx = x + m[1]
            if N > my > -1 and N > mx > -1:
                total = visited[y][x] + board[my][mx]
                if visited[my][mx] > total:
                    visited[my][mx] = total
                    nodes.append([my,mx])

    print(f'Problem {i}:',visited[N-1][N-1])