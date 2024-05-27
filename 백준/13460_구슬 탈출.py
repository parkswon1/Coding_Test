from collections import deque
import sys

def moveBall(y, x, dy, dx):
    count = 0
    while board[y + dy][x + dx] != '#' and board[y][x] != 'O':
        x += dx
        y += dy
        count += 1
    return y, x, count


def BFS():
    global nodes, visited
    while nodes:
        yRed, xRed, yBlue, xBlue, playCount = nodes.popleft()
        if playCount > 9:
            return -1

        for dy, dx in move:
            myRed, mxRed, redCount = moveBall(yRed, xRed, dy, dx)
            myBlue, mxBlue, blueCount = moveBall(yBlue, xBlue, dy, dx)

            if board[myBlue][mxBlue] == 'O':
                continue
            if board[myRed][mxRed] == 'O':
                return playCount + 1

            if myRed == myBlue and mxRed == mxBlue:
                if redCount > blueCount:
                    myRed -= dy
                    mxRed -= dx
                else:
                    myBlue -= dy
                    mxBlue -= dx

            if (myRed, mxRed, myBlue, mxBlue) not in visited:
                nodes.append((myRed, mxRed, myBlue, mxBlue, playCount + 1))
                visited.add((myRed, mxRed, myBlue, mxBlue))

    return -1

N, M = map(int, input().split())
board = []
for n in range(N):
    line = list(sys.stdin.readline().strip())
    board.append(line)
    for m in range(M):
        if line[m] == 'R':
            yRed, xRed = n, m
        elif line[m] == 'B':
            yBlue, xBlue = n, m

nodes = deque([(yRed, xRed, yBlue, xBlue, 0)])
visited = set((yRed, xRed, yBlue, xBlue))

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
print(BFS())