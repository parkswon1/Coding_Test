from collections import deque

def solution(maps):
    answer = []
    visited = set()
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    Y = len(maps)
    X = len(maps[0])
    for i in range(Y):
        for j in range(X):
            if (i,j) in visited or maps[i][j] == 'X':
                continue
            
            nodes = deque([(i,j)])
            count = int(maps[i][j])
            visited.add((i,j))
            
            while nodes:
                y, x = nodes.popleft()
                for dy, dx in move:
                    my = dy + y
                    mx = dx + x
                    if Y > my >= 0 and X > mx >= 0 and maps[my][mx] != 'X' and (my, mx) not in visited:
                        visited.add((my, mx))
                        count += int(maps[my][mx])
                        nodes.append((my,mx))
            answer.append(count)
    
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer