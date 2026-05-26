from collections import deque

def solution(maps):
    answer = float('inf')
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    nodes = deque([(0, 0, 1)])
    visited = set()
    visited.add((0,0))
    
    while(nodes):
        y, x, cost = nodes.popleft()
        for m in move:
            my = m[0] + y
            mx = m[1] + x
            
            if 0 <= my < len(maps) and 0 <= mx < len(maps[0]):
                if (my, mx) in visited or maps[my][mx] == 0:
                    continue
                if (my, mx) == (len(maps) - 1, len(maps[0]) - 1):
                    return cost + 1
                visited.add((my,mx))
                nodes.append((my, mx, cost + 1))                
    
    return -1