import heapq

def solution(board):
    answer = 0
    move = [(0,1),(-1,0),(0,-1),(1,0)]
    N = len(board)
    nodes = []
    heapq.heappush(nodes,(0,0,0,0))#cost,y,x,방향
    heapq.heappush(nodes,(0,0,0,3))
    visited = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]

    visited[0][0][0] = 0
    visited[0][0][3] = 0
    while nodes:
        cost, y, x, direction = heapq.heappop(nodes)
        
        if y == N -1 and x == N - 1:
            continue
        
        for i in range(4):
            my = y + move[i][0]
            mx = x + move[i][1]
            
            if direction == i:
                mcost = cost + 100
            else:
                mcost = cost + 600
            
            if 0 <= my < N and 0 <= mx < N and board[my][mx] != 1:
                if mcost >= visited[my][mx][i]:
                    continue
                visited[my][mx][i] = mcost
                heapq.heappush(nodes, (mcost, my, mx, i))

    return min(visited[N-1][N-1])