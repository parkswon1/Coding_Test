from collections import deque

def solution(board):
    answer = 0
    visited = set()
    move = ((1,0),(-1,0),(0,1),(0,-1))
    nodes = deque()
    Y = len(board)
    X = len(board[0])
    
    for y in range(Y):
        for x in range(X):
            if board[y][x] == 'R':
                nodes.append((y,x,0))
                visited.add((y,x))
            if board[y][x] == 'G':
                goal = (y,x)

    while nodes:
        y, x, count = nodes.popleft()
        for dy, dx in move:
            my = y
            mx = x
            while Y > my + dy >= 0 and X > mx + dx >= 0 and board[my + dy][mx + dx] != 'D':
                my += dy
                mx += dx

            if (my, mx) not in visited:
                visited.add((my, mx))
                nodes.append((my,mx,count + 1))
                
                if (my, mx) == goal:
                    return count + 1

    return -1