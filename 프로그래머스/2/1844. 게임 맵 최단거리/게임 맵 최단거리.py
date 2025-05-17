from collections import deque

def solution(maps):
    answer = 0
    move = [(0,1),(1,0),(-1,0),(0,-1)]
    
    N = len(maps)
    M = len(maps[0])
    
    nodes = deque([(0,0,1)])
    maps[0][0] = 0
    while(nodes):
        y, x, count = nodes.popleft()
        if y == N - 1 and x == M - 1:
            return count
        
        for mv in move:
            my = y + mv[0]
            mx = x + mv[1]
            
            if 0 <= my < N and 0 <= mx < M:
                if maps[my][mx] == 1:
                    maps[my][mx] = 0
                    nodes.append((my, mx, count + 1))
    
    return -1