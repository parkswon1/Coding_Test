from collections import deque

def solution(n, computers):
    answer = 0
    visited = set()
    for i in range(n):
        nodes = deque([i])
        
        if i in visited:
            continue
        visited.add(i)
        answer +=  1
        while(nodes):
            current = nodes.popleft()
            
            for j in range(len(computers[0])):
                if computers[current][j] == 1:
                    if j not in visited:
                        nodes.append(j)
                        visited.add(current)
    
    return answer