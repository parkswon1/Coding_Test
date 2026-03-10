from collections import deque

def solution(m, n, h, w, drops):
    answer = [-1, -1]
    board = [[float('inf') for _ in range(n)] for _ in range(m)]

    for i in range(1, len(drops) + 1):
        y, x = drops[i - 1][0], drops[i - 1][1]
        board[y][x] = i

    rowMin = [[0 for _ in range(n - w + 1)] for _ in range(m)]

    for y in range(m):
        dq = deque()
        for x in range(n):
            if dq and dq[0] < x - w + 1:
                dq.popleft()

            val = board[y][x]
            while dq and board[y][dq[-1]] >= val:
                dq.pop()
            dq.append(x)

            if x >= w - 1:
                rowMin[y][x - w + 1] = board[y][dq[0]]

    ansGrid = [[0 for _ in range(n - w + 1)] for _ in range(m - h + 1)]

    for x in range(n - w + 1):
        dq = deque()
        for y in range(m):
            if dq and dq[0] < y - h + 1:
                dq.popleft()

            val = rowMin[y][x]
            while dq and rowMin[dq[-1]][x] >= val:
                dq.pop()
            dq.append(y)

            if y >= h - 1:
                ansGrid[y - h + 1][x] = rowMin[dq[0]][x]

    bestTime = -1

    for y in range(m - h + 1):
        for x in range(n - w + 1):
            if ansGrid[y][x] > bestTime:
                bestTime = ansGrid[y][x]
                answer = [y, x]

    return answer