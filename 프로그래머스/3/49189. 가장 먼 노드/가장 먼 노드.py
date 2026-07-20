import heapq

def solution(n, edge):
    answer = 0
    nodes = []
    board = {}
    for x, y in edge:
        if x in board:
            board[x].append(y)
        else:
            board[x] = [y]
        if y in board:
            board[y].append(x)
        else:
            board[y] = [x]
    
    heapq.heappush(nodes, (0,1))
    long = -1
    visited = set()
    visited.add(1)
    while nodes:
        dist, node = heapq.heappop(nodes)
        
        for nextNode in board[node]:
            if nextNode in visited:
                continue
            
            visited.add(nextNode)
            if dist + 1 > long:
                long = dist + 1
                answer = 1
            elif dist + 1 == long:
                answer += 1
            
            heapq.heappush(nodes, (dist + 1, nextNode))
    
    return answer