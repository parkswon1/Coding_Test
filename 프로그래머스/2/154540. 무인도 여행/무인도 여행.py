from collections import deque

move = [(1,0),(-1,0),(0,1),(0,-1)]

def solution(maps):
    maps = [list(row) for row in maps]
    answer = []
    maxY = len(maps)
    maxX = len(maps[0])
    for i in range(maxY):
        for j in range(maxX):
            if maps[i][j] != 'X':
                answer.append(dfs(maps, i, j, maxY, maxX))
    
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer


def dfs(maps, startY, startX, maxY, maxX):
    count = int(maps[startY][startX])
    maps[startY][startX] = 'X'
    nodes = deque([(startY, startX)])
    
    while(nodes):
        y, x = nodes.popleft()
        for dy, dx in move:
            my = y + dy
            mx = x + dx
            
            if 0 <= my < maxY and 0 <= mx < maxX and maps[my][mx] != 'X':
                count += int(maps[my][mx])
                maps[my][mx] = 'X'
                nodes.append((my, mx))
    
    return count