from collections import deque

def solution(land):
    answer = 0
    oilMount = {}
    Y = len(land)
    X = len(land[0])
    mark = 1
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    for y in range(Y):
        for x in range(X):
            if land[y][x] == 1:
                mark += 1
                oilMount[mark] = 1
                node = deque([[y,x]])
                land[y][x] = mark
                while(node):
                    n = node.popleft()
                    for mv in move:
                        my = n[0] + mv[0]
                        mx = n[1] + mv[1]
                        if 0 <= my < Y and 0 <= mx < X and land[my][mx] == 1:
                            land[my][mx] = mark
                            oilMount[mark] += 1
                            node.append([my,mx])

    for x in range(X):
        oilSet = set()
        for y in range(Y):
            if 0 <= my < Y and 0 <= mx < X and land[y][x] != 0:
                oilSet.add(land[y][x])
        count = 0
        for oil in oilSet:
            count += oilMount[oil]
        answer = max(answer, count)

    return answer

land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
print(solution(land))