from collections import deque

def solution(x, y, n):
    answer = 0
    visited = set()
    visited.add(x)
    nodes = deque([(x,0)]) #노드, 실행 횟수
    while nodes:
        node, count = nodes.popleft() 
        if node == y:
            return count
        
        temp = node + n
        if temp not in visited and temp <= y:
            visited.add(temp)
            nodes.append((temp, count + 1))
        
        temp = node * 2
        if temp not in visited and temp <= y:
            visited.add(temp)
            nodes.append((temp, count + 1))
            
        temp = node * 3
        if temp not in visited and temp <= y:
            visited.add(temp)
            nodes.append((temp, count + 1))
    
    return -1
