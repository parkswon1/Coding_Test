from collections import deque

def solution(maps):
    answer = float('inf')
    move = [(1,0),(0,1),(-1,0),(0,-1)]
    nodes = deque([(0,0,1)]) #y,x,count
    visited = set()
    visited.add((0,0))
    while nodes:
        y,x,count = nodes.popleft()
        count += 1
        for dy, dx in move:
            my = dy + y
            mx = dx + x
            if 0 <= my < len(maps) and 0 <= mx < len(maps[0]):
                if (my, mx) in visited or maps[my][mx] == 0:
                    continue
                if (my, mx) == (len(maps) - 1, len(maps[0]) - 1):
                    answer = min(answer, count)
                nodes.append((my,mx,count))
                visited.add((my,mx))

    if answer == float('inf'):
        return -1
    return answer