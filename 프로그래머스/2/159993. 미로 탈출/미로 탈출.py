from collections import deque

def solution(maps):
    answer = 0
        
    def bfs(y, x, endWord):
        nodes = deque([(y,x,0)])
        move = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        visited.add((y,x))
        
        while(nodes):
            y, x, count = nodes.popleft()
            
            for m in move:
                my = y + m[0]
                mx = x + m[1]
                if 0 <= my < len(maps) and 0 <= mx < len(maps[0]) and (my, mx) not in visited and maps[my][mx] != 'X':
                    if maps[my][mx] == endWord:
                        return my, mx, count + 1
                    visited.add((my,mx))
                    nodes.append((my, mx, count + 1))
        return -1, -1, -1
    
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == 'S':
                my, mx, count = bfs(y, x, 'L')
                if count == -1:
                    return -1
                answer += count
                a, b, count = bfs(my, mx, 'E')
                if count == -1:
                    return -1
                answer += count
    
            
    return answer