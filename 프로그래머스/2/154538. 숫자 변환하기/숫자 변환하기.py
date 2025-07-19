from collections import deque

def solution(x, y, n):
    visited = set()
    queue = deque([(x, 0)])
    visited.add(x)
    
    while queue:
        num, count = queue.popleft()
        
        if num == y:
            return count
        
        for next_num in (num + n, num * 2, num * 3):
            if next_num <= y and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, count + 1))
    
    return -1