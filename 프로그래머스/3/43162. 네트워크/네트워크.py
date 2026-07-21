def solution(n, computers):
    answer = 0
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        visited.add(i)
        nodes = [i]
        while nodes:
            node = nodes.pop()
            for j in range(n):
                if computers[node][j] == 0 or j in visited:
                    continue
                nodes.append(j)
                visited.add(j)
            
        answer += 1
    
    return answer